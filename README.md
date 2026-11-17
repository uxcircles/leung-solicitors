# Leung & Co Law：網站重新設計概念

這是 UX CIRCLES 為 Leung & Co Law（布里斯托）製作的**非官方**重新設計概念網站，並非該律師行的官方網站。
官方網站：http://leung-solicitors.co.uk/

- 線上版：https://uxcircles.github.io/leung-solicitors/ （英文）、`/zh/`（繁體中文，香港用語）
- 每一頁都有 noindex，`robots.txt` 禁止收錄，不會跟官方網站搶搜尋排名。

## 頁面

| 頁面 | 英文 | 中文 |
|---|---|---|
| 首頁 | `index.html` | `zh/index.html` |
| 服務範圍 | `services.html` | `zh/services.html` |
| 公證服務 | `notary.html` | `zh/notary.html` |
| 關於我們、職位空缺 | `about.html` | `zh/about.html` |
| 聯絡（查詢表格、地圖、規管資料） | `contact.html` | `zh/contact.html` |
| 私隱政策（草稿） | `privacy.html` | `zh/privacy.html` |
| 404（雙語） | `404.html` | |

## 如何修改

所有頁面由 `_build/pages.py` 產生，英文和中文並排寫成 `T("English", "中文")`，聯絡資料集中在 `FIRM`。

```bash
python3 _build/pages.py     # 重新產生全部 HTML
python3 _build/fonts.py     # 改過中文字之後執行：只下載用到的中文字
```

改 CSS 或 JS 後，記得把 `pages.py` 裡的 `V` 加一，以及 `site.js` 裡 `map.js?v=` 的版本號。

- 標誌：`_build/trace_logo.py` 將官方網站上的 `LeungBirdC.jpg` 描成向量 `assets/img/seal.svg`。
- 地圖：MapLibre GL（BSD）＋ OpenFreeMap，配色在 `assets/map.js` 頂部的 `C`，捲動到附近才載入，下面有草圖作後備。
- 表格沒有後端：驗證後開啟已填好內容的電郵，網站不儲存任何資料。

## 設計概念

- **標誌元素**：律師行自己的朱紅橢圓印章，中間是一隻鳳鳥（呼應 Phoenix Consultancy）。它出現在頁首、首頁左右兩半的接縫、地圖釘、favicon、分隔線、公證頁頁首和 404 頁。
- **首屏類型**：`bilingual-split`（作品集中第一次使用）。左邊英文，用紙色底配布里斯托電話；右邊中文，用深印泥紅底配香港專線 9537 5410。兩半在印章處相遇。原網站寫著「Calling from Hong Kong: 9537 5410」，而且服務以英語及中文提供，所以用雙語分割最貼切。中文版左右對調。
- **字體**：英文用 Spectral（標題，帶文書氣質的襯線體）配 Onest（內文）；中文用 Chiron Sung HK（標題）配 Chiron Hei HK（內文），屬香港字形，配合 Amelia 的香港背景（香港中文大學）。這四款字體作品集都未用過。
- **顏色**：全部取自印章：朱紅 #e5601e 只用於圖形；印泥紅 #8a2c12 用於文字及大色塊，在紙色上對比度 8:1；深墨色 #201a17；紙色 #fbf8f2。
- **標題**：「A Bristol law office you can also ring from Hong Kong」／「人在香港，也找得到布里斯托的律師」
- **與上兩個律師行概念的分別**：Chung & Rea 是 document-object、中性黑白、Young Serif；Lu Oliphant 是 split-info-card、深藍、雙時鐘。這次沒有拱形相框、資訊卡、數字列，也沒有斜體強調。

## 需要律師行確認的事項

原網站多處資料互相矛盾，概念網站的選擇如下：

1. **SRA 編號**：首頁寫 557238，聯絡頁寫「ID No. 5572638」。SRA 登記冊上 Austen-Jones Solicitors Limited 是 **557238**，所以概念網站用 557238。
2. **電郵**：關於頁是 info@leung-solicitors.co.uk，聯絡頁及職位頁是 info@leung-law.co.uk，公證網站是 info@phoenix-law.uk。概念網站統一用 info@leung-solicitors.co.uk。
3. **電話**：總機 0333 577 7168（首頁、聯絡頁），Amelia 直線 0333 577 6688（關於頁、Austen Jones 網站）。
4. **辦公時間**：頁首寫「Today 9 AM – 5:30 PM」，聯絡頁寫 9:30–18:00。概念網站用 9:30–18:00，晚上及星期六的公證預約時間取自公證網站。
5. **公證人資格年份**：關於頁及 Austen Jones 網站寫 2009 年取得資格，公證網站寫 2010 年獲委任（劍橋大學公證實務深造文憑）。概念網站寫 2010 年獲委任。
6. **Taylor Rose**：首頁提到亦加入 Taylor Rose Limited（SRA 623604），但聯絡頁及頁尾只提 Austen-Jones。概念網站只寫 Austen-Jones，需要確認。
7. **移民服務用語**：原網站寫「Tiers 1 and 2」，這個分級制度 2020 年後已被取代。概念網站改寫成「points-based system」，沒有列出具體簽證類別。
8. **私隱政策**：原網站仍寫「New data protection legislation is coming into force」（2018 年）。`privacy.html` 是根據英國 GDPR 寫的草稿，需要律師行審閱。
9. **公證收費**：電子公證連電子海牙認證「£60 起」、到府服務最低 £50（布里斯托區），均取自公證網站。
10. 「預約前請準備」是一般指引，需要公證人確認。

沒有使用圖庫相片，沒有虛構評價、人物或數字。
