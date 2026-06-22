# Square Lake Family Dentistry — Website

A fast, responsive, single‑page marketing site for **Square Lake Family Dentistry**, a family‑owned dental practice in Troy, MI (owner: **Dr. Saif Hanna**). Built as plain HTML/CSS/JS — no build step, no dependencies — so it deploys anywhere static, including GitHub Pages.

```
index.html      → the whole site (all sections + SEO/JSON-LD schema)
styles.css      → design system + components + responsive + accessibility
script.js       → mobile menu, scroll reveal, sticky header, form handling
404.html        → branded not-found page
```

---

## 🚀 Get a live preview (GitHub Pages) — ~2 minutes

I'm **not connected to GitHub** in this session, so I can't push for you. Here's the exact path to go live yourself. The repo is already initialized and committed, so you only need to point it at your GitHub and turn on Pages.

### 1. Create an empty repo on GitHub
Go to <https://github.com/new>, name it (e.g. `square-lake-dentistry`), leave it **empty** (no README/license), and create it.

### 2. Push this code to it
From inside this project folder:

```bash
git remote add origin https://github.com/YOUR-USERNAME/square-lake-dentistry.git
git branch -M main
git push -u origin main
```

### 3. Turn on GitHub Pages
In the repo: **Settings → Pages → Build and deployment**
- **Source:** Deploy from a branch
- **Branch:** `main`  •  **Folder:** `/ (root)` → **Save**

Your live URL appears within a minute or two:
```
https://YOUR-USERNAME.github.io/square-lake-dentistry/
```

> Prefer one‑click hosting? Drag this folder onto <https://app.netlify.com/drop> for an instant preview URL, or run `npx vercel` from the folder.

---

## ⚠️ Confirm before you publish for real

I used the details that **cross‑checked across the official site, Yelp, and Google**, and softened anything unverified. Please confirm these with Dr. Hanna before treating the site as final:

| Item | What's on the site now | Action |
|---|---|---|
| **Phone** | `(248) 558‑2785` | ✅ Matches official site + Yelp. Confirm this is the line to ring (Google also lists `(248) 879‑5858`). |
| **Hours** | Mon–Thu 8–5, Fri 8–1, Sat–Sun closed | ✅ Official site + Yelp agree. The old "Saturday availability" claim was **dropped** — re‑add only if true. |
| **Dr. Hanna's credential** | "Dentist" (no DDS/DMD shown) | Listings disagree (DDS vs DMD). Add the correct post‑nominal to the bio. |
| **Other providers** | Only Dr. Hanna featured | If any associate dentists/hygienists should appear, send names + (optional) photos. |
| **Promotional offers** | Soft wording: "ask about specials" | The old "FREE Zoom whitening / free X‑rays" offers are **not hardcoded**. Confirm exact current offers before adding them. |
| **Photos** | Brand arch graphic + "SH" monogram placeholder | Drop in real office/team photos and a headshot of Dr. Hanna (see swap notes below). |
| **Booking** | Form is a front‑end demo (shows a thank‑you, doesn't send) | Wire it up — see below. |
| **Insurance** | "We accept many major plans" + logo chips | Phrased safely (no in‑network claims). Confirm the exact list. |

---

## 🔧 Easy edits

**Phone number** — it appears as `tel:+12485582785` and as display text `(248) 558‑2785`. Find/replace both if it changes.

**Add Dr. Hanna's photo** — in `index.html`, find the `team__frame` block and replace the monogram with an image:
```html
<div class="team__frame">
  <img src="dr-hanna.jpg" alt="Dr. Saif Hanna" style="width:100%;height:100%;object-fit:cover;border-radius:inherit;">
</div>
```

**Make the form actually send** — it's intentionally inert right now. Two simple options:
- **Formspree:** create a form, then set `<form ... action="https://formspree.io/f/XXXX" method="POST">` and remove the `e.preventDefault()` demo handler in `script.js`.
- **mailto fallback:** point the form at `action="mailto:office@yourdomain.com"`.

**Colors** live as CSS variables at the top of `styles.css` (`--pine`, `--honey`, `--brick`, etc.).

---

## 📈 What's already built in

- **SEO:** title/meta/Open Graph, semantic headings, and `Dentist` + `FAQPage` **JSON‑LD** structured data (address, phone, hours, 4.7★/109 rating, service area, services) for rich local results.
- **Accessibility:** skip link, visible keyboard focus, labeled controls, `prefers-reduced-motion` support, responsive down to small phones.
- **Performance:** no frameworks, system + Google fonts only, lazy‑loaded map.

## 🗺️ Suggested next steps
Break the single page into dedicated, individually‑ranking pages (one per service + per nearby city), add a blog, and connect Google Business Profile — the content map for all of that is in the knowledge base this was built from.

---
*Built from the project knowledge base. Treat the "Confirm before you publish" table as a go‑live checklist.*
