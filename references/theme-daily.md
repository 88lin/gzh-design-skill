# 公众号排版组件库 —— 珊瑚日报 Daily

> **使用说明**：本组件库为「珊瑚日报」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：报纸 masthead 直系——顶部「双细线报头」（报名 + 日期卷期号夹在两条横线之间），多栏导语区，正文章节用「条目标题 + 双短线」的日报条目感。珊瑚红 `#C33D46`（报头/条目编号）、蜜黄 `#FBD97C`（荧光笔）、孔雀绿 `#2C7967`（次条目）。信息密度高于其它主题，适合资讯汇总、快讯合集、周报盘点。
>
> **与克莱因蓝展册 / 橄榄内刊的区别**：那些主题走「展册/杂志」的疏朗路线；Daily 走**报纸密度**——细线多、留白少、条目短、双栏感（用并排 flex 模拟）、报头是全篇唯一的大色块元素。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class、`position`、`float`、`display:grid`
> - ✅ 支持内联 `style`、`display:flex`（双栏条目用）
>
> **WeChat 兼容铁律**：
> - 装饰性空元素（双细线）内部放 `<span leaf=""><br></span>`
> - 双栏 flex 内每栏是独立 section，文字各自 `<span leaf="">` 包裹
> - 报头大字不打在 `<strong>` 上
> - 结构化区域没有内容时整块删掉

---

## 设计变量速查表

```
报纸底：        #FEFAF5
墨色正文：      #1F2226
次要文字：      #4A4A52
辅助文字：      #8A8A92
珊瑚红主色：    #C33D46（深 #9E2E38）
蜜黄强调：      #FBD97C / 蜜黄底 #FEF2D3
孔雀绿次色：    #2C7967 / 绿底 #E6F2EE
细线：          2px solid #1F2226（报头粗线）+ 1px solid rgba(31,34,38,.2)（正文细线）
报头字体：      Georgia,'Songti SC','Noto Serif SC',serif
正文字号：      16px（报纸密度），line-height:1.9
```

三色比例：墨色 85%、珊瑚红 10%（报头+编号+条目标题）、蜜黄/绿 5%。

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#FEFAF5;padding:36px 24px 32px;font-family:-apple-system,'PingFang SC','Helvetica Neue',sans-serif;color:#1F2226;font-size:16px;line-height:1.9;overflow-x:hidden;">
  <!-- 所有文章组件放在这里 -->
</section>
```

---

## 组件 2 报头（双细线 + 报名 + 日期行）

```html
<section style="margin-bottom:24px;">
  <section style="border-bottom:2px solid #1F2226;font-size:0;line-height:0;"><span leaf=""><br></span></section>
  <section style="display:flex;justify-content:space-between;align-items:center;padding:12px 2px;">
    <span style="font-family:Georgia,'Songti SC','Noto Serif SC',serif;font-size:26px;font-weight:900;color:#C33D46;letter-spacing:2px;"><span leaf="">茉灵日报</span></span>
    <span style="font-size:12px;color:#8A8A92;letter-spacing:1px;"><span leaf="">第 042 期 · 十月十五日</span></span>
  </section>
  <section style="border-bottom:1px solid #1F2226;font-size:0;line-height:0;"><span leaf=""><br></span></section>
</section>
```

---

## 组件 3 今日头条（大标题 + 导语）

```html
<section style="margin-bottom:26px;">
  <p style="margin:0 0 10px;font-family:Georgia,'Songti SC','Noto Serif SC',serif;font-size:24px;font-weight:900;line-height:1.6;color:#1F2226;word-break:normal;overflow-wrap:normal;">
    <span leaf="">本周 AI 圈，</span><br>
    <span leaf="">值得记住的 6 件事</span>
  </p>
  <p style="margin:0;font-size:15px;line-height:2;color:#4A4A52;text-align:justify;"><span leaf="">导语一到两句，说清这期日报的口径：<span style="background:linear-gradient(transparent 60%, #FBD97C 60%);font-weight:bold;padding:0 1px;">只挑真的值得记的，不凑数。</span></span></p>
</section>
```

---

## 组件 4 条目（编号 + 条目标题 + 正文，本主题核心组件）

```html
<section style="margin-bottom:22px;">
  <section style="display:flex;align-items:baseline;margin-bottom:6px;">
    <span style="font-family:Georgia,serif;font-size:20px;font-weight:900;color:#C33D46;margin-right:10px;"><span leaf="">01</span></span>
    <span style="font-size:17px;font-weight:900;color:#1F2226;"><span leaf="">条目标题，一句话说清事件</span></span>
  </section>
  <p style="margin:0;font-size:15px;line-height:1.9;color:#4A4A52;text-align:justify;">
    <span leaf="">条目正文两到三行，先事实后观点。</span>
    <span style="background:linear-gradient(transparent 60%, #FBD97C 60%);font-weight:bold;padding:0 1px;"><span leaf="">蜜黄标记一句关键判断。</span></span>
  </p>
</section>
```

次要条目（孔雀绿编号，弱一级）：

```html
<section style="margin-bottom:22px;">
  <section style="display:flex;align-items:baseline;margin-bottom:6px;">
    <span style="font-family:Georgia,serif;font-size:20px;font-weight:900;color:#2C7967;margin-right:10px;"><span leaf="">05</span></span>
    <span style="font-size:17px;font-weight:900;color:#1F2226;"><span leaf="">次要条目标题</span></span>
  </section>
  <p style="margin:0;font-size:15px;line-height:1.9;color:#4A4A52;text-align:justify;"><span leaf="">正文。</span></p>
</section>
```

条目分级原则：重要条目珊瑚红编号，一般条目孔雀绿编号，每期红 3-4 条、绿 2-3 条。

---

## 组件 5 双栏短条目（两条并排，报纸多栏感）

```html
<section style="display:flex;margin-bottom:22px;">
  <section style="flex:1;padding-right:14px;">
    <section style="margin-bottom:6px;">
      <span style="font-family:Georgia,serif;font-size:18px;font-weight:900;color:#C33D46;"><span leaf="">07</span></span>
      <span style="font-size:15px;font-weight:900;color:#1F2226;"><span leaf="">左栏标题</span></span>
    </section>
    <p style="margin:0;font-size:14px;line-height:1.9;color:#4A4A52;text-align:justify;"><span leaf="">左栏短正文。</span></p>
  </section>
  <section style="flex:1;padding-left:14px;border-left:1px solid rgba(31,34,38,.2);">
    <section style="margin-bottom:6px;">
      <span style="font-family:Georgia,serif;font-size:18px;font-weight:900;color:#2C7967;"><span leaf="">08</span></span>
      <span style="font-size:15px;font-weight:900;color:#1F2226;"><span leaf="">右栏标题</span></span>
    </section>
    <p style="margin:0;font-size:14px;line-height:1.9;color:#4A4A52;text-align:justify;"><span leaf="">右栏短正文。</span></p>
  </section>
</section>
```

双栏只放短条目（正文 ≤2 行），长条目一律用组件 4。

---

## 组件 6 分版线（章节间：细线 + 版块名）

```html
<section style="margin:30px 0 22px;">
  <section style="display:flex;align-items:center;margin-bottom:14px;">
    <span style="font-size:13px;font-weight:900;letter-spacing:4px;color:#C33D46;margin-right:12px;"><span leaf="">▎产品版</span></span>
    <section style="flex:1;border-bottom:1px solid rgba(31,34,38,.2);font-size:0;line-height:0;"><span leaf=""><br></span></section>
  </section>
</section>
```

版块名可换：▎模型版 / ▎工具版 / ▎观点版 / ▎生活版。

---

## 组件 7 编者按框（蜜黄底，全篇一张）

```html
<section style="margin:24px 0;padding:16px 18px;background:#FEF2D3;border-radius:10px;">
  <p style="margin:0;font-size:14px;line-height:1.9;color:#1F2226;text-align:justify;"><span leaf="">✍️ 编者按：放在头条之后或日报末尾，说一段「为什么选这 6 件」的编辑逻辑。</span></p>
</section>
```

---

## 组件 8 图片（报纸图：细边框 + 图注）

```html
<span leaf=""><img src="{{图片URL}}" style="width:100%;border:1px solid rgba(31,34,38,.2);border-radius:4px;margin-bottom:6px;"></span>
<section style="text-align:center;margin-bottom:20px;">
  <span style="font-size:12px;color:#8A8A92;"><span leaf="">▲ {{图片说明}}（图源：{{来源}}）</span></span>
</section>
```

---

## 组件 9 订阅收尾条（深底反白）

```html
<section style="margin:30px 0 0;padding:18px 20px;background:#FFF4D6;border:1px solid #F8E6B0;border-radius:10px;text-align:center;">
  <p style="margin:0 0 6px;font-size:15px;font-weight:900;color:#92600A;"><span leaf="">每天 3 分钟，看懂 AI 圈</span></p>
  <p style="margin:0;font-size:13px;color:#C9C9D0;"><span leaf="">关注茉灵智库，下期日报准时送达 📰</span></p>
</section>
```

---

## 组件 10 签名档

```html
<section style="text-align:center;padding:18px 0 0;">
  <p style="margin:0 0 4px;font-size:14px;font-weight:bold;color:#1F2226;"><span leaf="">作者名</span></p>
  <p style="margin:0;font-size:12px;color:#8A8A92;line-height:1.8;">
    <span leaf="">▪️{{签名第一行}}</span><br>
    <span leaf="">▪️{{签名第二行}}</span>
  </p>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background:#FEFAF5;padding:36px 24px 32px;...">
  <!-- 1. 报头（组件 2） -->
  <!-- 2. 今日头条（组件 3） -->
  <!-- 3. 编者按（组件 7，可选） -->
  <!-- 4. 分版线（组件 6）→ 条目 ×3-4（组件 4） -->
  <!-- 5. 双栏短条目（组件 5，一组放两条短的） -->
  <!-- 6. 图片（组件 8，穿插） -->
  <!-- 7. 下一版块…（重复 4-6） -->
  <!-- 8. 编者按（组件 7，或放这里收束） -->
  <!-- 9. 订阅收尾条（组件 9） -->
  <!-- 10. 签名档（组件 10） -->
</section>
```

**节奏铁律**：报头唯一；每期 6-8 个条目（红 3-4 + 绿 2-3）；双栏组只一组或两组；编者按 ≤2；细线密度是其它主题的两倍——这正是报纸感来源，不要为了留白删细线。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **报头层** | 双细线 + 报名 + 头条大字 | 开场定调 | 全篇 1 次 |
| **条目层** | 编号 + 条目标题 + 短正文 | 信息主体 | 6-8 条 |
| **辅助层** | 分版线 / 编者按 / 双栏 | 结构与节奏 | 每版块 1 条线 |

---

## 文章类型 → 组件组合配方

| 文章类型 | 核心组合 | 点缀 |
|---|---|---|
| 资讯日报 | 全套按模板骨架走 | 图 8 |
| 周报盘点 | 报头 2 + 条目 4 ×6 | 编者按 7 |
| 快讯合集 | 条目 4 + 双栏 5 | 订阅条 9 |
| 版块型栏目 | 分版线 6 分 2-3 版 | 编者按 7 |

---

## Markdown → 珊瑚日报 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 组件 2 报头 + 组件 3 头条 | 报名固定，期号按日期 |
| `## 版块` | 组件 6 分版线 | |
| `### 条目` | 组件 4 条目 | 红绿编号分级 |
| 短消息两条 | 组件 5 双栏 | |
| `> 编者按` | 组件 7 | |
| `**加粗**` | 蜜黄荧光笔 span | |
| `![](图片)` | 组件 8 报纸图 | |
| 行内 `` `code` `` | `background:#FEF2D3;color:#9E2E38` 等宽胶囊 | |
| ` ``` 代码块 ``` ` | 通用库 1a/1b | |
| `[text](url)` | 通用库 4a/4b（角标珊瑚红 `#C33D46`） | |
| 文末 | 组件 9 订阅条 + 10 签名档 | |
