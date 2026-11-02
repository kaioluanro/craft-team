# Design Review Rubric

A scoring and checklist reference that unifies the usability, visual-craft, and HIG lenses.
Read it in **review mode** to classify findings consistently and to make sure you didn't skip
a whole category. It also works as a pre-flight check before shipping a design.

**Contents**
1. Severity levels
2. How to write a finding
3. The checklist (by lens)
4. Reporting and prioritization

---

## 1. Severity levels

Severity measures **impact on users**, not how much the change costs or how it makes you feel.
Assign the *lowest* level that fits; only escalate when the evidence supports it. Aesthetics
are subjective — never label a taste preference "critical".

| Level | Name | Definition | Typical examples |
| --- | --- | --- | --- |
| **S1** | **Blocker** | Prevents or badly corrupts the core task for most users. They cannot proceed, or will do the wrong thing. | Primary action not discoverable; form submits garbage; destructive action with no confirmation or undo; content unreadable (contrast/overflow); critical info hidden; broken navigation. |
| **S2** | **Serious** | Most users complete the task, but with real friction, doubt, or frequent error. | Ambiguous link/button labels; competing emphasis hiding the main thing; confusing error with no recovery; missing empty/loading/error state; labels inside fields; relies on color alone; low-contrast body text. |
| **S3** | **Moderate** | Noticeable, slows some users or devalues the interface, but people cope. | Inconsistent spacing/alignment; too many font sizes; weak hierarchy; noisy decoration; size-scaled icons/screenshots; unclear affordance on touch. |
| **S4** | **Minor / polish** | Small inconsistency or missed opportunity; low user impact. | Slightly-off shadow/elevation; missed accent border; border where a shadow would do; minor copy tightening. |
| **Q** | **Question / taste** | Depends on context or preference; needs a decision or a test, not a verdict. | Color preference; centered vs left headline within bounds; which metaphor for a feature. |

**Escalation rules**

- If it confuses *everyone*, it's at least S2 — and if it blocks the task, S1.
- Accessibility failures that make content unusable (contrast, missing labels/alt, keyboard
  traps) are S1–S2 even if they affect a minority — you can't call a product usable if part of
  the audience can't use it.
- If you can only *infer* the problem from a description rather than observing it, cap at S2
  and say so.
- "It depends" is a legitimate outcome; mark it Q and recommend a three-user test.

---

## 2. How to write a finding

Every finding has the same five parts. Keep them terse and concrete.

```
[S#] Short, specific title
Where:     screen / component / element
Evidence:  what you observed (or "inferred from description")
Impact:    which user, and what they fail to do or feel
Fix:       the specific change to make
```

Rules of thumb:

- **Title is the finding**, not the topic ("Primary button competes with four promos", not
  "Hierarchy").
- **Evidence is observable.** "The 'Continue' button uses the same blue as the four
  non-clickable headings" beats "button looks bad".
- **Impact names a user and a task.** "A first-time visitor can't tell which link starts the
  checkout".
- **Fix is actionable and scoped.** Prefer removing noise to adding explanation.
- **One finding per problem.** Don't bundle unrelated issues into one row.

---

## 3. The checklist (by lens)

Work top to bottom; stop and write a finding wherever the answer is "no".

### A. Usability (Krug) — *can a stranger use it?*

- [ ] **Self-evident** — can a newcomer say what this is and how to use it without thinking?
      If not, is it at least self-explanatory?
- [ ] **No question marks** — no cute/ambiguous names, no unclear clickability, no "is that an
      ad?" confusion.
- [ ] **Scannable** — clear visual hierarchy; defined regions; headings that outline the page
      and sit closer to what they introduce; short paragraphs; bullets for lists; sparse bold
      emphasis.
- [ ] **Mindless choices** — every click/link clearly scents its target; hard choices get
      brief, timely, unavoidable guidance.
- [ ] **Words trimmed** — no happy talk, no needless instructions; half the words could go.
- [ ] **Navigation** — meets the trunk test: site ID, page name, sections, local nav,
      "you are here", and search all pop at a squint; page name matches the link clicked;
      persistent nav present (or a sensible minimal version in forms).
- [ ] **Home / entry** — what the site is is clear at a glance (tagline/blurb), and entry
      points (search, browse, sign in, start) look like entry points.
- [ ] **Goodwill** — nothing hidden that users want (prices, contacts, shipping); no
      format-punishing inputs; no unnecessary data requests; no fake sincerity; no sizzle in
      the way.
- [ ] **Recovery** — errors explain how to recover; consequential actions are reversible or
      confirmed.

### B. Visual craft (Refactoring UI) — *does it look designed?*

- [ ] **Hierarchy** — primary/secondary/tertiary are visibly ranked; importance is carried by
      weight and color, not size alone; competitors are de-emphasized rather than the hero
      shouted louder.
- [ ] **Text color** — no grey text on colored backgrounds; 2–3 text colors and 2 weights max.
- [ ] **Labels** — not naive `label: value` rows; labels skipped, combined, or subordinated.
- [ ] **Actions** — clear pyramid (one primary, a few secondary, rest tertiary); destructive
      actions styled for their true importance.
- [ ] **Spacing** — generous and systematic (~25% steps); grouped items closer within than
      around; nothing cramped to fit a container.
- [ ] **Layout** — not filling the whole screen just because; fixed widths for non-scaling
      elements; `max-width` before shrinking; no fluid element that gets smaller as the screen
      grows.
- [ ] **Type** — constrained scale (px/rem, not em); line length 45–75 chars; line-height
      proportional to length and size; baseline alignment for mixed sizes; left-aligned long
      text; right-aligned numbers; hyphenated justification.
- [ ] **Color system** — grey + primary + semantic colors with full shade ramps; saturation
      maintained across shades; greys possibly temperature-tinted.
- [ ] **Depth** — light from above; consistent ~5-level elevation system; shadows pair a soft
      and a tight part; pressed/raised states use elevation meaningfully.
- [ ] **Images** — good photos; consistent text contrast on images (overlay/colorize/shadow);
      nothing scaled beyond its intended size; user content constrained and bleed-proofed.
- [ ] **Finishing** — empty states designed; fewer borders (shadow/spacing/background
      instead); defaults supercharged; backgrounds decorated tastefully.

### C. HIG / conventions — *is it predictable and accessible?*

- [ ] **Layout/safe areas** respected; layout adapts (reflows, not just shrinks).
- [ ] **Controls** match conventions; labels are verbs describing results; one clear primary
      action.
- [ ] **Navigation** shows position, offers an obvious way back, and keeps 3–5 top-level
      destinations.
- [ ] **Feedback** for every action; honest progress for non-trivial waits; modality
      justified, dismissible, rare.
- [ ] **Alerts** only for important, actionable, recoverable situations.
- [ ] **Accessibility** — contrast sufficient in light and dark; meaning never by color alone;
      every essential function reachable by keyboard with a visible focus; targets large
      enough; alt text/labels/hints present; motion reducible.
- [ ] **Copy** plain, consistent, actionable; errors say how to recover; privacy-respectful.

---

## 4. Reporting and prioritization

1. **Lead with the verdict.** One or two sentences: is this usable, and what's the biggest
   problem? Don't make the reader mine the list.
2. **Sort by severity, then by impact.** S1s first. Two S1s matter far more than ten S4s.
3. **Cap the list.** Surface the most serious problems. You can always find more problems than
   can be fixed; ruthlessly fixing the serious ones beats sprinkling minor ones.
4. **Recommend testing when it's a judgment call.** For Q findings and debates about taste,
   propose watching three users do the real task for a morning — that finds more problems than
   a month can fix.
5. **Include quick wins.** Keep a short separate list of items fixable by one person in under
   an hour with no approvals; they build momentum.
6. **State limitations.** Note anything you couldn't observe, anything inferred from a
   description, and any category you couldn't evaluate — never imply coverage you don't have.
