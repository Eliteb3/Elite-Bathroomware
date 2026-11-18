---
name: radio-ad-engine
description: >-
  Run Elite Bathroomware's monthly radio engine with NZME. Turns the Demand Radar
  signal, Shopify stock and the locked NZME "Bathrooms made simple" platform into one
  hero category per flight, then writes on-platform scripts in NZME's two frames
  ("Hear that?" and the zone-questions route), runs the pre-air checks, and hands NZME a paste-ready brief
  once Josh approves. USE THIS SKILL whenever the user asks for radio ads, radio
  scripts, an NZME brief, a radio flight, "what should the radio say this month",
  a new zone script or "Hear that?" spot, rewriting or reviewing radio scripts someone else
  wrote, or wants radio to follow what's selling or trending — even if they never
  say "radio engine". Also trigger to review last flight's results or plan the
  next month's radio.
---

# Elite Radio Engine

The radio sibling of Ivy. Same machine, different medium: demand signal in, a
**decision** out. Not "some radio ideas" — one hero, one script set, one brief NZME
can record from, with the reason and the data behind it.

## Before anything else — load the contract

| File | What it gives you |
|---|---|
| `references/nzme-platform.md` | The locked NZME platform: "Bathrooms made simple", four pillars, the two creative frames, jingle, mandatories. **The scripts are wrong without it.** |
| `references/script-craft.md` | How to write for radio at Elite: word budgets, structure, banned phrases, examples of bad → good |
| Ivy's `references/user.md` + `references/soul.md` (ivy-content-engine skill) | Josh, the team, the guardrails, the voice. Radio obeys every Ivy guardrail. |

NZME's platform is **locked**. The engine never invents a new structure, end line or
jingle — it chooses what goes *inside* NZME's frames.

## The one thing to get right

NZME gave us the frame; demand decides the contents.

| NZME frame | Fixed (NZME) | Swaps every flight (engine) |
|---|---|---|
| **Concept Two — "You have questions. Elite has answers."** | Zone opener, "It's the questions the Elite team asks…", jingle, big blue store + address | **Which zone** (= Demand Radar hero category) and **the four questions** (built from rising search queries) |
| **Concept One — "Hear that?"** | "Hear that?" device, Elite instrumental, jingle, big blue store + address | **SFX, pillar and proof point**, pointed at the same hero/season |

Default monthly output: **one zone script on the hero + one "Hear that?"** supporting it.
NZME records the new middle; the music, jingle and sign-off never change.

---

## The monthly run

Run it **~3 weeks before the flight starts** (NZME needs final scripts ~10 working
days before air — confirm the exact lead time with the NZME rep and update this line).

### Step 0 — Input state (be honest which tier)

- **Full:** Demand Radar runs live, Shopify stock readable, NZME platform filled,
  last flight's results available.
- **Partial:** any of those missing → run anyway and **state what's missing in line 1
  of the output.** Never fake a number.
- **Cold:** no flight dates and no demand data → one short ask: flight dates + spot
  lengths booked. Nothing else.

### Step 1 — Read the signal

1. **Demand Radar — monthly mode** (`demand-radar` skill). Want the categories in
   the 🔴 *head start* cell (search up, sales lagging) and genuine-not-seasonal rises.
   For a flight 3–6 weeks out, weight **search momentum + last year's shape for the
   flight month** over current sales — radio lands in the future.
2. **Shopify** — best sellers last 30 days inside the candidate category, and stock
   by SKU **and finish**.
3. **Known calendar** (Ivy `identity.md` §10) + any live tentpole brief. During a
   tentpole, the spots serve the campaign — don't invent a parallel strategy.
4. **Last flight's results** (Step 7 numbers) — what the last hero did.
5. **What Ivy is briefing** this month. Radio and social should share the hero.

### Step 2 — Pick ONE hero (five gates, all green)

| Gate | Question | Fail = |
|---|---|---|
| **Demand** | Is search climbing (ideally above last year) for this category in the flight month? | Bin it. |
| **Stock** | Stock covers the flight **plus 4 weeks** of follow-through, in the finish you'll name? | **Hard no.** Flag Josh, loop Dean. Shopify shows 0/negative on made-to-order lines (e.g. Elite shower kits) — treat as "unverified", not "out", and confirm with Dean. |
| **Showroom** | Is it on display at 59A so someone who walks in can see/touch it? | Radio drives ~91%-offline revenue through the door. Not on the floor = not on air. |
| **Web** | Is there a live collection/product page the URL can land on? | Fix with Ashlea first, or don't air it. |
| **Ear-ability** | Can a listener *picture* it from words alone (a freestanding bath, brushed-brass tapware, an LED mirror) — or is it a part number? | Pick the next candidate. |

Output the **pick + one runner-up**, one line each on why. Not a menu.

### Step 3 — Write the scripts

Follow `references/script-craft.md` exactly. Deliver:

1. **Zone script (30s)** — Concept Two on the hero category. If the zone isn't one NZME
   wrote (Tapware, Toilet, Accessories), write it in the same frame. Two question-sets
   (A/B) so NZME can rotate.
2. **"Hear that?" (30s)** — Concept One, pillar chosen to fit the month (see
   `nzme-platform.md` §2), SFX that points at the hero.
3. **15s zone cut-down** — opener, 1–2 questions, jingle, address.
4. Production notes: voices per frame, SFX, pronunciation (**Tāmaki = TAH-mah-kee**).

Then run the checker on every script and fix anything it flags:

```bash
python3 scripts/script_check.py scripts.txt
```

See `assets/example-tapware-zone.txt` for a passing example.
`scripts.txt` = one script per block, `### <name> (<length>s)` header line, body below,
one element per line prefixed `SFX:` / `MUSIC:` / `V1:` / `V2:` / `VO:` / `JINGLE:`.

Save the run to `radio/<YYYY-MM>-flight.md` and `radio/<YYYY-MM>-scripts.txt` in the repo
so Step 7 has a baseline.

**Semrush trend arrays run oldest → newest** (checked Nov 2026 against heated-towel-rail
winter peaks) — the demand-radar notes say the opposite. Read last year's flight month
accordingly.

### Step 4 — Pre-air checklist (every flight, every time)

- [ ] **59A** Allens Road, East Tāmaki — not 59, not "59 a". Macron on Tāmaki.
- [ ] Opening hours read on air (if any) match the hours for **every day of the flight**,
      incl. public holidays inside the window (Auckland Anniversary = Monday nearest
      29 Jan; Waitangi 6 Feb; Easter; King's Birthday; Labour Day).
- [ ] Every brand or product named is **currently stocked** and in the finish named.
- [ ] No Code Interiors, EliteOutlet, clearance or seconds in Elite radio.
- [ ] Brand phase = no price/discount. Sale phase = offer only if scoped and signed off
      by Dean ("up to X% off" defensible or not said).
- [ ] Jingle exactly "Speak to Elite. We make bathrooms simple." then "The big blue store,
      59A Allens Road, East Tāmaki." — nothing after the address.
- [ ] One pillar per spot; pillar rotated vs last flight.
- [ ] If a URL is read, it lands on the hero's page and the page is live.
- [ ] Word counts inside budget (checker passes).

### Step 5 — Josh approves

Output goes to Josh, phone-readable, under 10 minutes to approve. He kills, tweaks,
approves. **Nothing goes to NZME un-approved.**

### Step 6 — NZME handover

Produce the brief in `assets/nzme-brief-template.md`, filled — paste-ready for the
NZME rep. If Josh asks, draft the email in Outlook **Drafts** (never send) and create
an Asana task "Radio — <month> flight" with the brief and the NZME deadline as due date.

### Step 7 — Close the loop (after the flight)

Within 2 weeks of the flight ending, pull and record in the next run's Step 1:

- **Hero category sales** during flight vs same window last year vs the 30 days before
  (Shopify, category-mapped via demand-radar's script).
- **Branded search** ("elite bathroomware", "elite bathrooms") in Semrush NZ vs prior months.
- **Hero landing page sessions** during flight (ask Ashlea if not available).
- **Showroom attribution** — Jackson's floor team asks "how did you hear about us?";
  count of "radio" answers. If nobody's asking, say so: radio is unmeasured without it.

Report as a 4-line scorecard. Be honest: radio is a slow, multi-touch medium; one
flight proves little, three flights in the same direction prove something.

---

## Output format

```
RADIO — <Month YYYY> flight (<dates>, <station(s)>, <lengths>)
Input state: Full / Partial — <what's missing>

HERO ZONE: <category> — lead product <product + finish>  — <one-line verdict with the number behind it>
Runner-up: <…> — <why not first>
Gates: Demand ✅ Stock ✅ (<qty / weeks cover>) Showroom ✅ Web ✅ Ear ✅

ZONE SCRIPT 30s (A)  <script>   [<n> spoken words · ~<s>s + jingle]
ZONE SCRIPT 30s (B)  <alternate questions>
HEAR THAT? 30s       <script> — pillar: <…>
15s ZONE             <script>
Production notes     <tone, pace, pronunciation, music>
Pre-air checklist    <ticks / open items>
Last flight scorecard <4 lines, or "first flight — no baseline">
```

## Escalations (raise unprompted)

- Hero has no search behind it → say so before writing.
- Stock risk → Josh, loop Dean.
- Any price or discount → Dean before NZME.
- Someone hands in scripts that break the platform (no "Hear that?"/zone frame, no
  jingle, no big blue store, generic "huge range / every budget" copy, brand lists) → review them against `script-craft.md` and say plainly
  what fails and why, then supply the on-platform version.
- Radio and Ivy pointing at different heroes in the same month → flag it.
- NZME drafts over the word budget or missing the macron → send back corrected.

## Out of scope

Media buying, spot rotation and station mix (NZME + Josh own it) · Code Interiors
(has its own NZME campaign in the same deck — never mix) ·
EliteOutlet · trade/wholesale · producing audio.
