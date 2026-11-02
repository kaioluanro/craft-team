# Human Interface Guidelines (HIG)

A platform-agnostic digest of Apple's Human Interface Guidelines. HIG is Apple's opinionated
rulebook for iOS, iPadOS, macOS, watchOS, tvOS, and visionOS; here it is generalized into
conventions and patterns that make *any* interface predictable. Read it when the question is
"what should this control/flow feel like", or when reviewing for platform-convention
violations. When a rule is Apple-specific, it's flagged; the underlying idea usually
generalizes.

**Contents**
1. Design principles
2. Foundations
3. Components
4. Patterns
5. Inputs
6. Accessibility
7. Review checklist

---

## 1. Design principles

Apple frames three foundational themes, which generalize well:

- **Clarity.** Text is legible at every size, icons are precise and lucid, adornments are
  subtle and appropriate, and a sharpened focus on functionality motivates the design.
  Negative space, color, typography, and graphics communicate subtly and appropriately.
- **Deference.** The UI helps people understand and interact with content but never competes
  with it. Content typically fills the screen; translucency and blur hint at more without
  distracting; minimal bezels. The interface *yields* to the content.
- **Depth.** Distinct visual layers and realistic motion convey hierarchy, vitality, and
  understanding. Depth (and, on some platforms, touch/sound) helps people understand
  relationships and discover functionality without losing context.

Cross-cutting goals: the interface is **purposeful** (each element earns its place),
**focused**, **familiar** (reusing conventions and controls people know), and **flexible**
(adapting to different contexts, devices, and preferences).

---

## 2. Foundations

- **Layout.** Use a consistent, constrained layout with clear margins and alignment. Respect
  safe areas (notches, home indicators, rounded corners, toolbars). Use consistent spacing and
  sizing (grid/scale), and make layouts adapt — reflow rather than merely shrink. Avoid putting
  critical content or controls where they can be occluded.
- **Color.** Use color to convey meaning and communicate interactivity, but don't rely on it
  alone. Support both light and dark appearances. Ensure sufficient contrast (text, controls,
  glyphs) and never hard-code colors that break in the other appearance. Use semantic/dynamic
  colors rather than raw values so the system can adapt.
- **Dark Mode.** Design for both appearances as first-class; don't just invert. Use semantic
  colors, verify contrast in both, and keep imagery legible.
- **Typography.** Use the system font (or a well-considered custom family), use dynamic type so
  text scales with user settings, and preserve a clear hierarchy of styles. Don't mix too many
  styles; maintain consistent weight/size relationships.
- **Icons (SF Symbols / glyphs).** Prefer the platform's symbol set so icons match system
  conventions and scale with text. Use recognizable metaphors, don't overload an icon with
  meaning, and always pair ambiguous icons with labels. Never scale an icon far from its
  intended optical size.
- **Images.** Use high-resolution imagery, maintain aspect ratios, provide meaningfully cropped
  variants, and supply accessible descriptions. For content on images, ensure consistent
  contrast (overlay, gradient, material).
- **Materials & translucency.** Backgrounds can be blurred/translucent to establish hierarchy
  and hint at depth — use them to separate foreground chrome from scrolling content without a
  hard divider.
- **Motion.** Use motion to clarify relationships and give feedback, not to decorate. Keep it
  purposeful, brief, and consistent; respect reduced-motion settings; avoid gratuitous
  animation that competes with content.
- **Branding.** Branding should be subtle and integrated (accent color, type, imagery), not
  everywhere. The system chrome belongs to the platform; the content and brand live inside it.
- **Privacy.** Request the minimum data needed, request it only when needed, explain why, and
  let people decline without punishment. Provide clear indicators when data (camera, location,
  mic) is in use.
- **Writing.** Use plain, consistent, actionable language. Prefer sentence case, avoid jargon,
  keep labels short, and write errors that explain how to recover.

---

## 3. Components

HIG organizes controls by role; the generalized patterns:

**Bars (navigation chrome)**
- **Navigation bar** — shows position in a hierarchy, provides a way back, and holds the
  screen title and a few key actions. Keep titles short; don't overload with actions.
- **Tab bar** — top-level navigation between peer sections. Use 3–5 destinations, icon + short
  label, and preserve state per tab. Don't use tabs for actions or for a single destination.
- **Toolbar** — actions relevant to the current context; keep the most important, common
  actions accessible; use overflow for the rest.
- **Status bar** — system information; don't obscure it or rely on it for app content.

**Content views**
- **Lists / tables** — the workhorse for collections. One item per row, clear row hierarchy
  (primary/secondary text, leading/trailing accessories), and support selection, grouping, and
  editing where meaningful.
- **Collections / grids** — for browseable content where imagery matters; adapt the number of
  columns to the space.
- **Scroll views** — content can exceed the viewport; make it obvious there's more (partial
  peek, scroll indicators), and don't nest conflicting scroll axes carelessly.
- **Page controls / carousels** — for a small, bounded set of peer panels; show position; avoid
  auto-advancing content that can't be paused.

**Controls (selection & input)**
- **Buttons** — the primary affordance for actions. Style by importance (filled = primary,
  tinted/outline = secondary, plain/link = tertiary). One clear primary per screen. Use verb
  labels describing the result ("Save", "Delete"), not "OK/Cancel" unless truly generic.
- **Toggle/switch** — binary on/off that takes effect immediately; label the *thing*, not the
  action ("Wi-Fi", not "Enable Wi-Fi").
- **Checkbox / radio** — multi-select vs. single-select among visible options. Radios for few
  mutually exclusive choices; a menu/picker when options are many (avoid a context menu for
  something users change often).
- **Segmented control** — 2–5 mutually exclusive options in a row; keeps options visible.
- **Slider / stepper** — continuous vs. discrete numeric input; show the current value.
- **Picker / combo / menu button** — choose from a list; prefer a menu for many options and a
  segmented control or radio group for few.
- **Text field / search field** — single-line input with a persistent, associated label;
  use appropriate keyboard/autocorrect settings; keep labels outside the field.
- **Color well** — color selection; provide accessible alternatives (hex/label), never color
  alone.

**Presentation**
- **Alerts** — interrupt for important, actionable situations only. Title states the problem,
  the body explains, and buttons are verbs ordered by importance; a destructive action is
  clearly marked and typically requires confirmation. Never use an alert for routine success.
- **Action sheet / menu of options** — a set of choices in response to an action; include a
  clear cancel path.
- **Popover** — transient, anchored content; dismissible; appropriate on larger screens where
  the anchor is visible.
- **Modal / sheet** — when a task must be completed or is self-contained. Use sparingly;
  provide a clear way to dismiss, prefer non-modal when possible, and reserve full-screen
  modality for immersive or destructive flows.
- **Context menu** — shortcuts to frequent actions for an item; never the only way to do
  something.

**Status**
- **Activity indicator / progress** — indeterminate vs. determinate. For anything but very
  short waits, show determinate progress; keep feedback honest and near the action.
- **Gauges / ratings** — communicate bounded status; ensure they're understandable without
  color.

---

## 4. Patterns

- **Onboarding** — teach in context and get people to value quickly; don't front-load tours.
  Make it skippable, and don't make help the only way to learn the app.
- **Loading** — show progress, keep it honest (determinate when possible), avoid blocking the
  whole UI, and prefer skeleton/placeholder over blank screens for content.
- **Modality** — use only when a task genuinely requires it; always offer an escape hatch;
  minimize how often users are interrupted.
- **Feedback** — every action gets perceptible feedback appropriate to its importance. Keep it
  close to the source, timely, and unobtrusive; reserve interruption for the important.
- **Data entry** — ask only for what's needed, give sensible defaults, validate inline,
  present options instead of free text where possible, and make recovery easy.
- **Search** — make it easy to find and use; show recent/suggested queries; handle no-results
  gracefully with a path forward; let scope be refined after results.
- **Settings / preferences** — put the few things people change often in a clear settings
  area; don't hide essential settings in deep menus; prefer sensible defaults over options.
- **Notifications** — timely, relevant, actionable; respect permission and let people control
  them; never use them for ads.
- **Undo / redo** — support reversibility for consequential actions; confirm only when undo
  isn't available.
- **Drag and drop / sharing** — follow platform conventions; make targets obvious; provide
  non-drag alternatives for accessibility.
- **File management** — use the platform's document model (autosave, versions, open/recent)
  rather than reinventing it.

---

## 5. Inputs

- **Gestures** — use standard gestures for standard meanings (tap, swipe, pinch, long-press);
  never require undiscoverable custom gestures as the only path; provide alternatives.
- **Keyboard** — every essential function has a keyboard path; support focus, standard
  shortcuts, and full navigation without a pointer.
- **Pointing devices** — don't require precision; provide hover feedback where a pointer
  exists, but never make hover the *only* way to discover something (touch has none).
- **Focus & navigation** — a clear, visible focus state; logical focus order; don't trap focus.
- **Voice / speech** — offer as an input alternative, not a replacement.
- **Haptics / sound** — supplementary feedback only; never the sole signal, and respect
  user settings.

---

## 6. Accessibility

HIG treats accessibility as a foundation, not a feature. Generalize these:

- **Perceivable** — sufficient contrast, scalable text (dynamic type), don't convey meaning by
  color alone, provide text alternatives for images, icons, and audio.
- **Operable** — full keyboard/switch access, large-enough hit targets (Apple suggests ~44×44pt
  on touch), generous spacing between targets, no timing traps, motion controllable.
- **Understandable** — consistent, predictable behavior; clear labels and instructions; errors
  that explain recovery.
- **Robust** — use platform controls and semantics so assistive technology understands the UI;
  provide accessibility labels, values, and hints; don't fight the system.

Prefer building accessibility in from the start: it improves the experience for everyone, and
retrofitting is far harder.

---

## 7. Review checklist

Run this against any screen, then report violations with the standard finding shape (severity,
where, evidence, impact, fix):

- Safe areas, margins, alignment, and adaptive layout respected?
- Text legible at all sizes; dynamic type honored; hierarchy of type styles clear?
- Color: meaning not carried by color alone; contrast sufficient in light *and* dark?
- Controls match platform conventions and use correct labels/verbs?
- One clear primary action; destructive actions marked and confirmed?
- Navigation: clear position, an obvious way back, 3–5 top-level destinations?
- Feedback for every action; progress shown honestly for non-trivial waits?
- Modality justified, dismissible, and rare?
- Input: keyboard-reachable, visible focus, no hover-only discovery, adequate target sizes?
- Imagery: correct aspect ratios, consistent text contrast, accessible descriptions?
- Motion purposeful, brief, reduced-motion respected?
- Privacy: minimum data, asked in context, declinable?
