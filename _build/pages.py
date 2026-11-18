"""Leung & Co Law concept site generator. No dependencies.

    python3 _build/pages.py && python3 _build/fonts.py

Every page exists in English (/) and Traditional Chinese (/zh/). Text is written side by side
as T(english, 中文). Contact details live once, in FIRM.
"""
import json, os

BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD)
V = "12"  # cache-bust: bump on every CSS/JS change

FIRM = {
    "tel": "0333 577 7168", "tel_href": "+443335777168",
    "direct": "0333 577 6688", "direct_href": "+443335776688",
    "hk": "9537 5410", "hk_href": "+85295375410",
    "email": "info@leung-solicitors.co.uk",
    "addr_en": ["Filwood Green Business Park", "1 Filwood Park Lane", "Bristol BS4 1ET"],
    "addr_zh": ["Filwood Green Business Park", "1 Filwood Park Lane", "Bristol BS4 1ET（布里斯托）"],
    "official": "http://leung-solicitors.co.uk/",
    "lnglat": [-2.58515, 51.42003],
    "maps": "https://www.google.com/maps/search/?api=1&query=Filwood+Green+Business+Park+1+Filwood+Park+Lane+Bristol+BS4+1ET",
    "sra": "https://www.sra.org.uk/consumers/register/organisation/?sraNumber=557238",
}

LANG = "en"


def T(en, zh):
    return en if LANG == "en" else zh


def P():  # path prefix to site root
    return "" if LANG == "en" else "../"


def seal(cls="seal", title=None):
    t = f'<title>{title}</title>' if title else ""
    aria = f'role="img" aria-label="{title}"' if title else 'aria-hidden="true"'
    return f'<svg class="{cls}" viewBox="0 0 126 177" {aria}>{t}<use href="{P()}assets/img/seal.svg?v={V}#s"/></svg>'


def bird(cls="bird"):
    """The phoenix oval only, cropped from the seal: used as bullets and dividers."""
    return f'<svg class="{cls}" viewBox="0 0 80 106" aria-hidden="true"><use href="{P()}assets/img/seal.svg?v={V}#b"/></svg>'


def nav_items():
    return [
    ("services", T("Services", "服務範圍")),
    ("notary", T("Notary", "公證服務")),
    ("about", T("About", "關於我們")),
    ("contact", T("Contact", "聯絡")),
    ]


def head(slug, title, desc):
    other = "zh/" if LANG == "en" else ""
    page = "" if slug == "index" else f"{slug}.html"
    base = "https://uxcircles.github.io/leung-solicitors/"
    fonts = ["spectral-600", "onest"] if LANG == "en" else ["chiron-sung-hk-700", "chiron-hei-hk-400"]
    pre = "".join(f'<link rel="preload" href="{P()}assets/fonts/{f}.woff2" as="font" type="font/woff2" crossorigin>' for f in fonts)
    return f"""<!doctype html>
<html lang="{T('en-GB', 'zh-Hant-HK')}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="alternate" hreflang="en-GB" href="{base}{page}">
<link rel="alternate" hreflang="zh-Hant" href="{base}zh/{page}">
<link rel="icon" href="{P()}assets/img/favicon.svg?v={V}" type="image/svg+xml">
<meta name="theme-color" content="#8a2c12">
{pre}
<link rel="stylesheet" href="{P()}assets/site.css?v={V}">
</head>
<body class="lang-{LANG} page-{slug}">
<a class="skip" href="#main">{T('Skip to content', '跳到內容')}</a>
<div class="concept-bar" role="note">
  <div class="wrap concept-inner">
    <p><span class="concept-tag">{T('Concept', '概念')}</span><span class="concept-long">{T('Redesign concept. Not the', '重新設計概念，並非')} <a href="{FIRM['official']}" target="_blank" rel="noopener">{T('official Leung &amp; Co Law website', 'Leung &amp; Co Law 官方網站')}</a>{T('.', '。')}</span></p>
    <a href="https://ux-circles.com/professionals" target="_blank" rel="noopener"><span class="concept-by">{T('Designed by ', '設計：')}</span><strong>UX CIRCLES</strong> <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></a>
  </div>
</div>
"""


def header(slug):
    other_lang = "zh/" if LANG == "en" else ""
    page = "" if slug == "index" else f"{slug}.html"
    switch_href = (other_lang if LANG == "en" else "../") + page
    if LANG == "zh" and not page:
        switch_href = "../"
    links = "".join(
        f'<a href="{P()}{"zh/" if LANG == "zh" else ""}{s}.html"{" aria-current=\"page\"" if s == slug else ""}>{n}</a>'
        for s, n in nav_items())
    home = f'{P()}{"zh/" if LANG == "zh" else ""}'
    return f"""<header class="site-head">
  <div class="wrap head-row">
    <a class="brand" href="{home or './'}">{seal('brand-seal')}<span class="brand-name">Leung &amp; Co Law<small>{T('Solicitors · Notary Public · Bristol', '律師行 · 公證人 · 布里斯托')}</small></span></a>
    <nav class="nav" id="nav" aria-label="{T('Main', '主選單')}">
      {links}
      <a class="lang-switch" href="{switch_href}" lang="{T('zh-Hant', 'en')}">{T('中文', 'English')}</a>
    </nav>
    <a class="head-call" href="tel:{FIRM['tel_href']}">{FIRM['tel']}</a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav"><span></span><span class="sr">{T('Menu', '選單')}</span></button>
  </div>
</header>
<main id="main">
"""


def footer():
    zh = "zh/" if LANG == "zh" else ""
    addr = "<br>".join(T(FIRM["addr_en"], FIRM["addr_zh"]))
    return f"""</main>
<footer class="site-foot">
  <div class="wrap foot-grid">
    <div class="foot-brand">
      {seal('foot-seal')}
      <p class="foot-name">Leung &amp; Co Law</p>
      <p>{T('Prompt and friendly legal services in English, Cantonese, Putonghua and Malay.', '以英語、廣東話、普通話及馬來語，提供快捷友善的法律服務。')}</p>
    </div>
    <div>
      <h2 class="foot-h">{T('Office', '辦事處')}</h2>
      <p>{addr}</p>
      <p>{T('Monday to Friday, 9:30am to 6pm', '星期一至五 上午 9:30 至下午 6:00')}</p>
    </div>
    <div>
      <h2 class="foot-h">{T('Phone and email', '電話及電郵')}</h2>
      <p><a href="tel:{FIRM['tel_href']}">{FIRM['tel']}</a><br>
      {T('From Hong Kong', '香港專線')} <a href="tel:{FIRM['hk_href']}">{FIRM['hk']}</a><br>
      <a href="mailto:{FIRM['email']}">{FIRM['email']}</a></p>
    </div>
    <div>
      <h2 class="foot-h">{T('Pages', '頁面')}</h2>
      <p class="foot-links">{''.join(f'<a href="{P()}{zh}{s}.html">{n}</a>' for s, n in nav_items())}<a href="{P()}{zh}privacy.html">{T('Privacy', '私隱政策')}</a><a href="{P()}{'' if LANG == 'zh' else 'zh/'}" lang="{T('zh-Hant', 'en')}">{T('中文', 'English')}</a></p>
    </div>
  </div>
  <div class="wrap foot-legal">
    <p>{T(
        f'Leung &amp; Co Law is a trading name of Austen-Jones Solicitors Ltd, registered in England and Wales (company no. 07526477), authorised and regulated by the Solicitors Regulation Authority (<a href="{FIRM["sra"]}">SRA ID 557238</a>). Registered office: 145 Upland Road, London SE22 0DF. Notarial services are regulated by the Faculty Office of the Archbishop of Canterbury. We do not offer legal aid work.',
        f'Leung &amp; Co Law 為 Austen-Jones Solicitors Ltd 的營業名稱，於英格蘭及威爾斯註冊（公司編號 07526477），由律師規管局（Solicitors Regulation Authority）授權及規管（<a href="{FIRM["sra"]}">SRA 編號 557238</a>）。註冊地址：145 Upland Road, London SE22 0DF。公證服務由坎特伯雷大主教轄下的 Faculty Office 規管。本行不承辦法律援助個案。')}</p>
    <p class="foot-concept">{T('Unofficial redesign concept by', '非官方重新設計概念，由')} <a href="https://ux-circles.com/professionals">UX CIRCLES</a>{T('', ' 製作')}</p>
  </div>
</footer>
<nav class="mbar" aria-label="{T('Quick actions', '快速聯絡')}">
  <a href="tel:{FIRM['tel_href']}"><span class="mb-k">{T('Call', '致電')}</span><span class="mb-v">Bristol</span></a>
  <a href="tel:{FIRM['hk_href']}"><span class="mb-k">{T('From HK', '香港專線')}</span><span class="mb-v">{FIRM['hk']}</span></a>
  <a href="{P()}{zh}contact.html#enquiry"><span class="mb-k">{T('Enquire', '查詢')}</span><span class="mb-v">{T('Email us', '電郵')}</span></a>
</nav>
<script src="{P()}assets/site.js?v={V}" defer></script>
</body>
</html>
"""


# ---------- shared blocks ----------

def hours_block():
    return f"""<dl class="hours">
  <div><dt>{T('Monday to Friday', '星期一至五')}</dt><dd>9:30–18:00</dd></div>
  <div><dt>{T('Weekday evenings', '平日晚上')}</dt><dd>{T('Until 19:00, notary appointments by prior arrangement', '至 19:00，公證預約須事先安排')}</dd></div>
  <div><dt>{T('Saturday', '星期六')}</dt><dd>{T('10:30–12:30, notary appointments by prior arrangement', '10:30–12:30，公證預約須事先安排')}</dd></div>
  <div><dt>{T('Sunday', '星期日')}</dt><dd>{T('Closed', '休息')}</dd></div>
</dl>
<p class="open-now" data-open-now hidden></p>"""


def map_block():
    data = {"home": FIRM["lnglat"], "mark": f"{P()}assets/img/favicon.svg?v={V}", "label": "Leung &amp; Co Law", "routes": []}
    addr = ", ".join(T(FIRM["addr_en"], FIRM["addr_zh"]))
    return f"""<div class="map" data-map>
  <div class="map-sketch" aria-hidden="true">
    <svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice"><rect width="400" height="300" fill="#efe7da"/>
    <path d="M-10 210 C 90 190 180 205 410 160" stroke="#fff" stroke-width="16" fill="none"/>
    <path d="M150 -10 C 160 90 190 170 205 310" stroke="#fff" stroke-width="10" fill="none"/>
    <rect x="215" y="105" width="70" height="40" rx="4" fill="#e3d8c6"/><rect x="120" y="230" width="60" height="45" rx="4" fill="#dde6cf"/></svg>
  </div>
  <script type="application/json" id="map-data">{json.dumps(data)}</script>
  <a class="map-open" href="{FIRM['maps']}">{T('Open in Google Maps', '在 Google 地圖開啟')} ↗</a>
  <span class="sr">{addr}</span>
</div>"""


def divider():
    return f'<div class="divider" aria-hidden="true"><span></span>{bird()}<span></span></div>'


# ---------- pages ----------

def index():
    en_first = LANG == "en"
    en_h = "h1" if LANG == "en" else "p"
    zh_h = "h1" if LANG == "zh" else "p"
    en_half = f"""<section class="half half-en" lang="en">
    <p class="half-place">Filwood Green Business Park, Bristol</p>
    <{en_h} class="hero-title">A Bristol law office you can also ring from Hong Kong</{en_h}>
    <p class="hero-sub">Immigration, property, probate, licensing and notarial work for small businesses, charities, families and individuals. Prompt and friendly, in English, Cantonese, Putonghua and Malay.</p>
    <div class="hero-act">
      <a class="btn btn-ink" href="tel:{FIRM['tel_href']}"><small>Bristol office</small>{FIRM['tel']}</a>
      <a class="btn btn-line" href="{P()}services.html">Our services</a>
    </div>
    <p class="hero-meta">Monday to Friday, 9:30am to 6pm (UK time)</p>
  </section>"""
    zh_half = f"""<section class="half half-zh" lang="zh-Hant-HK">
    <p class="half-place">香港來電專線</p>
    <{zh_h} class="hero-title">人在香港，也找得到布里斯托的律師</{zh_h}>
    <p class="hero-sub">Amelia Leung 律師 1996 年在英國創立本行。移民及國籍、物業買賣、遺囑認證、商業牌照及公證，都可以用廣東話、普通話傾。</p>
    <div class="hero-act">
      <a class="btn btn-paper" href="tel:{FIRM['hk_href']}"><small>香港直撥</small>{FIRM['hk']}</a>
      <a class="btn btn-line-light" href="{P()}{'zh/' if LANG == 'en' else ''}services.html">服務範圍</a>
    </div>
    <p class="hero-meta">英國時間 星期一至五 9:30–18:00（即香港時間下午 5:30 起；英國夏令時間期間為 4:30 起）</p>
  </section>"""
    halves = en_half + zh_half if en_first else zh_half + en_half
    zh = "zh/" if LANG == "zh" else ""

    services = [
        ("immigration", T("Immigration and nationality", "移民及國籍"),
         T("Preparing and submitting immigration applications, and advice and representation at the First-tier Tribunal (Immigration and Asylum Chamber) on appeals against Home Office decisions. Business immigration, dependants and family reunion.",
           "準備及遞交移民申請；就內政部的簽證或移民決定，在初級審裁處（移民及庇護庭）提供上訴意見及代表。亦處理商業移民、受養人及家庭團聚申請。")),
        ("conveyancing", T("Residential conveyancing", "住宅物業轉讓"),
         T("Freehold or leasehold sales and purchases, mortgages and remortgages.", "永久業權或租賃業權物業的買賣、按揭及轉按。")),
        ("business", T("Small business and commercial property", "小型企業及商業物業"),
         T("Commercial contracts, buying and selling a business, and leases of commercial premises. This is the firm's specialism.", "商業合約、生意買賣及商業物業租約，是本行的專長。")),
        ("probate", T("Wills and probate", "遺囑及遺產承辦"),
         T("Non-contentious probate and estate administration where the assets are in the UK, and re-sealing of foreign grants of probate.", "非爭議性遺產承辦及遺產管理（資產位於英國），以及海外遺囑認證書的重新蓋印。")),
        ("licensing", T("Licensing", "商業牌照"),
         T("Advice, assistance and representation on licensing applications for business premises, including food safety.", "為商業處所的牌照申請提供意見、協助及代表，包括食物安全事宜。")),
        ("notary", T("Notarial services", "公證服務"),
         T("Amelia Leung is a Notary Public. Documents for use abroad, e-notarisation with e-apostille, and home or workplace visits.", "Amelia Leung 是執業公證人：海外使用的文件、電子公證及電子海牙認證，亦可到府或到公司辦理。")),
    ]
    rows = "".join(f"""<li class="svc">
      {bird('svc-bird')}
      <div><h3><a href="{P()}{zh}{'notary' if k == 'notary' else 'services'}.html{'' if k == 'notary' else '#' + k}">{t}</a></h3><p>{d}</p></div>
    </li>""" for k, t, d in services)

    return f"""<div class="hero">
  <div class="hero-grid">{halves}</div>
  <div class="hero-seam" aria-hidden="true"><span class="seam-disc">{seal('seam-seal')}</span></div>
</div>

<section class="reg-strip">
  <div class="wrap">
    <p>{T(f'Leung &amp; Co Law has joined Austen-Jones Solicitors (<a href="{FIRM["sra"]}">SRA 557238</a>). Our service to clients in the UK and abroad has not changed: Amelia Leung continues to act for you, with more support behind her.',
          f'Leung &amp; Co Law 已加入 Austen-Jones Solicitors（<a href="{FIRM["sra"]}">SRA 557238</a>）。我們為英國及海外客戶提供的服務不變，仍由 Amelia Leung 律師跟進，背後有更多支援。')}</p>
  </div>
</section>

<section class="sec">
  <div class="wrap two">
    <div class="two-head">
      <h2>{T('What we do', '服務範圍')}</h2>
      <p class="lede">{T('A general practice with an emphasis on immigration, commercial and residential property, for clients in Bristol, elsewhere in the UK and overseas.', '綜合律師行，以移民、商業及住宅物業為重點，客戶來自布里斯托、英國各地及海外。')}</p>
      <p><a class="more" href="{P()}{zh}services.html">{T('All practice areas', '全部服務範圍')} →</a></p>
    </div>
    <ul class="svc-list">{rows}</ul>
  </div>
</section>

<section class="langs" aria-labelledby="langs-h">
  <div class="wrap">
    <h2 id="langs-h" class="langs-h">{T('Four languages at the same desk', '同一張辦公桌，四種語言')}</h2>
    <ul class="lang-row">
      <li lang="en">English</li>
      <li lang="zh-Hant-HK">廣東話</li>
      <li lang="zh-Hant">普通話</li>
      <li lang="ms">Bahasa Melayu</li>
    </ul>
  </div>
</section>

<section class="sec">
  <div class="wrap who">
    <h2>{T('Who we act for', '我們的客戶')}</h2>
    <div class="who-grid">
      <div><h3>{T('Small businesses', '小型企業')}</h3><p>{T('Contracts, buying or selling a business, commercial leases, licences for your premises.', '合約、買賣生意、商業租約、處所牌照。')}</p></div>
      <div><h3>{T('Families and individuals', '家庭及個人')}</h3><p>{T('Visas, family reunion, buying a home, wills and estates.', '簽證、家庭團聚、置業、遺囑及遺產。')}</p></div>
      <div><h3>{T('Charities and non-profits', '慈善及非牟利機構')}</h3><p>{T('We support charities and take on work pro bono or at low cost.', '我們支持慈善團體，並承接義務或低收費的工作。')}</p></div>
      <div><h3>{T('Clients abroad', '海外客戶')}</h3><p>{T('Our immigration team has acted for clients from 20 different countries.', '本行移民團隊曾為來自 20 個國家的客戶辦理案件。')}</p></div>
    </div>
  </div>
</section>

{divider()}

<section class="sec">
  <div class="wrap principal">
    <div class="principal-mark">{seal('principal-seal')}<p>{T('Established November 1996', '1996 年 11 月創立')}</p></div>
    <div>
      <h2>{T('Amelia Leung, principal solicitor and Notary Public', 'Amelia Leung，主管律師及公證人')}</h2>
      <p class="lede">{T('Amelia studied Social Science at the Chinese University of Hong Kong, then law in Newcastle upon Tyne. She qualified as a solicitor in England and Wales in 1992 and set up this firm in 1996.', 'Amelia 在香港中文大學修讀社會科學，其後到英國紐卡素修讀法律，1992 年取得英格蘭及威爾斯律師資格，1996 年創立本行。')}</p>
      <ol class="roll">
        <li><span>1992</span>{T('Solicitor, England and Wales', '英格蘭及威爾斯律師')}</li>
        <li><span>1998</span>{T('Solicitor, Hong Kong', '香港律師')}</li>
        <li><span>2010</span>{T('Notary Public of England and Wales', '英格蘭及威爾斯公證人')}</li>
        <li><span>&nbsp;</span>{T('Solicitor, Ireland', '愛爾蘭律師')}</li>
      </ol>
      <p><a class="more" href="{P()}{zh}about.html">{T('About the firm', '關於本行')} →</a></p>
    </div>
  </div>
</section>

<section class="sec visit">
  <div class="wrap visit-grid">
    <div>
      <h2>{T('Visit the office', '到訪辦事處')}</h2>
      <address>{'<br>'.join(T(FIRM['addr_en'], FIRM['addr_zh']))}</address>
      <p>{T('Free parking for visitors. Meetings by appointment, so please call first.', '訪客可免費泊車。會面須預約，請先致電。')}</p>
      {hours_block()}
      <p class="visit-call"><a class="btn btn-seal" href="tel:{FIRM['tel_href']}">{T('Call', '致電')} {FIRM['tel']}</a></p>
    </div>
    {map_block()}
  </div>
</section>
"""


def services():
    zh = "zh/" if LANG == "zh" else ""
    blocks = [
        ("immigration", T("Immigration and nationality", "移民及國籍"), [
            T("We prepare and submit immigration applications for individuals.", "為個人準備及遞交移民申請。"),
            T("We advise on and represent clients in appeals at the First-tier Tribunal (Immigration and Asylum Chamber) against Home Office visa or immigration decisions.", "就內政部的簽證或移民決定，在初級審裁處（移民及庇護庭）提供上訴意見及代表。"),
            T("Business immigration under the points-based system: investors, the self-employed, study and work in the UK.", "計分制下的商業移民：投資者、自僱人士、來英升學及工作。"),
            T("Dependants and family reunion.", "受養人及家庭團聚。"),
            T("Member of the Immigration Law Practitioners' Association.", "本行為移民法執業者協會（ILPA）會員。"),
        ]),
        ("conveyancing", T("Residential conveyancing", "住宅物業轉讓"), [
            T("Freehold or leasehold sales and purchases.", "永久業權或租賃業權物業的買賣。"),
            T("Mortgages and remortgages.", "按揭及轉按。"),
        ]),
        ("business", T("Small business and commercial property", "小型企業及商業物業"), [
            T("Commercial contracts.", "商業合約。"),
            T("Sale and purchase of businesses.", "生意買賣。"),
            T("Leases of commercial premises, and lease and tenancy agreements.", "商業物業租約，以及租約及租賃協議。"),
            T("Guidance for small businesses.", "小型企業法律指引。"),
        ]),
        ("probate", T("Wills and probate", "遺囑及遺產承辦"), [
            T("Wills.", "訂立遺囑。"),
            T("Non-contentious probate and estate administration: collecting and distributing the assets of a person who has died, where the assets are in the UK and the matter is not contested.", "非爭議性遺產承辦及遺產管理：收集及分配已故人士的資產（資產位於英國，且沒有爭議）。"),
            T("Re-sealing of foreign grants of probate.", "海外遺囑認證書的重新蓋印。"),
        ]),
        ("licensing", T("Licensing and food safety", "商業牌照及食物安全"), [
            T("Advice, assistance and representation on licensing applications for business premises.", "為商業處所的牌照申請提供意見、協助及代表。"),
            T("Food safety.", "食物安全事宜。"),
        ]),
        ("family", T("Family and charities", "家庭事務及慈善機構"), [
            T("Family matters.", "家庭事務。"),
            T("Charities: we support charities and take on work pro bono or at low cost.", "慈善機構：我們支持慈善團體，並承接義務或低收費的工作。"),
        ]),
    ]
    out = "".join(f"""<section class="area" id="{k}">
      <h2>{bird('area-bird')}{t}</h2>
      <ul>{''.join(f'<li>{x}</li>' for x in items)}</ul>
      <p><a class="more" href="{P()}{zh}contact.html?matter={k}#enquiry">{T('Ask for a quote', '索取報價')} →</a></p>
    </section>""" for k, t, items in blocks)
    toc = "".join(f'<li><a href="#{k}">{t}</a></li>' for k, t, _ in blocks)
    return f"""<div class="page-head">
  <div class="wrap">
    <h1>{T('Practice areas', '服務範圍')}</h1>
    <p class="lede">{T('A general practice with an emphasis on immigration, commercial and residential property. We specialise in acting for small and medium-sized businesses.', '綜合律師行，以移民、商業及住宅物業為重點，專門為中小企提供法律服務。')}</p>
  </div>
</div>
<div class="wrap areas-wrap">
  <nav class="toc" aria-label="{T('On this page', '本頁內容')}"><ul>{toc}<li><a href="{P()}{zh}notary.html">{T('Notarial services', '公證服務')}</a></li></ul></nav>
  <div class="areas">{out}
    <p class="note">{T('We do not offer legal aid work.', '本行不承辦法律援助個案。')}</p>
  </div>
</div>
"""


def notary():
    zh = "zh/" if LANG == "zh" else ""
    return f"""<div class="page-head page-head-seal">
  <div class="wrap ph-grid">
    <div>
      <h1>{T('Notary Public in Bristol, with e-apostille', '布里斯托公證人，可辦電子海牙認證')}</h1>
      <p class="lede">{T('Amelia Leung has been a Notary Public of England and Wales since 2010, after the Postgraduate Diploma in Notarial Practice at the University of Cambridge. She is also a solicitor of England and Wales, Ireland and Hong Kong.', 'Amelia Leung 在劍橋大學完成公證實務深造文憑後，於 2010 年獲委任為英格蘭及威爾斯公證人；她同時是英格蘭及威爾斯、愛爾蘭及香港的律師。')}</p>
    </div>
    {seal('ph-seal')}
  </div>
</div>

<section class="sec">
  <div class="wrap fee-row">
    <div class="fee">
      <p class="fee-k">{T('e-Notarisation with e-apostille', '電子公證連電子海牙認證')}</p>
      <p class="fee-v">{T('From £60', '£60 起')}</p>
      <p>{T('Our Notary Public can sign with a Qualified Electronic Signature (QES) and obtain an e-apostille from the FCDO. Please check that the receiving authority accepts this before you book.', '公證人可使用合資格電子簽署（QES）公證文件，並向英國外交部（FCDO）申請電子海牙認證。預約前，請先向收件機構確認是否接受。')}</p>
    </div>
    <div class="fee">
      <p class="fee-k">{T('Home or workplace visit', '到府或到公司辦理')}</p>
      <p class="fee-v">{T('From £50 extra', '另加 £50 起')}</p>
      <p>{T('We can come to your home, workplace, a hospital or a care home. An extra charge covers travel and waiting, with a minimum of £50 in the Bristol area.', '可到府、到公司、醫院或安老院辦理。另收交通及等候費用，布里斯托區最低 £50。')}</p>
    </div>
    <div class="fee">
      <p class="fee-k">{T('Outside office hours', '辦公時間以外')}</p>
      <p class="fee-v">{T('By arrangement', '須事先預約')}</p>
      <p>{T('Weekday evenings until 7pm and Saturdays 10:30am to 12:30pm, by prior arrangement only.', '平日晚上至 7 時，及星期六上午 10:30 至中午 12:30，只限事先預約。')}</p>
    </div>
  </div>
</section>

<section class="sec sec-tint">
  <div class="wrap two">
    <div class="two-head"><h2>{T('What does a notary do?', '公證人做甚麼？')}</h2></div>
    <div class="prose">
      <p>{T('A notary is a qualified lawyer in the third and oldest branch of the legal profession in England and Wales. Most of the work is preparing and certifying documents that will be used abroad: powers of attorney, company papers, declarations, copies of passports and certificates.', '公證人是英格蘭及威爾斯法律界第三個、亦是歷史最悠久的分支。工作主要是準備及核證在海外使用的文件，例如授權書、公司文件、聲明書、護照及證書副本。')}</p>
      <p>{T('Notaries are appointed by the Court of Faculties of the Archbishop of Canterbury and regulated by the Master of the Faculties. They must be fully insured, keep client money separate, and renew their practising certificate every year.', '公證人由坎特伯雷大主教的 Court of Faculties 委任，受 Master of the Faculties 規管；必須投保、將客戶款項分開處理，並每年續領執業證書。')}</p>
      <p>{T('More from', '詳情可參閱')} <a href="https://www.thenotariessociety.org.uk/">{T('the Notaries Society', 'Notaries Society')}</a> {T('and', '及')} <a href="https://www.facultyoffice.org.uk/">{T('the Faculty Office', 'Faculty Office')}</a>{T('.', '。')}</p>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap two">
    <div class="two-head"><h2>{T('Before you book', '預約前請準備')}</h2><p class="small">{T('General guidance. We will confirm what your document needs when you call.', '一般指引，致電時我們會確認您的文件需要甚麼。')}</p></div>
    <ol class="steps">
      <li>{T('The document itself, unsigned if it needs to be signed in front of the notary.', '文件正本；如須在公證人面前簽署，請先不要簽。')}</li>
      <li>{T('Your passport or other photo ID, and proof of address.', '護照或其他附相片身份證明，以及住址證明。')}</li>
      <li>{T('Which country the document is going to, and who will receive it.', '文件寄往哪個國家、由哪個機構接收。')}</li>
      <li>{T('Any instructions from the receiving authority, such as whether an apostille or e-apostille is accepted.', '收件機構的要求，例如是否接受海牙認證或電子海牙認證。')}</li>
    </ol>
  </div>
</section>

<section class="cta-band">
  <div class="wrap cta-row">
    <h2>{T('Book a notary appointment', '預約公證')}</h2>
    <div class="hero-act">
      <a class="btn btn-paper" href="tel:{FIRM['tel_href']}">{FIRM['tel']}</a>
      <a class="btn btn-line-light" href="{P()}{zh}contact.html?matter=notary#enquiry">{T('Send an enquiry', '網上查詢')}</a>
    </div>
  </div>
</section>
"""


def about():
    return f"""<div class="page-head">
  <div class="wrap">
    <h1>{T('Established in November 1996 by Amelia Leung', '1996 年 11 月，由 Amelia Leung 創立')}</h1>
    <p class="lede">{T('Leung &amp; Co undertakes a wide range of work, including property and conveyancing, business affairs, immigration and nationality, debt and licensing. Our clients are based in Bristol and beyond, in the UK and overseas, and come from many backgrounds.', '本行業務範圍廣泛，包括物業及轉讓、商業事務、移民及國籍、債務及牌照。客戶來自布里斯托及其他地方、英國及海外，背景多元。')}</p>
  </div>
</div>

<section class="sec">
  <div class="wrap principal">
    <div class="principal-mark">{seal('principal-seal')}</div>
    <div>
      <h2>Amelia Leung</h2>
      <p class="role">{T('Principal solicitor and Notary Public', '主管律師及公證人')}</p>
      <div class="prose">
        <p>{T('Amelia studied for her first degree, in Social Science, at the Chinese University of Hong Kong. She completed her law studies in Newcastle upon Tyne, followed by a two-year training contract with a firm of solicitors, and qualified in 1992.', 'Amelia 在香港中文大學取得社會科學學士學位，其後在英國紐卡素完成法律課程，並在律師行完成兩年見習，1992 年取得律師資格。')}</p>
        <p>{T('She was admitted as a solicitor in Hong Kong in 1998 and later in Ireland, and became a Notary Public in 2010 after the Postgraduate Diploma in Notarial Practice at the University of Cambridge.', '她於 1998 年取得香港律師資格，其後再取得愛爾蘭律師資格；完成劍橋大學公證實務深造文憑後，於 2010 年獲委任為公證人。')}</p>
        <p>{T('Over the years she has developed expertise in business immigration under the points-based system, and in immigration work for dependants and family reunion. The immigration team has acted for clients from 20 different countries.', '多年來，她在計分制商業移民、受養人及家庭團聚申請方面累積了專門經驗。本行移民團隊曾為來自 20 個國家的客戶辦理案件。')}</p>
      </div>
      <ol class="roll">
        <li><span>B.Soc.Sc.</span>{T('Chinese University of Hong Kong', '香港中文大學')}</li>
        <li><span>1992</span>{T('Solicitor, England and Wales', '英格蘭及威爾斯律師')}</li>
        <li><span>1998</span>{T('Solicitor, Hong Kong', '香港律師')}</li>
        <li><span>2010</span>{T('Notary Public of England and Wales', '英格蘭及威爾斯公證人')}</li>
        <li><span>&nbsp;</span>{T('Solicitor, Ireland', '愛爾蘭律師')}</li>
      </ol>
      <p class="direct">{T('Direct line', '直線電話')} <a href="tel:{FIRM['direct_href']}">{FIRM['direct']}</a></p>
    </div>
  </div>
</section>

<section class="sec sec-tint">
  <div class="wrap two">
    <div class="two-head"><h2>{T('The team', '團隊')}</h2></div>
    <div class="prose">
      <p>{T('Please feel free to contact Amelia Leung, solicitor, or Sherman Li, practice manager, for a chat.', '歡迎聯絡 Amelia Leung 律師或業務經理 Sherman Li 傾談。')}</p>
      <p>{T('Our team members speak English, Cantonese, Putonghua and Malay.', '團隊成員能說英語、廣東話、普通話及馬來語。')}</p>
      <p>{T('In joining Austen-Jones Solicitors we have more support and resources behind us. Amelia continues to provide notary public and probate services under her Notary Public business, and non-reserved legal services under Phoenix Consultancy.', '加入 Austen-Jones Solicitors 後，我們有更多支援及資源。Amelia 繼續以其公證人業務提供公證及遺產承辦服務，並以 Phoenix Consultancy 提供非保留法律服務。')}</p>
    </div>
  </div>
</section>

<section class="sec" id="vacancies">
  <div class="wrap two">
    <div class="two-head"><h2>{T('Vacancies', '職位空缺')}</h2></div>
    <div class="job">
      <h3>{T('Caseworker or trainee solicitor', '個案助理或見習律師')}</h3>
      <ul>
        <li>{T('Full-time or part-time; we are committed to flexible working', '全職或兼職，本行支持彈性工作')}</li>
        <li>{T('Competent with Microsoft Office', '熟悉 Microsoft Office')}</li>
        <li>{T('Reading and writing Chinese is an advantage', '懂中文讀寫者優先')}</li>
        <li>{T('Salary negotiable according to experience and qualifications', '薪酬按經驗及資歷面議')}</li>
      </ul>
      <p>{T('You will handle matters from the start and progress from there, with procedural work and research. Send your CV and a covering letter to', '您會由案件開始時參與，逐步承擔更多，工作包括程序事務及資料搜集。請將履歷及求職信電郵至')} <a href="mailto:{FIRM['email']}?subject=Vacancy%3A%20caseworker%20%2F%20trainee%20solicitor">{FIRM['email']}</a>{T('.', '。')}</p>
    </div>
  </div>
</section>
"""


def contact():
    matters = [("", T("Choose one", "請選擇")), ("immigration", T("Immigration and nationality", "移民及國籍")),
               ("conveyancing", T("Residential conveyancing", "住宅物業轉讓")), ("business", T("Small business or commercial property", "小型企業或商業物業")),
               ("probate", T("Wills and probate", "遺囑及遺產承辦")), ("licensing", T("Licensing", "商業牌照")),
               ("notary", T("Notarial services", "公證服務")), ("family", T("Family or charity", "家庭事務或慈善機構")), ("other", T("Something else", "其他"))]
    opts = "".join(f'<option value="{k}"{" disabled selected" if not k else ""}>{n}</option>' for k, n in matters)
    return f"""<div class="page-head">
  <div class="wrap">
    <h1>{T('Call, email or come to Filwood Park', '致電、電郵，或到 Filwood Park 見面')}</h1>
    <p class="lede">{T('Meetings are by appointment. From Hong Kong, you can call our local number.', '會面須預約。身在香港，可撥打本地號碼聯絡我們。')}</p>
  </div>
</div>

<section class="sec">
  <div class="wrap contact-grid">
    <div class="contact-cards">
      <a class="ccard" href="tel:{FIRM['tel_href']}"><span class="ck">{T('Bristol office', '布里斯托辦事處')}</span><span class="cv">{FIRM['tel']}</span></a>
      <a class="ccard ccard-seal" href="tel:{FIRM['hk_href']}"><span class="ck">{T('Calling from Hong Kong', '香港來電專線')}</span><span class="cv">{FIRM['hk']}</span></a>
      <a class="ccard" href="mailto:{FIRM['email']}"><span class="ck">{T('Email', '電郵')}</span><span class="cv cv-sm">{FIRM['email']}</span></a>
      <div class="ccard ccard-plain"><span class="ck">{T('Address', '地址')}</span><address>{'<br>'.join(T(FIRM['addr_en'], FIRM['addr_zh']))}</address><span class="small">{T('Free visitor parking', '訪客免費泊車')}</span></div>
      <div class="ccard ccard-plain"><span class="ck">{T('Opening hours', '辦公時間')}</span>{hours_block()}</div>
    </div>
    <form class="enquiry" id="enquiry" novalidate>
      <h2>{T('Send an enquiry', '網上查詢')}</h2>
      <div class="field"><label for="f-name">{T('Your name', '姓名')}</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="f-contact">{T('Phone or email', '電話或電郵')}</label><input id="f-contact" name="contact" autocomplete="email" required></div>
      <div class="field"><label for="f-matter">{T('What is it about?', '查詢事項')}</label><select id="f-matter" name="matter" required>{opts}</select></div>
      <fieldset class="field"><legend>{T('Preferred language', '希望使用的語言')}</legend>
        <div class="chips">
          {''.join(f'<label class="chip"><input type="radio" name="lang" value="{v}"{" checked" if i == (0 if LANG == "en" else 1) else ""}><span>{v}</span></label>' for i, v in enumerate(["English", "廣東話", "普通話", "Bahasa Melayu"]))}
        </div>
      </fieldset>
      <div class="field"><label for="f-msg">{T('Message', '內容')}</label><textarea id="f-msg" name="message" rows="5" required></textarea></div>
      <p class="form-err" role="alert" hidden></p>
      <button class="btn btn-seal" type="submit">{T('Open in my email app', '用電郵程式發送')}</button>
      <p class="small">{T('This opens a pre-filled email to', '按下後會開啟已填好內容的電郵，寄往')} {FIRM['email']}{T('. Nothing is stored on this website. Please do not send original documents by email; fax and email are not for service.', '。本網站不會儲存任何資料。請勿以電郵寄出文件正本；傳真及電郵不接受法律文件送達。')}</p>
    </form>
  </div>
</section>

<section class="sec visit">
  <div class="wrap visit-grid visit-map-only">
    <div>
      <h2>{T('Finding us', '交通')}</h2>
      <p>{T('Filwood Green Business Park is in south Bristol, off Hengrove Way. There is free parking for visitors.', 'Filwood Green Business Park 位於布里斯托南部，近 Hengrove Way，設有訪客免費泊車位。')}</p>
    </div>
    {map_block()}
  </div>
</section>

<section class="sec sec-tint">
  <div class="wrap two">
    <div class="two-head"><h2>{T('Regulatory information', '規管資料')}</h2></div>
    <div class="prose small-prose">
      <p>{T(f'Leung &amp; Co Law is a trading name of Austen-Jones Solicitors Ltd, registered in England and Wales (company no. 07526477) and authorised and regulated by the Solicitors Regulation Authority, <a href="{FIRM["sra"]}">SRA ID 557238</a>. Registered office: 145 Upland Road, London SE22 0DF. Tel 0845 319 1119.', f'Leung &amp; Co Law 為 Austen-Jones Solicitors Ltd 的營業名稱，於英格蘭及威爾斯註冊（公司編號 07526477），由律師規管局授權及規管，<a href="{FIRM["sra"]}">SRA 編號 557238</a>。註冊地址：145 Upland Road, London SE22 0DF，電話 0845 319 1119。')}</p>
      <p>{T('Notarial services are regulated by the Faculty Office of the Archbishop of Canterbury. Member of the Immigration Law Practitioners\' Association.', '公證服務由坎特伯雷大主教轄下的 Faculty Office 規管。本行為移民法執業者協會（ILPA）會員。')}</p>
      <p>{T('Leung &amp; Co Law Limited, company no. 12372600. VAT reg. no. 682 0016 63.', 'Leung &amp; Co Law Limited，公司編號 12372600。增值稅登記號碼 682 0016 63。')}</p>
      <p><a href="https://www.austenjonessolicitors.co.uk/complaints-procedure/">{T('Complaints procedure', '投訴程序')} ↗</a> · <a href="{P()}{'zh/' if LANG == 'zh' else ''}privacy.html">{T('Privacy notice', '私隱政策')}</a></p>
    </div>
  </div>
</section>
"""


def privacy():
    return f"""<div class="page-head">
  <div class="wrap">
    <h1>{T('Privacy notice', '私隱政策')}</h1>
    <p class="lede">{T('Draft for the firm to review. The current website says a privacy policy is being updated; this is a plain-English starting point under the UK GDPR.', '供本行審閱的草稿。現有網站表示私隱政策正在更新；以下是根據英國 GDPR 撰寫的淺白版本，可作起點。')}</p>
  </div>
</div>
<section class="sec">
  <div class="wrap prose narrow">
    <h2>{T('Who we are', '我們是誰')}</h2>
    <p>{T('Leung &amp; Co Law is a trading name of Austen-Jones Solicitors Ltd (company no. 07526477), 145 Upland Road, London SE22 0DF. For notarial matters, the data controller is Amelia Leung, Notary Public.', 'Leung &amp; Co Law 為 Austen-Jones Solicitors Ltd（公司編號 07526477，145 Upland Road, London SE22 0DF）的營業名稱。公證事務的資料控制者為公證人 Amelia Leung。')}</p>
    <h2>{T('What we collect and why', '收集甚麼資料及原因')}</h2>
    <p>{T('Your name, contact details, identity documents and the information you give us about your matter. We use it to advise and act for you, to meet our legal and regulatory duties (including anti-money-laundering checks), and to keep proper records.', '您的姓名、聯絡資料、身份證明文件，以及您提供的案件資料。我們用這些資料為您提供意見及代表您行事、履行法律及規管責任（包括反洗錢核查），並妥善保存紀錄。')}</p>
    <h2>{T('Who we share it with', '與誰分享')}</h2>
    <p>{T('Only those who need it for your matter: courts and tribunals, the Home Office, HM Land Registry, lenders, other parties\' solicitors, our regulators and insurers, and service providers bound by confidentiality. We never sell your data.', '只會與處理您案件所需的人士分享：法院及審裁處、內政部、土地註冊處、貸款機構、對方律師、規管機構及保險公司，以及受保密責任約束的服務供應商。我們絕不出售您的資料。')}</p>
    <h2>{T('How long we keep it', '保存多久')}</h2>
    <p>{T('Usually at least six years after your matter ends, longer for wills, probate and property files.', '一般在案件完結後保存最少六年；遺囑、遺產承辦及物業檔案會保存更久。')}</p>
    <h2>{T('Your rights', '您的權利')}</h2>
    <p>{T('You can ask for a copy of your data, ask us to correct or delete it, or object to how we use it. Contact', '您可要求索取、更正或刪除您的資料，或反對我們使用資料的方式。請聯絡')} <a href="mailto:{FIRM['email']}">{FIRM['email']}</a>{T('. You can also complain to the', '。您亦可向')} <a href="https://ico.org.uk/make-a-complaint/">{T('Information Commissioner\'s Office', '資訊專員辦公室（ICO）')}</a>{T('.', '投訴。')}</p>
    <h2>{T('This website', '本網站')}</h2>
    <p>{T('This concept website uses no cookies or analytics. The enquiry form opens your own email app and stores nothing.', '本概念網站不使用 cookies 或分析工具。查詢表格只會開啟您的電郵程式，不會儲存任何資料。')}</p>
  </div>
</section>
"""


def notfound():
    return f"""<div class="nf">
  <div class="wrap">
    {seal('nf-seal')}
    <h1>{T('This page has no seal on it', '這一頁沒有蓋印')}</h1>
    <p class="lede">{T('The page you were looking for does not exist. Try the home page, or call us on', '找不到這一頁。請返回首頁，或致電')} <a href="tel:{FIRM['tel_href']}">{FIRM['tel']}</a>{T('.', '。')}</p>
    <p><a class="btn btn-seal" href="{P()}{'zh/' if LANG == 'zh' else ''}">{T('Home page', '返回首頁')}</a></p>
  </div>
</div>
"""


PAGES = {
    "index": (index, ("Leung &amp; Co Law, solicitors and Notary Public in Bristol", "Leung &amp; Co Law｜布里斯托律師行及公證人"),
              ("Immigration, property, probate, licensing and notarial services in Bristol, in English, Cantonese, Putonghua and Malay.", "布里斯托律師行：移民、物業、遺產承辦、商業牌照及公證服務，可用廣東話、普通話溝通。")),
    "services": (services, ("Practice areas | Leung &amp; Co Law", "服務範圍｜Leung &amp; Co Law"), ("Immigration, conveyancing, small business, probate and licensing.", "移民、物業轉讓、小型企業、遺產承辦及牌照。")),
    "notary": (notary, ("Notary Public in Bristol | Leung &amp; Co Law", "布里斯托公證人｜Leung &amp; Co Law"), ("e-Notarisation with e-apostille from £60; home and workplace visits.", "電子公證連電子海牙認證 £60 起；可到府辦理。")),
    "about": (about, ("About the firm | Leung &amp; Co Law", "關於本行｜Leung &amp; Co Law"), ("Established in Bristol in 1996 by Amelia Leung.", "Amelia Leung 於 1996 年創立。")),
    "contact": (contact, ("Contact | Leung &amp; Co Law", "聯絡我們｜Leung &amp; Co Law"), ("Phone, Hong Kong line, email, address and hours.", "電話、香港專線、電郵、地址及辦公時間。")),
    "privacy": (privacy, ("Privacy notice | Leung &amp; Co Law", "私隱政策｜Leung &amp; Co Law"), ("How we use your personal data.", "我們如何使用您的個人資料。")),
}


def build():
    global LANG
    for LANG in ("en", "zh"):
        outdir = ROOT if LANG == "en" else os.path.join(ROOT, "zh")
        os.makedirs(outdir, exist_ok=True)
        for slug, (fn, titles, descs) in PAGES.items():
            html_ = head(slug, T(*titles), T(*descs)) + header(slug) + fn() + footer()
            open(os.path.join(outdir, f"{slug}.html"), "w", encoding="utf-8").write(html_)
    LANG = "en"
    # 404 is served from the root for any language, so it is bilingual
    body = notfound()
    LANG = "zh"
    body_zh = notfound().replace('../', '')
    LANG = "en"
    page = head("404", "Page not found | Leung &amp; Co Law", "Not found") + header("404") + body + body_zh + footer()
    import re
    page = re.sub(r'(href|src)="(?!https?:|tel:|mailto:|#|/)([^"]*)"', lambda m: f'{m.group(1)}="/leung-solicitors/{m.group(2)}"', page)
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(page)
    print("built")


if __name__ == "__main__":
    build()
