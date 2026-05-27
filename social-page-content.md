# Social Media Page Content · Final Copy for `portfolio-social.html`

All four Instagram account descriptions in final, voice-checked form. Ready to swap into the HTML.

**Page framing note:** Per Hannah's call, the page treats the accounts as separate brands she operates, not as a mix of personal + client work. No stats numbers on the page (intentional, to avoid maintenance overhead).

---

## Account 1 — @hann.runs

- **Handle:** `@hann.runs`
- **Category label:** Owner · Running Community
- **Description:**

> A running journal built around one ritual: the same photo on every run, paired with honest reflections on how it actually felt. What started as personal accountability has grown into a community of women improving themselves one mile at a time. Bold, colorful, real. No curated highlight reel, no "crushed it" energy, just honest miles.

---

## Account 2 — @happy_healthy_hann

- **Handle:** `@happy_healthy_hann`
- **Category label:** Owner · Food & Wellness
- **Description:**

> Real food, mostly homemade, from a Methow Valley kitchen. An ex-D1 athlete with PCOS who started eating meat at 25 and is figuring out what real fueling looks like now. Organic, whole, no seed oils, no apologies. Anti-diet, pro-flavor, pro-color.

---

## Account 3 — @layla_weymuller

- **Handle:** `@layla_weymuller`
- **Category label:** Owner · Pet & Lifestyle
- **Description:**

> A golden retriever in the Methow Valley with a rich inner life and an iPhone-toting mom. Layla speaks in short, joyful bursts: the ball, the river, the nap, the mom who brought the ball to the river before the nap. Adventure dog by day, dramatic homebody by night, certified service dog when the vest goes on.

- **Pull quote (styled separately):**

> *Best day ever. Every day. Even the boring ones.*

  Suggested styling: italic Fraunces, magenta, positioned visually distinct from the description (e.g., floating beside or below it). Use existing `.section-heading` italic-em-color pattern if appropriate, or a new pull-quote class.

---

## Account 4 — @louploup_ski_team

- **Handle:** `@louploup_ski_team`
- **Category label:** Manager + Coach · Ski Team Community
- **Description:**

> The community space for the Loup Loup Ski Team, a 100% volunteer-coached alpine racing program for U8 through U12 athletes based out of Loup Loup Ski Bowl, the nonprofit hill in Okanogan County, WA. Race days across Washington State, the team's own Wolf Chase Race, and the daily reality of small-mountain ski racing. For team families, locals, fellow racers around the state, and anyone who loves what a small ski hill can produce.

---

## To-Do (Claude Code work)

### 1. Update `portfolio-social.html`

For each of the 4 account-breakout blocks, swap:
- The handle in the section heading
- The category label (currently a category placeholder)
- The `<p class="account-desc">[PLACEHOLDER — ...]</p>` text with the description above
- Remove or hide the stats blocks (`<div class="account-stat-num">[X]</div>` etc.) since we're not using numbers

### 2. Add the Layla pull quote

For the `@layla_weymuller` block only, add a pull quote element styled as italic Fraunces in magenta. Place visually adjacent to the description (designer's call on exact layout). Existing CSS likely supports this via the `.section-heading` italic em pattern or by adding a new `.account-pullquote` class.

### 3. Verify the 5th account slot

The original handoff doc was built for 4 accounts. Hannah owns a 5th (`@i_spy_vanity`, a vanity license plate hobby account) that has been **intentionally excluded** from the portfolio page. If `portfolio-social.html` has a 5th account-breakout block, remove it. If not, no action needed.

### 4. Phone frame screenshots (placeholder until IG embed widgets are wired)

Each `.phone-frame` block currently has `<!-- TODO: replace with embed widget -->` comments. As an interim solution until Elfsight/SnapWidget embeds are added, place a static screenshot of each account's grid view inside the phone screen.

Hannah has provided 4 IG profile screenshots. They need to be:

1. **Cropped to just the 3x3 grid area** (cut off the handle bar at the top, the tab icons row, and the bottom navigation bar). The result should be a clean rectangle of just the photo thumbnails, no Instagram app chrome.
2. **Saved into `/assets/`** with these filenames:
   - `ig-grid-hann-runs.jpg`
   - `ig-grid-happy-healthy-hann.jpg`
   - `ig-grid-layla.jpg`
   - `ig-grid-louploup.jpg`
3. **Placed inside each account's `.phone-screen` element** using `object-fit: cover` and `object-position: top` so the grid fills the phone screen naturally.

If the original screenshots are too tall for the phone-screen aspect ratio, crop further so only the top 6-9 thumbnails are visible. The goal is "real IG feed inside the phone," not "letterboxed screenshot."

### 5. Final voice check before commit

Confirm none of the descriptions contain:
- Em dashes
- Banned words (synergy, leverage, hustle, grind, circle back, disruptive, move the needle, stakeholder)

(They don't. Already checked. But worth a final eyeball.)

---

## Handle verification — RESOLVED

All four handles have been verified via Instagram screenshots. Final correct handles:

| Account | Final handle |
|---------|--------------|
| Running | `@hann.runs` |
| Food | `@happy_healthy_hann` |
| Layla | `@layla_weymuller` |
| Ski team | `@louploup_ski_team` |

Note that 3 of the 4 were misspelled in the original handoff doc. The versions in this doc are the verified correct ones.

---

## Notes on the editorial choices

A few things worth knowing about why the descriptions read the way they do:

**Each description leads with a different angle to demonstrate range.**
- `@hann.runs` leads with the ritual.
- `@happyhealthyhann` leads with the origin (PCOS + ex-D1 + late-to-meat).
- `@Layla_Weymuller` leads with the voice (Layla's POV).
- `@Louploup_ski_team` leads with the operational identity (the team).

This is intentional. A potential client landing on the Social Media services page sees four accounts that each demonstrate a different kind of social media work: community building, personal branding, character/voice writing, and team/institutional accounts. That's a stronger pitch than four variations of the same description.

**The Louploup description is the strongest piece of "I can do this for clients" evidence on the page.** It's the only one where Hannah is positioned as an operator (and coach) of someone else's program rather than the protagonist. A potential client will likely linger there.

**Voice shifts across the accounts.** `@hann.runs`, `@happyhealthyhann`, and `@Louploup_ski_team` are in Hannah's voice but at different registers (personal-essay, food-blogger, institutional). `@Layla_Weymuller` shifts into channeling Layla. The voice shifts themselves are the proof of versatility.

**No banned words. No em dashes. First person where personal, third person where institutional.** All consistent with the brand book.

**No numbers anywhere.** Intentional choice to avoid maintenance overhead. The accounts will speak for themselves once the IG embed widgets are wired up (separate decision, deferred per the original handoff doc).
