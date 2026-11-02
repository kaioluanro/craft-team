# Usability Principles (Krug)

Distilled from Steve Krug, *Don't Make Me Think, Revisited* (3rd ed.). This is the
"can a stranger use this without thinking?" lens. Read it when the question is whether an
interface is understandable and navigable, not whether it is beautiful.

**Contents**
1. The three laws
2. How people actually use the web
3. Billboard design: design for scanning
4. Mindless choices (clicks)
5. Omit needless words
6. Navigation
7. The home page
8. Usability testing on the cheap
9. Mobile
10. The reservoir of goodwill
11. Accessibility
12. Quick reference: definitive answers

---

## 1. The three laws

**First law: Don't make me think.** The overriding principle and the tie-breaker for every
design dispute. As far as humanly possible, a page or screen should be *self-evident* — the
user "gets it" (what it is, how to use it) without any effort. When something is inherently
complex or original, settle for *self-explanatory*: a little thought, but only a little, and
never doubt about whether you're on the right track.

Things that make people think (and therefore must be fixed):
- Cute, clever, marketing, company-specific, or unfamiliar technical names.
- Links and buttons that aren't obviously clickable.
- Anything forcing the user to ask: Where am I? Where should I begin? Where did they put
  X? What's most important here? Why did they call it that? Is that an ad or content?

Every question mark adds cognitive load and erodes confidence in the site and its makers.
Material for the fix: make choices obvious and links strongly scented.

**Second law: It doesn't matter how many clicks, as long as each is a mindless, unambiguous
choice.** What counts is not the number of clicks but how *hard* each one is — the thought
required and the doubt about whether it was right. Rule of thumb: three mindless clicks ≈
one click that requires thought. Fewer clicks matter more only when a path is repeated often
or pages are slow.

**Third law: Get rid of half the words on each page, then get rid of half of what's left.**
This is deliberately overstated to force ruthlessness. Cutting words reduces noise, makes
useful content prominent, and shortens pages so more is visible at a glance. Two offenders:
*happy talk* ("Welcome to…", self-congratulation — content-free) and *instructions* (nobody
reads them; make things self-explanatory instead, and when instructions are unavoidable cut
them to the bone).

---

## 2. How people actually use the web

Design for these three facts; they are the reason usability matters at all.

**Fact #1: We don't read pages; we scan them.** Users are on a mission, know they don't need
everything, and are good at scanning. They latch onto words matching (a) the task, (b) ongoing
interests, (c) hardwired triggers ("Free", "Sale", their own name). Exception: documents
(news, reports, product descriptions) are read — but even then, reading alternates with
scanning.

**Fact #2: We don't make optimal choices; we satisfice.** Users pick the *first reasonable*
option, not the best one — it's efficient and the penalty for being wrong is usually one or
two Back clicks. (Back is the most-used browser button.) Weighing options rarely pays off on
poorly designed sites and guessing is more fun.

**Fact #3: We don't figure out how things work; we muddle through.** Very few people read
instructions. They forge ahead with vague, sometimes wrong mental models. This is not about
intelligence but about *not caring*: if something works, however badly, we stick to it.
Muddling through is inefficient and error-prone; when users "get it", they find what they
want, discover more of what you offer, feel smarter, and come back.

**Design implication: if users act as if they're driving past billboards, design great
billboards.** The page must work at a glance.

---

## 3. Billboard design: design for scanning

Six levers for pages that get whizzed past:

1. **Take advantage of conventions.** Users expect location (logo top-left, nav top or
   left), behavior (shopping-cart metaphor), and appearance (video/search/social icons).
   Conventions aren't law, but they carry enormous accumulated value. Innovate only when you
   know you have a better idea; otherwise rely on conventions, and use them when you do.
   **Clarity trumps consistency** — if a small inconsistency makes something clearly more
   understandable, choose clarity.
2. **Create effective visual hierarchies.** A good hierarchy has three traits:
   - The more important something is, the more prominent (larger, bolder, distinctive color,
     more white space, nearer the top).
   - Things that are related logically are related visually (grouping, shared style,
     defined area).
   - Things are *nested* to show what's part of what.
   A clear hierarchy pre-processes the page, so users grasp the structure instantly.
3. **Break pages into clearly defined areas.** Let users point at regions and label them
   ("things I can do", "today's deals", "navigation"). Users decide in the first glance
   which regions to read and ignore the rest (banner blindness is the extreme).
4. **Make it obvious what's clickable.** Rely on shape, location, and formatting (one color
   for links, or underlining). Never use the same color for links and non-clickable headings.
   Touch has no cursor to change to a hand, so affordances must be visual.
5. **Keep noise down to a dull roar.** Three noise types: *shouting* (everything clamoring),
   *disorganization* (poor alignment/grids), *clutter* (too much stuff → low
   signal-to-noise). Start from "presumed guilty": everything is noise until it proves it
   contributes.
6. **Format text to support scanning.** Use plenty of well-written headings (with obvious
   level differences, and headings closer to the section they introduce than the one above);
   keep paragraphs short (single-sentence is fine); convert comma-lists into bulleted lists
   with a little extra space between items; highlight key terms in bold on first use — but
   sparingly.

---

## 4. Mindless choices (clicks)

- Provide a strong **scent of information**: links that clearly and unambiguously name their
  target tell users a click moves them toward what they want.
- When a choice is unavoidable and genuinely hard, give just-in-time guidance that is
  **brief, timely, and unavoidable** (e.g., "LOOK RIGHT" painted on a London curb; field
  tips; "What's this?" links; tooltips).
- In forms, make questions easy to answer: ask only what's needed, accept input in natural
  formats, and don't force a difficult decision before the user has to make it.

---

## 5. Omit needless words

Cutting has three benefits: less noise, more prominent content, shorter pages (more visible
without scrolling).

- **Happy talk must die.** If you can hear "blah blah blah" when reading it, cut it. Section
  fronts are the favorite habitat of happy talk — fill them with real content instead.
- **Instructions must die.** Nobody reads them; make everything self-explanatory. If you
  must keep them, prune hard (a 103-word instruction can often become 34).

---

## 6. Navigation

Users won't use a site they can't find their way around. Web navigation exists because the
web has **no sense of scale, direction, or location** — we're inherently "lost in space".

**What navigation does (beyond finding and orienting):** it reveals *what's here* (making the
hierarchy visible), tells users *how to use the site* (implicitly, replacing instructions),
and *builds confidence* in the people who built it.

**Persistent (global) navigation** appears on every page (except forms, where a minimal
version — site ID, Home, helpful utilities — is better). It should include four things:

- **Site ID / logo** — like a building's name; top of page, near the upper-left, framed to
  contain the whole page rather than compete with the content. Usually also a Home link.
- **Sections (primary navigation)** — links to the main sections / top of the hierarchy.
- **Utilities** — links that aren't content hierarchy: Sign in/Register, Help, Site Map,
  Cart, About, Contact. Slightly less prominent than sections; keep to four or five, rest in
  the footer.
- **Search** — unless the site is tiny and well organized, every page gets a search box.
  Use the formula: a box + a button + the word "Search" (or the magnifier icon). Avoid fancy
  wording ("Quick Find"), instructions, and scope options *in the persistent box*; offer
  scoping on the results page when it's actually useful.

**Page names** are the street signs of the web. Every page needs one, in the right place
(framing the unique content), prominent (often the largest text), and **matching the words
the user clicked** — this implicit contract matters even when the mismatch seems trivial.

**"You are here" indicators** show location by highlighting the current section/subsection.
The most common failing is being too subtle: use more than one visual distinction (e.g.,
color *and* bold). If a cue feels like it sticks out like a sore thumb to the designer, make
it twice as prominent.

**Breadcrumbs** show the path from Home to the current page and ease moving up levels. Best
practices: put them at the top; separate levels with `>`; boldface the last item (the current
page, which isn't a link). Most useful in large, deep sites.

**Tabs** work well as navigation because they're self-evident, hard to miss, and can look
polished. To read as tabs, the active tab must visually come to the front: a distinct
color/shade and a physical connection to the content area below.

**Secondary, tertiary, and lower navigation** is where most sites break down. It's vital to
design navigation for *all* levels, not just the top two — users spend as much time deep in
the site as at the top, and lower-level navigation is hard to graft on later.

**The trunk test (do this on any screen):** imagine being dropped onto an arbitrary page and
squinting. You should instantly find and identify: the site ID, the page name, the sections,
the local navigation, the "you are here" indicators, and search. If any of these don't pop
out, that's a finding.

---

## 7. The home page

**Big Bang theory:** the first few seconds are critical. People form snap impressions in
milliseconds that reliably predict their later impressions, and a wrong first assumption
gets force-fit onto everything afterward ("if people are lost when they start, they get
loster"). A home page must, at a glance, convey **what the site is**.

It carries competing demands: identity and mission, hierarchy, search, teases/promos,
timely content, deals, shortcuts, registration — plus abstract goals: show what I want,
expose what I didn't know I wanted, show where to start, and establish credibility. It is
also fought over by stakeholders, so it tends to accumulate "just one more thing" (the
tragedy of the commons).

**Getting the message across:** three places carry an explicit statement of what the site is:

- **Tagline** — a pithy phrase near the site ID. Good taglines are clear and informative,
  6–8 words, convey differentiation/benefit (ideally usable by no one but you), are
  personable, and avoid sounding generic. Don't confuse a tagline (value proposition) with a
  motto (guiding ideal).
- **Welcome blurb** — a terse prominent description (not the corporate mission statement).
- **"Learn more"** — a short explanatory video, which users now expect for novel products.

Use as much space as necessary and no more. The home page's real job is also to answer the
**fifth question**: *Where do I start?* Entry points (search, browse, sign in/register, the
start of a step-by-step process) should look like entry points and be labeled clearly.

Even though few people enter through the home page now, they still "bob up to the surface"
to get their bearings, so it still matters — and every page should orient as best it can.

---

## 8. Usability testing on the cheap

**Focus groups ≠ usability tests.** Focus groups gather opinions and reactions in the
abstract (good for planning, value proposition); usability tests watch one person at a time
actually *try to use* the thing. Only the latter tells you whether the design works.

**Core truths:**
- If you want a great site, test. After a few weeks you can't see it freshly.
- **Testing one user is 100% better than testing none.** Testing always works.
- **Testing one user early beats testing 50 late.** Keep it small so you actually do it.

**Do-it-yourself method:**
- **Cadence:** one morning a month; test three users, debrief over lunch. A fixed day (e.g.,
  the third Thursday) beats milestone-based scheduling.
- **Number:** three per round is ideal. The goal is *actionable insight*, not proof, and you
  can find more problems in half a day than you can fix in a month.
- **Participants:** recruit loosely and grade on a curve. Include some non-target users —
  "we're all beginners under the skin", and clarity for novices helps experts too.
- **Setup:** a quiet room, two chairs, a computer, screen-sharing so observers can watch
  from another room, and screen recording. Facilitator should be patient, calm, empathetic.
- **Observers:** as many as possible; watching is transformative. Each writes down their
  three most serious problems per session.
- **Tasks:** base them on what people must be able to do; word them carefully; let
  participants pick details to increase emotional investment.
- **During the test:** encourage thinking aloud; don't lead, don't help (say "What would you
  do if I wasn't here?"); save probing questions for the end. A one-hour session ≈ 4 min
  welcome, 2 min background questions, 3 min home-page tour, 35 min tasks, 5 min probing,
  5 min wrap-up.
- **Common problems you'll see:** users unclear on the concept; the words they look for
  aren't there; too much going on so the answer is present but invisible.

**Debrief:** list observed problems, vote for the ten most serious, rank them, and assign a
rough fix, owner, and resources for the next month. **Focus ruthlessly on fixing the most
serious problems first.** Keep a separate list of low-hanging fruit (fixable by one person in
under an hour). Resist the impulse to *add* (often the fix is to remove what obscures); take
"new feature" requests with a grain of salt; ignore "kayak" problems (brief stumbles users
recover from unaided).

**Alternatives:** remote testing (widens the recruiting pool), unmoderated remote testing
(cheap, no recruiting, but no interaction).

---

## 9. Mobile

The basic principles are unchanged — people move faster and read even less on small screens.
What's different is mostly **constraints and tradeoffs**, and most serious usability problems
come from a bad tradeoff (e.g., breaking a story into many slow-loading chunks to inflate
page views).

- **The itty-bitty living space.** Small screens force leaving things out or prioritizing
  hard. "Mobile First" is a good way to find what's essential, but don't assume mobile users
  only want "on the move" features — they want to do everything. Put frequent/urgent things
  close; make the path to the rest obvious. Managing real-estate challenges must not come at
  the cost of usability.
- **Responsive design** is a lot of work and hard to do well; if you can't fully mobilize,
  at least allow zooming, don't dump users on the mobile home page when they followed a deep
  link, and always offer a link to the "full" site.
- **Don't hide affordances.** Affordances/signifiers are the visual clues that suggest how to
  use something. On touch there is **no cursor and no hover**: tooltips, hover states, and
  hover-revealed menus vanish. Find replacements.
- **Flat design tradeoff.** Flattening removes visual distinctions — including the useful
  information that conveyed affordances. If you go flat, use the remaining dimensions
  (position, formatting, weight, contrast) to compensate.
- **Speed.** Computers can never be too fast; on mobile, slowness equals frustration and lost
  goodwill. Don't ship huge code and oversized images that the screen doesn't need.
- **Delight, learnability, memorability.** Delight = fun, surprising, impressive, clever,
  magical — but don't let it crowd out usability. Complex apps must be learnable (head
  instructions off at the pass) and memorable (if it was easy to learn, it's easy to relearn).
- **Mobile testing** is the same process; the hard part is logistics (seeing fingers and the
  screen). Favor a camera pointed at the *screen* attached to the device, so it can move
  naturally; skip the face camera.

---

## 10. The reservoir of goodwill

Think of every visit as starting with a **reservoir of goodwill** that each problem drains.
It's idiosyncratic, situational, refillable, and sometimes a single mistake empties it.

**Things that diminish goodwill:** hiding information the user wants (support numbers,
shipping rates, prices); punishing the user for not doing things your way (input formatting);
asking for information you don't need; fake sincerity ("Your call is important to us");
putting sizzle/marketing in the user's way; an amateurish, sloppy-looking site.

**Things that increase goodwill:** know and make easy the main tasks; tell users what they
want to know (be upfront about costs, outages); save steps (pre-filled links, no re-typing);
put real effort into the content; answer likely questions (genuine, updated, candid FAQs);
provide creature comforts (printer-friendly pages); make it easy to recover from errors; when
in doubt, apologize.

---

## 11. Accessibility

Accessibility *is* part of usability: you can't call a site usable if people with disabilities
can't use it. It's the right thing to do, and it often improves usability for everyone. Two
fears drive avoidance — more work, and "compromised design" (buttered cats, where good design
for some seems to oppose good design for others) — but good solutions usually serve both (the
Braille under Plexiglas that let print and Braille each be optimal).

Automated validators are like grammar checkers, not spell checkers: useful for obvious
problems, noisy with vague warnings.

**Four things to do right now:**

1. **Fix the usability problems that confuse everyone.** If something confuses typical users,
   it certainly confuses users with accessibility issues, who also recover harder.
2. **Read about how blind users actually work.** They *scan with their ears*, listening to the
   first few words of a link or line — so keywords must be front-loaded.
3. **Read a book** on accessible UX/standards for the big picture.
4. **Go for the low-hanging fruit:** appropriate alt text (empty `alt=""` for decorative
   images); correct heading structure; form labels associated with fields; a "Skip to main
   content" link; full keyboard accessibility; strong text/background contrast; an accessible
   template.

---

## 12. Quick reference: definitive answers

Almost every usability question is "it depends — test it", but a few are near-absolute:

- **Never** use small, low-contrast type. (Large low-contrast or small high-contrast is
  acceptable; both are still risky.)
- **Don't** put labels inside form fields unless the form is trivial, labels vanish on typing
  and reappear when empty, they can't be confused with answers, they can't be submitted as
  data, and they're fully accessible.
- **Preserve** the visited/unvisited link distinction (it's tracked by URL, so it also tells
  users when differently-worded links lead to the same place).
- **Don't** float headings between paragraphs: a heading belongs closer to the text it
  introduces than to the text above it.
- **Resist the temptation to manipulate** users; usability's job is to advocate for them.
- If a rule must be bent, know *which* rule and have a deliberate reason.
