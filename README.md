# market-bell-site

Landing + support + privacy pages for **Market Bell** (iOS). Served by GitHub Pages at
`https://artzmy.github.io/market-bell-site/`.

| File | Purpose | Referenced by |
|------|---------|---------------|
| `index.html` | Landing page — this is what you share | — |
| `support.html` | Support page | **ASC → version page → Support URL** |
| `privacy.html` | Privacy policy | **ASC → App Information → Privacy Policy URL** |
| `style.css` | Shared styles (light + dark) | all pages |
| `icon.png` | App icon, 512px — hero, favicon **and** `og:image` | all pages |

## The share thumbnail is just the app icon

`og:image` on every page points at `icon.png` (512×512). Deliberate: no custom
1200×630 card is maintained, so there is nothing to keep in sync or re-cut.

Consequences worth knowing:

- Platforms that want a wide card (Twitter/X, WhatsApp, Telegram) will render a **small
  square thumbnail** instead of a large banner, because the image is square. That is the
  accepted trade-off, not a bug.
- WeChat and iMessage crop `og:image` toward a square anyway, so a square source is
  actually the safest single asset.
- If a real card is ever made, add it as a **new versioned filename** (`og-v2.png`) and
  point the tags at it. WhatsApp, Telegram, iMessage and Slack cache `og:image` by URL,
  sometimes for weeks — **never overwrite an existing og image in place**, or people keep
  seeing the old one.

## App Store links carry campaign tokens

Download buttons link to `…/id6783567802?ct=<token>`:

- `ct=site-landing` — hero button
- `ct=site-landing-bottom` — footer button

`ct` shows up in App Store Connect → Analytics, so installs coming from this site can be
told apart from App Store search. Add a `pt=` provider token alongside `ct` if you want
the stricter legacy campaign attribution.

## Local preview

    python3 -m http.server 8000

then open `http://localhost:8000`.
