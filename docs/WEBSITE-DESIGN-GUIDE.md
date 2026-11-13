# Meraki Ascent — Website Design Guide

*Brand book chapter: how merakiascent.com is designed, so new pages, social posts, decks, emails and print can match it.*
*Version 1 · November 2026 · matches the live site after the November 12 redesign.*

**The idea in one line:** the site is the logo, opened up into a whole landscape. A soft sky, hand-inked pink mountains, a white moon, and plum type, with generous calm space around them.

---

## 1. Principles

1. **Clean, elegant, on-brand.** One idea per section. Leave room. If a section feels busy, remove something before adding anything.
2. **The mountains carry the color.** Backgrounds stay quiet (sky, cream, plum). The pinks live in the mountains, the Venn and small accents.
3. **Drawn, not blocky.** Mountains always look like the logo: hand-inked plum outlines, wavy gully lines down each face, faceted pinks, overlapping ridges like the North Cascades. Never flat triangles or solid shapes.
4. **Proof early.** Real client numbers appear near the top and are always sourced.
5. **Human.** Hannah's real photo, first-person warmth, and her own words. Never stock-photo people.
6. **Movement is slow and purposeful.** Things rise, draw and settle as you scroll. Nothing bounces, flashes or loops fast.

---

## 2. Color

### Core palette

| Role | Name | Hex | Use |
|---|---|---|---|
| Sky | Mist Sky | `#E2F2F4` | Hero and CTA backgrounds, page headers, light bands |
| Primary text / dark ground | Deep Plum | `#3B1328` | All headings and body on light; dark sections; buttons |
| Linework | Ink Plum | `#24091A` | Mountain and Venn outlines, photo frames, ground line |
| Accent | Meraki Magenta | `#E3288A` | Mountain front faces, Venn, keylines, small accents |
| Accent (hover / text accent) | Deep Magenta | `#DE1C7E` | Link hover, button hover, eyebrows on cream |
| Soft accent | Blush | `#F3A6CC` | Italic emphasis and labels on plum; Venn third circle |
| Logo sky | Ascent Teal | `#47AEBC` | Venn BD circle and the logo itself. Not a page background (too busy with mountains) |
| Light ground | Warm Cream | `#FBF8F4` | Content sections, FAQ |
| Body on plum | Plum Mist | `#E6D3DD` | Paragraph text on Deep Plum |
| Hairlines | Rose Line | `#E6D9DF` | Dividers on cream; `#6B3A55` dividers on plum |

### Ridge palettes (far → near)

Each ridge uses a shaded side (left of each peak) and a lit side (right of each peak).

| Layer | Shaded faces | Lit faces |
|---|---|---|
| 0 — far | `#F2A9CB` `#EE97C0` `#F5BBD6` | `#F9D3E5` `#F7C6DD` `#FADDEB` |
| 1 | `#EC7DB3` `#E86BA6` `#F09BC4` | `#F6BBD7` `#F3A6CC` `#F8CDE1` |
| 2 | `#E5469B` `#E8579F` `#EC6FA9` | `#F09BC4` `#EF8FBE` `#F3A6CC` |
| 3 — near | `#E3288A` `#DE1C7E` `#E5469B` | `#EF8FBE` `#EA7DB3` `#F3A6CC` |

Distance rule: further ridges are paler; the nearest ridge is full magenta.

### Section rhythm

Alternate grounds so the page breathes: **Sky → Plum → Cream → (banner) → Plum → Cream → Sky**. Never put two plum sections back to back, or two cream sections without a divider.

### Text on each ground

| Ground | Heading | Italic emphasis | Body | Label |
|---|---|---|---|---|
| Mist Sky | Deep Plum | Deep Plum, weight 500 | Deep Plum | Deep Plum |
| Warm Cream | Deep Plum | Deep Magenta | `#5A3A4A` | Deep Magenta |
| Deep Plum | White | Blush | Plum Mist | Blush |

---

## 3. Typography

| Role | Font | Settings |
|---|---|---|
| Display / headings | **Fraunces** (Google Fonts) | Weight 400; one key phrase in *italic* (500 on sky). Hero 48–88 px, section 38–58 px, line-height 1.02–1.1, letter-spacing −0.01em |
| Big numbers | Fraunces | Weight 300, 64–76 px, line-height 1 |
| Body | **Inter** | 400, 17–18 px, line-height 1.6–1.75, max ~520 px wide |
| Eyebrows / labels | Inter | 600, 12 px, UPPERCASE, letter-spacing 0.22em |
| Buttons / nav | Inter | 600, 13 px, UPPERCASE, letter-spacing 0.14em |
| Handwritten notes | — | Not used on the live site. Keep script fonts for social only. |

**Headline pattern:** a plain clause plus an italic turn.
*"Three tables. **One seat at all of them.**"* · *"Ready for the **next ascent?**"* · *"Strategic operator. **Human connector.**"*

---

## 4. Logo use on the site

- **Header:** icon (48 px) + plum wordmark.
- **Hero badge:** the full-color icon (`assets/logo-icon-moon.png`, moon filled white) inside a slowly spinning ring of text: `PASSION · PURPOSE · PROGRESS · MERAKI ·` in Inter 600, 13 px, Deep Plum. One full turn every 40 seconds.
- **Venn center:** the icon with a 6 px ring of the section background around it.
- **Footer:** white one-color wordmark on plum.
- **Link previews:** `assets/share-card.jpg` (1200×630). iPhone icon: `assets/apple-touch-icon.png`.
- Never put the transparent-background logo where a preview or thumbnail is generated. It renders blank.

---

## 5. Signature elements

### 5.1 The mountain range
- Four separate ridge layers: `assets/hero-range-0.svg` (far) to `hero-range-3.svg` (near).
- **Drawing style:** jagged ridgeline; wavy hand-drawn gully lines fanning down from each summit; short wavy bands cutting across faces; 5–6 px Ink Plum outlines with round joins; faceted fills from the ridge palettes.
- **Composition:** ridges overlap and interlock; no sky between rows; sky only above the highest peaks; several distinct spires (Liberty Bell–like), never a regular zig-zag.
- **Ground:** a gently curving plum band with an ink outline, under the front ridge.
- **Regenerate or make new ranges:** `python3 tools/mountains.py assets/` (change the seeds or peak lists for a new range in the same style).

### 5.2 The Venn (Three tables)
- Three circles: BD = Ascent Teal, IR = Meraki Magenta, Marketing = Blush; ~85% opacity, `multiply` blend, 6 px Ink Plum outlines.
- Labels in Fraunces 20 px; the icon sits in the triple overlap.

### 5.3 Arched photo frame
- Rounded arch top (full radius), 18–20 px bottom corners.
- 6 px Ink Plum border, plus a 2 px Meraki Magenta outline 8 px outside it.
- Used for Hannah's portrait and page-header photos.

### 5.4 Results row
- Three numbers in Fraunces 300, 76 px, centered, separated by thin plum dividers.
- Under each: what it measures, then the client name in Blush.
- Always add the source line ("from each client's Meta and Google Business Profile analytics").

### 5.5 Client banner
- Client names in Fraunces italic, 26 px, Deep Plum, separated by small dots (alternating magenta and teal).
- Scrolls slowly sideways (one loop ≈ 48 s), between hairlines on cream.

### 5.6 Buttons and links
- **Primary:** pill (fully rounded), Deep Plum fill, white Inter 600 caps; hover Deep Magenta.
- **On plum:** pill in Meraki Magenta or outline.
- **Text link:** Inter 600 caps with an arrow (→), magenta underline on hover.

---

## 6. Layout and spacing

- Max content width 1120–1280 px, centered; side gutters `clamp(16px, 4vw, 56px)`.
- Section padding 120–150 px top and bottom on desktop, ~80 px on phone.
- Two-column splits (text + Venn, text + photo) wrap to one column under ~900 px.
- Text never sits on top of the mountains. Mountains live in their own band below the words.

---

## 7. Motion

All motion is driven by scrolling and respects the "reduce motion" setting. Browsers without scroll-animation support simply show the finished state.

| Element | Behavior |
|---|---|
| Hero ridges | Screen holds while the 4 layers rise in turn (far first), each from 160–400 px below; ease `cubic-bezier(.2,.6,.3,1)` |
| Hero badge | Text ring spins slowly (40 s per turn); badge drifts up 70 px with the ridges |
| Headings and blocks | Rise 28–32 px and fade in as they enter the screen |
| Result numbers | Count up from 0 as they come into view |
| Ridgeline under results | Draws itself left to right |
| Venn | Circles slide in from left, right and below; the icon appears last |
| Client banner | Continuous slow sideways scroll |
| Inner-page headers | Ridges rise into place during the first ~420 px of scroll |

---

## 8. Page templates

**Home:** Hero (sky + rising ridges + badge) → Results (plum) → Three tables + Venn (cream) → Client banner → Founder (plum, arched photo) → FAQ (cream) → CTA (sky + ridges) → Footer.

**Inner page:** Header (sky, eyebrow, headline with italic turn, optional arched photo, ridges along the bottom) → content sections in the plum / cream / sky rhythm → CTA (sky + ridges) → Footer with ridge line.

Inner pages get this automatically by loading `/elevate.css` after `styles.css`:
```html
<link rel="stylesheet" href="/elevate.css?v=1">
```

---

## 9. Using the look beyond the website

| Format | How to apply it |
|---|---|
| Social posts and carousels | Mist Sky or Deep Plum ground; a ridge band along the bottom (crop `hero-range-*.svg`); Fraunces headline with an italic turn; one big number per slide |
| Slides | Title slides use sky + ridges; content slides on cream; data slides on plum with Fraunces 300 numbers |
| Email / signatures | Icon + plum wordmark; Inter body; magenta for links only |
| Proposals and reports | Cream pages; plum headings; arched photo frame for portraits; Venn for the three services |
| Print | Same palette; keep the Ink Plum linework thick enough to hold up at small sizes (≥ 1 pt) |

---

## 10. Don'ts

- Don't fill large areas with Ascent Teal behind mountains. It was tested and read as too busy.
- Don't draw mountains as flat triangles or blocks of color.
- Don't let mountains or badges overlap text.
- Don't use more than one italic phrase per headline.
- Don't use stock photos of people, emoji, or gradients as backgrounds.
- Don't publish a number without its source.

---

## Files

| File | What it is |
|---|---|
| `styles.css` | Base site styles (nav, footer, components) |
| `elevate.css` | Shared layer that gives inner pages the home-page look |
| `index.html` | Home page; its `<style>` block holds the hero, Venn and motion code |
| `assets/hero-range-0…3.svg` | The four ridge layers |
| `assets/logo-icon-moon.png` | Icon with white moon, for colored grounds |
| `assets/share-card.jpg` | Link-preview card |
| `assets/apple-touch-icon.png` | iPhone home-screen icon |
| `tools/mountains.py` | Generator for the ridge artwork |
| `docs/CHANGELOG-2026-11-website-redesign.md` | What changed on November 12, 2026 |
