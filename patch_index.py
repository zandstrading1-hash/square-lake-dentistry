"""patch_index.py — bring the hand-authored homepage in line with the new multi-page site."""
import re
from buildlib import _header, _footer, PHONE_ICON, PHONE_TEL, PHONE_DISPLAY

html = open("index.html", encoding="utf-8").read()

# 1) Swap header (util strip -> opening <main>) for the canonical shared header
header_new = _header("home").lstrip("\n")
html, n1 = re.subn(r'<div class="util" id="top">.*?<main id="main">',
                   lambda m: header_new, html, count=1, flags=re.S)

# 2) Replace the appointment-form contact section with a phone-forward "Visit us" section
new_section = '''  <!-- Visit / Call to book -->
  <section class="section" id="contact">
    <div class="wrap">
      <header class="section__head reveal">
        <p class="eyebrow">Visit us</p>
        <h2 class="section__title">Call to book your visit</h2>
        <p class="section__intro">We schedule by phone so we can find the right time for you \u2014 new patients of all ages are always welcome.</p>
      </header>
      <div class="contact__grid">
        <div class="contact__info reveal">
          <div class="contact__block">
            <h3>Call or text</h3>
            <p><a class="contact__phone" href="tel:%TEL%">%DISP%</a></p>
            <a class="btn btn--primary" href="tel:%TEL%" style="margin-top:10px">%ICON%Call to book</a>
          </div>
          <div class="contact__block">
            <h3>Find us</h3>
            <p><a href="https://www.google.com/maps?q=6053+Rochester+Rd,+Troy,+MI+48085" target="_blank" rel="noopener">6053 Rochester Rd<br />Troy, MI 48085</a></p>
          </div>
          <div class="contact__block">
            <h3>Office hours</h3>
            <table class="hours">
              <tr><th>Mon \u2013 Thu</th><td>8:00 AM \u2013 5:00 PM</td></tr>
              <tr><th>Friday</th><td>8:00 AM \u2013 1:00 PM</td></tr>
              <tr><th>Sat \u2013 Sun</th><td>Closed</td></tr>
            </table>
          </div>
        </div>
        <div class="contact__map reveal">
          <iframe title="Map to Square Lake Family Dentistry" src="https://www.google.com/maps?q=6053+Rochester+Rd,+Troy,+MI+48085&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>
      <div class="section__cta reveal">
        <a class="btn btn--ghost" href="contact.html">Contact &amp; directions \u2192</a>
      </div>
    </div>
  </section>
'''
new_section = (new_section.replace("%TEL%", PHONE_TEL)
               .replace("%DISP%", PHONE_DISPLAY).replace("%ICON%", PHONE_ICON))
html, n2 = re.subn(r'  <!-- Contact / location -->.*?</section>\s*</main>',
                   lambda m: new_section + "</main>", html, count=1, flags=re.S)

# 3) Convert every remaining CTA to call-to-book
html = html.replace('href="#contact"', f'href="tel:{PHONE_TEL}"')
html = html.replace("Request an appointment", "Call to book").replace("Request appointment", "Call to book")

# 4) Swap footer (closing </main> -> </html>) for the canonical shared footer
footer_new = _footer()
html, n4 = re.subn(r'</main>.*</html>', lambda m: footer_new, html, count=1, flags=re.S)

assert n1 == 1, f"header swap matched {n1}"
assert n2 == 1, f"contact section swap matched {n2}"
assert n4 == 1, f"footer swap matched {n4}"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("index.html patched OK")
