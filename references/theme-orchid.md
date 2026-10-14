# 公众号排版组件库 —— 藕荷 Orchid

> **使用说明**：本组件库为「藕荷」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：源自品牌配色 G「藕荷 Orchid」——梦幻兰紫配奶油黄，甜而不腻；朱砂点缀拉出精神。暖白底、大圆角软卡、衬线标题、花瓣圆点。适合创作分享、美学随笔、女性向干货、个人成长。气质关键词：梦幻但压得住。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id、`position:fixed/absolute`、`float`、`@media`/`@keyframes`、`display:grid`
> - ✅ 支持内联 `style`、`display:flex`（有限）、`linear-gradient`、`border-radius`、`box-shadow`、`<section>/<p>/<span>/<strong>/<img>` 等基础标签
>
> **WeChat 兼容铁律**（本主题组件全部已按此写好，改动时必须遵守）：
> - 所有"装饰性空元素"（圆点、渐变分割线、花瓣点、装饰线）**必须在内部放 `<span leaf=\"\"><br></span>` 占位**，否则微信会剥掉样式
> - **不要把 `font-size`/`border-bottom` 打在 `<strong>` 上**，也不要在同一个 `<p>` 里混多个不同 `font-size`——微信编辑器会自动"纠正"导致样式被重写。正确做法：拆成多个 `<p>`，每个 `<p>` 只有一个字号；高亮样式统一挂在外层 `<span>` 上
> - 不用 `position:absolute` 做划线/高亮，删除线用 `text-decoration:line-through`
> - 引用/提示块用**圆角软底卡**，不用左竖条（Notion 感）也不用四周虚线框
> - 结构化区域没有内容时**整块删掉**，不留空 section

---

## 设计变量速查表

```
主色调：       #8A2F84（兰紫）
主色深：       #662061（深兰紫）
主色浅：       #C356BC（兰紫浅调）
兰紫浅底：     #F6E9F5（提示/引用软底）
兰紫浅边：     #ECD8EA
奶油高亮：     #F7DEA4（下划线/荧光笔，强调色 30%）
奶油浅底：     #FAF1DE（浅底提示）
朱砂点缀：     #BF4436（点缀 10%，小标签/数据/强调）
朱砂浅底：     #FBE9E6
暖白背景：     #FDFBF9
卡片底：       #FEFDFC
暖灰浅底：     #F5EFE7（旁注）
标题色：       #2D1D2C（暖黑，非纯黑）
正文色：       #594057（暖灰）
次要文字：     #746174
辅助文字：     #A99CA6（浅暖灰）
边框/发丝线：  #ECD8EA / #F3E7F1
衬线标题字体： Georgia,'Noto Serif SC','Songti SC',serif
正文无衬线：   -apple-system,'PingFang SC','Microsoft YaHei',sans-serif
```

三色比例：兰紫 60% · 奶油黄 30% · 朱砂 10%。朱砂只出现在小标签、数据数字、重点锚点。

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#FDFBF9;color:#594057;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.8;letter-spacing:0.4px;overflow-x:hidden;">
  <!-- 所有文章组件放在这里 -->
</section>
```

---

## 组件 2 开头引言卡片（兰紫渐变卡）

> 观点/随笔的默认封面级引言卡：兰紫渐变 + 衬线白字，每篇最多一个。

```html
<section style="margin:12px 10px 32px;padding:28px 22px 24px;background:linear-gradient(135deg,#8A2F84 0%,#662061 100%);border-radius:16px;">
  <p style="margin:0 0 14px;font-family:Georgia,'Noto Serif SC',serif;font-size:10px;color:#F0D9EE;letter-spacing:2px;"><span leaf="">ORCHID NOTES ✦</span></p>
  <p style="margin:0;font-family:Georgia,'Noto Serif SC','Songti SC',serif;font-size:18px;font-weight:600;color:#FFFFFF;line-height:1.85;">
    <span leaf="">Agent 不是抹平差距，而是在</span>
    <span style="border-bottom:2px solid #F7DEA4;"><span leaf="">放大</span></span>
    <span leaf="">它。而 Skill，是把经验变成</span>
    <span style="border-bottom:2px solid #F7DEA4;"><span leaf="">能力商品</span></span>
    <span leaf="">的那道桥。</span>
  </p>
</section>
```

浅色变体（一篇想更素净时用）：

```html
<section style="margin:12px 10px 32px;padding:26px 22px 22px;background:#FEFDFC;border:1px solid #ECD8EA;border-radius:16px;">
  <section style="margin-bottom:14px;">
    <span style="display:inline-block;width:7px;height:7px;background:#8A2F84;border-radius:50%;font-size:0;line-height:0;"><span leaf=""><br></span></span>
    <span style="display:inline-block;width:56px;height:1px;background:#ECD8EA;margin:0 0 0 8px;font-size:0;line-height:0;vertical-align:middle;"><span leaf=""><br></span></span>
    <span style="margin-left:8px;font-family:Georgia,'Noto Serif SC',serif;font-size:10px;color:#C356BC;letter-spacing:2px;"><span leaf="">MOMENT ✦</span></span>
  </section>
  <p style="margin:0;font-family:Georgia,'Noto Serif SC','Songti SC',serif;font-size:18px;font-weight:600;color:#2D1D2C;line-height:1.8;">
    <span leaf="">引言金句占位，关键词用</span>
    <span style="border-bottom:2px solid #F7DEA4;"><span leaf="">奶油黄下划线</span></span>
    <span leaf="">标记。</span>
  </p>
</section>
```

---

## 组件 3 前言导读（本文看点）

```html
<section style="margin:0 10px 32px;padding:20px 18px;background:#F6E9F5;border-radius:16px;">
  <p style="margin:0 0 14px;font-size:11px;color:#8A2F84;font-weight:700;letter-spacing:2px;"><span leaf="">本文看点 · CONTENTS</span></p>
  <section style="margin-bottom:10px;">
    <span style="display:inline-block;font-family:Georgia,'Noto Serif SC',serif;font-size:15px;color:#BF4436;font-weight:700;margin-right:8px;"><span leaf="">01</span></span>
    <span style="font-size:14px;color:#2D1D2C;font-weight:600;"><span leaf="">Skill 是能力商品</span></span>
  </section>
  <section style="margin-bottom:10px;">
    <span style="display:inline-block;font-family:Georgia,'Noto Serif SC',serif;font-size:15px;color:#BF4436;font-weight:700;margin-right:8px;"><span leaf="">02</span></span>
    <span style="font-size:14px;color:#2D1D2C;font-weight:600;"><span leaf="">经验如何被外化</span></span>
  </section>
  <section>
    <span style="display:inline-block;font-family:Georgia,'Noto Serif SC',serif;font-size:15px;color:#BF4436;font-weight:700;margin-right:8px;"><span leaf="">03</span></span>
    <span style="font-size:14px;color:#2D1D2C;font-weight:600;"><span leaf="">复利飞轮</span></span>
  </section>
</section>
```

---

## 组件 4 章节分割线（兰紫渐变 + 花瓣点）

```html
<section style="margin:36px 10px;display:flex;align-items:center;">
  <span style="flex:1;height:1px;background:linear-gradient(to right,transparent,#ECD8EA);font-size:0;line-height:0;"><span leaf=""><br></span></span>
  <span style="display:inline-block;width:7px;height:7px;background:#C356BC;border-radius:50% 50% 50% 2px;margin:0 12px;font-size:0;line-height:0;"><span leaf=""><br></span></span>
  <span style="flex:1;height:1px;background:linear-gradient(to left,transparent,#ECD8EA);font-size:0;line-height:0;"><span leaf=""><br></span></span>
</section>
```

---

## 组件 5 章节标题（兰紫渐变圆标 + 衬线大标题）

> 第一章 `margin-top:20px`，后续 `margin-top:48px`。

```html
<section style="margin:48px 10px 24px;">
  <section style="display:flex;align-items:center;margin-bottom:6px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;background:linear-gradient(135deg,#8A2F84,#662061);color:#FFFFFF;font-family:Georgia,'Noto Serif SC',serif;font-size:16px;font-weight:700;border-radius:12px 12px 12px 2px;margin-right:12px;flex-shrink:0;"><span leaf="">01</span></span>
    <span style="font-size:10px;color:#C356BC;letter-spacing:2px;font-weight:600;"><span leaf="">CAPABILITY · 商品</span></span>
  </section>
  <h3 style="margin:0;font-family:Georgia,'Noto Serif SC','Songti SC',serif;font-size:21px;font-weight:700;color:#2D1D2C;line-height:1.5;">
    <span leaf="">Skill 是能力商品</span>
  </h3>
</section>
```

结语章变体（编号 `∞`、英文标签 `THE END`）：

```html
<span style="display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;background:linear-gradient(135deg,#8A2F84,#662061);color:#FFFFFF;font-family:Georgia,'Noto Serif SC',serif;font-size:18px;font-weight:700;border-radius:12px 12px 12px 2px;margin-right:12px;flex-shrink:0;"><span leaf="">∞</span></span>
```

---

## 组件 6 正文段落

> 每段主动标 1~3 个关键短语，用**奶油黄下划线（7d）**——本主题标志性标记。

```html
<p style="margin:0 10px 20px;font-size:16px;line-height:1.85;color:#594057;text-align:justify;">
  <span leaf="">我最近几次聊 Skills，有一个越来越明确的判断：大家都在说 Agent，但</span>
  <span style="border-bottom:2px solid #F7DEA4;font-weight:600;color:#2D1D2C;"><span leaf="">大多数人还没真正理解它</span></span>
  <span leaf="">。Agent 不是简单抹平能力差距，</span>
  <strong style="color:#662061;"><span leaf="">而是在放大能力差距</span></strong>
  <span leaf="">。</span>
</p>
```

---

## 组件 6b 子标题（`###` 小节标题）

```html
<section style="margin:28px 10px 14px;display:flex;align-items:center;">
  <span style="display:inline-block;width:8px;height:8px;background:#8A2F84;border-radius:50% 50% 50% 2px;margin-right:10px;font-size:0;line-height:0;flex-shrink:0;"><span leaf=""><br></span></span>
  <span style="font-family:Georgia,'Noto Serif SC','Songti SC',serif;font-size:17px;font-weight:700;color:#2D1D2C;"><span leaf="">一个设计类 Skill 的例子</span></span>
</section>
```

---

## 组件 7 正文高亮样式（6 种变体）

### 7a. 加粗强调

普通加粗（默认）：

```html
<strong style="color:#2D1D2C;"><span leaf="">普通加粗强调</span></strong>
```

兰紫加粗（锚点 ≤5 处/篇）：

```html
<strong style="color:#662061;"><span leaf="">兰紫加粗锚点</span></strong>
```

### 7b. 兰紫浅底标签（核心概念，每篇 2~4 个）

```html
<span style="background:#F6E9F5;color:#662061;padding:2px 8px;border-radius:999px;font-weight:700;font-size:15px;"><span leaf="">核心概念标签</span></span>
```

### 7c. 朱砂标签（点缀，每篇 ≤3 个）

```html
<span style="background:#FBE9E6;color:#913128;padding:2px 8px;border-radius:999px;font-weight:700;font-size:15px;"><span leaf="">朱砂点缀标签</span></span>
```

### 7d. 奶油黄下划线（最常用，本风格标志性标记）

```html
<span style="border-bottom:2px solid #F7DEA4;font-weight:600;color:#2D1D2C;"><span leaf="">奶油黄下划线关键词</span></span>
```

### 7e. 荧光笔效果（偶尔用于长句强调）

```html
<span style="background:linear-gradient(180deg,transparent 60%,#FAEAC0 60%);font-weight:700;color:#2D1D2C;"><span leaf="">荧光笔效果的重要长句</span></span>
```

### 7f. 行内代码

```html
<span style="background:#F5EFE7;color:#662061;padding:1px 7px;border-radius:6px;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:15px;"><span leaf="">SKILL.md</span></span>
```

---

## 组件 8 引用块（圆角软底卡，无竖条）

### 8a. 兰紫金句卡（视觉焦点，核心金句）

```html
<section style="margin:0 10px 24px;padding:20px 22px;background:linear-gradient(135deg,#8A2F84 0%,#662061 100%);border-radius:16px;">
  <p style="margin:0 0 8px;font-family:Georgia,'Noto Serif SC',serif;font-size:22px;line-height:1;color:#C356BC;"><span leaf="">“</span></p>
  <p style="margin:0;font-family:Georgia,'Noto Serif SC','Songti SC',serif;font-size:16px;font-weight:600;color:#FFFFFF;line-height:1.9;text-align:justify;"><span leaf="">「真正值得被看见的，不只是答案，还有答案背后的判断方式。」</span></p>
</section>
```

### 8b. 兰紫浅底引用卡（Prompt / 引用内容）

```html
<section style="margin:0 10px 24px;padding:16px 20px;background:#F6E9F5;border-radius:16px;">
  <p style="margin:0;font-size:15px;color:#594057;line-height:1.8;text-align:justify;"><span leaf="">引用内容占位：Prompt、摘录或需要完整呈现的材料。</span></p>
</section>
```

### 8c. 暖灰软卡旁注（轻量吐槽/注解）

```html
<section style="margin:0 10px 24px;padding:14px 20px;background:#F5EFE7;border-radius:16px;">
  <p style="margin:0;font-size:14px;color:#746174;line-height:1.8;text-align:justify;"><span leaf="">旁注占位：轻量的个人吐槽或补充说明。</span></p>
</section>
```

### 8d. 居中过渡金句（章节之间）

```html
<section style="margin:32px 10px;padding:18px 14px;text-align:center;border-top:1px solid #ECD8EA;border-bottom:1px solid #ECD8EA;">
  <p style="margin:0;font-family:Georgia,'Noto Serif SC','Songti SC',serif;font-size:16px;font-weight:600;color:#8A2F84;line-height:1.8;"><span leaf="">让一段思考，在章节之间停留片刻。</span></p>
</section>
```

---

## 组件 9 提示 / 警示条

### 9a. 兰紫提示卡（重要提醒）

```html
<section style="margin:0 10px 24px;padding:15px 20px;background:#F6E9F5;border-radius:16px;">
  <p style="margin:0;font-size:15px;font-weight:700;color:#662061;line-height:1.8;"><span leaf="">💡 重要提示内容占位。</span></p>
</section>
```

### 9b. 轻提醒（暖灰软卡 + 朱砂标签）

```html
<section style="margin:0 10px 24px;padding:13px 20px;background:#F5EFE7;border-radius:16px;">
  <p style="margin:0 0 4px;font-size:12px;font-weight:700;color:#BF4436;letter-spacing:1px;"><span leaf="">！踩坑提示</span></p>
  <p style="margin:0;font-size:14px;color:#594057;line-height:1.7;text-align:justify;"><span leaf="">提示内容占位。</span></p>
</section>
```

---

## 组件 10 内容标签组（STEP / SKILL / TOOL / CASE）

### 10a. step-label（教程步骤）

```html
<section style="margin:0 10px 22px;">
  <section style="display:flex;align-items:center;margin-bottom:10px;">
    <span style="display:inline-block;background:#8A2F84;color:#FFFFFF;font-size:11px;font-weight:700;padding:3px 10px;border-radius:999px;margin-right:10px;"><span leaf="">STEP 01</span></span>
    <span style="font-size:16px;font-weight:700;color:#2D1D2C;"><span leaf="">步骤标题占位</span></span>
  </section>
  <p style="margin:0;font-size:16px;color:#594057;line-height:1.8;text-align:justify;"><span leaf="">步骤内容占位。</span></p>
</section>
```

### 10b. tool-card（工具/条目软卡）

```html
<section style="margin:0 10px 16px;padding:15px 20px;background:#FEFDFC;border:1px solid #ECD8EA;border-radius:16px;">
  <section style="display:flex;align-items:center;margin-bottom:6px;">
    <span style="display:inline-block;width:6px;height:6px;background:#C356BC;border-radius:50% 50% 50% 2px;margin-right:8px;font-size:0;line-height:0;"><span leaf=""><br></span></span>
    <span style="font-size:15px;font-weight:700;color:#2D1D2C;"><span leaf="">条目标题占位</span></span>
  </section>
  <p style="margin:0;font-size:14px;color:#746174;line-height:1.75;text-align:justify;"><span leaf="">条目说明占位。</span></p>
</section>
```

---

## 组件 11 列表组件

### 11a. ordered-list（兰紫圆标编号列表）

```html
<section style="margin:0 10px 24px;">
  <section style="display:flex;align-items:flex-start;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#8A2F84;color:#FFFFFF;font-size:12px;font-weight:700;border-radius:50% 50% 50% 2px;flex-shrink:0;margin-top:2px;margin-right:10px;"><span leaf="">1</span></span>
    <p style="font-size:16px;color:#594057;margin:0;line-height:1.8;flex:1;text-align:justify;"><span leaf="">列表项内容占位。</span></p>
  </section>
  <section style="display:flex;align-items:flex-start;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#C356BC;color:#FFFFFF;font-size:12px;font-weight:700;border-radius:50% 50% 50% 2px;flex-shrink:0;margin-top:2px;margin-right:10px;"><span leaf="">2</span></span>
    <p style="font-size:16px;color:#594057;margin:0;line-height:1.8;flex:1;text-align:justify;"><span leaf="">列表项内容占位。</span></p>
  </section>
  <section style="display:flex;align-items:flex-start;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#BF4436;color:#FFFFFF;font-size:12px;font-weight:700;border-radius:50% 50% 50% 2px;flex-shrink:0;margin-top:2px;margin-right:10px;"><span leaf="">3</span></span>
    <p style="font-size:16px;color:#594057;margin:0;line-height:1.8;flex:1;text-align:justify;"><span leaf="">列表项内容占位（末项后不留 margin）。</span></p>
  </section>
</section>
```

### 11b. pill-list（无序要点，花瓣圆点 + 说明）

```html
<section style="margin:0 10px 14px;">
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;font-size:15px;font-weight:700;color:#662061;background:#F6E9F5;padding:3px 12px;border-radius:999px;"><span style="display:inline-block;width:6px;height:6px;background:#8A2F84;border-radius:50% 50% 50% 2px;margin-right:5px;vertical-align:middle;font-size:0;line-height:0;"><span leaf=""><br></span></span><span leaf="">要点标题占位</span></span>
  </p>
  <p style="font-size:15px;color:#746174;margin:0;line-height:1.75;text-align:justify;"><span leaf="">要点说明占位。</span></p>
</section>
```

### 11c. timeline（时间线 / 经历脉络，兰紫圆点）

```html
<section style="margin:0 10px 24px;display:flex;">
  <section style="display:flex;flex-direction:column;align-items:center;margin-right:14px;flex-shrink:0;">
    <section style="width:12px;height:12px;border-radius:50% 50% 50% 2px;background:#8A2F84;margin-top:5px;font-size:0;line-height:0;"><span leaf=""><br></span></section>
    <section style="width:2px;background:#ECD8EA;flex:1;margin-top:4px;min-height:44px;font-size:0;line-height:0;"><span leaf=""><br></span></section>
  </section>
  <section style="flex:1;padding-bottom:14px;">
    <p style="margin:0 0 5px;font-size:16px;font-weight:700;color:#2D1D2C;"><span leaf="">节点标题占位</span></p>
    <p style="margin:0;font-size:15px;color:#594057;line-height:1.8;text-align:justify;"><span leaf="">节点内容占位。</span></p>
  </section>
</section>
```

最后一个节点去掉竖线段。

---

## 组件 12 数据 / 要点卡片组

### 两列版（兰紫/朱砂交替）

```html
<section style="margin:0 10px 24px;display:flex;">
  <section style="flex:1;background:#F6E9F5;border-radius:16px;padding:18px 14px;margin-right:8px;text-align:center;">
    <p style="font-size:26px;font-weight:900;color:#8A2F84;margin:0 0 4px;font-family:Georgia,'Noto Serif SC',serif;"><span leaf="">92%</span></p>
    <p style="font-size:12px;color:#A99CA6;margin:0;"><span leaf="">说明占位</span></p>
  </section>
  <section style="flex:1;background:#FBE9E6;border-radius:16px;padding:18px 14px;text-align:center;">
    <p style="font-size:26px;font-weight:900;color:#BF4436;margin:0 0 4px;font-family:Georgia,'Noto Serif SC',serif;"><span leaf="">3×</span></p>
    <p style="font-size:12px;color:#A99CA6;margin:0;"><span leaf="">说明占位</span></p>
  </section>
</section>
```

### 表格（真实数据表用）

```html
<section style="margin:0 10px 24px;overflow-x:auto;">
  <table style="width:100%;border-collapse:collapse;font-size:14px;">
    <thead>
      <tr>
        <th style="background:#8A2F84;color:#FFFFFF;font-weight:700;padding:9px 12px;text-align:left;"><span leaf="">列标题</span></th>
        <th style="background:#8A2F84;color:#FFFFFF;font-weight:700;padding:9px 12px;text-align:left;"><span leaf="">列标题</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:9px 12px;border-bottom:1px solid #ECD8EA;color:#594057;"><span leaf="">内容占位</span></td>
        <td style="padding:9px 12px;border-bottom:1px solid #ECD8EA;color:#594057;"><span leaf="">内容占位</span></td>
      </tr>
      <tr>
        <td style="padding:9px 12px;border-bottom:1px solid #ECD8EA;color:#594057;background:#F6E9F5;"><span leaf="">内容占位</span></td>
        <td style="padding:9px 12px;border-bottom:1px solid #ECD8EA;color:#594057;background:#F6E9F5;"><span leaf="">内容占位</span></td>
      </tr>
    </tbody>
  </table>
</section>
```

---

## 组件 13 标签胶囊

兰紫浅底（默认）：

```html
<span style="display:inline-block;background:#F6E9F5;color:#662061;font-size:12px;font-weight:700;padding:2px 11px;border-radius:999px;margin:0 6px 6px 0;"><span leaf="">标签名</span></span>
```

朱砂浅底（点缀）：

```html
<span style="display:inline-block;background:#FBE9E6;color:#913128;font-size:12px;font-weight:700;padding:2px 11px;border-radius:999px;margin:0 6px 6px 0;"><span leaf="">标签名</span></span>
```

---

## 组件 14 图片容器

> 图片直接放容器里，**不要再套一层 `<section style="overflow:hidden">`**——公众号编辑器会剥离嵌套 section 的样式。

```html
<section style="background:#FEFDFC;border-radius:16px;padding:6px;border:1px solid #ECD8EA;margin:0 10px 10px;text-align:center;">
  <span leaf=""><img src="{{图片URL}}" style="max-width:100%;height:auto;display:block;margin:0 auto;border-radius:12px;"></span>
</section>
```

带说明文字时，其后加：

```html
<p style="font-size:12px;color:#A99CA6;text-align:center;margin:0 10px 24px;"><span leaf="">— {{图片说明}}</span></p>
```

多行代码块用通用库 `common-components.md` 的 1a 深色 / 1b 浅色（1b 左竖条换 `#8A2F84`、底色换 `#F6E9F5`、边框换 `#ECD8EA`），禁 `white-space:pre`。

---

## 组件 15 END 结尾分割线

```html
<section style="margin:0 10px;">
  <section style="text-align:center;margin:0 0 28px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:1px;width:54px;background:linear-gradient(to right,transparent,#ECD8EA);margin-right:12px;font-size:0;line-height:0;"><span leaf=""><br></span></span>
      <span style="font-family:Georgia,'Noto Serif SC',serif;font-size:11px;color:#C356BC;letter-spacing:4px;font-weight:600;"><span leaf="">✦ END ✦</span></span>
      <span style="height:1px;width:54px;background:linear-gradient(to left,transparent,#ECD8EA);margin-left:12px;font-size:0;line-height:0;"><span leaf=""><br></span></span>
    </section>
  </section>
</section>
```

---

## 组件 16 尾部作者签名区（含互动三连卡）

```html
<section style="margin:0 10px;padding:22px 20px;background:linear-gradient(135deg,#8A2F84 0%,#662061 100%);border-radius:16px;">
  <p style="margin:0 0 12px;font-size:16px;line-height:1.85;color:#FFFFFF;text-align:justify;">
    <span leaf="">我是 {{作者名}}，{{一句话简介，如：专注 AI 观察与知识干货}}。</span>
  </p>
  <p style="margin:0 0 16px;font-size:16px;line-height:1.85;color:#FFFFFF;text-align:justify;">
    <span leaf="">如果你觉得今天这篇有收获，欢迎</span>
    <strong style="color:#F7DEA4;"><span leaf="">点赞、转发、推荐</span></strong>
    <span leaf="">三连，我们下篇见。</span>
  </p>
  <p style="margin:0;text-align:center;">
    <span style="display:inline-block;margin:0 4px;padding:6px 14px;background:#FFFFFF;color:#8A2F84;border-radius:999px;font-size:12px;font-weight:700;"><span leaf="">点赞</span></span>
    <span style="display:inline-block;margin:0 4px;padding:6px 14px;background:#F7DEA4;color:#662061;border-radius:999px;font-size:12px;font-weight:700;"><span leaf="">转发</span></span>
    <span style="display:inline-block;margin:0 4px;padding:6px 14px;border:1px solid #FFFFFF;color:#FFFFFF;border-radius:999px;font-size:12px;font-weight:700;"><span leaf="">推荐</span></span>
  </p>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background:#FDFBF9;color:#594057;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.8;letter-spacing:0.4px;overflow-x:hidden;">

  <!-- 1. 开头引言卡（组件 2，渐变版或浅色版二选一） -->
  <!-- 2. 前言正文（组件 6 × N） -->
  <!-- 3. 前言导读（组件 3，3+ 章节时生成） -->
  <!-- 4. 第一章（组件 5，margin-top:20px） -->
  <!--    章内：组件 6 正文 + 6b 子标题 + 7 高亮 + 8 引用 + 9 提示 + 10 标签组 + 11 列表 + 12 数据 + 14 图片 -->
  <!-- 5. 章节分割线（组件 4）+ 第二章…第N章（组件 5，margin-top:48px） -->
  <!-- 6. 结语章（组件 5 变体：∞ + THE END） -->
  <!-- 7. END 分割线（组件 15） -->
  <!-- 8. 尾部签名（组件 16） -->

</section>
```

**骨架铁律**：引言卡在最前（渐变版每篇最多一个）；导读在前言正文之后、第一章之前；章节之间用组件 4 花瓣渐变线分隔；一篇只有一个 END + 一个签名区；深色渐变卡（2 渐变版 / 8a / 16）不连续出现。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 兰紫加粗 7a / 金句卡 8a / 渐变章节头 5 | 核心结论、产品名、关键金句 | 全文 ≤5 处 |
| **标记层** | 奶油黄下划线 7d（默认）/ 兰紫浅底标签 7b | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | 软底引用卡 8x / 提示卡 9x / 标签组 10 / 卡片 11-12 | 引用、旁注、提示、结构化信息 | 按需 |

**克制原则**：
- 三色比例兰紫 60% · 奶油黄 30% · 朱砂 10%；朱砂每篇 ≤3 处
- 引用/提示用**圆角软底卡**，不用左竖条、不用四周虚线框
- 文字永远非纯黑（`#2D1D2C` 起），背景永远暖白（`#FDFBF9` 起）

---

## 文章类型 → 组件组合配方

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 创作/美学分享 | 正文6 + tool-card 10b + pill-list 11b | 数据卡12、标签胶囊13 |
| 个人成长随笔 | 正文6 + 金句卡8a + 居中金句8d | 暖灰旁注8c |
| 温柔系教程 | step-label 10a + 代码块(通用1a/1b) + ordered-list 11a | 兰紫提示9a |
| 观点/深度分析 | 正文6 + 金句卡8a + 居中金句8d | 踩坑提示9b |
| 盘点/清单 | tool-card 10b + pill-list 11b + 标签胶囊13 | 数据卡12 |
| 访谈/人物特稿 | 正文6 + 金句卡8a + timeline 11c | 居中金句8d |

所有类型共用固定结构：引言卡 2 + 导读 3（3+ 章节）+ 编号章节 5 + END 15 + 签名 16。

---

## Markdown → 藕荷排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| 文章开头 `> 引言金句` | 组件 2 引言卡（渐变版或浅色版） | |
| `## 章节标题` | 组件 5 章节标题 | 渐变圆标 01/02…，末章 ∞ + THE END |
| `### 子标题` | 组件 6b 花瓣点衬线子标题 | 不套编号章节样式 |
| 普通段落 | 组件 6 正文段落 | 每段标 1~3 处奶油黄下划线 7d |
| `**加粗文字**` | 组件 7a 普通加粗（默认）/ 兰紫加粗（锚点 ≤5） | |
| `==高亮文字==` | 组件 7b 兰紫浅底标签 | 核心概念 |
| `<u>下划线</u>` / `++文字++` | 组件 7d 奶油黄下划线 | 次要强调 |
| `~~删除线~~` | `text-decoration:line-through` + `#A99CA6` | |
| 行内 `` `code` `` | 组件 7f 行内代码 | |
| `> 引用段落`（金句） | 组件 8a 金句卡 | |
| `> 引用段落`（旁注） | 组件 8c 暖灰软卡 | |
| 操作步骤 | 组件 10a step-label | STEP 01/02… |
| 工具/条目 | 组件 10b tool-card | |
| 案例/经历脉络 | 组件 11c timeline | |
| ` ``` 多行代码块 ``` ` | 通用库 1a 深色 / 1b 浅色（左竖条换 `#8A2F84`） | 每行一个 `<p style="margin:0">` |
| 并列要点 | 组件 11b pill-list | |
| `1. 2. 3.` 编号列表 | 组件 11a ordered-list | 兰紫/浅紫/朱砂圆标 |
| 数据展示 | 组件 12 数据卡（兰紫/朱砂交替）/ 表格 | |
| 注意/警告 | 组件 9a 兰紫提示 / 9b 轻提醒 | |
| 行内标签 | 组件 13 标签胶囊 | |
| `---` | 组件 4 章节分割线 | |
| `![](图片)` | 组件 14 图片容器 | 圆角卡 + 说明 |
| `[text](url)` 超链接 | 通用库 4a 上标角标 + 4b 参考资料列表 | 角标套兰紫 `#8A2F84` |
| 文末 | 组件 15 END + 16 签名 | |
