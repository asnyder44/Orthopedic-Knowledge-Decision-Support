> Reference copy for the okds repo (copied 2026-11-01): the UI style the portal uses.

# Design 21: Clinic Blue

Based on your Orthopedics Hub site: navy and medical blue, serif headings, calm pale-blue sections.

- **Tone:** Light-mid + night mode
- **Layout:** One scrolling page: sticky header, gradient hero with search, tile grid, tabbed explorer, chat card
- **Based on:** https://ortho-knowledge-and-decision-support.netlify.app/
- **Picture:** [`21-clinic-blue.jpg`](21-clinic-blue.jpg) shows the design.

## Look and feel
- Trustworthy and clinical, like a good hospital or health-education site.
- Based on your Orthopedics Hub site, with softer backgrounds (blue-gray instead of pure white) and a few modern touches.

## Colors
| Token | Value | Use |
|---|---|---|
| `bg` | `#f1f5f9` | Page background |
| `surface` | `#fbfcfe` | Cards and panels |
| `surface2` | `#e7eff8` | Inputs, table headers, subtle fills |
| `line` | `#d3e0ee` | Borders and dividers |
| `ink` | `#12263f` | Main text |
| `muted` | `#4d6179` | Secondary text |
| `accent` | `#0b5cad` | Primary buttons, active nav |
| `accentText` | `#0a4f96` | Accent used as text or links |
| `accentInk` | `#ffffff` | Text on accent fills |
| `accentSoft` | `#dcebfa` | Selected and highlighted fills |
| `accent2` | `#0a3d73` | Second accent (glows, gradients) |
| `ok` | `#1f7a4f` | Success |
| `warn` | `#8a5a00` | Warning |
| `bad` | `#b2382c` | Error |

**Night mode:**

| Token | Value | Use |
|---|---|---|
| `bg` | `#132235` | Page background |
| `surface` | `#182b42` | Cards and panels |
| `surface2` | `#1e3550` | Inputs, table headers, subtle fills |
| `line` | `#2a4462` | Borders and dividers |
| `ink` | `#e6eef8` | Main text |
| `muted` | `#a9bdd3` | Secondary text |
| `accent` | `#5aa9f2` | Primary buttons, active nav |
| `accentText` | `#8cc4f7` | Accent used as text or links |
| `accentInk` | `#0b1624` | Text on accent fills |
| `accentSoft` | `#1f4166` | Selected and highlighted fills |
| `accent2` | `#9ccbf7` | Second accent (glows, gradients) |
| `ok` | `#6fd3a0` | Success |
| `warn` | `#f0c56a` | Warning |
| `bad` | `#f59b92` | Error |

Text colors on their backgrounds pass WCAG AA (4.5:1).

## Type
- **Headings:** Georgia, "Times New Roman", serif
- **Body:** "Segoe UI", system-ui, -apple-system, Helvetica, Arial, sans-serif, 15px, line height 1.55
- **Mono (IDs, numbers, code):** ui-monospace, "SF Mono", Menlo, Consolas, monospace
- **Sizes:** page title about 2rem, section title 1.1–1.4rem, body 15px, small text 0.85rem
- Use system fonts only. No web-font downloads, so pages work offline.

## Shape and depth
- **Corner radius:** 14px on cards, about 60% of that on buttons and inputs, full pills on chips
- White-ish cards with 1px pale-blue borders, a 14–18px radius, and soft navy shadows. Sections alternate between the page background and a pale blue band.

## Layout and navigation
One long scrolling page. A sticky header holds the logo (white bone on a blue rounded square), anchor links (Specialties, Explore, OrthoBot, Sources), a night-mode button, and a Style button. The active section gets a pale fill and a blue underline, and the header gains a shadow when you scroll.

## Signature effects
- Hero: navy-to-blue gradient with a faint medical-cross pattern and a slow light sweep. An x-ray card shows a line-art knee with a moving scan line, a pulsing "joint space" marker, and two floating badges.
- Live search suggestions with highlighted matches; arrow keys and Enter work.
- Sections fade up as you scroll; stats count up; night mode uses the site’s own dark palette, softened.
- Respect "reduce motion": turn animations off when the user asks for it.

## Components
- Georgia serif headings over a Segoe UI / system body at 16px, line height 1.65.
- Subspecialty tiles: icon in a pale-blue square that turns solid blue on hover; the tile lifts and an arrow appears.
- Explorer panel: illustration strip, underline tabs, and +/× accordions. Evidence rows show 3-step strength bars plus a labeled chip (Strong / Moderate / Limited).
- Footer in deep navy `#0a3d73`.
- Shared parts in every design: page header (eyebrow, title, one-line lead), stat tiles, cards, chips for status, tables, a chat with numbered citation chips like [1], and a source list.
- Status always uses an icon or a word as well as color (e.g. ✓ pass, ⚠ warning).

## For a Streamlit app
Colors, Georgia headings, and the radius carry over to Streamlit. The hero and x-ray card need custom HTML.

## CSS variables
```css
:root {
  --bg: #f1f5f9;
  --surface: #fbfcfe;
  --surface2: #e7eff8;
  --line: #d3e0ee;
  --ink: #12263f;
  --muted: #4d6179;
  --accent: #0b5cad;
  --accentText: #0a4f96;
  --accentInk: #ffffff;
  --accentSoft: #dcebfa;
  --accent2: #0a3d73;
  --ok: #1f7a4f;
  --warn: #8a5a00;
  --bad: #b2382c;
  --radius: 14px;
  --font: "Segoe UI", system-ui, -apple-system, Helvetica, Arial, sans-serif;
  --font-head: Georgia, "Times New Roman", serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}
```
