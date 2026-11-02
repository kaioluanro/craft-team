# Visual Hierarchy & Layout (Refactoring UI)

Distilled from Adam Wathan & Steve Schoger, *Refactoring UI* — the "Starting from Scratch",
"Hierarchy is Everything", and "Layout and Spacing" sections. Read it when the question is
whether an interface *looks designed*: what leads the eye, how elements are sized and spaced,
and how structure is built.

**Contents**
1. Starting from scratch
2. Hierarchy is everything
3. Layout and spacing
4. Quick reference

---

## 1. Starting from scratch

The order in which you make decisions determines whether you get stuck.

- **Start with a feature, not a layout.** "Designing the app" first (top nav or sidebar? where
  does the logo go?) is the fastest route to frustration, because an app is a collection of
  features and you don't yet know what the shell must do. Instead design a real piece of
  functionality (e.g., "search for a flight" → departure field, destination field, date
  fields, a search button) and let the shell emerge from a few features.
- **Detail comes later.** Early on, don't get hung up on typefaces, shadows, icons. A trick
  for staying low-fidelity is to sketch with a thick Sharpie — details are impossible, so you
  explore many layout ideas fast.
- **Hold the color.** Design in grayscale first. Forced to use spacing, contrast, and size,
  you get a clearer interface with a stronger hierarchy that's easy to enhance with color
  later.
- **Don't over-invest.** Sketches and wireframes are disposable; users can't do anything with
  static mockups. Use them to decide, then leave them behind.
- **Don't design too much.** You don't need to solve every feature and edge case before
  implementing. Trying to imagine 2,000 contacts, error placement, overlapping events — in the
  abstract — is a setup for frustration.
- **Work in cycles.** Design a simple version of the next feature, make it *real*, iterate on
  the working design until the problems are gone, then return to design mode for the next
  feature. It's easier to fix design problems in something you can actually use.
- **Be a pessimist.** Don't imply functionality you aren't ready to build. The smallest useful
  version you can ship reduces risk; ship it first and treat "nice-to-haves" as later.

### Choose a personality

Every design has a personality (a bank might be *secure and professional*; a startup *fun and
playful*). It's not hand-wavy — it comes from a few concrete levers:

- **Font choice** — serif for elegant/classic; rounded sans for playful; neutral sans for
  plain (letting other elements carry personality).
- **Color** — blue is safe/familiar; gold can read expensive/sophisticated; pink more fun/less
  serious. Color psychology is less useful than noticing how a color *feels* to you.
- **Border radius** — small is neutral; large feels playful; none feels serious/formal. Stay
  consistent: mixing square and rounded corners almost always looks worse.
- **Language** — the words in the UI massively shape personality (formal/official vs.
  friendly/casual).

To decide, look at what the people you want to reach already use; borrow from those, but not
too heavily from direct competitors (don't look like a second-rate copy).

### Limit your choices

Unlimited options are paralyzing: 12px or 13px? 10% or 15% opacity? Define systems ahead of
time so you rarely face an unbounded decision.

- **Define systems in advance.** Choose color from a predefined set of 8–10 shades; pick type
  sizes from a fixed scale. You do the hard work once instead of every time.
- **Design by process of elimination.** With a constrained set, guess a value, try the values
  on either side, discard the bad ones, keep the best, and only re-compare if an outer option
  wins.
- **Systematize everything.** Build systems for font size, weight, line height, color, margin,
  padding, width, height, box shadows, border radius, border width, opacity — anything you
  labor over twice. Avoid making the same minor decision twice.

---

## 2. Hierarchy is everything

Visual hierarchy — how important elements appear relative to one another — is the single
biggest factor in making something "look designed", and it has nothing to do with innate
artistic talent. When everything competes for attention, the result is noise; de-emphasize the
secondary/tertiary and the same colors, fonts, and layout suddenly look better.

- **Not all elements are equal.** Deliberately rank primary, secondary, and tertiary content.
- **Size isn't everything.** Relying on font size alone makes primary content too large and
  secondary too small. Use **weight** and **color** too:
  - Stick to two or three text colors: a dark for primary, a grey for secondary, a lighter
    grey for tertiary.
  - Two font weights are usually enough (≈400/500 normal, ≈600/700 emphasis). Avoid weights
    under 400 for UI text; to de-emphasize, use a lighter color or smaller size instead of a
    lighter weight.
- **Don't use grey text on colored backgrounds.** Grey-on-white works because of *reduced
  contrast*, not because it's grey. On color, making text lighter grey — or white at reduced
  opacity — looks dull, washed out, sometimes disabled, and lets backgrounds bleed through.
  Instead hand-pick a new color on the same hue, adjusting saturation and lightness.
- **Emphasize by de-emphasizing.** When a key element still won't stand out, don't add more
  emphasis — reduce the competing elements instead (soften inactive nav items; drop a
  sidebar's background so it stops fighting the content).
- **Labels are a last resort.** Naive `label: value` pairs give every datum equal emphasis.
  - *You might not need a label* when the format or context is self-evident (an email,
    a phone number, a price, a department under a name).
  - *Combine labels and values* into one unit when you can ("12 left in stock",
    "3 bedrooms").
  - *Labels are secondary* when you do need them (dashboards): make them smaller, lower
    contrast, lighter weight.
  - *Emphasize the label instead* when users are scanning for the label (specs pages):
    just make the label darker and the value slightly lighter.
- **Separate visual hierarchy from document hierarchy.** Semantic tags (`h1`, `h2`) carry
  browser default sizes that tempt bad choices in app UIs. Section titles usually act like
  *labels*, not headlines — often they should be small, and sometimes present for
  accessibility but visually hidden. Pick elements for semantics; style them for hierarchy.
- **Balance weight and contrast.** Bold text feels emphasized because it covers more surface
  area. The same relationship applies elsewhere:
  - *Use contrast to compensate for weight*: a heavy icon next to text (which can't change
    weight) can be softened by lowering its color contrast.
  - *Use weight to compensate for contrast*: a 1px border that's too subtle at a soft color
    can be emphasized by making it slightly thicker instead of darker/harsher.
- **Semantics are secondary.** Buttons are semantic (primary/secondary/tertiary), but every
  page also has a *pyramid of importance*. Most pages have one true primary action, a couple
  of secondary actions, a few tertiary ones:
  - Primary: obvious — solid, high-contrast background.
  - Secondary: clear but not prominent — outline or lower-contrast background.
  - Tertiary: discoverable but unobtrusive — styled like a link.
  - **Destructive actions** aren't automatically big/red/bold. If a destructive action isn't
    the primary action, give it a secondary/tertiary treatment; make it big and red *only*
    where it truly is primary (e.g., in the confirmation step).

---

## 3. Layout and spacing

**Start with too much white space.** Adding space until something stops looking cramped gives
the minimum to avoid looking *bad*; to look *great* you usually need more. So start with way
too much space and remove it until it's right — what looks like "a little too much" in
isolation usually reads as "just enough" in context. Dense UIs have their place (dashboards
packing information onto one screen), but make density a deliberate decision, not the default.

**Establish a spacing and sizing system.**

- **A linear scale won't work.** Relative difference is what matters: 12→16px is +33% (huge at
  small sizes), while 500→520px is +4% (imperceptible at large sizes). Ensure no two values
  in the scale are closer than about 25%.
- **Define the system.** Start from a sensible base (16px divides evenly and is the browser
  default) and build with factors/multiples. Values at the small end should be packed
  together and get progressively further apart up the scale:
  `4, 8, 12, 16, 24, 32, 48, 64, 96, 128, …`
- **Using the system.** Grab a value from the scale, try it, and try the next when it's not
  enough. Designing in the browser (typing numbers) makes sticking to a system easier.

**You don't have to fill the whole screen.** Having 1200–1400px of canvas doesn't mean using
it. If 600px is enough, use 600px. Don't make one element worse just to match another's
width. To make a narrow layout feel balanced, split supporting content into a second column
rather than widening the main one. *Shrink the canvas*: design the ~400px mobile layout first,
then adapt upward and change less than you expect. Don't force things into small spaces either.

**Grids are overrated.**

- **Not all elements should be fluid.** A 12-column grid is just constrained percentage
  widths. A sidebar at 25% gets wastefully wide on large screens and too narrow on small
  ones — give it a *fixed* width optimized for its content and let the main area flex.
- **Don't shrink an element until you need to.** Fluid sizing can make a card *narrower on
  medium screens than on large ones*. Give fixed-optimal elements a `max-width`, and only
  force shrinking below that width.
- **Relative sizing doesn't scale.** A `2.5em` headline tuned for desktop is far too big once
  body text shrinks on mobile — the "relationship" wasn't real. Large elements should shrink
  *faster* than small ones; the small/large gap should be less extreme on small screens. The
  same applies *within* a component: a button's padding shouldn't scale proportionally with
  its font size if you want the large one to feel large and the small one to feel small.
- **Avoid ambiguous spacing.** When there's no border or background to group elements,
  spacing does the work: there must be **more space around a group than within it**. Equal
  label/input margins make form groups unclear; headings too close to preceding text mislead;
  horizontal components make the same mistake. Interfaces that are hard to parse always look
  worse.

---

## 4. Quick reference

- Start with a feature; sketch in grayscale; hold color for last.
- Constrain choices with systems: spacing/size, type, color shades, radius, shadows.
- Hierarchy comes from **weight and color**, not size alone.
- 2–3 text colors and 2 font weights carry most UIs.
- De-emphasize competitors instead of amplifying the hero.
- Labels: skip, combine, or subordinate — rarely lead with them.
- Icons are heavy; soften with lower contrast. Thin borders: emphasize with width, not
  darkness.
- Start with too much space, then remove it; keep the scale in ~25% steps.
- Fixed width for things that shouldn't scale; `max-width` before shrinking.
- Group with space: more around a group than within it.
