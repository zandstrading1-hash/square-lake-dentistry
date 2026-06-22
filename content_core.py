"""content_core.py — About, Services hub, New Patients, Insurance, Reviews, FAQ, Contact."""
from buildlib import PHONE_TEL, PHONE_DISPLAY, PHONE_ICON, SITE
from content_services import book_aside, split

# Service hub icons (reused from homepage), keyed to SERVICES order
ICONS = {
    "general-dentistry.html": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3c2 0 3 1.2 4.6 1.2C18.4 4.2 20 5.6 20 8.4c0 2.4-.9 4.2-1.6 7.2-.6 2.6-.8 5-2.2 5-1.6 0-1-3.8-2.2-3.8s-.7 3.8-2.2 3.8c-1.4 0-1.6-2.4-2.2-5C6.7 12.6 5.8 10.8 5.8 8.4 5.8 5.6 7.4 4.2 9.2 4.2 10.8 4.2 11 3 12 3Z"/></svg>',
    "childrens-dentistry.html": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="7" r="2.4"/><circle cx="16" cy="8.5" r="1.8"/><path d="M4.5 19c0-2.8 2-4.8 4.5-4.8s4.5 2 4.5 4.8"/><path d="M14 19c.1-2.2 1.4-3.6 3.2-3.6 1.8 0 3 1.4 3.1 3.6"/></svg>',
    "emergency-dentistry.html": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2 4 14h6l-1 8 9-12h-6z"/></svg>',
    "cosmetic-dentistry.html": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l1.8 4.4L18 9l-4.2 1.6L12 15l-1.8-4.4L6 9l4.2-1.6z"/><path d="M18.5 14.5l.7 1.8 1.8.7-1.8.7-.7 1.8-.7-1.8-1.8-.7 1.8-.7z"/></svg>',
    "restorative-dentistry.html": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l7 3v5c0 4.5-3 8.4-7 9.6C8 19.4 5 15.5 5 11V6z"/><path d="M9.5 11.5l1.8 1.8 3.4-3.6"/></svg>',
    "dental-implants.html": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3c1.6 0 3 1.4 3 3.4 0 1.6-.7 2.6-1 4.6-.4 2.4-.6 9-2 9s-1.6-6.6-2-9c-.3-2-1-3-1-4.6C6 4.4 7.4 3 9 3"/><path d="M8 8h8"/></svg>',
    "dentures.html": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9c2-.8 5 .8 8 .8S18 8.2 20 9c0 5-1.6 9-3 9-1.2 0-1.2-2.4-2.4-2.4S13.2 18 12 18s-1.4-2.4-2.6-2.4S8 18 7 18c-1.4 0-3-4-3-9z"/></svg>',
    "gum-disease-treatment.html": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.6-7 10-7 10z"/></svg>',
}
from buildlib import SERVICES

DENTIST_SCHEMA = {
    "@context": "https://schema.org", "@type": "Dentist",
    "name": "Square Lake Family Dentistry", "url": SITE + "/", "telephone": "+1-248-558-2785",
    "priceRange": "$$",
    "address": {"@type": "PostalAddress", "streetAddress": "6053 Rochester Rd", "addressLocality": "Troy",
                "addressRegion": "MI", "postalCode": "48085", "addressCountry": "US"},
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "08:00", "closes": "17:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "08:00", "closes": "13:00"}],
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.7", "reviewCount": "109"},
}


def hub_cards():
    out = ""
    for slug, name, blurb in SERVICES:
        out += (f'<a class="svc-card svc-card--link" href="{slug}">'
                f'<span class="svc-card__icon">{ICONS[slug]}</span>'
                f'<h3>{name}</h3><p>{blurb}</p></a>')
    return out


PAGES = [
    # ---------- ABOUT ----------
    dict(
        slug="about.html", active="about",
        title="About Us | Square Lake Family Dentistry | Troy, MI Dentist",
        description="Meet Square Lake Family Dentistry \u2014 a family-owned dental practice in Troy, MI led by Dr. Saif Hanna, caring for patients of every age for over 25 years.",
        cta_title="We'd love to meet your family",
        cta_sub="Become a patient at Square Lake Family Dentistry. Call our Troy office to book your first visit.",
        banner=dict(eyebrow="About our practice", h1="A family dental home in Troy",
                    lead="For over 25 years, Square Lake Family Dentistry has cared for families across Troy and the surrounding communities \u2014 one trusted, welcoming office for every age.",
                    crumbs=[("Home", "index.html"), ("About", None)]),
        body='''
<section class="section"><div class="wrap"><div class="prose reveal" style="max-width:760px">
  <p class="lede">We believe great dental care is built on trust, honesty and treating people the way we'd want our own families treated. That's the standard we hold ourselves to at every visit.</p>
  <h2>Local, independent and personal</h2>
  <p>Square Lake Family Dentistry is a family-owned practice \u2014 not a corporate chain. That independence lets us slow down, get to know you, and recommend only the care you actually need. Many of our patients have been with us for years, and we're proud to now care for their children and grandchildren too.</p>
  <h2>Care for every stage of life</h2>
  <p>From a toddler's very first checkup to dentures and implants later in life, we provide comprehensive care under one roof. No bouncing between offices, no starting over with someone new \u2014 just the same familiar team looking after your whole family.</p>
</div></div></section>

<section class="section section--pine"><div class="wrap">
  <header class="section__head reveal"><p class="eyebrow eyebrow--light">Meet your dentist</p><h2 class="section__title">Dr. Saif Hanna</h2></header>
  <div class="team-grid2 reveal">
    <div class="member">
      <span class="member__avatar"><span>SH</span></span>
      <div><h3>Dr. Saif Hanna</h3><p class="role">Owner &amp; Dentist</p>
      <p>Dr. Hanna leads the Square Lake team with a simple philosophy: treat every patient like family and make good dental care feel easy and clear. He welcomes patients of all ages from Troy and nearby communities.</p></div>
    </div>
    <div class="member">
      <span class="member__avatar"><span>\u2665</span></span>
      <div><h3>Our care team</h3><p class="role">Hygienists &amp; front office</p>
      <p>Our experienced hygienists and friendly front-desk team keep every visit comfortable, on time and stress-free \u2014 from your first phone call to your next checkup.</p></div>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <header class="section__head reveal"><p class="eyebrow">Why families choose us</p><h2 class="section__title">What makes Square Lake different</h2></header>
  <div class="why-grid">
    <div class="why-item reveal"><h3>Family-owned &amp; local</h3><p>An independent Troy practice that's cared for this community for over 25 years.</p></div>
    <div class="why-item reveal"><h3>Modern technology</h3><p>3D oral scanners, low-radiation digital X-rays and a paperless office.</p></div>
    <div class="why-item reveal"><h3>Clear, honest plans</h3><p>We explain your options and give estimates before treatment \u2014 no surprises.</p></div>
    <div class="why-item reveal"><h3>Comfort-focused</h3><p>Nitrous oxide and oral sedation options help anxious patients relax.</p></div>
    <div class="why-item reveal"><h3>All ages welcome</h3><p>One office for toddlers, teens, adults and seniors alike.</p></div>
    <div class="why-item reveal"><h3>Convenient &amp; flexible</h3><p>Early starts and scheduling that works around real life.</p></div>
  </div>
</div></section>
''',
    ),

    # ---------- SERVICES HUB ----------
    dict(
        slug="services.html", active="services",
        title="Dental Services in Troy, MI | Square Lake Family Dentistry",
        description="Explore dental services at Square Lake Family Dentistry in Troy, MI \u2014 preventive care, children's dentistry, emergency, cosmetic and restorative dentistry, implants, dentures and gum care.",
        cta_title="Not sure what you need?",
        cta_sub="Tell us what's going on and we'll point you in the right direction. Call our Troy office.",
        schema_extra={"@context": "https://schema.org", "@type": "ItemList",
                      "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n.replace("&amp;", "&"),
                                            "url": f"{SITE}/{s}"} for i, (s, n, _) in enumerate(SERVICES)]},
        banner=dict(eyebrow="Our services", h1="Complete care for every smile",
                    lead="Everything your family needs in one familiar office \u2014 from routine cleanings to emergencies, cosmetic upgrades and full restorations.",
                    crumbs=[("Home", "index.html"), ("Services", None)]),
        body=f'''
<section class="section"><div class="wrap">
  <div class="svc-grid reveal">{hub_cards()}</div>
</div></section>

<section class="section section--mist"><div class="wrap">
  <div class="callout callout--emergency reveal" style="max-width:880px;margin:0 auto">
    <h3>Having a dental emergency?</h3>
    <p>For severe pain, swelling, a broken or knocked-out tooth, don't wait \u2014 call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>. We offer same-day appointments when available. See our <a href="emergency-dentistry.html">emergency dentistry</a> page for what to do right now.</p>
  </div>
</div></section>
''',
    ),

    # ---------- NEW PATIENTS ----------
    dict(
        slug="new-patients.html", active="newpatients",
        title="New Patients | Square Lake Family Dentistry | Troy, MI",
        description="Welcome to Square Lake Family Dentistry in Troy, MI. Here's what to expect at your first visit, what to bring, and how to book. New patients of all ages welcome.",
        cta_title="Become a new patient",
        cta_sub="We're welcoming new patients of all ages. Call our Troy office to schedule your first visit.",
        banner=dict(eyebrow="New patients", h1="Welcome to the practice",
                    lead="We're glad you're here. Here's everything you need to know to make your first visit smooth, comfortable and easy.",
                    crumbs=[("Home", "index.html"), ("New patients", None)]),
        body=split('''
<p class="lede">Your first visit is about getting to know you, understanding your goals, and building a plan that fits your needs and budget \u2014 at a relaxed, unhurried pace.</p>
<h2>Your first visit, step by step</h2>
<ol class="steps">
  <li><strong>Warm welcome</strong><span>We'll get you checked in and review your health history together.</span></li>
  <li><strong>Comprehensive exam</strong><span>A thorough look at your teeth and gums, with digital X-rays as needed.</span></li>
  <li><strong>Cleaning, if time allows</strong><span>Many new patients receive a cleaning at the first visit.</span></li>
  <li><strong>Your personalized plan</strong><span>We explain what we found and walk through options and estimates \u2014 no pressure, no surprises.</span></li>
</ol>
<h2>What to bring</h2>
<ul class="check-list cols-2">
  <li>Photo ID</li>
  <li>Dental insurance card (if you have one)</li>
  <li>List of current medications</li>
  <li>Any recent dental records or X-rays</li>
</ul>
<h2>Comfort comes first</h2>
<p>If dental visits make you anxious, you're in good company \u2014 and we're here to help. We offer comfort options including nitrous oxide and oral sedation, and we'll always explain what's happening before we begin.</p>
<div class="callout">
  <h3>Insurance &amp; financing</h3>
  <p>We accept many major dental insurance plans and offer CareCredit financing. See our <a href="insurance.html">insurance &amp; financing</a> page, or just call and we'll help you sort out coverage.</p>
</div>
'''),
    ),

    # ---------- INSURANCE ----------
    dict(
        slug="insurance.html", active="insurance",
        title="Insurance & Financing | Square Lake Family Dentistry | Troy, MI",
        description="Square Lake Family Dentistry in Troy, MI accepts many major dental insurance plans and offers CareCredit financing. Contact us to verify your coverage.",
        cta_title="Let's check your coverage",
        cta_sub="Call our Troy office with your plan details and we'll help you understand your benefits.",
        banner=dict(eyebrow="Insurance &amp; financing", h1="Quality care that fits your budget",
                    lead="We work with many major dental insurance plans and offer flexible financing, so cost is one less thing to worry about.",
                    crumbs=[("Home", "index.html"), ("Insurance & financing", None)]),
        body='''
<section class="section"><div class="wrap"><div class="prose reveal" style="max-width:820px">
  <p class="lede">We accept many major dental insurance plans. Not sure whether yours is included? Give us a call with your plan details and our team will gladly help you verify your coverage before your visit.</p>
</div>
<div class="insurance__logos reveal" style="max-width:820px;margin-top:28px">
  <span>Delta Dental</span><span>Blue Cross Blue Shield</span><span>Cigna</span>
  <span>Aetna</span><span>MetLife</span><span>Guardian</span>
  <span>Humana</span><span>UnitedHealthcare</span><span>United Concordia</span>
  <span>Principal</span><span>GEHA</span><span>Assurant</span>
</div>
<p class="reveal" style="max-width:820px;color:var(--ink-soft);margin-top:16px;font-size:.95rem">Plan participation can change \u2014 please contact our office to confirm your specific coverage. We're happy to help you get the most from your benefits.</p>
</div></section>

<section class="section section--mist"><div class="wrap"><div class="split">
  <div class="prose reveal">
    <h2>Flexible financing with CareCredit</h2>
    <p>If you'd like to spread the cost of care over time, we offer CareCredit \u2014 a healthcare financing option with plans that can make treatment more manageable. Ask us about it when you call, and we'll help you find an approach that works for your budget.</p>
    <h2>No insurance? No problem.</h2>
    <p>Many of our patients don't have dental insurance, and we'll always be upfront about costs and options. Call our office to talk through the most affordable way to get the care you need.</p>
  </div>
  <aside class="aside reveal">
    <div class="aside-card aside-card--pine">
      <h3>Questions about cost?</h3>
      <p>We provide clear estimates before treatment begins \u2014 always.</p>
      <a class="aside-phone" href="tel:''' + PHONE_TEL + '''">''' + PHONE_DISPLAY + '''</a>
      <a class="btn btn--primary" href="tel:''' + PHONE_TEL + '''">''' + PHONE_ICON + '''Call our office</a>
    </div>
  </aside>
</div></div></section>
''',
    ),

    # ---------- REVIEWS ----------
    dict(
        slug="reviews.html", active="reviews",
        title="Patient Reviews | Square Lake Family Dentistry | Troy, MI",
        description="Read patient reviews for Square Lake Family Dentistry in Troy, MI \u2014 rated 4.7 stars across 109 Google reviews for friendly, high-quality family dental care.",
        cta_title="Experience the difference",
        cta_sub="See why families across Troy trust us with their smiles. Call to book your visit.",
        banner=dict(eyebrow="Patient reviews", h1="Trusted by families across Troy",
                    lead="We're grateful for every patient who takes the time to share their experience. Here's what your neighbors are saying.",
                    crumbs=[("Home", "index.html"), ("Reviews", None)]),
        body='''
<section class="trustband"><div class="wrap trustband__row">
  <div class="trustband__item"><strong>4.7\u2605</strong><span>Google rating</span></div>
  <div class="trustband__item"><strong>109</strong><span>Patient reviews</span></div>
  <div class="trustband__item"><strong>25+</strong><span>Years in Troy</span></div>
  <div class="trustband__item"><strong>All ages</strong><span>One family office</span></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="review-grid reveal">
    <figure class="review"><span class="stars">\u2605\u2605\u2605\u2605\u2605</span><blockquote>Excellent service and great advice on all of my dental work. The whole team is friendly and thorough.</blockquote><figcaption>Google review</figcaption></figure>
    <figure class="review"><span class="stars">\u2605\u2605\u2605\u2605\u2605</span><blockquote>Highly recommend this office to anyone looking for top-quality dental care. They make you feel at ease.</blockquote><figcaption>Google review</figcaption></figure>
    <figure class="review"><span class="stars">\u2605\u2605\u2605\u2605\u2605</span><blockquote>Friendly, gentle dental care for the whole family. My kids actually look forward to their checkups now.</blockquote><figcaption>Google review</figcaption></figure>
    <figure class="review"><span class="stars">\u2605\u2605\u2605\u2605\u2605</span><blockquote>The staff are warm and welcoming, and they take time to explain everything. A great dental experience.</blockquote><figcaption>Google review</figcaption></figure>
    <figure class="review"><span class="stars">\u2605\u2605\u2605\u2605\u2605</span><blockquote>Clean, modern office and a caring team. I've finally found a dentist I trust for the whole family.</blockquote><figcaption>Google review</figcaption></figure>
    <figure class="review"><span class="stars">\u2605\u2605\u2605\u2605\u2605</span><blockquote>Quick to see me when I had a problem and very gentle throughout. Highly recommend this practice.</blockquote><figcaption>Google review</figcaption></figure>
  </div>
  <div class="reassure reveal">
    <h3>No surprises at checkout</h3>
    <p>We believe every patient should understand their treatment and its cost before care begins. Our team walks you through your options, answers your questions and provides estimates up front \u2014 so you can make confident decisions about your smile.</p>
  </div>
  <div class="section__cta reveal">
    <a class="btn btn--primary" href="https://www.google.com/search?q=Square+Lake+Family+Dentistry+Troy+MI+reviews" target="_blank" rel="noopener">Read more on Google</a>
  </div>
</div></section>
''',
    ),

    # ---------- FAQ ----------
    dict(
        slug="faq.html", active="",
        title="FAQs | Square Lake Family Dentistry | Troy, MI Dentist",
        description="Answers to common questions about Square Lake Family Dentistry in Troy, MI \u2014 new patients, emergency visits, insurance, children's dentistry, sedation and more.",
        cta_title="Still have a question?",
        cta_sub="We're happy to help \u2014 just give our Troy office a call.",
        schema_extra={"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": "Are new patients welcome?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. New patients of all ages are welcome at Square Lake Family Dentistry."}},
            {"@type": "Question", "name": "Do you offer emergency dental appointments?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. We keep room for urgent visits and offer same-day appointments when available."}},
            {"@type": "Question", "name": "How often should I visit the dentist?", "acceptedAnswer": {"@type": "Answer", "text": "Most patients do well with a cleaning and exam every six months, though your needs may differ."}},
            {"@type": "Question", "name": "Do you accept dental insurance?", "acceptedAnswer": {"@type": "Answer", "text": "We accept many major dental insurance plans. Contact our office to verify your specific coverage."}},
        ]},
        banner=dict(eyebrow="Good to know", h1="Frequently asked questions",
                    lead="Quick answers to the questions we hear most. Don't see yours? Give us a call.",
                    crumbs=[("Home", "index.html"), ("FAQs", None)]),
        body='''
<section class="section"><div class="wrap faq__wrap">
  <div class="faq reveal">
    <details class="faq__item"><summary>Are new patients welcome?</summary><div class="faq__body"><p>Yes \u2014 new patients of all ages are always welcome. Just call our office to get started.</p></div></details>
    <details class="faq__item"><summary>How do I book an appointment?</summary><div class="faq__body"><p>We schedule by phone so we can find the time that works best for you. Call us and our front desk will take care of the rest.</p></div></details>
    <details class="faq__item"><summary>Do you offer emergency dental appointments?</summary><div class="faq__body"><p>We do. We keep room in our schedule for urgent visits and offer same-day appointments whenever possible for issues like severe pain, swelling, broken teeth or a lost filling.</p></div></details>
    <details class="faq__item"><summary>How often should I visit the dentist?</summary><div class="faq__body"><p>Most patients do well with a cleaning and exam every six months, though your needs may differ based on your oral health. We'll recommend a schedule that's right for you.</p></div></details>
    <details class="faq__item"><summary>Do you accept my insurance?</summary><div class="faq__body"><p>We accept many major dental insurance plans. Contact our office with your plan details and we'll help verify your specific coverage. See our <a href="insurance.html">insurance &amp; financing</a> page for more.</p></div></details>
    <details class="faq__item"><summary>Is financing available?</summary><div class="faq__body"><p>Yes. We offer CareCredit financing to help make care more manageable. Ask us about your options when you call.</p></div></details>
    <details class="faq__item"><summary>What should I bring to my first visit?</summary><div class="faq__body"><p>Please bring a photo ID, your insurance card, a list of any medications, and any recent dental records or X-rays. See our <a href="new-patients.html">new patients</a> page for what to expect.</p></div></details>
    <details class="faq__item"><summary>Do you offer options for anxious patients?</summary><div class="faq__body"><p>Yes. We offer comfort options including nitrous oxide and oral sedation, and our team takes time to keep nervous patients relaxed and informed.</p></div></details>
    <details class="faq__item"><summary>Do you treat children?</summary><div class="faq__body"><p>Absolutely. We provide <a href="childrens-dentistry.html">children's dentistry</a> and family care for toddlers, kids, teens, adults and seniors \u2014 all in one office.</p></div></details>
  </div>
</div></section>
''',
    ),

    # ---------- CONTACT ----------
    dict(
        slug="contact.html", active="contact",
        title="Contact & Directions | Square Lake Family Dentistry | Troy, MI",
        description="Call Square Lake Family Dentistry at (248) 558-2785 to book. Find our address, hours and directions at 6053 Rochester Rd, Troy, MI 48085.",
        cta=False,
        schema_extra=DENTIST_SCHEMA,
        banner=dict(eyebrow="Visit us", h1="Call to book your visit",
                    lead="We schedule by phone so we can match you with the right time. Give us a call \u2014 new patients of all ages are always welcome.",
                    crumbs=[("Home", "index.html"), ("Contact", None)], cta=True),
        body=f'''
<section class="section"><div class="wrap">
  <div class="contact__grid">
    <div class="contact__info reveal">
      <div class="contact__block">
        <h3>Square Lake Family Dentistry</h3>
        <p><a href="https://www.google.com/maps?q=6053+Rochester+Rd,+Troy,+MI+48085" target="_blank" rel="noopener">6053 Rochester Rd<br />Troy, MI 48085</a></p>
      </div>
      <div class="contact__block">
        <h3>Call or text</h3>
        <p><a class="contact__phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
      </div>
      <div class="contact__block">
        <h3>Office hours</h3>
        <table class="hours">
          <tr><th scope="row">Mon \u2013 Thu</th><td>8:00 AM \u2013 5:00 PM</td></tr>
          <tr><th scope="row">Friday</th><td>8:00 AM \u2013 1:00 PM</td></tr>
          <tr><th scope="row">Sat \u2013 Sun</th><td>Closed</td></tr>
        </table>
      </div>
      <div class="contact__map">
        <iframe title="Map to Square Lake Family Dentistry" src="https://www.google.com/maps?q=6053+Rochester+Rd,+Troy,+MI+48085&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>

    <div class="contact__form-wrap reveal">
      <h3 style="font-family:var(--display);color:var(--pine);font-size:1.3rem;margin-bottom:6px">Send us a message</h3>
      <p style="color:var(--ink-soft);font-size:.95rem;margin-bottom:18px">For non-urgent questions. To book an appointment or for anything urgent, please call \u2014 it's the fastest way to reach us.</p>
      <form class="form" id="apptForm" novalidate>
        <div class="form__row">
          <label class="form__field"><span>First name</span><input type="text" name="firstName" autocomplete="given-name" required /></label>
          <label class="form__field"><span>Last name</span><input type="text" name="lastName" autocomplete="family-name" required /></label>
        </div>
        <div class="form__row">
          <label class="form__field"><span>Phone</span><input type="tel" name="phone" autocomplete="tel" required /></label>
          <label class="form__field"><span>Email</span><input type="email" name="email" autocomplete="email" /></label>
        </div>
        <label class="form__field"><span>How can we help?</span><textarea name="message" rows="4" placeholder="Let us know what you're looking for."></textarea></label>
        <button type="submit" class="btn btn--primary btn--block">Send message</button>
        <p class="form__fineprint">Please don't include sensitive medical details. We'll get back to you during office hours.</p>
        <p class="form__success" id="formSuccess" role="status" hidden>Thanks! Your message has been noted \u2014 we'll be in touch during office hours. For anything urgent, please call {PHONE_DISPLAY}.</p>
      </form>
    </div>
  </div>
</div></section>
''',
    ),
]
