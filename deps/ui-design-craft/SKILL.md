---
name: ui-design-craft
description: Design and review user interfaces with human interface guidelines, usability heuristics, and visual design craft. Use this skill whenever the user wants to build, redesign, critique, audit, or improve any interface, screen, page, app, dashboard, form, settings panel, navigation, table, empty state, or design system, or asks about visual hierarchy, spacing, typography, color, shadows/depth, accessibility, contrast, usability testing, or platform conventions such as Apple's Human Interface Guidelines (HIG) - even when they never say "design", "usability", or "HIG" and only describe a screen in plain words.
---

# UI Design Craft

A field guide for doing two jobs well: **designing** an interface that a stranger can use
without thinking, and **reviewing** an interface that already exists and making it better.
It distills three sources that reinforce each other:

- **Apple Human Interface Guidelines (HIG)** — platform-agnostic conventions, controls, and
  interaction patterns that make an interface feel native and predictable.
- **Steve Krug, *Don't Make Me Think, Revisited*** — usability: how people actually scan,
  satisfice, and muddle through, and how to design for that reality.
- **Adam Wathan & Steve Schoger, *Refactoring UI*** — visual craft: hierarchy, layout,
  spacing, typography, color, depth, and finishing touches.

Use all three lenses together. Usability keeps the interface *understandable*; visual craft
makes it *readable and pleasant*; conventions make it *predictable*. A great screen is all
three at once.

## Two modes

Figure out which mode the user is in before doing anything else. When in doubt, ask one
short question rather than guessing, because the deliverables differ.

- **Design mode** — they want something new or changed (a new screen, a redesign, a
  component, a design system, "make this look better"). Output a design direction plus
  concrete decisions, ideally exploring more than one option.
- **Review mode** — they want an existing interface judged (a screenshot, a URL, code,
  or a description). Output a prioritized findings report with severity and specific fixes.
- Often both: review first to find problems, then design the fixes.

## The non-negotiables

These are the few rules that hold almost always; treat them as defaults that need a
deliberate, stated reason to break. Everything else is context-dependent, and the honest
answer to most design questions is "it depends — test it".

1. **Don't make me think.** Every page or screen should be self-evident; if it can't be,
   make it self-explanatory. The user should never spend effort decoding what something is
   or whether it's clickable.
2. **Clarity trumps consistency.** Consistency is a means, not a goal. If making one thing
   slightly inconsistent makes it clearly more understandable, do it.
3. **Omit needless words.** Get rid of half the words, then half of what's left. Kill happy
   talk ("Welcome to…") and instructions that exist only because the design isn't clear.
4. **Every click should be a mindless, unambiguous choice.** The number of clicks matters
   far less than how much thought and doubt each one costs. Strong "scent of information"
   beats fewer steps.
5. **Hierarchy is everything.** If everything is emphasized, nothing is. Make importance
   visible through size, weight, color, spacing, and position — and de-emphasize the
   competition rather than shouting louder.
6. **Start with too much white space, then remove it.** Space is the cheapest, most
   reliable way to make an interface look designed.
7. **Systematize.** Define scales up front (spacing/size, type, color shades, elevation,
   radius) and pick from them instead of hand-tuning values one pixel at a time.
8. **Never rely on color alone.** Pair color with text, icon, shape, or position so it
   survives color blindness, grayscale, and low-quality screens.
9. **Respect the reservoir of goodwill.** Hiding information, punishing input formats,
   asking for unneeded data, and fake sincerity drain it; candor, saved steps, and easy
   error recovery refill it.
10. **Design in grayscale first; add color last.** Spacing, contrast, and size should carry
    the hierarchy before color is allowed to.

## Design mode workflow

Work top-down; resist the pull to pick typefaces and shadows first — details come later.

1. **Frame the feature, not the shell.** Start from a real piece of functionality (e.g.
   "search for a flight"), not the nav bar or page chrome. You don't know how the shell
   should work until you've designed a few features.
2. **Choose a personality.** Decide, in concrete terms, whether the product is
   serious/classic, playful/friendly, or neutral/minimal. Personality is expressed through
   typeface choice, color, border radius, and the words you use — pick a direction and stay
   consistent (don't mix square and rounded corners).
3. **Sketch low-fidelity and in grayscale.** Explore several layouts quickly before
   committing. Cheap sketches are disposable; don't over-invest in them.
4. **Establish hierarchy before decoration.** Decide what is primary, secondary, tertiary
   on each screen. Prefer weight and color over size alone; keep to ~2–3 text colors and
   ~2 font weights.
5. **Lay out with a spacing system.** Start with too much space, then tighten. Give each
   element just the width it needs; don't fill the whole screen. Use fixed widths for
   things that shouldn't scale (sidebars, cards) and let content flex.
6. **Set type.** Pick a constrained type scale (hand-crafted, not a naive modular scale),
   keep body line length to 45–75 characters, and make line-height proportional to both
   length and size.
7. **Add color as a system.** Choose grey, primary, and semantic (accent/state) colors and
   define full shade ramps (roughly 100–900) up front. Work in HSL/HSB so lightness,
   saturation, and hue behave predictably.
8. **Add depth only where it earns its place.** Emulate a single light source from above;
   define a small elevation system (≈5 shadow levels) and reuse it.
9. **Finish.** Fix empty states, replace excessive borders, supercharge defaults, and
   handle images and user-uploaded content deliberately.
10. **Be a pessimist.** Don't design functionality you can't ship yet; build the smallest
    useful version, make it real, and iterate in cycles.

## Review mode workflow

1. **Collect the artifact.** Get the screenshot, URL, code, or a precise description; if
   only a description, restate your assumptions explicitly before judging.
2. **Run the trunk test.** Imagine being dropped onto the screen: can you instantly answer
   *What site/app is this? What page am I on? What are the main sections? What are my
   options here? Where am I in the hierarchy? How do I search?* Anything you can't answer
   at a squint is a finding.
3. **Scan as a user would.** Assume the user scans, satisfices, and muddles through. Look
   for question marks: unclear names, ambiguous clickability, competing emphasis, hidden
   information, and misleading affordances.
4. **Inspect visual craft.** Check hierarchy, spacing/alignment, size/type scale, color
   contrast and semantics, depth/elevation, and image handling.
5. **Check accessibility.** Contrast ratios, color-only meaning, labels, headings, keyboard
   reachability, alt text, and target sizes.
6. **Classify and prioritize.** For each finding, give a severity (see the rubric), the
   evidence, *why* it hurts the user, and a concrete fix. Surface the most serious problems
   first — you can always find more problems than can be fixed, so rank ruthlessly.
7. **Separate severity from sensation.** Aesthetics are subjective; don't inflate a taste
   preference into a critical bug. Reserve the top severity for things that block or
   confuse almost everyone.

## Routing to references

Read only what the task needs. Each file is self-contained and starts with its own summary.

| Question | Read |
| --- | --- |
| Can users understand and navigate it? Scanning, satisficing, navigation, home page, forms, mobile, goodwill, accessibility, usability testing | `references/usability-principles.md` |
| Does it look designed? Hierarchy, emphasis, layout, spacing, grids, sizing | `references/visual-hierarchy-and-layout.md` |
| Type, color, depth, shadows, images, empty states, finishing touches | `references/typography-color-and-depth.md` |
| Platform conventions, controls, patterns, navigation styles, feedback | `references/apple-hig.md` |
| Scoring a review, severity levels, a checklist to work through | `references/design-review-rubric.md` |

## Output formats

Match the mode. Keep prose tight; lead with the conclusion.

**Design mode** — use `assets/design-brief-template.md` when the user wants a document,
otherwise answer inline with: the chosen personality, the hierarchy plan, layout/spacing
decisions, type and color systems, and what you deliberately left out.

**Review mode** — use `assets/review-report-template.md`. Every finding has the same shape:

```
[Severity] Short title
Where:      screen / component / element
Evidence:   what you observed (or "inferred from description")
Impact:     which user and what they'd fail to do
Fix:        the specific change
```

## Tooling

- Run `scripts/contrast.py` to check WCAG contrast numerically instead of eyeballing it:

  ```bash
  python scripts/contrast.py "#111827" "#f9fafb"
  python scripts/contrast.py --list pairs.txt
  ```

  It reports the contrast ratio and whether it passes WCAG AA (4.5:1 normal text, 3:1
  large text) and AAA (7:1 / 4.5:1). Use it whenever text-on-color or color-on-color
  decisions are in play.

## Guardrails

- Don't invent specifics about a target you can't see. If you only have a description,
  say which claims are inferred.
- Don't recommend flat, low-contrast decoration that destroys affordances for the sake of
  looking modern; note the tradeoff explicitly when you do.
- Don't use small, low-contrast type, put labels inside form fields (except under strict
  conditions), float headings between paragraphs, or break visited/unvisited link
  distinction — these are among the rare near-absolute rules.
- Prefer removing noise to adding explanations. When users don't "get" something, the fix
  is usually to take something away, not to bolt on a tooltip.
- Usability testing beats opinion. When the user is debating taste, recommend watching
  three users for a morning — that half a day will find more problems than can be fixed
  in a month.
