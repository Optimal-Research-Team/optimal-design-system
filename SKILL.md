# Optimal Health Design System — SKILL.md

Agent entrypoint for the **Optimal Health** brand. Optimal is a members-only, Nurse Practitioner-led family health clinic in Barrie, Ontario, plus a companion **weight-loss app** used by members.

## When to use
- Any artifact (web page, email, deck, brochure, app screen, prototype) that represents Optimal externally.
- Any work that touches the marketing site or the weight-loss app.
- When you need brand colours, typography, voice, or reusable components.

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
- Hero: "A new kind of family health clinic is here."
- Hero sub: "A private clinic built for personalized and preventative health. Fees are HSA eligible."
- CTA: "Become a member" / "Join now" / "Learn more"
- Banner: "Now accepting patients in Barrie →"
- Closing: "Start your journey to lifelong *wellness*."
- Testimonial byline format: `-  KATIE, 56`
- Copyright: `© Optimal 2024`

## Iconify references (use by name)
App: `cuida:notification-bell-outline`, `mdi:water-outline`, `tabler:meat`, `icon-park-outline:dumbbell`, `iconoir:yoga`, `mdi:fire`, `fe:calendar`, `majesticons:chat-line`, `tabler:send`, `uil:paperclip`, `mingcute:search-line`, `lets-icons:check-fill`, `gg:profile`, `octicon:goal-16`.
Website: `tabler:chevron-up`, `tabler:chevron-down`, `tabler:arrow-right`, `lets-icons:check-fill`.

## Caveats before delivering
- Fonts load from Google Fonts (not bundled). If the user needs offline, add TTFs to `fonts/` and extend the `@font-face` rules.
- Hover/focus/press states aren't in the Figma. The defaults in this system are reasonable but not designer-signed.
- No dark mode exists.
- The Figma is the source of truth if any value here disagrees with a newer revision.
