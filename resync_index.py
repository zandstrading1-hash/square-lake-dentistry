"""resync_index.py — re-apply the shared header/footer to the hand-authored homepage.

Safe to run repeatedly. Use after changing the header or footer in buildlib.py so
index.html stays in sync with the generated pages.
"""
import re
from buildlib import _header, _footer

html = open("index.html", encoding="utf-8").read()

html, n1 = re.subn(r'<div class="util" id="top">.*?<main id="main">',
                   lambda m: _header("home").lstrip("\n"), html, count=1, flags=re.S)
html, n2 = re.subn(r'</main>.*</html>', lambda m: _footer(), html, count=1, flags=re.S)

# Accessibility: row-header scope on the homepage hours table
html = html.replace('<th>Mon \u2013 Thu</th>', '<th scope="row">Mon \u2013 Thu</th>')
html = html.replace('<th>Friday</th>', '<th scope="row">Friday</th>')
html = html.replace('<th>Sat \u2013 Sun</th>', '<th scope="row">Sat \u2013 Sun</th>')

assert n1 == 1, f"header resync matched {n1}"
assert n2 == 1, f"footer resync matched {n2}"

open("index.html", "w", encoding="utf-8").write(html)
print("resynced index.html header/footer + table scope")
