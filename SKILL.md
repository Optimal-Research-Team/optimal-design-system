---
name: optimal-design-system
description: Optimal Health (Barrie, ON) brand design system. Covers colours, typography, voice, components, logos, the Forest night dark theme, the animated "Into Range" logo, and the engraved-plate illustration and social layer. Use for any page, deck, email, ad, social post, TV screen or app screen that represents Optimal.
---

# Optimal Health Design System — SKILL.md

Agent entrypoint for the **Optimal Health** brand. Optimal is a members-only, Nurse Practitioner-led family health clinic in Barrie, Ontario, plus a companion **weight-loss app** used by members.

## When to use
- Any artifact (web page, email, deck, brochure, app screen, prototype) that represents Optimal externally.
- Any work that touches the marketing site or the weight-loss app.
- When you need brand colours, typography, voice, or reusable components.

## Current facts first (Oct 2026)
The Figma is from 2024. Before writing any copy, read "Current clinic facts" in `README.md`:
- The address is 630 Huronia Rd, Unit 5, not Mapleview.
- Prices come from beoptimal.ca/membership, never the Figma's $80/$839.
- Don't advertise anything still marked coming soon.

## Get oriented in this order
1. Read `README.md` — the single source of truth for company context, content fundamentals, visual foundations, and iconography. Don't skip the "Content fundamentals" and "Visual foundations" sections; the brand has specific tics (italic-noun emphasis, ring accents, pills-not-rectangles) that are easy to miss.
2. Load `colors_and_type.css` — all design tokens (colour, type, radii, shadows, spacing) and semantic element styles. Import it from any new HTML file with:
   ```html
   <link rel="stylesheet" href="/path/to/colors_and_type.css">
   ```
   Then add `class="oh"` to the document root (or `<body>`) to get default type and background.
3. Reference the two working UI kits:
   - `ui_kits/website/index.html` — full desktop marketing page (hero → benefits → accordion → comparison → pricing → team → testimonial → FAQ → footer).
   - `ui_kits/weight-loss-app/index.html` — Home, Lessons, Chat, Progress screens in a pan/zoom design-canvas layout.
   Copy working markup from these kits rather than rebuilding from scratch.
4. Reference `preview/` for single-purpose specimens of colour swatches, type scale, spacing, components, logo variants, and iconography.
5. **Dark surfaces** (TVs, explainers, dark dashboards): add `forest-night.css` after the tokens and put `class="forest-night"` on the root. Don't invent a new dark palette.
6. **The animated logo**: load `assets/logos/optimal-logo.js`, then use `<optimal-logo variant="stage|inline" theme="light|dark" play="visible|load|manual">`. Use it for ambient screens, reel outros, footers and booking confirmations, never a hero. Video renders are in `assets/motion/`. Preview: `preview/brand-logo-animated.html`.
7. **Illustration and social (v1.2)**: for posts, stories, ads and explainers, use `assets/illustration/` (engraved plates, engravings, isometric figure stills) and `social.css`. Engravings go in green ink on cream, or cream ink on forest. Forest grounds are only for cream-ink engravings. Use one illustration per frame, add mild grain at export (`assets/textures/grain-1024.png`), and put text over photos in capsules. Previews: `preview/illustration.html`, `preview/social.html`.
8. **Micrographs (v1.3)**: `assets/illustration/micrographs/` holds fluorescence micrographs (for Forest Night grounds), brightfield stained sections (for cream) and square field plates with a ring accent. The stain palette is fixed (leaf green, coral, cyan). Use one per frame, matched to the topic. They are generated and illustrative: never show one as a member's sample or a lab result. Preview: `preview/micrographs.html`. The README has the rules and the recipe.
9. **Specimen plates, motion plates and concept films (v1.4)**: `assets/illustration/specimen/` holds generated plates in four families: engraved (transparent ink, `name.webp` for cream grounds and `name-cream.webp` for Forest Night), red-chalk studies, specimens on cream and Ontario photographs. Any plate can move: generate a 3 s image-to-video clip, grade it back to its still with `tools/motion_plate.py`, and play about 0.9 s of motion per shot. Concept films (no voice or copy) carry no words or numerals on screen, no ring accents and no skeletons. They score with licensed, low-key, Eno-style ambient (no piano, no beat) at −15 LUFS and end on the logo alone. Preview: `preview/specimen.html`. The README has the rules and the recipe.

## Two surfaces, one system
| | Website (marketing) | Weight-loss app (member) |
|---|---|---|
| Canvas | Cream `#FFFCF7` | Cream `#FFFCF7` |
| Primary | Forest `#2C4E25` | Navy `#182E6C` |
| Display type | Castoro 40–96 px, tight `-0.04em` | Castoro italic 48–64 px (outside the device) |
| UI type | Public Sans 14–24 px | Hanken Grotesk (labels) + Inter (body) |
| CTA shape | 48 px pill | 6–8 px rounded rect |

Share: greens, cream, Castoro italic for display titles, hairline borders, sage-25 badges, shadow recipes, iconography (Iconify).

## Non-negotiable brand rules
- **Italic-noun emphasis:** serif-italic the key noun in display headlines — *"This is **Optimal**"*, *"Meet the **team**"*, *"Frequently asked **questions**"*.
- **Ring accents:** hand-drawn elliptical rings (`1.3px solid rgba(26,80,18,0.5)`, `border-radius:50%`, slight rotation) around select words. Used sparingly — one per section at most.
- **Pills for action, 8 px for content cards, 4 px for UI chrome.** Never mix.
- **Sentence case everywhere** except all-caps eyebrows (`WHAT MEMBERS ARE SAYING`) and footer section labels (`COMPANY`, `CONTACT`).
- **No emoji. Ever.** Use Iconify or nothing.
- **No gradients on buttons.** The only gradients allowed are the hero overlay (transparent → `#253821`) and the pricing card (`#2C4E25` → `#1C3118`).
- **Capsules, not scrims.** Glass chrome = blurred `rgba()` capsule with `backdrop-filter:blur()`, never a full-width gradient scrim.
- **Real photography, no custom illustration.** Warm, naturally-lit, softly desaturated. Circular portraits get a 5 px white ring.

## Voice in one paragraph
Warm, calm, clinical but human. Reassuring without being saccharine. Collective first-person for the clinic ("our clinicians"), second-person for the reader ("your NP"). Em-dashes, curly quotes. Product names are capitalised ("Annual Longevity Assessment", "Monthly Plan"); everything else is sentence case. Never marketing-y, never breezy.

## Copy the user can reuse verbatim
- Hero (live site, 2026): "A *new* kind of health clinic is here." (The 2024 Figma said "family health clinic".)
- Hero sub: "A private clinic built for personalized and preventative health. Fees are HSA eligible."
- CTA: "Become a member" / "Join now" / "Learn more"
- Banner: "Now accepting patients in Barrie →"
- Closing: "Start your journey to lifelong *wellness*."
- Testimonial byline format: `-  KATIE, 56`
- Copyright: `© Optimal <current year>`

## Iconify references (use by name)
App: `cuida:notification-bell-outline`, `mdi:water-outline`, `tabler:meat`, `icon-park-outline:dumbbell`, `iconoir:yoga`, `mdi:fire`, `fe:calendar`, `majesticons:chat-line`, `tabler:send`, `uil:paperclip`, `mingcute:search-line`, `lets-icons:check-fill`, `gg:profile`, `octicon:goal-16`.
Website: `tabler:chevron-up`, `tabler:chevron-down`, `tabler:arrow-right`, `lets-icons:check-fill`.

## Caveats before delivering
- Fonts load from Google Fonts (not bundled). If the user needs offline, add TTFs to `fonts/` and extend the `@font-face` rules.
- Hover/focus/press states aren't in the Figma. The defaults in this system are reasonable but not designer-signed.
- Dark mode isn't in the Figma. Use `forest-night.css` (v1.1), which is already in use on the clinic's screens.
- The Figma is the source of truth if any value here disagrees with a newer revision.
