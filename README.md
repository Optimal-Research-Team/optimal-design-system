# Optimal Health — Design System

A design system for **Optimal Health Clinic**, a members-only family health clinic based in Barrie, Ontario. This system supports two surfaces:

1. **Website** — marketing site (desktop + mobile) explaining the clinic, membership plans, providers, and FAQ.
2. **Weight-Loss App** — an iOS-style companion app for members doing a weight-loss / behaviour-change program (streaks, lessons, chat with a coach, progress tracking).

The two surfaces share brand DNA — the same **dark forest green** (`#2C4E25`), the same **cream** (`#FFFCF7`) canvas, the same **Castoro** serif for display, the same pill-shaped CTAs and hairline-outlined cards. The app layers a **navy** (`#182E6C`) for system chrome, and swaps Public Sans for **Hanken Grotesk + Inter** for tighter UI typography on small screens.

---

## Sources

Everything in this system was lifted from a single Figma file the user attached as a virtual filesystem:

- **Figma file:** `[Content Copy] Optimal Health Website.fig`
  - `/Website/Desktop` (`node 3:17`) — 1440 px hero, membership benefits, provider cards, pricing, testimonials, FAQ, footer.
  - `/Website/Mobile` (responsive counterpart)
  - `/Weight-Loss-App/Home` (`node 2554:998`) — home, streaks, recent activities, log-activity modal, tab nav.
  - `/Weight-Loss-App/Lessons` (`node 2554:1491`) — modules + lesson path.
  - `/Weight-Loss-App/Chat` (`node 2554:306`) — chat list + in-message view.
  - `/Weight-Loss-App/Progress-Profile` (`node 2554:541`) — profile + activity.
  - `/Icons/Frame-1` — a single nurse illustration.
- **Uploaded logos** (see `assets/logos/`): `OptimalLogo-Green.png`, `OptimalLogo-Opposite.png`, `Optimal_Logo_Inverted.png`, `Optimal_Favicon_Transparent.png`, `symbol-green-nobg.png`, `symbol-white.png`.

The `.fig` pseudocode is the source of truth for values (layout, colour, type, spacing). Screenshots were used only for high-level orientation.

> The user has full access to the Figma; if a value here disagrees with a newer version of the file, trust the file.

---

## Company / product context

> "A new kind of family health clinic is here. A private clinic built for personalized and preventative health. Fees are HSA eligible."

Optimal is a members-only primary care clinic led by **Nurse Practitioners** (NPs) rather than family physicians. The business is Barrie, ON-based (`Optimal Health Holdings Inc., 225 Mapleview Drive East, Unit 3, Barrie, ON, L4N 0W5`), contact `care@beoptimal.ca`, `(437)-370-0291`.

Positioning:
- **Not** a walk-in, **not** telemedicine-only — longer visits, same or next-day bookings, own long-term provider, modern portal.
- Annual in-depth **Longevity Assessment** (positioned at $300 value, included with membership).
- Prescriptions and renewals (including remote).
- Referrals to OHIP-covered specialists when needed.
- Diagnostics, lab tests, imaging orders.
- A "suite of longevity, wellness, and nutrition services (coming soon)" — the weight-loss app is part of that suite.

Membership pricing (from the Figma, 2024):
- **Monthly Plan** — $80 / month, 3-month minimum, "Grand opening" badge.
- **Annual Plan** — $839 / year, "Save $120 annually".
- Both plans are **HSA-eligible**.

Voice highlights from real copy:
- "A new kind of family health clinic is here."
- "Start your journey to lifelong wellness."
- "We're not just here to heal — we're here to hear."
- "Sometimes slower is better: feeling rushed isn't a good experience."

---

## Content fundamentals

**Tone.** Warm, calm, clinical but human. Reassuring without being saccharine. Never breezy, never marketing-y. Reads like a thoughtful clinician talking, not an ad.

**Voice.** Collective first person when describing the clinic ("**We** offer comprehensive care…", "**Our** clinicians…"), direct second person when addressing the reader ("**Your** NP will…", "**You'll** get actionable insights…"). Avoids the corporate "we" that distances — this one feels like a small practice.

**Casing.** Sentence case everywhere **except**:
- All-caps eyebrows above hero and testimonial titles: `WHAT MEMBERS ARE SAYING`, `THIS IS OPTIMAL`.
- Footer section labels: `COMPANY`, `CONTACT`.
- Inline "NEW" chips in hero banners.
- Member bylines under testimonial quotes: `-  KATIE, 56`.

Title case is avoided for body content. Even section headings are sentence case: "Meet the team", "Experience the Optimal difference", "Frequently asked questions", "Your Optimal Membership Benefits" (the only title-cased headline, because "Optimal Membership" is a proper-noun product name).

**Serif italic as emphasis.** A distinctive stylistic tic: key nouns in a headline are set in **italic Castoro** while the rest is roman: *"This is **Optimal**"*, *"Your **Optimal** Membership **Benefits**"*, *"Experience the **Optimal** difference"*, *"Start your journey to lifelong **wellness**"*, *"Meet the **team**"*, *"Frequently asked **questions**"*. The italic word is almost always a brand or benefit-claim.

**Punctuation.** Em-dashes (`—`) for asides, not hyphens. Curly quotes `"…"` and curly apostrophes `'`. Price formatting: `$80/month*` with an asterisk footnote when there's a qualifier (3-month minimum).

**Pronouns.** "I" is never used. "You" addresses the prospective member; "we" / "our" describes the clinic; "your NP" / "your provider" personalises the relationship.

**Emoji.** **Never** used. No emoji appear anywhere in the designs. Use an illustration, an Iconify icon, or nothing.

**Abbreviations.** NP (Nurse Practitioner), PHC (Primary Health Care), HSA (Healthcare Spending Account), OHIP (Ontario Health Insurance Plan). Expanded on first use; comfortable abbreviated thereafter.

**Sample phrasings the system preserves:**
- Product names: "Annual Longevity Assessment", "Longevity+ membership", "Monthly Plan", "Annual Plan".
- CTAs: "Become a member", "Join now", "Learn more".
- Banner: "Now accepting patients in Barrie →" (trailing arrow, no `&rarr;`).
- Testimonial credit: `-  KATIE, 56` — double space after the dash, all-caps name, comma age.
- Copyright: `© Optimal 2024`.
- Legal: `Privacy Policy`.

---

## Visual foundations

**Canvas.** Cream `#FFFCF7` is the default page background on both products. True white `#FFFFFF` is reserved for card surfaces nested on cream (e.g. the pricing card's right pane, the app's streak card, expanded benefit cards). Pure black is used sparingly — only for 1px dividers in comparison tables and the darkest body copy `#040504`.

**Colour vibe.** Earthy, forested, HSA-friendly. The two greens (`#2C4E25` forest, `#1A500F` deep accent, `#87A482` sage at 25% alpha for badges) carry the brand; navy `#182E6C` is exclusively the weight-loss app's header + primary button. **No gradients on buttons.** Two content-scale gradients exist and both go dark green → darker green: the hero overlay (transparent → `#253821`) and the pricing card (`#2C4E25` → `#1C3118`).

**Type.** Four families do everything:
- **Castoro** (serif) — all display headlines. Small x-height, generous ascenders, friendly but classic. Set tight: `line-height: 1.0`, `letter-spacing: -0.04em`. Italic is reserved for the emphasised noun trick.
- **Public Sans** — all website body, buttons, nav, footer. Set at `letter-spacing: -0.02em`, `line-height: 1.1` for tight UI and `1.4` for paragraphs. Weights: 400 body, 500 buttons/nav, 700 "NEW"-style chips.
- **Hanken Grotesk** — weight-loss app section labels and headers only. Bold, tracked tighter (`-0.03` to `-0.04em`).
- **Inter** — weight-loss app body, inputs, stat cards. Regular 400, Medium 500. Tracked `-0.03em`.

No mono. No custom font beyond those four. Helvetica Neue appears only in the iOS status bar render of the device mock.

**Backgrounds.** Full-bleed **photographic imagery** with a dark-green → transparent **linear gradient** over it (bottom of hero). Editorial portraits (patients, clinicians) are used in **circular masks** with a 5px white inner ring. Long cream stretches are broken only by a thin hairline (`1px solid rgb(0,0,0)` in comparison tables, `1px solid rgb(44,78,37)` on benefit cards). The footer is a forest photo with a hard-edged green block over the left half — not a gradient, a clean geometric overlay.

**Ring accents.** A signature detail: **thin elliptical rings** (`1.315px solid rgba(26,80,18,0.5)`) hand-drawn around key words (over "wellness", over "team", under "Frequently asked questions"). These are NOT SVG squiggles — they are simple CSS borders with `border-radius: 50%` positioned over text, sometimes rotated by a few degrees.

**No illustration.** The brand does not use custom illustrations (except the single nurse vector on `/Icons/Frame-1`, which is a filler, not a system asset). It uses **real photography** — clinical portraits, natural imagery, candid members. Imagery vibe is **warm, softly desaturated, natural light**, often slightly green-biased. Never cool, never clinical-sterile stock, never black & white, no grain filter.

**Animation.** The Figma doesn't specify motion. Defaults for this system are conservative: **simple fades and 150–300ms transitions on the standard ease curve** (`cubic-bezier(.2,.7,.2,1)`). No bouncing, no spring, no parallax. Carousel advance is a slide + crossfade.

**Hover states.** None explicitly defined. Recommended:
- Buttons: darken background 6% (for light-on-green) or shift background to forest-700 at 92% (for white-on-dark).
- Links / nav: underline if not already, or colour shift cream → white on dark / forest-700 → forest-900 on light.
- Cards (benefit, lesson): `box-shadow` elevates from none → `var(--shadow-card)`, border stays identical.

**Press states.** A subtle `transform: scale(0.98)` on tappable tiles (log-activity tiles, stat cards) and buttons; no colour change.

**Borders.** Almost everything is **1 px**. The benefit accordion, the monthly/annual pricing pane, the streak card, the lesson module tile, the app search field — all `1px solid`. Colour choices: `#2C4E25` (forest, on light backgrounds), `#76736D` (warm grey, on app chrome) or `rgba(118,115,109,0.25)` (hairline on app cards).

**Shadows.**
- `0px 4px 25px rgba(0,0,0,0.16)` — elevated CTAs that float (hero "Join now", nav "Become a member").
- `0px 4px 25px rgba(0,0,0,0.15)` — app screens and floating log-activity modal.
- `0px 4px 25px rgba(0,0,0,0.25)` — app lesson cards (heavier).
- `0px 4px 13.5px rgba(135,164,130,0.25)` — a sage-tinted glow under the green "Become a member" button on the dark hero. A neat, restrained signature.

No inner shadows. No multi-layer shadow stacks.

**Protection gradients vs capsules.** The nav bar on the hero uses a **blurred dark capsule** (`rgba(0,0,0,0.35)` + `backdrop-filter: blur(21px)`, `border-radius: 54px`) rather than a linear-gradient protector. The carousel pager under testimonials is another blurred capsule (`rgba(255,255,255,0.25)` + `blur(4.945px)`). The design preference is **capsules, not gradient scrims**.

**Corner radii.**
- **`48px` pill** — every single CTA and the "Accepting patients in Barrie" hero chip.
- **`54px` pill** — the nav bar capsule.
- **`8px`** — pricing card, lesson module card, comparison-table vertical highlighter, badge fills.
- **`4px`** — streak cells, lesson tile, search inputs, app log-activity tiles (small UI chrome).
- **`50%` ellipse** — hand-drawn ring accents around words, circular photo masks (with a 5px white inset border).
- **`0`** — benefit accordion rows, footer split, section dividers. Sharp edges are used deliberately when the content is editorial/newsprint-feeling.

The hierarchy: **pills for action, 8 px for content cards, 4 px for UI chrome, sharp edges for editorial blocks**.

**Cards.**
- *Website benefit card* (closed): outlined rectangle, no shadow, `1px solid #2C4E25`, padding `16px 24px`, Castoro 24 px title, tabler:chevron-up icon on the right.
- *Website benefit card* (open): adds 20 px Public Sans body copy below, height grows to 148 px.
- *Pricing card*: 8 px radius, forest→forest-dark gradient with a white `#FFFCF7` right pane, no border.
- *App stat card*: 1 px warm-grey border, 4 px radius, icon top-left, value + label inside.
- *App lesson card*: full-bleed photo, 1 px `#76736D` border, progress bar top-left on a `rgba(255,255,255,0.25)` capsule, title bottom-left white on a black-to-transparent gradient.

**Layout rules.**
- Desktop grid: 1440 canvas, content aligned to a ~76 px side gutter, core content width ~1288–1345 px.
- Mobile app: 390×844 iOS viewport, 96 px header bar, 16 px side inset, 71 px tab bar at bottom.
- Sections sit flush to the gutter — no max-width centering that leaves huge margins.
- Pills on cream are green-filled or white-filled with green text; never outlined-on-cream (white fill is the outlined equivalent, relying on shadow to separate).

**Transparency and blur.**
- Only two places use `backdrop-filter: blur(...)` — the top nav (21 px blur) and the carousel pager (~5 px blur).
- `rgba(...)` is used for: nav dim, pager dim, sage badge fill (25%), chip strokes (50%), body copy at 90% on dark (`rgba(255,255,255,0.9)`).
- Never use translucent whites or greens for card surfaces — they're opaque.

**Iconography:** see the dedicated section below.

---

## Iconography

**Primary icon system: Iconify, multi-set.** The Figma's external components reference Iconify icons by their canonical name. Concrete icons in use:

| Use | Iconify name |
| --- | --- |
| Notification bell (app header) | `cuida:notification-bell-outline` |
| Hydration (Water) | `mdi:water-outline` |
| Protein | `tabler:meat` |
| Exercise | `icon-park-outline:dumbbell` |
| Meditation | `iconoir:yoga` |
| Lesson complete (check) | `lets-icons:check-fill` |
| Chat list | `majesticons:chat-line` |
| Streak / fire | `mdi:fire` |
| Calendar (upcoming events) | `fe:calendar` |
| Chat send | `tabler:send` |
| Chat attach | `uil:paperclip` |
| Chat search | `mingcute:search-line` |
| Profile tab | `gg:profile` |
| Goal | `octicon:goal-16` |
| Edit | `lucide:edit` |
| Chevron (menu, accordion) | `tabler:chevron-up` |

These are served from `https://api.iconify.design/` via the `<iconify-icon>` web component. Stroke and fill style varies by set — outline on dark navy chrome, solid on check states. **When an icon isn't in the Iconify list above, pick the nearest same-set match rather than mixing a new family in.**

**SVG inline.** The site's logo, ring accents and a couple of bespoke tab-bar glyphs are inline SVG — see `assets/logos/*.png` (rasterised exports from Figma) and the inline SVG fragments in each UI kit. These are **not redrawn**; they were extracted from the Figma binary.

**Logo variants** (in `assets/logos/`):
- `OptimalLogo-Green.png` — primary wordmark, green on cream.
- `OptimalLogo-Opposite.png` — wordmark for dark backgrounds.
- `Optimal_Logo_Inverted.png` — fully inverted variant.
- `symbol-green-nobg.png` — just the mark, green, transparent bg.
- `symbol-white.png` — mark, white, for app chrome.
- `Optimal_Favicon_Transparent.png` — favicon.

**Emoji:** never used. Do not substitute an emoji for a missing icon — use an Iconify fallback or leave it blank.

**Unicode as icon:** sparingly and intentionally. The hero banner uses `→` (U+2192) rather than an SVG arrow. The chat time separator in messages uses a middle dot. Don't go beyond these.

---

## Index

| Path | Purpose |
| --- | --- |
| `README.md` | You are here. |
| `SKILL.md` | Agent-compatible entrypoint. |
| `colors_and_type.css` | All design tokens: colour, type, radii, shadows, spacing, semantic styles. |
| `assets/logos/` | Wordmark + symbol exports. |
| `assets/images/` | Photographic assets lifted from the Figma. |
| `fonts/` | Empty — system currently imports Google Fonts. See CAVEATS. |
| `preview/` | Small HTML cards surfaced on the Design System tab — colour swatches, type specimens, spacing, components. |
| `ui_kits/website/` | Hi-fi recreation of the marketing website (desktop). `index.html` is a clickable reference. |
| `ui_kits/weight-loss-app/` | Hi-fi recreation of the mobile app screens (home, lessons, chat, progress). `index.html` shows all four. |

### Caveats
- **Fonts are loaded from Google Fonts**, not shipped as TTFs in `fonts/`. All four families (Castoro, Public Sans, Hanken Grotesk, Inter) are free and available there, so this is usually fine — but if you need offline usage please drop TTFs into `fonts/` and adjust the `@font-face` in `colors_and_type.css`.
- **Hover / press / focus states** are not in the Figma. The values in this system are defensible defaults, not designer-signed-off.
- **No dark mode.** Neither product has a dark scheme in the Figma.
- **No illustrated iconography.** The nurse SVG on `/Icons/Frame-1` is a filler, not a system asset.
