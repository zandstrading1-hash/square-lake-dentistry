"""
buildlib.py — shared chrome + helpers for Square Lake Family Dentistry.
Generates static HTML pages that share the homepage's header/footer/design.
Output is plain HTML (no runtime dependency) suitable for GitHub Pages.
"""
import json
import os

SITE = "https://www.squarelakefamilydentistry.com"
PHONE_DISPLAY = "(248) 558\u20112785"
PHONE_TEL = "+12485582785"

# Nav: (label, href, key)
NAV = [
    ("Services", "services.html", "services"),
    ("New patients", "new-patients.html", "newpatients"),
    ("Insurance", "insurance.html", "insurance"),
    ("Reviews", "reviews.html", "reviews"),
    ("About", "about.html", "about"),
    ("Contact", "contact.html", "contact"),
]

# Service pages for footer + related lookups: (slug, name, blurb)
SERVICES = [
    ("general-dentistry.html", "General &amp; preventive", "Cleanings, exams, X\u2011rays and early detection."),
    ("childrens-dentistry.html", "Children's dentistry", "Gentle, friendly care from the very first visit."),
    ("emergency-dentistry.html", "Emergency dentistry", "Same\u2011day relief for pain, swelling and breaks."),
    ("cosmetic-dentistry.html", "Cosmetic dentistry", "Whitening, veneers and Invisalign."),
    ("restorative-dentistry.html", "Restorative dentistry", "Fillings, crowns and bridges that last."),
    ("dental-implants.html", "Dental implants", "Permanent, natural\u2011feeling tooth replacement."),
    ("dentures.html", "Dentures &amp; repairs", "Comfortable dentures and fast repairs."),
    ("gum-disease-treatment.html", "Gum disease care", "Protect the foundation of your smile."),
]

BRAND_MARK = ('<svg viewBox="0 0 40 40" width="40" height="40"><circle cx="20" cy="20" r="20" fill="#0C3B36"/>'
              '<path d="M8 27c0-9 5.5-15 12-15s12 6 12 15" fill="none" stroke="#E2A03F" stroke-width="3.5" '
              'stroke-linecap="round"/><circle cx="20" cy="27" r="1.8" fill="#E9F2F0"/></svg>')
BRAND_MARK_FOOT = ('<svg viewBox="0 0 40 40" width="36" height="36"><circle cx="20" cy="20" r="20" fill="#0A322E"/>'
                   '<path d="M8 27c0-9 5.5-15 12-15s12 6 12 15" fill="none" stroke="#E2A03F" stroke-width="3.5" '
                   'stroke-linecap="round"/></svg>')
PHONE_ICON = ('<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M6.6 10.8a15 15 0 0 0 '
              '6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.2.4 2.4.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6'
              '.4-1 1-1h3.4c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.4 0 .8-.3 1z" fill="currentColor"/></svg>')


def cta_btn(label="Call to book", primary=True, lg=False):
    cls = "btn " + ("btn--primary" if primary else "btn--ghost") + (" btn--lg" if lg else "")
    return f'<a class="{cls}" href="tel:{PHONE_TEL}">{PHONE_ICON}{label}</a>'


def cta_band(title, sub):
    return f'''<section class="cta-band">
    <div class="wrap">
      <h2 class="reveal">{title}</h2>
      <p class="reveal">{sub}</p>
      <div class="cta-band__row reveal">
        {cta_btn("Call to book your visit", True, True)}
        <a class="btn btn--ghost btn--lg" href="contact.html" style="background:rgba(255,255,255,.08);color:#fff;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.35)">Visit &amp; hours</a>
      </div>
      <a class="cta-band__phone reveal" href="tel:{PHONE_TEL}">{PHONE_ICON}{PHONE_DISPLAY}</a>
    </div>
  </section>'''


def related(exclude_slugs, n=3):
    cards = []
    for slug, name, blurb in SERVICES:
        if slug in exclude_slugs:
            continue
        cards.append(f'<a class="related-card" href="{slug}"><h3>{name}</h3><p>{blurb}</p></a>')
        if len(cards) >= n:
            break
    return ('<section class="section section--mist"><div class="wrap">'
            '<header class="section__head reveal"><p class="eyebrow">Keep exploring</p>'
            '<h2 class="section__title">Related care</h2></header>'
            f'<div class="related-grid reveal">{"".join(cards)}</div></div></section>')


def _head(title, description, slug, crumbs, schema_extra):
    canonical = f"{SITE}/{slug}"
    # Breadcrumb schema
    schema_blocks = ""
    if crumbs:
        items = []
        for i, (name, href) in enumerate(crumbs, start=1):
            entry = {"@type": "ListItem", "position": i, "name": name}
            if href:
                entry["item"] = f"{SITE}/{href}"
            items.append(entry)
        bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}
        schema_blocks += '<script type="application/ld+json">' + json.dumps(bc) + '</script>\n'
    if schema_extra:
        schema_blocks += '<script type="application/ld+json">' + json.dumps(schema_extra) + '</script>\n'

    fav = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'>"
           "<rect width='32' height='32' rx='8' fill='%230C3B36'/><path d='M6 22c0-7 4.5-12 10-12s10 5 10 12' "
           "fill='none' stroke='%23E2A03F' stroke-width='3' stroke-linecap='round'/></svg>")
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{description}" />
<meta name="theme-color" content="#0C3B36" />
<link rel="canonical" href="{canonical}" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{description}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:locale" content="en_US" />
<link rel="icon" href="{fav}" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600;12..96,700;12..96,800&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="styles.css" />
{schema_blocks}</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>'''


def _header(active):
    links = ""
    for label, href, key in NAV:
        links += f'<a href="{href}">{label}</a>'
    return f'''
<div class="util" id="top">
  <div class="wrap util__row">
    <span class="util__item">\U0001F4CD 6053 Rochester Rd, Troy, MI 48085</span>
    <span class="util__sep" aria-hidden="true">\u2022</span>
    <span class="util__item">Mon\u2013Thu 8\u20135 \u00b7 Fri 8\u20131</span>
    <span class="util__item util__item--push">Welcoming new patients of all ages</span>
  </div>
</div>
<header class="site-header" id="siteHeader">
  <div class="wrap header__row">
    <a class="brand" href="index.html" aria-label="Square Lake Family Dentistry \u2014 home">
      <span class="brand__mark" aria-hidden="true">{BRAND_MARK}</span>
      <span class="brand__text"><span class="brand__name">Square Lake</span><span class="brand__sub">Family Dentistry</span></span>
    </a>
    <nav class="nav" id="primaryNav" aria-label="Primary">{links}</nav>
    <div class="header__actions">
      <a class="tel" href="tel:{PHONE_TEL}">{PHONE_ICON}<span>{PHONE_DISPLAY}</span></a>
      <a class="btn btn--primary header__cta" href="tel:{PHONE_TEL}">Call to book</a>
      <button class="hamburger" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="primaryNav"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<main id="main">'''


def _banner(b):
    crumb_html = ""
    if b.get("crumbs"):
        parts = []
        for name, href in b["crumbs"]:
            if href:
                parts.append(f'<a href="{href}">{name}</a>')
            else:
                parts.append(f'<b>{name}</b>')
        crumb_html = '<nav class="breadcrumb" aria-label="Breadcrumb">' + '<span>/</span>'.join(parts) + '</nav>'
    cta = ""
    if b.get("cta", True):
        cta = f'<div class="banner__cta">{cta_btn("Call to book", True)}<a class="btn btn--ghost" href="services.html" style="background:rgba(255,255,255,.08);color:#fff;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.3)">View all services</a></div>'
    lead = f'<p class="banner__lead">{b["lead"]}</p>' if b.get("lead") else ""
    return f'''<section class="banner"><div class="wrap"><div class="banner__inner reveal">
    {crumb_html}
    <p class="eyebrow">{b.get("eyebrow","")}</p>
    <h1>{b["h1"]}</h1>
    {lead}
    {cta}
  </div></div></section>'''


def _footer():
    svc_links = "".join(f'<a href="{slug}">{name}</a>' for slug, name, _ in SERVICES)
    return f'''</main>
<footer class="footer">
  <div class="wrap footer__grid">
    <div class="footer__brand">
      <span class="brand brand--footer">
        <span class="brand__mark" aria-hidden="true">{BRAND_MARK_FOOT}</span>
        <span class="brand__text"><span class="brand__name">Square Lake</span><span class="brand__sub">Family Dentistry</span></span>
      </span>
      <p class="footer__tag">A family\u2011owned dental home in Troy, Michigan \u2014 comprehensive, comfortable care for every age.</p>
      <div class="footer__social">
        <a href="https://www.facebook.com/SquareLakeFam/" target="_blank" rel="noopener">Facebook</a>
        <a href="https://www.instagram.com/dentist9983__dr._saif_hanna/" target="_blank" rel="noopener">Instagram</a>
      </div>
    </div>
    <div class="footer__col">
      <h4>Care</h4>
      {svc_links}
    </div>
    <div class="footer__col">
      <h4>Practice</h4>
      <a href="about.html">About us</a>
      <a href="new-patients.html">New patients</a>
      <a href="insurance.html">Insurance &amp; financing</a>
      <a href="reviews.html">Reviews</a>
      <a href="faq.html">FAQs</a>
      <a href="blog.html">Blog</a>
    </div>
    <div class="footer__col footer__col--wide">
      <h4>Visit</h4>
      <a href="https://www.google.com/maps?q=6053+Rochester+Rd,+Troy,+MI+48085" target="_blank" rel="noopener">6053 Rochester Rd<br />Troy, MI 48085</a>
      <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
      <span class="footer__hours">Mon\u2013Thu 8\u20135 \u00b7 Fri 8\u20131<br />Sat\u2013Sun Closed</span>
      <p class="footer__cities" style="margin-top:14px">Serving Troy, Rochester Hills, Sterling Heights, Shelby Township, Utica, Clawson, Royal Oak, Madison Heights, Auburn Hills &amp; nearby.</p>
    </div>
  </div>
  <div class="wrap footer__bar">
    <span>\u00a9 <span id="year">2026</span> Square Lake Family Dentistry. All rights reserved.</span>
    <span>New patients of all ages welcome.</span>
  </div>
</footer>
<a class="mobile-call" href="tel:{PHONE_TEL}" aria-label="Call Square Lake Family Dentistry">{PHONE_ICON}</a>
<script src="script.js"></script>
</body>
</html>'''


def render(page):
    """page: dict with slug, title, description, active, banner, body, optional schema_extra, cta_title, cta_sub."""
    crumbs = page.get("banner", {}).get("crumbs")
    html = _head(page["title"], page["description"], page["slug"], crumbs, page.get("schema_extra"))
    html += _header(page.get("active", ""))
    if page.get("banner"):
        html += _banner(page["banner"])
    html += page["body"]
    if page.get("cta", True):
        html += cta_band(page.get("cta_title", "Ready when you are."),
                         page.get("cta_sub", "Call our Troy office to book your visit \u2014 new patients of all ages are always welcome."))
    html += _footer()
    return html


def write_all(pages, outdir="."):
    for p in pages:
        path = os.path.join(outdir, p["slug"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(p))
        print("wrote", p["slug"])
