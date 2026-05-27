# Writing Page Content · Final Copy for `portfolio-writing.html`

All five article cards in their final, voice-checked form. Ready to swap into the HTML.

**Display order:** most recent first (matches existing card layout).

---

## Article 1 — FEATURED

- **Title:** Hold the Impostor's Hand
- **Publication:** LinkedIn · Self-Published
- **Date:** May 2026
- **URL:** https://www.linkedin.com/pulse/hold-impostors-hand-hannah-weymuller-ezajc/
- **Thumbnail filename:** `assets/article-impostor.jpg`
- **Featured treatment:** Yes (magenta corner accent per existing CSS)
- **Excerpt:**

> What if the impostor and the athlete are the same person? A reflection on a NARP turned Division I triathlete turned founder, and the voice that has been asking "who do you think you are" since freshman year. Spoiler: I stopped trying to answer it.

---

## Article 2

- **Title:** 8 Years in the Making: How I Became Managing Partner at 26
- **Publication:** LinkedIn · Self-Published
- **Date:** April 2026
- **URL:** https://www.linkedin.com/pulse/8-years-making-how-i-became-managing-partner-26-hannah-weymuller-h4bmc
- **Thumbnail filename:** `assets/article-deer-trail.jpg`
- **Excerpt:**

> I scored a 9% on my first college exam. Not 90. Nine. The story of how dyslexia, a cold LinkedIn message in 2020, and six years of unglamorous follow-through led to a Managing Partner offer at 26. Careers aren't interstates. They're deer trails.

---

## Article 3

- **Title:** The Bottleneck Nobody Talks About. And the Tech Quietly Solving It.
- **Publication:** LinkedIn · Self-Published
- **Date:** April 2026
- **URL:** https://www.linkedin.com/pulse/bottleneck-nobody-talks-tech-quietly-solving-hannah-weymuller-xea8c
- **Thumbnail filename:** `assets/article-bottleneck.jpg`
- **Excerpt:**

> The clean energy transition has never lacked vision. What it has lacked is speed. A look at where AI is actually making a difference in clean energy deployment right now, from site screening to interconnection queues, and why the unglamorous version of the technology matters more than the hype cycle.

---

## Article 4

- **Title:** What Happened When I Got Out of My Own Way
- **Publication:** LinkedIn · Self-Published
- **Date:** October 2022
- **URL:** https://www.linkedin.com/pulse/what-happened-when-i-got-out-my-own-way-hannah-weymuller
- **Thumbnail filename:** `assets/article-out-of-my-way.jpg`
- **Excerpt:**

> Fresh out of university and asked to mentor accomplished engineers from Kazakhstan and Nigeria, my first instinct was to discount myself out of the room. The story of what happened when I flipped the internal dialogue and said "if not now, when?" instead. One of the early moments that taught me the impostor doesn't get the last word.

---

## Article 5

- **Title:** How I Ditched the Application Headache, and Designed my Ideal Internship
- **Publication:** LinkedIn · Self-Published
- **Date:** May 2021
- **URL:** https://www.linkedin.com/pulse/how-i-ditched-application-headache-designed-my-ideal-hannah-weymuller
- **Thumbnail filename:** `assets/article-callisto.jpg`
- **Excerpt:**

> The original story behind the deer trail. Years before I learned to call it that, I was a college junior tired of scouring LinkedIn and Indeed. So I emailed Callisto a pitch for an internship position that didn't exist. The phone call I got back in a Minnesota airport security line started a pattern I would keep using for the next eight years.

---

## To-Do (Hannah, ~15 min)

### 1. Save thumbnails from LinkedIn

For each article, open the LinkedIn URL, right-click the article's cover image, save as the filename listed above into `/Users/hannahweymuller/Desktop/Meraki Ascent LLC/Website/assets/`.

Target spec: ~1200×800 JPG, 3:2 ratio. LinkedIn covers vary, so just save what's there and Claude Code can crop/resize if needed.

| Article | Save as |
|---------|---------|
| 1 | `article-impostor.jpg` |
| 2 | `article-deer-trail.jpg` |
| 3 | `article-bottleneck.jpg` |
| 4 | `article-out-of-my-way.jpg` |
| 5 | `article-callisto.jpg` |

### 2. Update `portfolio-writing.html`

For each of the 6 existing article cards in the HTML, swap:
- `href` → the real LinkedIn URL
- `<img src=...>` → the real thumbnail path
- `<span class="article-publication">` → "LinkedIn · Self-Published"
- `<span class="article-date">` → the real date
- `<h3>` → the real title
- `<p>` → the real excerpt
- `<span class="article-link">` → "Read on LinkedIn →" (already correct)

### 3. Decide what to do with the 6th card

You have **5 articles** but the page has **6 card slots**. Options:
- **A.** Remove the 6th card entirely. Page shows 5 cards.
- **B.** Leave the 6th card as a styled "More coming soon" placeholder.
- **C.** Wait until you write a 6th article, then fill it in.

Recommended: **A**, the grid will adjust gracefully.

### 4. Keep the About page teaser in sync

The About page shows the **first 3 articles** in a "Writing & Press" teaser. After updating `portfolio-writing.html`, also update `about.html` so the first 3 cards match (Articles 1, 2, and 3 above).

### 5. Voice flag for later

Article 2 ("8 Years in the Making") uses the word **"grinding"** in your original LinkedIn text ("digging deep and grinding your way through"). Your brand voice rules ban "grind." Worth a quiet edit on LinkedIn at some point. The website excerpt doesn't use the word.

---

## Notes on the editorial choices

A few things worth knowing about why the excerpts read the way they do:

**The arc is intentional.** Articles 1, 4, and 5 all reference each other. Article 1 is the mature reflection on the impostor. Article 4 is labeled "one of the early moments" in that arc. Article 5 is labeled "the original story behind the deer trail" referenced in Article 2. This turns the page from "five disconnected pieces" into "a body of work with internal threads," which is a stronger Portfolio statement than the parts would be alone.

**The older pieces are framed as origins, not artifacts.** This protects the 2021 and 2022 articles from looking dated next to the 2026 work.

**No em dashes anywhere.** Voice rule respected throughout.

**No banned words.** No synergy, leverage, hustle, grind, circle back, disruptive, move the needle, or stakeholder.

**First person throughout.** Matches the Writing page's personal-pieces voice.

**Specifics over generalities.** "9% on my first college exam," "Minnesota airport security line," "Kazakhstan and Nigeria," "interconnection queues." Cards earn clicks by being specific, not by summarizing themes.
