"""content_services.py — the 8 individual service pages."""
from buildlib import PHONE_TEL, PHONE_DISPLAY, PHONE_ICON, related, cta_btn


def book_aside(emergency=False):
    if emergency:
        card = f'''<div class="aside-card aside-card--pine">
        <h3>Dental emergency?</h3>
        <p>Don't wait it out. Call now and we'll do our best to see you the same day.</p>
        <a class="aside-phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        {cta_btn("Call now", True)}
      </div>'''
    else:
        card = f'''<div class="aside-card aside-card--pine">
        <h3>Book your visit</h3>
        <p>We book by phone so we can match you with the right time. New patients welcome.</p>
        <a class="aside-phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        {cta_btn("Call to book", True)}
      </div>'''
    hours = '''<div class="aside-card">
        <h3>Office hours</h3>
        <ul class="aside-hours">
          <li><span>Mon\u2013Thu</span><span>8:00\u20135:00</span></li>
          <li><span>Friday</span><span>8:00\u20131:00</span></li>
          <li><span>Sat\u2013Sun</span><span>Closed</span></li>
        </ul>
      </div>'''
    return f'<aside class="aside reveal">{card}{hours}</aside>'


def split(content, emergency=False):
    return (f'<section class="section"><div class="wrap"><div class="split">'
            f'<div class="prose reveal">{content}</div>{book_aside(emergency)}</div></div></section>')


PAGES = [
    # 1. General & preventive
    dict(
        slug="general-dentistry.html", active="services",
        title="General & Preventive Dentistry in Troy, MI | Square Lake Family Dentistry",
        description="Routine cleanings, exams, X-rays, sealants and oral cancer screenings in Troy, MI. Preventive dental care for the whole family at Square Lake Family Dentistry.",
        cta_title="Due for a checkup?",
        cta_sub="A six-month cleaning and exam is the easiest way to keep small problems small. Call to book.",
        banner=dict(eyebrow="General &amp; preventive", h1="Preventive dentistry that keeps smiles healthy",
                    lead="Routine care is the quiet hero of a healthy mouth. Regular visits help us catch issues early \u2014 when they're simpler, gentler and less expensive to fix.",
                    crumbs=[("Home", "index.html"), ("Services", "services.html"), ("General &amp; preventive", None)]),
        body=split('''
<p class="lede">Most dental problems are far easier to prevent than to repair. At Square Lake Family Dentistry, preventive care is the heart of what we do \u2014 thorough, unhurried checkups for every member of your family.</p>
<h2>What a preventive visit includes</h2>
<ul class="check-list cols-2">
  <li>Professional cleaning to remove plaque and tartar</li>
  <li>Comprehensive dental exam</li>
  <li>X-rays as needed</li>
  <li>Oral cancer screening</li>
  <li>Gum (periodontal) health check</li>
  <li>Fluoride treatment when helpful</li>
  <li>Dental sealants to protect against decay</li>
  <li>Personalized brushing &amp; flossing guidance</li>
</ul>
<h2>Why six-month checkups matter</h2>
<p>Even with great brushing at home, plaque hardens into tartar that only a professional cleaning can remove. Regular exams let us spot cavities, gum changes and other concerns before you feel them \u2014 often before they need anything more than a small fix.</p>
<h2>What to expect</h2>
<ol class="steps">
  <li><strong>Welcome &amp; history</strong><span>We review your health history and any concerns you'd like to discuss.</span></li>
  <li><strong>Exam &amp; imaging</strong><span>A careful look at your teeth and gums, with X-rays as needed.</span></li>
  <li><strong>Cleaning</strong><span>A gentle, thorough cleaning and polish from your hygienist.</span></li>
  <li><strong>Plan &amp; next steps</strong><span>We explain what we found and agree on a plan \u2014 with estimates up front.</span></li>
</ol>
'''),
        related_excl={"general-dentistry.html"},
    ),

    # 2. Children's
    dict(
        slug="childrens-dentistry.html", active="services",
        title="Children's Dentistry in Troy, MI | Square Lake Family Dentistry",
        description="Gentle children's dentistry in Troy, MI \u2014 first visits, cleanings, sealants and cavity care that help kids feel comfortable and build healthy habits early.",
        cta_title="Ready for your child's visit?",
        cta_sub="We love welcoming little ones. Call to book a friendly first appointment.",
        banner=dict(eyebrow="Children's dentistry", h1="Friendly dental care that kids actually like",
                    lead="From the very first tooth, we make dental visits calm, positive and even a little fun \u2014 setting your child up for a lifetime of healthy smiles.",
                    crumbs=[("Home", "index.html"), ("Services", "services.html"), ("Children's dentistry", None)]),
        body=split('''
<p class="lede">A good early experience shapes how a child feels about the dentist for years. Our team takes the time to build trust, explain things gently, and keep every visit pressure-free.</p>
<h2>Care for growing smiles</h2>
<ul class="check-list cols-2">
  <li>Comfortable first visits</li>
  <li>Gentle cleanings &amp; exams</li>
  <li>Fluoride treatments</li>
  <li>Protective dental sealants</li>
  <li>Tooth-colored fillings</li>
  <li>Thumb-sucking &amp; habit guidance</li>
  <li>Custom sports mouthguards</li>
  <li>Brushing &amp; flossing coaching for kids</li>
</ul>
<div class="callout">
  <h3>When should my child first see the dentist?</h3>
  <p>Most dentists recommend a first visit by your child's first birthday, or within six months of their first tooth appearing. Early visits are short, friendly, and mostly about getting comfortable.</p>
</div>
<h2>Tips for a great first appointment</h2>
<ul>
  <li>Keep your own tone upbeat \u2014 kids take their cues from you.</li>
  <li>Schedule for a time when your child is usually rested and fed.</li>
  <li>Bring a favorite comfort toy if it helps.</li>
  <li>Let us do the explaining \u2014 we use kid-friendly language and lots of encouragement.</li>
</ul>
'''),
        related_excl={"childrens-dentistry.html"},
    ),

    # 3. Emergency
    dict(
        slug="emergency-dentistry.html", active="services",
        title="Emergency Dentist in Troy, MI | Same-Day Dental Care | Square Lake",
        description="Tooth pain, swelling, a broken or knocked-out tooth? Square Lake Family Dentistry offers same-day emergency dental appointments in Troy, MI when available. Call now.",
        cta_title="Tooth pain that can't wait?",
        cta_sub="Call our Troy office now \u2014 we keep room for urgent visits and offer same-day care when available.",
        banner=dict(eyebrow="Urgent dental care", h1="Same-day emergency dentistry in Troy",
                    lead="Dental emergencies don't keep office hours. When something goes wrong, call us right away \u2014 we'll do everything we can to get you seen and out of pain quickly.",
                    crumbs=[("Home", "index.html"), ("Services", "services.html"), ("Emergency dentistry", None)],
                    cta=True),
        body=split('''
<div class="callout callout--emergency">
  <h3>In severe pain or have facial swelling?</h3>
  <p>Call <a href="tel:''' + PHONE_TEL + '''">''' + PHONE_DISPLAY + '''</a> now. If you have trouble breathing or swallowing, or significant swelling, seek emergency medical care immediately.</p>
</div>
<h2>Emergencies we treat</h2>
<div class="signs-grid">
  <div class="sign"><h3>Severe tooth pain</h3><p>Throbbing or constant pain that over-the-counter relief isn't touching.</p></div>
  <div class="sign"><h3>Swelling or abscess</h3><p>A swollen gum, jaw or face can signal infection that needs prompt care.</p></div>
  <div class="sign"><h3>Broken or chipped tooth</h3><p>Cracks and breaks that are painful, sharp or affecting your bite.</p></div>
  <div class="sign"><h3>Knocked-out tooth</h3><p>Act fast \u2014 a tooth has the best chance if treated within the hour.</p></div>
  <div class="sign"><h3>Lost filling or crown</h3><p>Exposed teeth can be sensitive and vulnerable to further damage.</p></div>
  <div class="sign"><h3>Soft-tissue injury</h3><p>Cuts to the lips, cheeks or tongue along with dental damage.</p></div>
</div>
<h2>What to do right now</h2>
<p><strong>Knocked-out tooth:</strong> Pick it up by the crown (not the root), gently rinse, and try to place it back in the socket. If you can't, keep it in milk and call us immediately.</p>
<p><strong>Broken tooth:</strong> Rinse with warm water and apply a cold compress to reduce swelling. Save any pieces.</p>
<p><strong>Toothache:</strong> Rinse with warm salt water and floss gently to remove any trapped food. Avoid placing aspirin directly on the gum.</p>
<p><strong>Lost filling or crown:</strong> Keep the area clean and avoid chewing on that side until we can see you.</p>
''', emergency=True),
        related_excl={"emergency-dentistry.html"},
    ),

    # 4. Cosmetic
    dict(
        slug="cosmetic-dentistry.html", active="services",
        title="Cosmetic Dentist in Troy, MI | Whitening, Veneers, Clear Aligners | Square Lake",
        description="Brighten and reshape your smile with cosmetic dentistry in Troy, MI \u2014 teeth whitening, porcelain veneers, bonding and clear aligners for natural-looking results.",
        cta_title="Love your smile again",
        cta_sub="Ask about a cosmetic consultation. Call our Troy office to get started.",
        banner=dict(eyebrow="Cosmetic dentistry", h1="A brighter, more confident smile",
                    lead="Small changes can make a big difference. We focus on natural-looking results that fit your face and feel like you \u2014 only more confident.",
                    crumbs=[("Home", "index.html"), ("Services", "services.html"), ("Cosmetic dentistry", None)]),
        body=split('''
<p class="lede">Whether you want a subtle refresh or a full smile makeover, our cosmetic options are designed to look natural and wear beautifully.</p>
<h2>Ways we can enhance your smile</h2>
<ul class="check-list cols-2">
  <li>Professional teeth whitening</li>
  <li>Porcelain veneers</li>
  <li>Cosmetic bonding</li>
  <li>Tooth reshaping &amp; contouring</li>
  <li>Clear aligner options</li>
  <li>Complete smile makeovers</li>
</ul>
<h2>Natural-looking, made for you</h2>
<p>Great cosmetic dentistry shouldn't look "done." We take time to understand the result you're after, then match shade, shape and proportion to your features so your smile looks healthy and authentic.</p>
<h2>How it works</h2>
<ol class="steps">
  <li><strong>Consultation</strong><span>We listen to your goals and look at what's possible for your smile.</span></li>
  <li><strong>Custom plan</strong><span>A clear plan and estimate \u2014 often with a preview of the result.</span></li>
  <li><strong>Treatment</strong><span>We bring the plan to life, comfortably and at your pace.</span></li>
</ol>
'''),
        related_excl={"cosmetic-dentistry.html"},
    ),

    # 5. Restorative
    dict(
        slug="restorative-dentistry.html", active="services",
        title="Restorative Dentistry in Troy, MI | Fillings, Crowns, Bridges | Square Lake",
        description="Repair damaged or missing teeth with restorative dentistry in Troy, MI \u2014 tooth-colored fillings, crowns, bridges and root canal therapy that restore comfort and function.",
        cta_title="Restore comfort and function",
        cta_sub="If a tooth is bothering you, let's take a look. Call our Troy office to book.",
        banner=dict(eyebrow="Restorative dentistry", h1="Bringing damaged teeth back to health",
                    lead="When teeth are worn, decayed or missing, the right restoration brings back comfort, function and confidence \u2014 and helps protect the teeth around them.",
                    crumbs=[("Home", "index.html"), ("Services", "services.html"), ("Restorative dentistry", None)]),
        body=split('''
<p class="lede">From a small filling to rebuilding a worn smile, we use durable, natural-looking materials and explain every option clearly before we begin.</p>
<h2>Restorative treatments we offer</h2>
<ul class="check-list cols-2">
  <li>Tooth-colored (composite) fillings</li>
  <li>Dental crowns</li>
  <li>Fixed bridges</li>
  <li>Inlays &amp; onlays</li>
  <li>Root canal therapy</li>
  <li>Full-mouth restoration</li>
</ul>
<p>For missing teeth, we also offer <a href="dental-implants.html">dental implants</a> and <a href="dentures.html">dentures</a> \u2014 and we'll help you weigh which option fits your needs and budget.</p>
<h2>Built to last and feel natural</h2>
<p>Modern restorations are tooth-colored and carefully shaped to your bite, so they blend in and feel comfortable. Our goal is always the longest-lasting, most conservative fix for your situation.</p>
'''),
        related_excl={"restorative-dentistry.html"},
    ),

    # 6. Implants
    dict(
        slug="dental-implants.html", active="services",
        title="Dental Implants in Troy, MI | Permanent Tooth Replacement | Square Lake",
        description="Replace missing teeth with dental implants in Troy, MI. Permanent, natural-feeling tooth replacement from Square Lake Family Dentistry \u2014 single tooth to full restoration.",
        cta_title="Replace missing teeth for good",
        cta_sub="Wondering if implants are right for you? Call our Troy office for a consultation.",
        banner=dict(eyebrow="Dental implants", h1="Permanent, natural-feeling tooth replacement",
                    lead="Dental implants look, feel and function like your own teeth. They're the closest thing to a natural replacement \u2014 and they help preserve your jawbone and surrounding teeth.",
                    crumbs=[("Home", "index.html"), ("Services", "services.html"), ("Dental implants", None)]),
        body=split('''
<p class="lede">An implant is a small titanium post that acts as a new tooth root, topped with a custom crown. Once healed, it's stable, comfortable, and cared for just like a natural tooth.</p>
<h2>Why patients choose implants</h2>
<ul class="check-list cols-2">
  <li>Look and feel like natural teeth</li>
  <li>Stay firmly in place \u2014 no slipping</li>
  <li>Help preserve jawbone &amp; facial shape</li>
  <li>Don't rely on grinding down neighboring teeth</li>
  <li>Eat and speak with confidence</li>
  <li>Built to last with good care</li>
</ul>
<h2>The implant process</h2>
<ol class="steps">
  <li><strong>Consultation &amp; imaging</strong><span>We assess your bone and plan the placement using detailed imaging.</span></li>
  <li><strong>Implant placement</strong><span>The post is gently placed into the jaw under local anesthetic.</span></li>
  <li><strong>Healing</strong><span>The implant fuses with the bone over a few months for a stable foundation.</span></li>
  <li><strong>Your new tooth</strong><span>We attach a custom crown that matches your smile.</span></li>
</ol>
<div class="callout">
  <h3>Implants or dentures?</h3>
  <p>Both restore missing teeth beautifully. Implants are fixed and permanent; <a href="dentures.html">dentures</a> are removable and often more affordable up front. We'll help you compare \u2014 and some patients combine the two with implant-supported dentures.</p>
</div>
'''),
        related_excl={"dental-implants.html"},
    ),

    # 7. Dentures
    dict(
        slug="dentures.html", active="services",
        title="Dentures & Denture Repairs in Troy, MI | Square Lake Family Dentistry",
        description="Comfortable, great-fitting dentures and fast denture repairs in Troy, MI. Full, partial and implant-supported dentures from Square Lake Family Dentistry.",
        cta_title="Eat and smile with confidence",
        cta_sub="Need new dentures or a quick repair? Call our Troy office today.",
        banner=dict(eyebrow="Dentures &amp; repairs", h1="Comfortable dentures, made to fit",
                    lead="Today's dentures look natural and fit securely. Whether you need a full set, a partial, or a fast repair, we'll help you eat, speak and smile with comfort.",
                    crumbs=[("Home", "index.html"), ("Services", "services.html"), ("Dentures &amp; repairs", None)]),
        body=split('''
<p class="lede">A well-made denture should feel secure and look like a natural smile. We take careful impressions and adjust for a comfortable, confident fit.</p>
<h2>Denture options &amp; services</h2>
<ul class="check-list cols-2">
  <li>Full dentures</li>
  <li>Partial dentures</li>
  <li>Implant-supported dentures</li>
  <li>Relines &amp; adjustments</li>
  <li>Same-day &amp; fast denture repairs</li>
  <li>Replacement of worn dentures</li>
</ul>
<h2>A fit that feels right</h2>
<p>Ill-fitting dentures can cause sore spots and make eating frustrating. We focus on a precise fit and natural appearance \u2014 and for the most stability, ask us about <a href="dental-implants.html">implant-supported dentures</a> that snap securely into place.</p>
<h2>Caring for your dentures</h2>
<ul>
  <li>Rinse after eating and brush daily with a soft denture brush.</li>
  <li>Soak overnight to keep them moist and clean.</li>
  <li>Handle over a folded towel or water to avoid breakage.</li>
  <li>Keep regular checkups so we can adjust the fit as needed.</li>
</ul>
'''),
        related_excl={"dentures.html"},
    ),

    # 8. Gum disease
    dict(
        slug="gum-disease-treatment.html", active="services",
        title="Gum Disease Treatment in Troy, MI | Periodontal Care | Square Lake",
        description="Treat bleeding gums and gum disease in Troy, MI with periodontal evaluations, deep cleanings and scaling & root planing at Square Lake Family Dentistry.",
        cta_title="Protect your gums, protect your smile",
        cta_sub="Notice bleeding or tender gums? Call our Troy office for a periodontal evaluation.",
        banner=dict(eyebrow="Gum disease care", h1="Healthy gums, the foundation of your smile",
                    lead="Gum disease is common, often painless early on \u2014 and very treatable when caught in time. Healthy gums protect your teeth and your overall health.",
                    crumbs=[("Home", "index.html"), ("Services", "services.html"), ("Gum disease treatment", None)]),
        body=split('''
<p class="lede">Bleeding, tender or receding gums are signs worth taking seriously. The earlier we treat gum disease, the simpler it is to reverse and control.</p>
<h2>Warning signs to watch for</h2>
<div class="signs-grid">
  <div class="sign"><h3>Bleeding gums</h3><p>Gums that bleed when you brush or floss.</p></div>
  <div class="sign"><h3>Persistent bad breath</h3><p>Ongoing bad breath or a bad taste in the mouth.</p></div>
  <div class="sign"><h3>Receding gums</h3><p>Teeth that look longer as gums pull away.</p></div>
  <div class="sign"><h3>Tender or swollen gums</h3><p>Red, puffy or sore gum tissue.</p></div>
  <div class="sign"><h3>Loose teeth</h3><p>Teeth that feel loose or are shifting position.</p></div>
  <div class="sign"><h3>Sensitivity</h3><p>New sensitivity along the gumline.</p></div>
</div>
<h2>How we treat gum disease</h2>
<ul class="check-list cols-2">
  <li>Thorough periodontal evaluation</li>
  <li>Scaling &amp; root planing (deep cleaning)</li>
  <li>Gingivitis treatment</li>
  <li>Ongoing periodontal maintenance</li>
  <li>Personalized home-care plan</li>
  <li>Monitoring to keep gums stable</li>
</ul>
<p>If you're concerned about your gum health, give us a call \u2014 we'll be glad to take a look and talk through the right next steps for you.</p>
'''),
        related_excl={"gum-disease-treatment.html"},
    ),
]

# attach related-services section to each page body
for _p in PAGES:
    _p["body"] = _p["body"] + related(_p.pop("related_excl"))
