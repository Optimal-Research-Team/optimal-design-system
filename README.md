# Optimal Health — Design System

A design system for **Optimal Health Clinic**, a members-only family health clinic based in Barrie, Ontario. This system supports two surfaces:

1. **Website** — marketing site (desktop + mobile) explaining the clinic, membership plans, providers, and FAQ.
2. **Weight-Loss App** — an iOS-style companion app for members doing a weight-loss / behaviour-change program (streaks, lessons, chat with a coach, progress tracking).

The two surfaces share brand DNA — the same **dark forest green** (`#2C4E25`), the same **cream** (`#FFFCF7`) canvas, the same **Castoro** serif for display, the same pill-shaped CTAs and hairline-outlined cards. The app layers a **navy** (`#182E6C`) for system chrome, and swaps Public Sans for **Hanken Grotesk + Inter** for tighter UI typography on small screens.

---

## What's new in v1.4 (Oct 24, 2026)

The Specimen layer, from the *Specimen* concept film. It adds generated plates in four families, motion plates (the same plates as short moving clips), and the rules for conceptual brand films.

**Generated plates** (`assets/illustration/specimen/`)
- **Engraved** (`engraved/`): écorché (Vitruvian, with a cloth wrap), bronchial tree, iris, cochlea, spine, neuron, hand, alveoli, femur and heart. Each is transparent ink trimmed to the drawing, in the v1.2 convention: `name.webp` in forest ink `#183015` for cream grounds and `name-cream.webp` in cream ink for Forest Night.
- **Red-chalk studies** (`chalk/`): heart, head and knee, 2560×1440 on their own cream paper. Red chalk is the only warm accent in its frame.
- **Specimens on cream** (`specimens/`): dandelion, birch rings, fiddlehead, maple leaf, pomegranate, robin's egg, honeycomb and lichen stone. Each is one object on cream seamless `#FCF8F1`, 2560×1440.
- **Ontario** (`ontario/`): oak in snow, delta, kettle lake, lightning over a lake, frost, a starling murmuration, lake ice, pine on granite, gneiss, maple canopy, surf, moonrise over lake ice and a birch forest. All are photo-graded, 2560×1440. Never caption one as a named real place.
- Export script: `tools/specimen_export.py`. Preview: `preview/specimen.html`.

**Motion plates** (`assets/illustration/specimen/motion/` has eight 1280×720 samples)

Any plate can become a short moving clip: lungs breathe, an iris dilates, a heart beats, neurons fire, starlings flow, surf rolls in.
1. **Generate.** Make an image-to-video clip from the plate, or from its original generation id, with Higgsfield `kling3_0` in mode `pro`, sound off. Use 3 s, or 5 s for a hold longer than about 2.5 s. The prompt is the subject's motion in one sentence, followed by its family's suffix:
   - Engraved: "Locked-off camera: no zoom, no pan, no camera movement. Small, gentle movement only. It stays a flat Victorian steel engraving in dark green ink on cream paper in every frame: the same crisp cross-hatched line work, no colour, no solid black fills, no 3D, no photorealism. The cream paper stays still."
   - Red chalk: "Locked-off camera: no zoom, no pan. It stays a red-chalk drawing on cream paper in every frame: the same loose chalk lines and construction grid, no colour change, no 3D, no photorealism. Small, gentle movement only."
   - Specimen: "Locked-off camera: no zoom, no pan. The object stays in place on its cream seamless backdrop under soft studio light. Subtle motion only. Keep the exact colours and composition."
   - Photograph: "Locked-off tripod camera: no zoom, no pan, no camera shake. Subtle, natural real-world motion only. Keep the exact colours, light and composition of the photograph."
   - Micrograph: "Locked-off microscope view: no zoom, no pan, no rotation. A live-cell time-lapse. Keep the exact colours, the near-black background and the scientific microscopy look."
2. **Grade it back to its still:** `python3 tools/motion_plate.py raw.mp4 still.jpg engraving|night|match out.mp4 [--graded-source]`. Engravings are re-mapped to the ink duotone, so any solid fills the model adds fall back into line work. Forest Night clips are inverted from the engraving clip rather than generated separately.
3. **Play about 0.9 s of motion per shot.** In a short cut the clip runs up to 3× faster; holds play at 1×. `playback()` in the same script returns the media start and rate, and gives each reuse of a plate a different stretch of its clip. Use the first second or so: later frames can drift (a hand curls into a fist, nuclei turn into rings).
4. **Check** that the engraving is still line work and that nothing flashes past the WCAG three-flashes rule (lightning, glints). If a later overlay depends on a subject's position, as the logo handoff depends on the moon, it must stay within a pixel of the still.

**Rules for concept films**

These apply to brand films with no voice or copy, like *Specimen*.
- No words on screen: no captions, Fig. labels, plate counters, leader lines or taglines, and no numerals in the image. The film ends on the "Into Range" logo alone.
- No ring accents drawn around subjects; the only ring is the logo's. A ring may come from a subject's own edge (the moon's limb) on its way to the logo's ring.
- Living anatomy only: no skeletons, skulls or skeletal hands. Bone in cross-section and the spine as a study are fine. A longevity brand doesn't centre death.
- Stills move: every plate plays as a motion plate.
- Music is licensed, low-key, uplifting ambient in the Brian Eno vein: slow pads in a major or Lydian key, with no piano, no beat and nothing percussive. Never use a synthesized bed. Master to −15 LUFS with one static gain and a limiter, because single-pass loudnorm flattens the arc. Pixabay's and Mixkit's licences cover ads. Record each track's YouTube Content ID status; it doesn't affect Meta.
- Deliver a 16:9 master plus 9:16, 1:1 and 1.91:1 for Meta, all full-bleed. Use 9:16 outpaints for photographs that a crop would lose. The Reels safe zone is 269 px at the top, 672 px at the bottom and 65 px at the sides.
- Safety: a 2-frame floor, with dark frames grouped so light and dark never alternate more than three times a second (WCAG 2.3.1).
- Everything here is generated and illustrative: no AI people or faces as photographs (drawn anatomy is fine), no clinic rooms and no generated text.

## What's new in v1.3 (Oct 22, 2026)

The micrograph layer: cell and tissue microscopy for research pages, explainers, social posts and film. It has two families, one on each of the system's grounds, so the images sit with the plates instead of fighting them.

- **Fluorescence** (`assets/illustration/micrographs/fluorescence/`): cardiomyocytes, neurons, mitochondria in a fibroblast, a pancreatic islet, retinal vasculature, an oocyte in its follicle, a skeletal-muscle cross-section and an intestinal organoid. Each is graded onto night-950 `#0B1608` with one fixed three-stain palette: **leaf green** for structure, **coral** for the subject of the story, and **cyan** for nuclei.
- **Brightfield** (`assets/illustration/micrographs/brightfield/`): H&E thyroid follicles, an H&E liver lobule, Masson's-trichrome trabecular bone and a Wright-stained blood smear. The slide is balanced to cream `#FCF8F1`.
- **Field plates** (`assets/illustration/micrographs/field/`): 1600×1600 squares with a circular field of view and a ring accent, so the microscope eyepiece and the brand ring become one shape. Fluorescence fields sit on forest-night `#152511` and brightfield fields on cream.
- Grading script: `tools/micrograph_grade.py`. Preview: `preview/micrographs.html`.

**Rules for micrographs**
- Fluorescence goes on Forest Night grounds and brightfield on cream, never the other way round.
- One micrograph per frame. Don't set a micrograph beside a plate or a figure; in film they may follow one another as a shape rhyme (engraved neuron, then fluorescent neuron).
- The stain palette is fixed: leaf green, coral and cyan. Don't recolour an image or add a fourth stain colour. Make new images with the recipe below and grade them with the script.
- Fit the subject to the topic: the islet for metabolic health, the oocyte for menopause and fertility, cardiomyocytes for the heart, mitochondria or muscle for VO₂ max, the retina for vessels and ApoB, the blood smear for iron, thyroid follicles for the thyroid, trabecular bone for bone.
- These images are generated and illustrative. Never present one as a member's sample, a lab result or the clinic's own research, and keep them out of the results page's data panels. Captions name the structure ("*Fig. 3* Cardiomyocytes"), not a protocol or an antibody.
- Use them full-bleed or as a field plate, never as a rounded-card crop. Social and video exports take the same mild grain as everything else.

**Recipe** (Higgsfield `gpt_image_2_5`, 16:9, quality high, 2k):
- Fluorescence: "Confocal fluorescence micrograph of [cells or tissue]: [structure] stained leaf green, [subject] in warm coral, nuclei in cyan-blue. Deep near-black background with the faintest dark green tint. Realistic scientific immunofluorescence microscopy, rich saturated colour, high dynamic range. No text, no scale bar, no labels, no watermark."
- Brightfield: "Brightfield light micrograph of a [stain]-stained section of [tissue] at [10x or 20x]: [what fills the frame]. Warm pale cream slide background. Realistic scientific histology, crisp cellular detail, natural stain colours, gentle vignette. No text, no scale bar, no labels, no watermark."
- Then run `python3 tools/micrograph_grade.py <pngs> <film-out> assets/illustration/micrographs`.

## What's new in v1.2 (Oct 12, 2026)

The illustration, motion and social layer, built for the @beoptimal.ca Instagram relaunch.

- **Engraved plates.** `assets/illustration/plates/`: sage steel-plate engravings of organs (blood, heart, thyroid, liver, kidney, pancreas, ovary, testis, lymph, bladder, electrolytes, nutrients) and a lakeshore. Each comes in green ink for cream grounds and `-cream` ink for forest grounds. They first appeared on the longevity results page.
- **Engravings.** `assets/illustration/engravings/`: the IV iron set (iron tablets, gut wall, stomach, IV bag, vein with red cells, liver, test tubes, figures of women), plus ApoB particles and arterial plaque. Same ink and both variants.
- **Isometric figures.** `assets/illustration/figures/`: still frames of the 15 interactive anatomy figures from [optimal-anatomy-figures](https://optimal-research-team.github.io/optimal-anatomy-figures/), as transparent images. Embed the live versions from that repo, and never recolour them.
- **Social layer.** `social.css`: 1080px frames (post 1080×1350, story/reel 1080×1920), safe areas, forest hairline hatching, ring accents, capsules over photos, hatched stat numerals, the keyword pill and the photo grade.
- **Grain.** `assets/textures/grain-1024.png`. Social and photo exports take a mild monochrome film grain, about 8/255 on photos and 6/255 on flat grounds, applied at export and never to UI. This is a deliberate change (Peter, Oct 12) to the original "no grain" rule, and it covers social only.
- Previews: `preview/illustration.html` and `preview/social.html`.

**Rules for the layer**
- Use one illustration per frame. Engravings go on cream, or in their cream ink on forest.
- Forest grounds are reserved for cream-ink engravings. Every other social frame sits on cream or sage.
- Text over photos sits in a capsule (`rgba(28,49,24,.9)`), never on a dark gradient.
- Social copy follows the menopause and ad guardrails: no drug brand names, no outcome timelines, no testimonials, and comparisons only where they're factual.

## What's new in v1.1 (Oct 2026)

- **The animated logo, "Into Range".** `assets/logos/optimal-logo.js` is the `<optimal-logo>` web component: live SVG, 12 KB gzipped, no dependencies. Video renders are in `assets/motion/`. Preview: `preview/brand-logo-animated.html`. Source repo: [optimal-logo-animation](https://github.com/Optimal-Research-Team/optimal-logo-animation).
- **Forest night, a dark theme.** `forest-night.css` holds the dark scheme already used on the clinic TVs, the hormone explainers and the anatomy figures. Load it after `colors_and_type.css` and add `class="forest-night"`.
- **Current clinic facts** (below). The April 2026 Figma predates the clinic's move and current pricing.
- **Ready for other projects** as a Claude Code skill, a CDN link or an npm dependency (below).

### Current clinic facts (Oct 2026)

These override the Figma-era values in "Company / product context" and the UI kits.

| | |
| --- | --- |
| Address | 630 Huronia Rd, Unit 5, Barrie, ON L4N 0W5. The Mapleview Dr E address in the UI kits is out of date. |
| Contact | care@beoptimal.ca · (437) 370-0291 · Instagram @beoptimal.ca |
| Booking | `https://book.beoptimal.ca`, optionally with `?service=hormone`, `hbot`, `vo2max`, `creator600` or `inbody` |
| Hours | Mon 9–5 · Tue 8:30–8 · Wed 10–6 · Thu 9–8 · Fri 9–4 |
| Membership | Longevity Membership Core: annual and HSA eligible. Prices change, so take them from beoptimal.ca/membership. Never reuse the Figma's 2024 prices ($80/month, $839/year). |
| Live services | Menopause & Perimenopause Care, VO₂ Max Testing, Creator 600 running gait analysis, InBody 580, Hyperbaric Oxygen Therapy (at a partner facility; always use the site's investigational wording), and the free Optimal Longevity Protocol and Optimal Menopause Protocol guides |
| Not launched | Men's Hormone Optimization Protocol and a standalone Longevity Assessment. Don't advertise either until they are live. IV iron is pre-launch: advertise only the founding waitlist (no referral required, founding rate set at launch). |
| Care team | Led by Nurse Practitioners, with a physician medical advisor |

Headlines from the live site that follow the italic-noun rule: *"A **new** kind of health clinic is here."*, "Seen this week. Not this month.", *"This is **Optimal**."*, "Measured, not estimated.", *"Start with a **conversation**, not a treadmill."*

### Using this in other projects

**As a Claude Code skill.** This is the recommended route for cloud sessions. Put the repo at `.claude/skills/optimal-design-system/` inside the project:

```bash
git submodule add https://github.com/Optimal-Research-Team/optimal-design-system .claude/skills/optimal-design-system
```

You can also run `git clone --depth 1 <url> .claude/skills/optimal-design-system` for a one-off copy. `SKILL.md` has skill frontmatter, so Claude Code loads it as the `optimal-design-system` skill, and every path it mentions resolves inside that folder.

**From a CDN.** jsDelivr serves the public repo. Pin a tag:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Optimal-Research-Team/optimal-design-system@v1.4.0/colors_and_type.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Optimal-Research-Team/optimal-design-system@v1.4.0/forest-night.css">
<script src="https://cdn.jsdelivr.net/gh/Optimal-Research-Team/optimal-design-system@v1.4.0/assets/logos/optimal-logo.js" defer></script>
```

**From npm.** This installs straight from GitHub:

```bash
npm i github:Optimal-Research-Team/optimal-design-system#v1.4.0
```

```js
import 'optimal-design-system/tokens.css';        // = colors_and_type.css
import 'optimal-design-system/forest-night.css';  // optional dark theme
import 'optimal-design-system/optimal-logo.js';   // registers <optimal-logo>
```

**Browse it:** https://optimal-research-team.github.io/optimal-design-system/

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

> Figma-era context (2024). For the current address, services and pricing see "Current clinic facts" above.

Optimal is a members-only primary care clinic led by **Nurse Practitioners** (NPs) rather than family physicians. The business is Barrie, ON-based (`Optimal Health Holdings Inc., 225 Mapleview Drive East, Unit 3, Barrie, ON, L4N 0W5`), contact `care@beoptimal.ca`, `(437)-370-0291`.

Positioning:
- **Not** a walk-in, **not** telemedicine-only — longer visits, same or next-day bookings, own long-term provider, modern portal.
- Annual in-depth **Longevity Assessment** (positioned at $300 value, included with membership).
- Prescriptions and renewals (including remote).
- Referrals to OHIP-covered specialists when needed.
- Diagnostics, lab tests, imaging orders.
- A "suite of longevity, wellness, and nutrition services (coming soon)" — the weight-loss app is part of that suite.

Membership pricing (from the Figma, 2024; **historical, do not reuse**):
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

**Animation.** The Figma doesn't specify motion. The one signature motion piece is the animated logo (see "What's new in v1.1"). Defaults for this system are conservative: **simple fades and 150–300ms transitions on the standard ease curve** (`cubic-bezier(.2,.7,.2,1)`). No bouncing, no spring, no parallax. Carousel advance is a slide + crossfade.

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
| `forest-night.css` | Forest night dark theme (v1.1). Remaps the semantic tokens. |
| `social.css` | Social layer (v1.2): 1080px frames, hatching, ring accents, capsules, stat numerals, keyword pill. |
| `assets/illustration/` | Engraved plates, engravings and isometric figure stills (v1.2), WebP with transparency. |
| `assets/textures/grain-1024.png` | Tileable film grain for social exports (v1.2). |
| `assets/illustration/micrographs/` | Fluorescence and brightfield micrographs plus square field plates (v1.3), WebP. Grading script in `tools/micrograph_grade.py`. |
| `assets/logos/optimal-logo.js` | `<optimal-logo>` animated logo web component (v1.1). |
| `assets/motion/` | "Into Range" logo renders, cream and forest green, 16:9 / 9:16 / 1:1 (v1.1). |
| `index.html` | Gallery of every preview card and UI kit, served on GitHub Pages. |
| `package.json` | Lets projects install the system from GitHub with npm. |
| `assets/logos/` | Wordmark + symbol exports, plus the animated logo component. |
| `assets/images/` | Photographic assets lifted from the Figma. |
| `fonts/` | Empty — system currently imports Google Fonts. See CAVEATS. |
| `preview/` | Small HTML cards surfaced on the Design System tab — colour swatches, type specimens, spacing, components. |
| `ui_kits/website/` | Hi-fi recreation of the marketing website (desktop). `index.html` is a clickable reference. |
| `ui_kits/weight-loss-app/` | Hi-fi recreation of the mobile app screens (home, lessons, chat, progress). `index.html` shows all four. |

### Caveats
- **Fonts are loaded from Google Fonts**, not shipped as TTFs in `fonts/`. All four families (Castoro, Public Sans, Hanken Grotesk, Inter) are free and available there, so this is usually fine — but if you need offline usage please drop TTFs into `fonts/` and adjust the `@font-face` in `colors_and_type.css`.
- **Hover / press / focus states** are not in the Figma. The values in this system are defensible defaults, not designer-signed-off.
- **Dark mode** isn't in the Figma. `forest-night.css` (v1.1) is the dark scheme already in use on Optimal's TVs, explainers and anatomy figures.
- **No illustrated iconography.** The nurse SVG on `/Icons/Frame-1` is a filler, not a system asset.
