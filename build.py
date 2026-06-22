"""
build.py — generate all inner pages for Square Lake Family Dentistry.

Run from the project folder:  python3 build.py
Outputs static .html files (plus sitemap.xml, robots.txt) next to index.html.
index.html is hand-authored and intentionally NOT generated here.
"""
from buildlib import write_all, SITE
import content_core
import content_services
import content_blog

ALL_PAGES = content_core.PAGES + content_services.PAGES + content_blog.PAGES


def write_sitemap():
    urls = ["index.html"] + [p["slug"] for p in ALL_PAGES]
    items = "\n".join(
        f"  <url><loc>{SITE}/{u}</loc><changefreq>monthly</changefreq></url>" for u in urls
    )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{items}\n</urlset>\n")
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml)
    print("wrote sitemap.xml")


def write_robots():
    txt = f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n"
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(txt)
    print("wrote robots.txt")


if __name__ == "__main__":
    write_all(ALL_PAGES, outdir=".")
    write_sitemap()
    write_robots()
    print(f"\nDone: {len(ALL_PAGES)} generated pages + index.html")
