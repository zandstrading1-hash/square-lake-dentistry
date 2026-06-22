"""content_blog.py — blog index + 3 starter posts."""
from buildlib import PHONE_TEL, PHONE_DISPLAY

ICON_BOLT = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h6l-1 8 9-12h-6z"/></svg>'
ICON_KIDS = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="7" r="2.4"/><circle cx="16" cy="8.5" r="1.8"/><path d="M4.5 19c0-2.8 2-4.8 4.5-4.8s4.5 2 4.5 4.8"/><path d="M14 19c.1-2.2 1.4-3.6 3.2-3.6 1.8 0 3 1.4 3.1 3.6"/></svg>'
ICON_TOOTH = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3c2 0 3 1.2 4.6 1.2C18.4 4.2 20 5.6 20 8.4c0 2.4-.9 4.2-1.6 7.2-.6 2.6-.8 5-2.2 5-1.6 0-1-3.8-2.2-3.8s-.7 3.8-2.2 3.8c-1.4 0-1.6-2.4-2.2-5C6.7 12.6 5.8 10.8 5.8 8.4 5.8 5.6 7.4 4.2 9.2 4.2 10.8 4.2 11 3 12 3Z"/></svg>'

# Published posts (have pages)
POSTS = [
    dict(slug="blog-tooth-pain-emergency.html", icon=ICON_BOLT, category="Emergency", date="June 2026",
         title="How to Know If Tooth Pain Is a Dental Emergency",
         excerpt="Not every ache means a trip to the dentist today \u2014 but some signs shouldn't wait. Here's how to tell the difference."),
    dict(slug="blog-childs-first-visit.html", icon=ICON_KIDS, category="Children", date="June 2026",
         title="When Should Children First Visit the Dentist?",
         excerpt="Earlier than most parents expect. Here's the simple rule of thumb, and how to make that first visit a happy one."),
    dict(slug="blog-dentures-vs-implants.html", icon=ICON_TOOTH, category="Restorative", date="June 2026",
         title="Dentures vs. Dental Implants: Which Is Right for You?",
         excerpt="Both replace missing teeth beautifully. We break down the real differences in cost, comfort and care."),
]

# Topics planned but not yet written (shown as "coming soon", no link)
SOON = [
    "5 Signs You May Have a Cavity",
    "Why Cleanings Matter Even If You Brush Daily",
    "Teeth Whitening: What Works and What to Avoid",
]


def _post_card(p):
    return (f'<a class="post-card" href="{p["slug"]}">'
            f'<div class="post-card__cover">{p["icon"]}</div>'
            f'<div class="post-card__body"><span class="post-meta">{p["category"]} \u00b7 {p["date"]}</span>'
            f'<h3>{p["title"]}</h3><p>{p["excerpt"]}</p><span class="more">Read article \u2192</span></div></a>')


def _soon_card(title):
    return (f'<div class="post-card soon"><div class="post-card__cover">{ICON_TOOTH}</div>'
            f'<div class="post-card__body"><span class="post-meta">Coming soon</span>'
            f'<h3>{title}</h3><p>We\u2019re working on this one \u2014 check back shortly.</p></div></div>')


def _article(slug, category, date, title, lead, html_body):
    banner = dict(eyebrow=f"{category} \u00b7 {date}", h1=title, lead=lead,
                  crumbs=[("Home", "index.html"), ("Blog", "blog.html"), (category, None)], cta=False)
    body = (f'<section class="section"><div class="wrap"><article class="article prose reveal">{html_body}'
            f'<div class="article-foot"><p style="color:var(--ink-soft);font-size:.92rem">'
            f'This article is general information, not medical advice. For guidance about your specific situation, '
            f'please call our Troy office at <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>'
            f'<p style="margin-top:14px"><a href="blog.html">\u2190 Back to all articles</a></p></div>'
            f'</article></div></section>')
    return dict(slug=slug, active="", title=f"{title} | Square Lake Family Dentistry",
                description=lead, banner=banner, body=body)


PAGES = [
    # Blog index
    dict(slug="blog.html", active="",
         title="Dental Health Blog | Square Lake Family Dentistry | Troy, MI",
         description="Practical dental health tips from Square Lake Family Dentistry in Troy, MI \u2014 emergencies, kids\u2019 dentistry, whitening, implants and everyday oral care.",
         cta_title="Have a question we haven't covered?",
         cta_sub="Our team is happy to help \u2014 give our Troy office a call.",
         banner=dict(eyebrow="Dental health blog", h1="Tips for healthier smiles",
                     lead="Straightforward advice from our team to help your family take great care of your teeth between visits.",
                     crumbs=[("Home", "index.html"), ("Blog", None)]),
         body=('<section class="section"><div class="wrap"><div class="blog-grid reveal">'
               + "".join(_post_card(p) for p in POSTS)
               + "".join(_soon_card(t) for t in SOON)
               + '</div></div></section>')),

    # Post 1
    _article("blog-tooth-pain-emergency.html", "Emergency", "June 2026",
             "How to Know If Tooth Pain Is a Dental Emergency",
             "Not every ache means a trip to the dentist today \u2014 but some signs shouldn\u2019t wait. Here\u2019s how to tell the difference.",
             '''
<p class="lede">Tooth pain has a way of making everything feel urgent. The good news: many toothaches can wait a day or two for a regular appointment. The important part is knowing which ones can\u2019t.</p>
<h2>Signs you should be seen right away</h2>
<p>Call a dentist promptly \u2014 the same day if you can \u2014 if you notice any of these:</p>
<ul>
  <li><strong>Severe or persistent pain</strong> that over-the-counter relief isn\u2019t controlling.</li>
  <li><strong>Swelling</strong> in your gums, jaw or face, which can signal an infection.</li>
  <li><strong>A knocked-out tooth.</strong> Time matters most here \u2014 ideally within an hour.</li>
  <li><strong>A broken tooth</strong> that\u2019s painful, sharp, or bleeding.</li>
  <li><strong>Fever along with a toothache,</strong> which may point to an abscess.</li>
</ul>
<blockquote>If swelling is making it hard to breathe or swallow, don\u2019t wait for a dental visit \u2014 seek emergency medical care immediately.</blockquote>
<h2>What can usually wait (but still needs attention)</h2>
<p>Some issues are uncomfortable but not emergencies. Mild sensitivity to hot or cold, a dull ache that comes and goes, or mild food-trapping between teeth can typically wait for a scheduled visit. Don\u2019t ignore them, though \u2014 small problems tend to grow.</p>
<h2>What to do until you\u2019re seen</h2>
<p>Rinse gently with warm salt water, floss carefully to remove any trapped food, and use a cold compress on the outside of your cheek to ease swelling. Avoid placing aspirin directly against the gum, which can irritate the tissue.</p>
<h2>When in doubt, call</h2>
<p>If you\u2019re not sure how serious your situation is, it\u2019s always okay to call and ask. We keep room in our schedule for urgent visits and offer same-day appointments when available. Learn more on our <a href="emergency-dentistry.html">emergency dentistry</a> page.</p>
'''),

    # Post 2
    _article("blog-childs-first-visit.html", "Children", "June 2026",
             "When Should Children First Visit the Dentist?",
             "Earlier than most parents expect. Here\u2019s the simple rule of thumb, and how to make that first visit a happy one.",
             '''
<p class="lede">It\u2019s one of the most common questions new parents ask \u2014 and the answer surprises a lot of people: your child should see a dentist earlier than you might think.</p>
<h2>The simple rule of thumb</h2>
<p>Most dentists recommend a first visit by your child\u2019s <strong>first birthday</strong>, or within six months of their first tooth appearing \u2014 whichever comes first. Starting early helps in two ways: it lets us catch any concerns while they\u2019re tiny, and it helps your child get comfortable with the dentist before any treatment is ever needed.</p>
<h2>What happens at the first visit</h2>
<p>Early visits are short and gentle. We\u2019ll gently check your child\u2019s teeth and gums, talk through teething and home care, and answer your questions about brushing, diet and habits like thumb-sucking. Mostly, it\u2019s about making the chair a friendly, no-pressure place.</p>
<h2>Helping your child feel at ease</h2>
<ul>
  <li>Keep your own tone upbeat \u2014 children take their cues from you.</li>
  <li>Book a time when your child is usually well-rested and fed.</li>
  <li>Bring a favorite comfort toy if it helps.</li>
  <li>Let us do the explaining; we use kid-friendly language and plenty of encouragement.</li>
</ul>
<h2>Building habits that last</h2>
<p>Brush twice a day with a smear of fluoride toothpaste as soon as that first tooth appears, and make it part of the routine. Those early habits \u2014 and early visits \u2014 set the foundation for a lifetime of healthy smiles.</p>
<p>Ready when you are: see our <a href="childrens-dentistry.html">children\u2019s dentistry</a> page, or call to book a friendly first appointment.</p>
'''),

    # Post 3
    _article("blog-dentures-vs-implants.html", "Restorative", "June 2026",
             "Dentures vs. Dental Implants: Which Is Right for You?",
             "Both replace missing teeth beautifully. We break down the real differences in cost, comfort and care.",
             '''
<p class="lede">If you\u2019re replacing one or more missing teeth, two of the most common options are dentures and dental implants. Both can restore your smile \u2014 but they work differently, and the right choice depends on your needs, health and budget.</p>
<h2>Dental implants</h2>
<p>An implant is a small titanium post placed in the jaw that acts as a new tooth root, topped with a custom crown. Implants are <strong>fixed and permanent</strong>, feel very much like natural teeth, and help preserve the jawbone over time. They tend to cost more up front and involve a healing period, but they\u2019re built to last with good care.</p>
<h2>Dentures</h2>
<p>Dentures are <strong>removable</strong> replacements for several or all teeth. Modern dentures look natural and are often more affordable up front, making them a great fit for many patients. They do require daily cleaning and occasional adjustments, and some people need time to get used to the feel.</p>
<h2>A middle path: implant-supported dentures</h2>
<p>You don\u2019t always have to choose one or the other. Implant-supported dentures combine the two \u2014 a denture that snaps securely onto a few implants \u2014 for much more stability than a traditional denture, often at a lower cost than replacing every tooth with an individual implant.</p>
<h2>How to decide</h2>
<p>There\u2019s no single right answer. The best option depends on how many teeth you\u2019re replacing, the health of your jawbone and gums, your lifestyle and your budget. The clearest way forward is a conversation: we\u2019ll examine your smile, lay out your options with honest estimates, and help you choose with confidence.</p>
<p>Explore <a href="dental-implants.html">dental implants</a> and <a href="dentures.html">dentures</a>, or call our Troy office to talk it through.</p>
'''),
]
