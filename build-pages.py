#!/usr/bin/env python3
"""从一张文案表生成四个语言的落地页。

为什么要一个语言一页：og 标签是静态 HTML、由爬虫读取，爬虫不跑 JS，
而 GitHub Pages 是纯静态托管、无法按 Accept-Language 变响应。
所以「一个 URL 按语言变卡片」做不到，只能一个语言一个 URL——
再由 app 按当前界面语言挑对应链接去分享。
"""
import io

BASE = "https://artzmy.github.io/market-bell-site/"

# 正文/卡片文案沿用 docs/build/app-store-listing.md 里已拍板、与商店 listing 一致的措辞，
# 避免站点和商店两处口径分裂。
L = {
 "en": dict(
  file="index.html", lang="en", locale="en_US", label="English",
  title="Market Bell — Global Market Open & Close Countdown for iOS",
  desc="Market Bell tells you at a glance whether a market is open, closed, or about to change. Lunch breaks, daylight saving and exchange holidays are handled automatically. Widgets, alerts and Live Activities included.",
  og_title="Market Bell — Know exactly when the markets open",
  og_desc="Countdowns to every open and close, across every timezone that matters to you. Lunch breaks, daylight saving and exchange holidays handled automatically. Free on the App Store.",
  hero="Know exactly when<br>the markets open.",
  sub="Market Bell shows you the moment that matters &mdash; how long until a market opens, closes, or comes back from lunch. Across every timezone you care about.",
  cta="Download on the App Store",
  cta_note="Free &middot; iPhone &middot; Widgets, alerts and Live Activities included",
  mock_label="Example of the market list",
  rows=[("US","New York","NYSE &amp; Nasdaq","open","Open","closes in 2:41:07"),
        ("HK","Hong Kong","HKEX","lunch","Lunch","back in 22:14"),
        ("JP","Tokyo","TSE","closed","Closed","opens in 14:08:51"),
        ("GB","London","LSE","closed","Holiday","Summer Bank Holiday")],
  why="Why Market Bell",
  feats=[("Lunch breaks, handled right","Hong Kong, mainland China, Japan and Korea all pause midday. Market Bell knows exactly when trading stops and when it resumes."),
         ("Daylight saving, done for you","US and European market hours shift by an hour through the year. No more mental math about what time the open actually lands in your day."),
         ("Holidays and half days, built in","Every supported exchange's holiday calendar ships inside the app and is kept current &mdash; including shortened trading days."),
         ("Never open the app","Home Screen widgets, open alerts and Live Activities put the countdown where you already look. The widget is the product.")],
  markets_h="Markets covered",
  markets="United States &middot; Japan &middot; South Korea &middot; Hong Kong &middot; mainland China &middot; United Kingdom &middot; Germany &middot; Euronext",
  support_h="Support",
  support_q="Questions, bugs, or a market you want added?",
  support_p="Open Market Bell &rarr; <strong>Settings &rarr; Feedback</strong> and send a message directly from the app. It goes straight to the developer's inbox, and it's the fastest way to get a reply.",
  support_more='Common questions &mdash; wrong market hours, a widget that isn\'t refreshing, requesting a market or language &mdash; are answered on the <a href="support.html">Support page</a>. Data handling is covered in the <a href="privacy.html">Privacy Policy</a>.',
  nav_support="Support", nav_privacy="Privacy Policy", nav_home="Home",
  footer="Market Bell for iOS",
 ),
 "zh": dict(
  file="zh.html", lang="zh-Hans", locale="zh_CN", label="简体中文",
  title="Market Bell — 全球股市开收盘倒计时",
  desc="一眼看清各大市场还有多久开盘、收盘、午休结束。午休时段、夏令时、节假日全部自动处理，还有小组件、开盘提醒和灵动岛。",
  og_title="Market Bell — 全球股市开收盘倒计时",
  og_desc="一眼看清各大市场还有多久开盘、收盘、午休结束。午休、夏令时、节假日全自动处理。App Store 免费下载。",
  hero="一眼看清<br>各大市场还有多久开盘。",
  sub="Market Bell 只告诉你最要紧的那件事——距离开盘、收盘或午休结束还有多久。覆盖你关心的每一个时区。",
  cta="App Store 免费下载",
  cta_note="免费 &middot; iPhone &middot; 含小组件、开盘提醒与灵动岛",
  mock_label="市场列表示意",
  rows=[("US","纽约","纽交所 &amp; 纳斯达克","open","交易中","距收盘 2:41:07"),
        ("HK","香港","港交所","lunch","午休","22:14 后恢复"),
        ("JP","东京","东证","closed","已收盘","距开盘 14:08:51"),
        ("GB","伦敦","伦交所","closed","休市","夏季银行假日")],
  why="为什么是 Market Bell",
  feats=[("午休时段，处理得准","港股、A股、日股、韩股盘中都有午休。Market Bell 精确知道什么时候停、什么时候恢复。"),
         ("夏令时，自动换算","美股、欧股的开盘时间一年里会变。不用再自己算它落在你这边的几点。"),
         ("节假日与半日市，内置","每个支持市场的假期日历都内置在 app 里并持续更新——含半日市。"),
         ("不用打开 app","主屏小组件、开盘提醒、灵动岛，把倒计时放在你本来就会看的地方。小组件才是产品本体。")],
  markets_h="支持市场",
  markets="美股 &middot; 日股 &middot; 韩股 &middot; 港股 &middot; A股 &middot; 英股 &middot; 德股 &middot; 欧股",
  support_h="支持",
  support_q="有问题、发现 bug，或想加某个市场？",
  support_p="打开 Market Bell &rarr; <strong>设置 &rarr; 反馈</strong>，直接在 app 里发消息。它会直达开发者的收件箱，是最快能得到回复的方式。",
  support_more='常见问题——市场时间不对、小组件不刷新、想申请新市场或语言——都在<a href="support.html">支持页</a>（英文）。数据处理方式见<a href="privacy.html">隐私政策</a>（英文）。',
  nav_support="支持", nav_privacy="隐私政策", nav_home="首页",
  footer="Market Bell for iOS",
 ),
 "ja": dict(
  file="ja.html", lang="ja", locale="ja_JP", label="日本語",
  title="Market Bell — 世界の市場の開場・閉場カウントダウン",
  desc="開場・閉場・昼休み終了までの時間をひと目で。昼休み、サマータイム、祝日はすべて自動で処理。ウィジェット、開場アラート、Dynamic Island に対応。",
  og_title="Market Bell — 世界の市場の開場・閉場カウントダウン",
  og_desc="開場・閉場・昼休み終了までの残り時間をひと目で。昼休みもサマータイムも祝日も自動で処理します。App Store で無料。",
  hero="市場が開くまで、<br>あと何分か。",
  sub="Market Bell が教えるのは、いちばん知りたいこと——開場・閉場・昼休み終了までの残り時間。気になるすべてのタイムゾーンで。",
  cta="App Store で無料ダウンロード",
  cta_note="無料 &middot; iPhone &middot; ウィジェット・通知・Dynamic Island 対応",
  mock_label="マーケット一覧のイメージ",
  rows=[("US","ニューヨーク","NYSE &amp; ナスダック","open","取引中","閉場まで 2:41:07"),
        ("HK","香港","香港取引所","lunch","昼休み","22:14 後に再開"),
        ("JP","東京","東証","closed","閉場","開場まで 14:08:51"),
        ("GB","ロンドン","LSE","closed","休場","サマーバンクホリデー")],
  why="Market Bell を選ぶ理由",
  feats=[("昼休みも正確に対応","香港・中国本土・日本・韓国は取引中に昼休みがあります。Market Bell は止まる時刻も再開する時刻も正確に把握しています。"),
         ("サマータイムも自動調整","米国・欧州市場の取引時間は年によって変わります。手元の時刻に換算する必要はありません。"),
         ("祝日・短縮取引も内蔵","対応する各取引所の祝日カレンダーをアプリに内蔵し、常に最新の状態に保っています。"),
         ("アプリを開かなくていい","ホーム画面ウィジェット、開場アラート、Dynamic Island。普段見ている場所にカウントダウンを置きます。")],
  markets_h="対応市場",
  markets="米国 &middot; 日本 &middot; 韓国 &middot; 香港 &middot; 中国 &middot; 英国 &middot; ドイツ &middot; ユーロネクスト",
  support_h="サポート",
  support_q="ご質問、不具合、追加してほしい市場はありますか？",
  support_p="Market Bell を開いて <strong>設定 &rarr; フィードバック</strong> から直接メッセージを送ってください。開発者に直接届き、いちばん早く返信できます。",
  support_more='よくある質問（市場時間の誤り、ウィジェットが更新されない、市場や言語の追加リクエスト）は<a href="support.html">サポートページ</a>（英語）に。データの取り扱いは<a href="privacy.html">プライバシーポリシー</a>（英語）をご覧ください。',
  nav_support="サポート", nav_privacy="プライバシー", nav_home="ホーム",
  footer="Market Bell for iOS",
 ),
 "ko": dict(
  file="ko.html", lang="ko", locale="ko_KR", label="한국어",
  title="Market Bell — 전 세계 증시 개장·폐장 카운트다운",
  desc="개장·폐장·점심시간 종료까지 남은 시간을 한눈에. 점심시간, 서머타임, 공휴일까지 모두 자동으로 처리합니다. 위젯, 개장 알림, 다이나믹 아일랜드 지원.",
  og_title="Market Bell — 전 세계 증시 개장·폐장 카운트다운",
  og_desc="개장·폐장·점심시간 종료까지 남은 시간을 한눈에. 점심시간도 서머타임도 공휴일도 자동으로 처리됩니다. App Store에서 무료.",
  hero="장이 열리기까지<br>얼마나 남았는지.",
  sub="Market Bell은 가장 궁금한 것만 알려줍니다 — 개장·폐장·점심시간 종료까지 남은 시간. 신경 쓰는 모든 시간대에서.",
  cta="App Store에서 무료 다운로드",
  cta_note="무료 &middot; iPhone &middot; 위젯·알림·다이나믹 아일랜드 포함",
  mock_label="시장 목록 예시",
  rows=[("US","뉴욕","NYSE &amp; 나스닥","open","거래 중","폐장까지 2:41:07"),
        ("HK","홍콩","홍콩거래소","lunch","점심시간","22:14 후 재개"),
        ("JP","도쿄","도쿄증권거래소","closed","폐장","개장까지 14:08:51"),
        ("GB","런던","런던증권거래소","closed","휴장","서머 뱅크 홀리데이")],
  why="왜 Market Bell인가",
  feats=[("점심시간도 정확하게","홍콩·중국 본토·일본·한국은 거래 중 점심시간이 있습니다. Market Bell은 멈추는 시각과 재개하는 시각을 정확히 압니다."),
         ("서머타임도 자동 반영","미국과 유럽 시장의 거래 시간은 해마다 바뀝니다. 내 시간으로 환산할 필요가 없습니다."),
         ("공휴일과 단축 거래일 내장","지원하는 각 거래소의 휴장일 캘린더가 앱에 내장되어 있고 항상 최신 상태로 유지됩니다."),
         ("앱을 열지 않아도","홈 화면 위젯, 개장 알림, 다이나믹 아일랜드. 이미 보고 있는 곳에 카운트다운을 놓습니다.")],
  markets_h="지원 시장",
  markets="미국 &middot; 일본 &middot; 한국 &middot; 홍콩 &middot; 중국 &middot; 영국 &middot; 독일 &middot; 유로넥스트",
  support_h="지원",
  support_q="질문, 버그, 추가했으면 하는 시장이 있나요?",
  support_p="Market Bell을 열고 <strong>설정 &rarr; 피드백</strong>에서 바로 메시지를 보내세요. 개발자에게 직접 전달되며 가장 빠르게 답변을 받을 수 있습니다.",
  support_more='자주 묻는 질문(잘못된 장 시간, 새로고침되지 않는 위젯, 시장·언어 추가 요청)은 <a href="support.html">지원 페이지</a>(영어)에 있습니다. 데이터 처리는 <a href="privacy.html">개인정보 처리방침</a>(영어)을 참고하세요.',
  nav_support="지원", nav_privacy="개인정보", nav_home="홈",
  footer="Market Bell for iOS",
 ),
}

ORDER = ["en","zh","ja","ko"]

def page(key):
    d = L[key]
    url = BASE + ("" if key=="en" else d["file"])
    # hreflang：向搜索引擎声明这几页互为语言版本，x-default 指英文
    alt = "\n".join(
        f'<link rel="alternate" hreflang="{L[k]["lang"]}" href="{BASE + ("" if k=="en" else L[k]["file"])}">'
        for k in ORDER
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{BASE}">'
    langnav = " ".join(
        (f'<span class="lang-current">{L[k]["label"]}</span>' if k==key
         else f'<a href="{"./" if k=="en" else L[k]["file"]}">{L[k]["label"]}</a>')
        for k in ORDER
    )
    rows = "\n".join(
        f'''    <div class="mock-row">
      <span class="mock-flag" aria-hidden="true">{f}</span>
      <span class="mock-name">{n} <em>{e}</em></span>
      <span class="mock-state {cls}">{st}</span>
      <span class="mock-time">{t}</span>
    </div>''' for f,n,e,cls,st,t in d["rows"])
    feats = "\n".join(
        f'''      <div class="feat">
        <h3>{h}</h3>
        <p>{p}</p>
      </div>''' for h,p in d["feats"])
    return f'''<!doctype html>
<html lang="{d["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{d["title"]}</title>
<meta name="description" content="{d["desc"]}">
<link rel="canonical" href="{url}">
{alt}
<link rel="icon" href="icon.png">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Market Bell">
<meta property="og:locale" content="{d["locale"]}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{d["og_title"]}">
<meta property="og:description" content="{d["og_desc"]}">
<meta property="og:image" content="{BASE}icon.png">
<meta property="og:image:width" content="512">
<meta property="og:image:height" content="512">
<meta property="og:image:alt" content="{d["og_title"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{d["og_title"]}">
<meta name="twitter:description" content="{d["og_desc"]}">
<meta name="twitter:image" content="{BASE}icon.png">
<meta name="twitter:image:alt" content="{d["og_title"]}">

<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="wrap wide">
  <nav class="top"><a href="{"./" if key=="en" else d["file"]}">{d["nav_home"]}</a><a href="support.html">{d["nav_support"]}</a><a href="privacy.html">{d["nav_privacy"]}</a></nav>

  <header class="hero">
    <img class="hero-icon" src="icon.png" alt="Market Bell" width="96" height="96">
    <h1 class="hero-title">{d["hero"]}</h1>
    <p class="hero-sub">{d["sub"]}</p>
    <p class="cta">
      <a class="btn" href="https://apps.apple.com/app/id6783567802?ct=site-{key}">{d["cta"]}</a>
    </p>
    <p class="cta-note">{d["cta_note"]}</p>
  </header>

  <!-- 纯 CSS 画的示意，不是截图 -->
  <section class="mock" aria-label="{d["mock_label"]}">
{rows}
  </section>

  <section class="features">
    <h2 class="section-title">{d["why"]}</h2>
    <div class="grid">
{feats}
    </div>
  </section>

  <section class="markets">
    <h2 class="section-title">{d["markets_h"]}</h2>
    <p class="market-list">{d["markets"]}</p>
  </section>

  <section class="support-block">
    <h2 class="section-title">{d["support_h"]}</h2>
    <div class="card">
      <p><strong>{d["support_q"]}</strong></p>
      <p>{d["support_p"]}</p>
      <p class="support-more">{d["support_more"]}</p>
    </div>
  </section>

  <p class="cta cta-bottom">
    <a class="btn" href="https://apps.apple.com/app/id6783567802?ct=site-{key}-bottom">{d["cta"]}</a>
  </p>

  <nav class="langnav">{langnav}</nav>

  <footer>{d["footer"]} &middot; <a href="support.html">{d["nav_support"]}</a> &middot; <a href="privacy.html">{d["nav_privacy"]}</a></footer>
</div>
</body>
</html>
'''

for k in ORDER:
    io.open(L[k]["file"],"w",encoding="utf-8").write(page(k))
    print("wrote", L[k]["file"])
