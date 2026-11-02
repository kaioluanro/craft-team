# Typography, Color, Depth & Finishing (Refactoring UI)

Distilled from Adam Wathan & Steve Schoger, *Refactoring UI* — the "Designing Text",
"Working with Color", "Creating Depth", "Working with Images", and "Finishing Touches"
sections. Read it for the concrete craft of type, color, elevation, imagery, and the details
that separate "fine" from "designed".

**Contents**
1. Designing text
2. Working with color
3. Creating depth
4. Working with images
5. Finishing touches
6. Quick reference

---

## 1. Designing text

**Establish a type scale.** Most interfaces use too many font sizes (every pixel from 10–24).
A scale fixes that and speeds decisions.

- *Modular scales* (ratio-based, e.g. 4:5, 2:3, golden 1:1.618) look pure but produce
  fractional values (avoid subpixel issues) and too few sizes for UI work.
- *Hand-crafted scales* are better for interfaces: you control which sizes exist and avoid
  rounding errors. A practical hand-crafted scale aligned with a 16px spacing base:
  `12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72`.
- **Avoid em units.** Because em is relative to the current font size, nested em values
  compute to sizes *not* in your scale. Use `px` or `rem`.

**Use good fonts.** You probably don't have years to develop an eye, so:

- *Play it safe* — a neutral sans-serif is the safest UI choice; the system font stack works
  and users already know it:
  `-apple-system, Segoe UI, Roboto, Noto Sans, Ubuntu, Cantarell, Helvetica Neue, sans-serif`.
- *Ignore typefaces with fewer than five weights* (a rough proxy for care and craft; on
  Google Fonts, filtering to 10+ styles cuts ~85%).
- *Optimize for legibility* — fonts built for small text have wider letter-spacing and taller
  x-heights; avoid condensed, short-x-height fonts for main UI text.
- *Trust the crowd* — popular fonts are usually good and directories let you sort by
  popularity.
- *Steal from people who care* — inspect sites you admire; strong design teams make great
  picks you'd never find otherwise.

**Keep line length in check.** For the best reading experience, aim for **45–75 characters
per line** (≈20–35em). When mixing prose with images or wide components, keep paragraph width
limited even if the overall content area is wider.

**Baseline, not center.** When mixing font sizes on one line, align by **baseline** (the line
letters rest on) instead of vertical centering — the eye already perceives it and the result
looks cleaner.

**Line-height is proportional.**

- *To line length*: longer lines need taller line-height (narrow text can use ~1.5; wide
  content may need up to 2) because the eye travels further back to the line start.
- *To font size (inversely)*: small text needs more extra spacing; large headlines can use
  ~1.0.

**Not every link needs a color.** When almost everything is a link, a "pop" treatment is
overbearing. Emphasize most links subtly (heavier weight or darker color); for ancillary
links, reveal color/underline only on hover.

**Align with readability in mind.**

- Left-align for left-to-right languages. Center only headlines or short independent blocks —
  never center long-form text (over ~2–3 lines). If one centered block is too long, shorten
  the copy.
- **Right-align numbers** in tables so decimals line up and values compare at a glance.
- **Hyphenate justified text** — otherwise you get awkward gaps. Justified text suits a
  print-like look; left-aligned is a safe default otherwise.

**Use letter-spacing effectively** (mostly trust the typeface designer):

- *Tighten headlines* — if using a wide-spaced UI family for headlines, reduce letter-spacing
  to mimic a purpose-built display font. Don't do the reverse (headline fonts rarely work
  small even with increased spacing).
- *All-caps legibility* — caps are uniform in height, so default spacing reads poorly; increase
  letter-spacing for all-caps text.

---

## 2. Working with color

**Ditch hex for HSL/HSB.** Hex/RGB hide the relationships between colors. HSL exposes the
attributes the eye perceives: **hue** (position on the wheel, 0° red, 120° green, 240° blue),
**saturation** (0% grey → 100% vivid), **lightness** (0% black → 100% white, 50% pure color).
Note HSL ≠ HSB: HSB 100% brightness equals HSL 100% saturation / 50% lightness. Design tools
often use HSB; browsers use HSL.

**You need more colors than you think.** A "5 perfect colors" palette can't build a real UI.
A good palette has three categories:

- **Greys** — almost everything is grey (text, backgrounds, panels, controls). You need ~8–10
  shades, from a very dark grey (true black looks unnatural) up to white.
- **Primary color(s)** — one, maybe two colors for primary actions and active nav; needs 5–10
  shades. Ultra-light shades make tinted backgrounds; dark shades make text.
- **Accent / semantic colors** — a few colors for emphasis and states (red = destructive,
  yellow = warning, green = positive), each with several shades. Categorizing UIs (graph
  lines, calendar events, tags) may need ~10 colors × 5–10 shades.

**Define your shades up front.** Don't generate shades on the fly with `lighten`/`darken`
(you'll get 35 near-identical blues). Build a fixed ramp:

- *Choose the base first* — the mid shade that would work as a button background.
- *Find the edges* — the darkest shade (usually text) and lightest (usually a tinted
  background). An alert component exercises both, so it's a good place to pick them.
- *Fill the gaps* — nine shades divides cleanly: name them `100…900`, base `500`, then pick
  `700`/`300` as perfect compromises, then `800/600/400/200`.
- *Greys*: the base matters less; pick the darkest from the darkest text and lightest from a
  subtle off-white background, then fill in.
- It's not a science — tweak by eye, but avoid adding new shades often (a bloated palette is
  as good as no system).

**Don't let lightness kill your saturation.** In HSL, saturation's effect weakens as lightness
moves away from 50%: increase saturation as shades get lighter or darker so they don't look
washed out.

**Use perceived brightness to your advantage.** Equal HSL lightness looks different across
hues (yellow reads lighter than blue) because of *perceived brightness* (§ calculation from
RGB weights) — three local minimums (red, green, blue) and three maximums (yellow, cyan,
magenta).

- You can change a color's brightness by **rotating its hue** toward a bright hue
  (60°, 180°, 300°) or a dark hue (0°, 120°, 240°) instead of only changing lightness — this
  keeps saturation rich (e.g., a yellow ramp that rotates toward orange as it darkens reads
  warm and rich instead of dull brown). Combine hue rotation and lightness, but keep rotation
  under ~20–30° or it becomes a different color.

**Greys don't have to be grey.** True grey has 0% saturation; many "greys" are saturated and
that saturation gives them temperature. Saturate greys slightly with blue for cool, yellow/
orange for warm — and increase saturation for the lighter/darker shades to keep temperature
consistent.

**Accessible doesn't have to mean ugly.** WCAG recommends ≥ **4.5:1** contrast for normal
text (<~18px) and ≥ **3:1** for large text. Getting there with color is tricky:

- *Flip the contrast* — instead of white text on a dark color (which often must be so dark it
  dominates the page), use dark colored text on a light colored background.
- *Rotate the hue* — for colored text on colored backgrounds, rotate toward a brighter hue
  (cyan/magenta/yellow) to raise contrast without approaching white.

**Don't rely on color alone.** Color-blind users can't read meaning carried only by hue. Pair
color with an icon, label, or shape (e.g., up/down arrows on metrics). In charts, prefer
contrast (light vs dark) over many distinct hues. Always let color *support* meaning, never be
the only signal.

---

## 3. Creating depth

**Emulate a light source.** Interfaces feel raised or inset because they mimic how light hits
real objects — and **light comes from above**. Raised surfaces are lighter on top (facing the
sky) and darker below; inset surfaces are the opposite (a shadow at the top, lighter bottom
lip). Since people look slightly *down* at screens, reveal a little of the top edge and hide
the bottom.

- *Raised elements*: a slightly lighter top edge (top border or inset shadow with a small
  positive vertical offset — pick the lighter color by hand, not semi-transparent white, which
  drains saturation) plus a small dark shadow below (small blur, sharp edges, slight vertical
  offset).
- *Inset elements* (wells, inputs, checkboxes): a lighter bottom border/inset shadow plus a
  small dark inset shadow at the top.
- *Don't get carried away* — borrow cues, don't chase photorealism; busy, unclear interfaces
  are the result.

**Use shadows to convey elevation.** Shadows place elements on a virtual z-axis: tighter blur
= slightly raised; larger blur = closer to the user = more focus. Buttons get small shadows,
dropdowns medium, modals large. Shadows are also interaction cues — a dragged list item pops
forward; a pressed button loses its shadow.

**Establish an elevation system.** Define a fixed set of ~5 shadow levels (smallest and
largest first, then fill linearly) and reuse them. Think in terms of *where on the z-axis the
element should sit*, then assign the shadow.

**Shadows can have two parts.** A larger, softer shadow (considerable vertical offset, large
blur) simulates the direct-light shadow, and a tighter, darker shadow (small offset/blur)
simulates the dark area right under the object. Together they're subtle yet well-defined. As
elevation increases, the tight dark shadow fades (ambient light reaches under higher objects)
— distinct at low elevation, nearly invisible at high elevation.

**Even flat designs can have depth.**

- *With color*: lighter objects read closer, darker read farther. Make an element lighter than
  its background to raise it, darker to inset it.
- *With solid shadows*: short, vertically offset shadows with no blur keep a flat aesthetic
  while lifting a card or button.
- *Overlap to create layers*: offset a card across two backgrounds, or let an element overlap
  its parent on both sides. For overlapping images, give them an invisible border matching the
  background so layers read without clashing.

---

## 4. Working with images

**Use good photos.** Bad photos ruin a good design. Either hire a professional or use quality
stock photography. Never design with placeholders expecting to swap in phone photos later —
it never works.

**Text needs consistent contrast.** The problem with headline-on-image is usually the *image*:
its dynamic range means no single text color works everywhere.

- *Add an overlay* — a semi-transparent black overlay tames light areas for light text; white
  for the reverse.
- *Lower the image contrast* (then adjust brightness to compensate) for finer control.
- *Colorize the image* — lower contrast, desaturate, then a solid fill in "multiply" blend
  mode — also helps brand pairing.
- *Add a text shadow* — a soft, offset-less glow (large blur) raises contrast only where
  needed, letting you keep more image dynamics.

**Everything has an intended size.**

- *Don't scale up icons* — icons drawn at 16–24px look chunky at 3–4×. Enclose a small icon in
  a shape with a background so it stays near its intended size while filling a larger space.
- *Don't scale down screenshots* — shrinking a full screenshot crams illegible detail.
  Screenshot at a smaller layout, take a partial screenshot, or draw a simplified diagram.
- *Don't scale down icons either* — a 128px logo shrunk to a favicon turns to mush; redraw a
  simplified version at the target size.

**Beware user-uploaded content.**

- *Control shape and size* — center user images in fixed containers with `object-fit: cover` /
  `background-size: cover` so aspect ratios don't wreck the layout.
- *Prevent background bleed* — when an uploaded image's background matches your UI, use a
  subtle inner box shadow (or semi-transparent inner border) instead of a border, which clashes
  with image colors.

---

## 5. Finishing touches

- **Supercharge the defaults.** Liven what's already there: replace bullets with icons
  (checks, arrows, or something specific like a padlock), promote quotes into visual elements
  (bigger, colored), style links (color/weight or a custom underline), and use brand-colored
  custom checkboxes/radios.
- **Add color with accent borders.** A colored rectangle across the top of a card, beside an
  active nav item, along an alert, under a headline, or across a layout — no graphic-design
  talent required, big perceived-polish payoff.
- **Decorate your backgrounds.** Change a background color or use a subtle gradient (two hues
  ≤ ~30° apart); add a low-contrast repeating pattern (full or single-edge); or place a simple
  shape/illustration. Keep contrast low so content stays readable.
- **Don't overlook empty states.** If a feature depends on user content, the empty state is a
  priority, not an afterthought — it's the first interaction. Use an image/illustration and a
  prominent call to action, and hide supporting UI (tabs, filters) that does nothing yet.
- **Use fewer borders.** Before reaching for a border: use a box shadow (subtler, outlines
  without distraction — works best when the element differs from its background), use two
  different background colors (often enough on its own; drop the border), or add extra spacing
  (separation without new UI).
- **Think outside the box.** Dropdowns, tables, radios don't have to look the way they always
  have. Break a dropdown into sections/columns with supporting text or icons; combine related
  table columns and add images/color when a column needn't be sortable; turn important radios
  into selectable cards. Constraints are powerful, but some freedom takes an interface up a
  level.

---

## 6. Quick reference

- Hand-crafted type scale; `px`/`rem`, never `em`; 45–75 char lines.
- Line-height rises with line length, falls with font size; align mixed sizes on baseline.
- HSL for reasoning; 9-step shade ramps per color; saturate as lightness departs 50%.
- Perceived brightness differs by hue; rotate hue (≤20–30°) to change brightness richly.
- WCAG 4.5:1 (normal) / 3:1 (large); flip contrast, rotate hue; never color alone.
- Light from above; raised = lighter top + soft shadow below; ~5 elevation levels.
- Two-part shadows; tighter/shorter for pressed; fade the tight shadow as elevation rises.
- Icons and screenshots have an intended size — never scale them blindly.
- Overlay/contrast/colorize/text-shadow fixes headline-on-image.
- Empty states, fewer borders, accent borders, and background decoration are cheap polish.
