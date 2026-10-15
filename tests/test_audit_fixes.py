"""Offline regression cases for the post-PR-14 audit."""
import datetime
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import unquote, urljoin, urlsplit
from html.parser import HTMLParser
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from extract_docx import extract, para_text, W, R, A
from minify_gzh_html import minify_html
from validate_gzh_html import validate
import wechat_draft as draft

try:
    import requests
except ImportError:
    requests = None


def response(value):
    class Response:
        content = json.dumps(value, ensure_ascii=False).encode('utf-8')
    return Response()


class TokenTests(unittest.TestCase):
    def test_cache_must_belong_to_configured_account(self):
        with tempfile.TemporaryDirectory() as directory:
            config, cache = Path(directory) / 'config.json', Path(directory) / 'token.json'
            config.write_text(json.dumps({'WECHAT_APP_ID': 'account-B', 'WECHAT_APP_SECRET': 'fake'}))
            for owner in [None, 'account-A', 'account-B']:
                data = {'access_token': 'cached', 'expires': (
                    datetime.datetime.now() + datetime.timedelta(hours=1)).isoformat()}
                if owner is not None:
                    data['appid'] = owner
                cache.write_text(json.dumps(data))
                with self.subTest(owner=owner), patch.object(draft, 'CONFIG_FILE', str(config)), \
                        patch.object(draft, 'TOKEN_FILE', str(cache)), \
                        patch.object(draft, 'refresh_token', return_value='fresh') as refresh:
                    self.assertEqual(draft.get_token(), 'cached' if owner == 'account-B' else 'fresh')
                    self.assertEqual(refresh.called, owner != 'account-B')

    @unittest.skipUnless(requests, 'requires requests')
    def test_switching_account_refreshes_and_persists_cache_identity(self):
        with tempfile.TemporaryDirectory() as directory:
            config, cache = Path(directory) / 'config.json', Path(directory) / 'token.json'
            with patch.object(draft, 'CONFIG_FILE', str(config)), patch.object(draft, 'TOKEN_FILE', str(cache)), \
                    patch('requests.post', side_effect=[response({'access_token': 'token-A'}),
                                                        response({'access_token': 'token-B'})]) as post:
                for account in ['A', 'B']:
                    config.write_text(json.dumps({'WECHAT_APP_ID': account, 'WECHAT_APP_SECRET': 'fake'}))
                    self.assertEqual(draft.get_token(), 'token-' + account)
                    self.assertEqual(draft.get_token(), 'token-' + account)
                    self.assertEqual(json.loads(cache.read_text())['appid'], account)
                self.assertEqual(post.call_count, 2)


class MinifierAuditTests(unittest.TestCase):
    def test_entity_spelling_and_literal_ampersands_are_preserved(self):
        for text in ['AT&T and R&D', 'foo&copycat', '&copy &copy; &amp; &#65 &#x41;',
                     'A\n&unknown; &notit; &amp=2']:
            source = '<pre>' + text + '</pre>'
            with self.subTest(text=text):
                self.assertEqual(minify_html(source), source)
                self.assertEqual(minify_html(minify_html(source)), source)

    def test_inline_display_keeps_word_separators_at_both_edges(self):
        for style in ['display:inline', 'display:inline-block', 'display:inline flex', 'display:flow-root inline',
                      'DISPLAY: INLINE', 'display:block;display:inline',
                      'display:inline!important;display:block']:
            source = f'<section><p style="{style}">Hello</p> <p style="{style}">world</p></section>'
            with self.subTest(style=style):
                self.assertEqual(minify_html(source), source)

    def test_explicit_block_still_removes_indentation(self):
        source = '<section>\n <span style="display:block">Hello</span>\n <span style="display:block">world</span>\n</section>'
        self.assertEqual(minify_html(source), source.replace('\n ', '').replace('\n', ''))


def make_docx(path, body, media=None):
    document = f'<w:document xmlns:w="{W[1:-1]}" xmlns:r="{R[1:-1]}" xmlns:a="{A[1:-1]}"><w:body>{body}</w:body></w:document>'
    with zipfile.ZipFile(path, 'w') as z:
        z.writestr('word/document.xml', document)
        if media is not None:
            z.writestr('word/_rels/document.xml.rels',
                       '<Relationships><Relationship Id="pic" Target="media/image1.png"/></Relationships>')
            z.writestr('word/media/image1.png', media)


class WordAuditTests(unittest.TestCase):
    def test_converting_second_article_does_not_replace_first_articles_images(self):
        body = '<w:p><w:r><w:drawing><a:blip r:embed="pic"/></w:drawing></w:r></w:p>'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = []
            for name, media in [('first article #1%中文', b'first image'), ('second article', b'second image')]:
                make_docx(root / (name + '.docx'), body, media)
                output = root / (name + '.md')
                self.assertEqual(extract(str(root / (name + '.docx')), str(output)), 0)
                reference = re.search(r'!\[\]\(<([^>]+)>\)', output.read_text(encoding='utf-8')).group(1)
                self.assertFalse(urlsplit(reference).fragment)
                paths.append(root / unquote(reference))
            self.assertNotEqual(paths[0], paths[1])
            self.assertEqual(paths[0].read_bytes(), b'first image')
            self.assertEqual(paths[1].read_bytes(), b'second image')

    def test_content_controls_keep_order_and_table_content(self):
        body = ('<w:p><w:r><w:t>before</w:t></w:r></w:p>'
                '<w:sdt><w:sdtPr/><w:sdtContent><w:sdt><w:sdtContent>'
                '<w:p><w:r><w:t>controlled</w:t></w:r></w:p>'
                '</w:sdtContent></w:sdt>'
                '<w:tbl><w:sdt><w:sdtContent><w:tr><w:sdt><w:sdtContent><w:tc>'
                '<w:p><w:r><w:t>cell</w:t></w:r></w:p>'
                '</w:tc></w:sdtContent></w:sdt></w:tr></w:sdtContent></w:sdt></w:tbl>'
                '</w:sdtContent></w:sdt><w:p><w:r><w:t>after</w:t></w:r></w:p>')
        with tempfile.TemporaryDirectory() as directory:
            source, output = Path(directory) / 'article.docx', Path(directory) / 'article.md'
            make_docx(source, body)
            self.assertEqual(extract(str(source), str(output)), 0)
            text = output.read_text(encoding='utf-8')
            self.assertEqual(text, 'before\n\ncontrolled\n\n| cell |\n|---|\n\nafter\n')

    def test_literal_stars_are_not_removed_when_merging_bold_runs(self):
        for runs, expected in [
            ('<w:r><w:t>口令是 ****，请原样输入。</w:t></w:r>', '口令是 ****，请原样输入。'),
            ('<w:r><w:rPr><w:b/></w:rPr><w:t>A</w:t></w:r>'
             '<w:r/>'
             '<w:r><w:rPr><w:b/></w:rPr><w:t>B</w:t></w:r>'
             '<w:r><w:t> ****</w:t></w:r>', '**AB** ****'),
        ]:
            with self.subTest(expected=expected):
                p = ET.fromstring(f'<w:p xmlns:w="{W[1:-1]}">{runs}</w:p>')
                self.assertEqual(para_text(p), expected)


class ValidatorAuditTests(unittest.TestCase):
    def test_single_outer_section_requires_an_independent_background(self):
        source = '<section style="background:#fff"><p><span leaf="">正文</span></p></section>'
        self.assertTrue(any('底色' in warning for warning in validate(source)[1]))
        covered = source.replace('<p>', '<p style="background:#fff">')
        self.assertEqual(validate(covered)[:2], ([], []))

    def test_punctuation_is_checked_across_inline_markup(self):
        for text in ['<span leaf="">这是</span><strong><span leaf="">重点</span></strong><span leaf="">,继续说明</span>',
                     '<span leaf="">重点</span><span leaf="">,</span>',
                     '<span leaf="">说</span><span leaf="">"</span><span leaf="">你好</span>']:
            source = '<section><p style="background:#fff">' + text + '</p></section>'
            with self.subTest(text=text):
                self.assertTrue(any('半角' in warning for warning in validate(source)[1]))

    def test_punctuation_keeps_numeric_contractions_and_code_exemptions(self):
        for text in ['<span leaf="">时间:</span><strong><span leaf="">30</span></strong>',
                     '<span leaf="">don</span><span leaf="">\'</span><span leaf="">t</span>',
                     '<span style="font-family:monospace"><span leaf="">中文,"code"</span></span>',
                     '<svg><text>中文,"SVG"</text></svg>']:
            source = '<section><p style="background:#fff">' + text + '</p></section>'
            with self.subTest(text=text):
                self.assertEqual(validate(source)[:2], ([], []))
        source = ('<section><p style="background:#fff"><span leaf="">中文</span></p>'
                  '<p style="background:#fff"><span leaf="">,English</span></p></section>')
        self.assertEqual(validate(source)[:2], ([], []))


@unittest.skipUnless(requests, 'requires requests')
class CleanupAuditTests(unittest.TestCase):
    def test_unchanged_or_partially_cleaned_readback_cannot_report_success(self):
        article = {'title': '标题', 'content': '<p>A&nbsp;&nbsp;B&nbsp;C</p>', 'thumb_media_id': 'cover'}
        for content in [article['content'], '<p>AB&nbsp;&nbsp;C</p>', '<p>ABC</p>']:
            with self.subTest(content=content), patch('requests.post', side_effect=[
                    response({'news_item': [article]}), response({'errcode': 0}),
                    response({'news_item': [dict(article, content=content)]})]):
                with self.assertRaises(draft.DraftVerificationError) as raised:
                    draft.cleanup_draft_nbsp('fake-token', 'existing')
                self.assertEqual(raised.exception.media_id, 'existing')

    def test_normalized_single_nbsp_is_accepted(self):
        article = {'title': '标题', 'content': '<p>A&nbsp;&nbsp;B&nbsp;C</p>', 'thumb_media_id': 'cover'}
        with patch('requests.post', side_effect=[response({'news_item': [article]}), response({'errcode': 0}),
                response({'news_item': [dict(article, content='<p>AB&#160;C</p>')]})]):
            self.assertEqual(draft.cleanup_draft_nbsp('fake-token', 'existing'), 'existing')


class OutputAuditTests(unittest.TestCase):
    def test_cli_input_errors_are_clean_and_nonzero(self):
        with tempfile.TemporaryDirectory() as directory:
            invalid = Path(directory) / 'invalid.html'
            invalid.write_bytes(b'\xff')
            for path in [Path(directory) / 'missing.html', invalid]:
                result = subprocess.run([sys.executable, str(ROOT / 'scripts/wechat_draft.py'),
                                         'cover', 'title', 'digest', '--html-file', str(path)], capture_output=True)
                with self.subTest(path=path.name):
                    self.assertEqual(result.returncode, 1)
                    self.assertNotIn(b'Traceback', result.stderr)
                    self.assertIn('失败', result.stderr.decode('utf-8'))

    def test_relocated_preview_resolves_resources_against_source(self):
        class Resources(HTMLParser):
            def __init__(self):
                super().__init__()
                self.base = ''
                self.image = ''
            def handle_starttag(self, tag, attrs):
                if tag == 'base':
                    self.base = dict(attrs)['href']
                elif tag == 'img':
                    self.image = dict(attrs)['src']

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_dir, output_dir = root / '文章 #1', root / 'previews'
            source_dir.mkdir(); output_dir.mkdir()
            source = source_dir / 'article.html'
            source.write_text('<section><img src="image.svg"></section>', encoding='utf-8')
            for preview in [output_dir / 'preview.html', source_dir / 'preview.html']:
                result = subprocess.run([sys.executable, str(ROOT / 'scripts/wrap_preview.py'),
                                         str(source), str(preview)], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                parser = Resources(); parser.feed(preview.read_text(encoding='utf-8'))
                resolved = urljoin(urljoin(preview.as_uri(), parser.base), parser.image)
                self.assertEqual(resolved, (source_dir / 'image.svg').as_uri())
                self.assertIn('<section><img src="image.svg"></section>', preview.read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
