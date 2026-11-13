# Website redesign — change log

**Site:** merakiascent.com (GitHub Pages, repo `merakiascent-llc/merakiascent-llc.github.io`, branch `main`)
**Date:** Thursday, November 12, 2026
**Status:** All changes below are live.

For how the new look is built and how to match it in other work, see [`WEBSITE-DESIGN-GUIDE.md`](WEBSITE-DESIGN-GUIDE.md).

---

## At a glance

| Time (PT) | Commit | What changed |
|---|---|---|
| 11:47 | `e68cf02` | New home page: rising mountain hero, spinning logo badge, results, Venn, founder photo |
| 11:57 | `eaab8b0` | Social portfolio: real Instagram grids for Twisp River Suites and Winthrop; updated Methow Cycle grid |
| 12:02 | `cecdc51` | Mobile menu fix, iMessage/social link-preview card, iPhone icon, bigger desktop mountains |
| 12:13 | `6dcb0c1` | Every inner page restyled to match the home page (`elevate.css`) |

To undo any one change: `git revert <commit>` and push to `main`.

---

## 1. Home page redesign (`index.html`) — `e68cf02`, refined in `cecdc51`

**Why:** the old home page "laid flat": one white column, no depth, the same fade on every section.

**How we got here:** 20 concept pages were explored on the *Meraki Ascent Home Concepts* design canvas over four rounds (motion-forward; light and human; dark/light contrast with data first; then "Elevated"). Hannah chose **Elevated**, then refined it:

- Mountains redrawn in the logo's own style: hand-inked plum outlines, wavy gully lines running down from each peak, faceted pink planes. Not flat blocks of color.
- Reference: North Cascades ridgelines (Liberty Bell / Washington Pass). Ridges stack and overlap like a real range, with no sky showing between rows.
- Sky changed from saturated teal to a soft light blue with dark plum text, because the teal plus mountains was too busy.
- The four ridge layers rise into place one after another as you scroll (far to near) while the screen holds still.
- The real logo replaces the plain moon, with PASSION · PURPOSE · PROGRESS · MERAKI slowly circling it.
- Hannah's headshot added to the founder section.

**Page order now:**

1. **Hero** — light-blue sky, eyebrow (Business development · Investor relations · Marketing), headline "Connecting people. Driving *meaningful* growth.", spinning logo badge, "Scroll to begin the ascent ↓", four rising ridges.
2. **Results** (plum) — 95.4K plays (East 20 Pizza), 15K→52K monthly views (Methow Cycle & Sport), +96% booking clicks (Twisp River Suites). Numbers count up; a pink ridgeline draws itself beneath.
3. **The practice** (cream) — "Three tables. *One seat at all of them.*" with links to Business Development, Investor Relations and Services, next to a Venn of BD / IR / Marketing drawn in the logo's style that slides together around the logo.
4. **Client banner** — slow, self-scrolling names: Terra Axis, Methow Cycle & Sport, East 20 Pizza, Winthrop Chamber, Twisp River Suites, Gamble Sands, Blue Star Coffee Roasters.
5. **Founder** (plum) — arched, plum-outlined portrait; "Strategic operator. *Human connector.*" → /about.
6. **FAQ** — unchanged. Still matches the FAQPage schema Google reads.
7. **Closing CTA** (light-blue sky + ridges) — "Ready for the *next ascent?*" → /contact.

**Kept as-is:** shared top menu, footer, page title and description, structured data, FAQ.

**Quality check before publishing:** rendered at six screen sizes (1440, 1366×680, 1280, tablet 820, phone 390 and 375) and scrolled top to bottom testing for any text touching text, the badge, the photo or the mountains. Fixes made from that check:
- mountains moved into their own band below the text, so they can never cover words;
- badge moves above the headline on tablet and phone;
- ridges anchored by their peaks so summits never get cut off on short screens;
- top menu tightened on phones.

**Desktop follow-up (`cecdc51`):** on desktop the ridge art is zoomed (150% wide, centered) so it shows fewer, bigger peaks like the phone view, and the hero fills the full screen height on large monitors.

**New files:** `assets/hero-range-0.svg` … `hero-range-3.svg` (four ridge layers), `assets/logo-icon-moon.png` (icon with the moon filled white, for use on colored backgrounds).

## 2. Social Media portfolio phones (`portfolio-social.html`) — `eaab8b0`

- **Twisp River Suites:** logo placeholder replaced with the real Instagram grid → `assets/ig-grid-twispriversuites.jpg`
- **Winthrop Chamber:** logo placeholder replaced with the real Instagram grid → `assets/ig-grid-winthrop.jpg`
- **Methow Cycle & Sport:** grid updated → `assets/ig-grid-methowcycle-2026-11.jpg` (the old `ig-grid-methowcycle.jpg` is still in the repo, unused)
- Each appears in both the scrolling phone banner and the client's own section. Screenshots were cropped below the phone status bar and saved at 736 px wide to match the other grids.

## 3. Mobile menu fix (`styles.css`) — `cecdc51`

**Bug:** on phones the hamburger menu showed only one option at a time.
**Cause:** the top bar's frosted-glass blur (`backdrop-filter`) made the bar the "container" for the slide-out menu, squashing the menu to the bar's 76 px height.
**Fix:** under 900 px wide the bar is solid white with no blur, and the menu fills the screen below the bar (`100dvh − 76px`) and scrolls if needed. Applies to every page. Stylesheet cache version bumped to `styles.css?v=20261112`.

## 4. Link previews in iMessage and social — `cecdc51`

**Bug:** sending merakiascent.com in iMessage showed a blank preview.
**Cause:** the preview image was the logo on a fully transparent background.
**Fix:**
- New 1200×630 share card `assets/share-card.jpg`: horizontal logo lockup with the teal tagline, on the light-blue sky, with the four ridges and MERAKIASCENT.COM.
- `og:image` and `twitter:image` now point at it on the home page and on every page that used the transparent logo, with `og:image:width`, `og:image:height` and `og:image:alt`. Pages with their own photo kept it.
- `assets/apple-touch-icon.png` (180×180, icon on light blue) added to every page, for iPhone home-screen saves.
- iMessage caches previews. To see the new card in an old thread, send `merakiascent.com/?hi`.

## 5. Inner pages restyled to match home (`elevate.css`) — `6dcb0c1`

Drafted on branch `redesign-drafts`, reviewed on the *Inner page drafts* page of the design canvas (now vs. desktop draft vs. phone draft for all 12 pages), then merged to `main`.

**How it works:** one new shared stylesheet, `/elevate.css?v=1`, loaded last on 14 pages. It restyles only; page text, photos, links, prices and FAQs are untouched.

**Pages:** about, about-meraki, services, photography-videography, writing-services, business-development, investor-relations, portfolio, portfolio-writing, portfolio-social, portfolio-photography, contact, and both album pages. The album pages have no header, so they mostly pick up the buttons and footer.

**What it changes:**
- **Page headers:** light-blue sky, plum headline, the four ridges along the bottom rising in on scroll.
- **Header photos** (About, Services, Contact): arched top, 6 px ink outline, magenta keyline.
- **Sections:** dark → plum, pale pink → light blue, cream stays. Old radial-gradient glows removed. Headings rise in gently.
- **Buttons:** plum pills that turn magenta on hover.
- **Closing CTAs:** sky + ridges, like the home page ending.
- **Footer:** plum ridge line where every page meets the footer.

**To turn it off for one page:** delete that page's `<link rel="stylesheet" href="/elevate.css?v=1">` line.

---

## Not changed

Site structure and URLs, navigation links, all copy, SEO titles and descriptions, structured data, Google verification file, sitemap.

## Known follow-ups (optional)

- At tablet widths (~900–1100 px) the top menu wraps "Meraki Ascent" and "Get in Touch" onto two lines. This predates the redesign.
- Second pass on busier pages: Services pricing cards and Portfolio overview tiles could adopt the home page's counting numbers and Venn style.
- Unused file `assets/ig-grid-methowcycle.jpg` can be deleted.

## Where the design work lives

- **Design canvas:** *Meraki Ascent Home Concepts* (claude.ai artifact), with all concept rounds, the Elevated page and the inner-page drafts.
- **Ridge artwork generator:** `tools/mountains.py` (regenerates the four ridge SVGs; see the design guide).
