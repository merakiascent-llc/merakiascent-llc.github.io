# Albums Feature Addendum · Photography Page Enhancement

## Instructions for Claude Code

This addendum extends the Photography page (`/portfolio-photography.html`) and CMS framework you've built. The goal is to add an "Album" content type that lets the site owner group photos by event, project, or shoot, while preserving the existing category-based masonry gallery.

The masonry gallery with filter pills stays as the primary view. A new "Browse by Album" section is added to the page. Each album has its own shareable URL.

---

# 1. CMS Configuration Update

Add a new content collection to `/admin/config.yml`:

```yaml
  # ===== ALBUMS =====
  - name: "albums"
    label: "Photo Albums"
    label_singular: "Album"
    folder: "_content/albums"
    create: true
    slug: "{{slug}}"
    fields:
      - {label: "Album Title", name: "title", widget: "string", hint: "Short title shown on cards and album page. E.g. 'Methow Spring 2026' or 'Loup Loup Opening Day'."}
      - {label: "Slug", name: "slug", widget: "string", hint: "URL slug, lowercase with hyphens. E.g. 'methow-spring-2026'. This becomes the URL: /portfolio-photography/[slug]"}
      - {label: "Event or Location", name: "event", widget: "string", required: false, hint: "Optional. E.g. 'Methow Valley, WA' or 'Loup Loup Ski Bowl'."}
      - {label: "Date or Date Range", name: "date_range", widget: "string", hint: "Free-form text. E.g. 'March 2026' or 'May 15-17, 2026'."}
      - {label: "Sort Date", name: "sort_date", widget: "datetime", format: "YYYY-MM-DD", time_format: false, hint: "Used internally to order albums (most recent first). Use the start date of the shoot."}
      - {label: "Cover Photo", name: "cover_image", widget: "image", hint: "The album's hero image. Used on the album card and at the top of the album page."}
      - {label: "Optional Intro", name: "intro", widget: "text", required: false, hint: "Optional short paragraph (2-4 sentences) telling the story behind the album. Shown above the photo grid on the album page."}
      - {label: "Featured on Photography Page", name: "featured", widget: "boolean", default: true, hint: "Show this album in the 'Browse by Album' section on the main Photography page. Uncheck to hide it (album page URL still works, just not promoted)."}
      - {label: "Display Order", name: "order", widget: "number", default: 100, hint: "Lower numbers appear first in the 'Browse by Album' section. Leave at 100 to sort by date."}
```

## Update the existing Photos collection

Add an optional `album` field to each photo so a photo can be associated with an album:

In the existing `photos` collection in `/admin/config.yml`, add this field before the `Display Order` field:

```yaml
      - label: "Album"
        name: "album"
        widget: "relation"
        collection: "albums"
        search_fields: ["title"]
        value_field: "slug"
        display_fields: ["title"]
        required: false
        hint: "Optional. Tag this photo as part of an album. The photo will appear both in the main category grid AND on the album's dedicated page."
```

This widget gives Hannah a searchable dropdown of existing albums when she's editing a photo.

---

# 2. Build Script Update

Update `scripts/build-content.js` (or whatever the content build script is) to:

1. Read all files in `_content/albums/` and output `/data/albums.json` containing each album's metadata
2. For each album, also include an array `photos` containing all photos in `_content/photos/` whose `album` field matches this album's slug
3. The albums JSON should be sorted by `order` ascending, then by `sort_date` descending

Schema example for `albums.json`:

```json
[
  {
    "title": "Methow Spring 2026",
    "slug": "methow-spring-2026",
    "event": "Methow Valley, WA",
    "date_range": "March 2026",
    "sort_date": "2026-03-15",
    "cover_image": "/assets/uploads/methow-cover.jpg",
    "intro": "Three days of unexpected snow in March, light at golden hour that lasted forever, and the kind of quiet you only find in the off-season.",
    "featured": true,
    "order": 10,
    "photos": [
      {
        "image": "/assets/uploads/photo-001.jpg",
        "caption": "Sunrise over Goat Wall",
        "category": "landscapes",
        "featured": true,
        "date": "2026-03-14",
        "order": 10
      }
    ]
  }
]
```

---

# 3. Photography Page Update (`/portfolio-photography.html`)

Add a new section to the Photography page positioned **between the hero and the existing filter pills + masonry gallery**. So the new page order is:

1. Hero
2. **NEW: Browse by Album section**
3. **NEW: A small section divider with "BROWSE BY CATEGORY" eyebrow**
4. Filter pills (sticky)
5. Masonry gallery with lightbox

## Browse by Album section

**Section header:**
- Eyebrow: "Browse by Album"
- Headline: "Series, shoots, and stories." with "stories." in magenta italic
- One-sentence intro: "Bodies of work that belonged together. Click any cover to see the full set."

**Album cards:**

Fetch from `/data/albums.json`. Filter to only albums where `featured: true`. Sort by `order` ascending then `sort_date` descending. Render as a grid:

- Desktop: 3 columns
- Tablet: 2 columns
- Mobile: 1 column

Each album card:
- Cover image (aspect ratio 3:2, with subtle Deep Plum gradient overlay at the bottom for text legibility)
- Overlaid at the bottom of the cover image, in Warm Cream text:
  - Album title in italic Fraunces (1.3rem)
  - Below: date range + photo count in small Inter uppercase tracked (e.g., "MARCH 2026 · 24 PHOTOS")
- Hover state: image scales subtly (1.04x), Deep Plum overlay strengthens slightly, a magenta corner accent appears at top-right
- The entire card is a clickable link to the album page: `/portfolio-photography/[slug]/`

Below the album cards, a quiet line: a thin horizontal magenta rule (1px, 60% width centered) with the eyebrow "BROWSE BY CATEGORY" centered on top of it. This visually transitions into the category-based masonry section.

**Empty state:** If there are no featured albums, hide the entire "Browse by Album" section. Don't show an empty header.

## Photo album badges on the main masonry

For each photo in the main masonry gallery that belongs to an album, show a small badge on hover (desktop) or always-visible at the bottom of the photo (mobile):

- A tiny pill-shaped element in Soft Pink with Deep Plum text
- Text: the album title (e.g., "Methow Spring 2026")
- Clickable: goes to that album's page

This connects the two browsing modes. A user browsing landscapes can see "this photo is from the Methow Spring 2026 series" and jump to the full series.

---

# 4. New Album Page Template

Create a new page template at `/portfolio-photography/album.html` (or use whatever templating approach Claude Code chose). This is the template for individual album pages.

For each album in `/data/albums.json`, the build process should generate a static HTML page at `/portfolio-photography/[slug]/index.html`.

## Album page structure

**Nav:** Same shared nav as all other pages.

**Page header:**
- A breadcrumb in small Inter uppercase tracked: "Photography / [Album Title]" with the slash in magenta and "Photography" being a link back to `/portfolio-photography.html`
- Album title as the page H1 in italic Fraunces, large (clamp(2.5rem, 5vw, 4rem))
- Below the title: date range + event location in a quiet horizontal row, with bullet separator
  - Example: "MARCH 2026 · METHOW VALLEY, WA · 24 PHOTOS"

**Hero cover image (optional):**

Display the album's cover image as a large hero (max-height: 60vh, object-fit: cover) below the page header. This sets the visual tone of the album.

**Optional intro paragraph:**

If the album has an `intro` field, display it below the cover image:
- Max-width: 640px centered
- Italic Fraunces, 1.15rem
- Color: deep plum
- Padded vertically with generous breathing room

If no intro, skip this section entirely.

**Photo grid:**

The same masonry grid + lightbox system from the main Photography page, but showing ONLY photos in this album. Photos are sorted by `order` ascending, then `date` descending.

The lightbox should navigate only within the album's photos (arrow keys go between photos in this album, not across all photos site-wide).

**Bottom navigation:**

A horizontal row at the bottom of the page:
- Left: "← Back to all photography" link (magenta, with arrow)
- Right: If there are other featured albums, show "Next album: [Title] →" link (magenta) leading to the next album in sort order
- This creates a natural browsing path through your albums

**Sharing helper (subtle):**

A small text line in Inter uppercase tracked: "SHARE THIS ALBUM" with a small clipboard icon button next to it. Clicking copies the album's URL to clipboard and briefly shows a "Link copied" tooltip in Caveat script. This makes it dead simple for Hannah to share a specific album.

---

# 5. URL Structure Update

The Netlify config (`netlify.toml`) needs a redirect rule to handle pretty URLs for album pages:

```toml
[[redirects]]
  from = "/portfolio-photography/:slug/"
  to = "/portfolio-photography/album.html?slug=:slug"
  status = 200

[[redirects]]
  from = "/portfolio-photography/:slug"
  to = "/portfolio-photography/:slug/"
  status = 301
```

If Claude Code is using static page generation (creating `/portfolio-photography/methow-spring-2026/index.html` as actual files at build time), these redirects aren't needed. The build approach is preferred for SEO and performance.

---

# 6. Sitemap and SEO

Update any sitemap.xml generation logic to include each album's URL. Each album page should have:

- Unique `<title>` tag: `[Album Title] · Photography · Meraki Ascent`
- Meta description from the album's intro paragraph (or auto-generated from title + date if no intro)
- Open Graph image set to the album's cover image (so when shared on social, it shows the cover)

---

# 7. Initial Seed Albums

To validate the feature works without waiting for Hannah to populate real albums, create 2 seed album files:

**File: `_content/albums/methow-spring-2026.md`**

```yaml
---
title: "Methow Spring 2026"
slug: "methow-spring-2026"
event: "Methow Valley, WA"
date_range: "March 2026"
sort_date: 2026-03-15
cover_image: "/assets/uploads/album-placeholder-methow.jpg"
intro: "Three days of unexpected late-season snow in March, golden hour light that lasted forever, and the kind of quiet you only find in the off-season."
featured: true
order: 10
---
```

**File: `_content/albums/loup-loup-opening-day.md`**

```yaml
---
title: "Loup Loup Opening Day"
slug: "loup-loup-opening-day"
event: "Loup Loup Ski Bowl"
date_range: "December 2025"
sort_date: 2025-12-15
cover_image: "/assets/uploads/album-placeholder-louploup.jpg"
intro: "Opening day at the Loup. Lift line stories, first turns of the season, and the kids learning to send it on the lower mountain."
featured: true
order: 20
---
```

Generate placeholder cover images for these albums as 1200×800 colored blocks with the album title overlaid in italic Fraunces. Use these brand colors:
- `album-placeholder-methow.jpg`: Soft Pink (#E89BBE) gradient to Deep Plum
- `album-placeholder-louploup.jpg`: Sky Mist (#B8DDE4) gradient to Teal (#3CA0B4)

Then update 2-3 of the existing seed photos to belong to these albums (set their `album` field to the appropriate slug) so the album pages aren't empty.

---

# 8. After Population

After implementing the albums feature:

1. Run the build script and verify `/data/albums.json` is generated with the 2 seed albums
2. Open `/portfolio-photography.html` and verify the "Browse by Album" section appears between the hero and the category gallery, showing 2 album cards
3. Click an album card and verify it navigates to the album page (e.g. `/portfolio-photography/methow-spring-2026/`)
4. On the album page, verify:
   - Breadcrumb works (clicking "Photography" goes back to main photography page)
   - Title, date range, and event display correctly
   - Optional intro displays (or is hidden if not present)
   - Only photos belonging to this album appear in the grid
   - Lightbox only navigates within the album's photos
   - "Back to all photography" and "Next album" links work
   - The share-link button copies the URL to clipboard
5. Go back to the main Photography page and verify photos that belong to an album show the small album badge on hover
6. Click the album badge on a photo and verify it goes to the album page
7. Open the admin UI (`/admin`) and verify:
   - "Photo Albums" collection appears in the left sidebar
   - Creating a new album works
   - Editing a photo, the "Album" dropdown shows existing albums
   - The whole thing publishes correctly via the CMS

Report any issues, broken links, missing fields, or styling inconsistencies.
