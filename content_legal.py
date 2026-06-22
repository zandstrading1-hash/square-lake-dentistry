"""content_legal.py — standard legal/policy pages for a real practice website.

NOTE: These are professionally-structured starting templates. The practice should
have them reviewed by qualified counsel and tailored to its actual data practices
(analytics, cookies, vendors) and to its official HIPAA Notice of Privacy Practices.
"""
from buildlib import PHONE_TEL, PHONE_DISPLAY

UPDATED = "June 2026"


def legal(slug, title, description, h1, eyebrow, lead, body_html):
    intro = (f'<p style="color:var(--ink-soft);font-size:.9rem;margin:0 0 22px">Last updated: {UPDATED}</p>')
    return dict(
        slug=slug, active="", title=title, description=description, cta=False,
        banner=dict(eyebrow=eyebrow, h1=h1, lead=lead, cta=False,
                    crumbs=[("Home", "index.html"), (h1, None)]),
        body=(f'<section class="section"><div class="wrap"><div class="prose reveal">'
              f'{intro}{body_html}</div></div></section>'),
    )


PAGES = [
    # -------------------- PRIVACY POLICY --------------------
    legal(
        "privacy.html",
        "Privacy Policy | Square Lake Family Dentistry | Troy, MI",
        "Privacy Policy for the Square Lake Family Dentistry website \u2014 what information we collect, how we use it, and your choices.",
        "Privacy Policy", "Your privacy",
        "This policy explains how we handle information collected through this website. It is separate from the privacy of your health records, which is governed by our Notice of Privacy Practices.",
        f'''
<p>Square Lake Family Dentistry (\u201cwe,\u201d \u201cus,\u201d or \u201cour\u201d) respects your privacy. This Privacy Policy describes how we collect, use, and protect information when you visit <strong>squarelakefamilydentistry.com</strong> (the \u201cSite\u201d). It applies to the Site only and does not govern protected health information collected as part of your dental care, which is described in our <a href="notice-of-privacy-practices.html">Notice of Privacy Practices</a>.</p>

<h2>Information we collect</h2>
<p><strong>Information you provide.</strong> If you use our contact form, you may give us your name, phone number, email address, and the contents of your message. Please do not submit sensitive medical details through the Site.</p>
<p><strong>Information collected automatically.</strong> Like most websites, our Site may automatically collect limited technical information such as your IP address, browser type, device, pages viewed, and the date and time of your visit. This may be collected through cookies or similar technologies, including basic website analytics.</p>

<h2>How we use information</h2>
<ul>
  <li>To respond to your questions and requests</li>
  <li>To operate, maintain, and improve the Site</li>
  <li>To understand how visitors use the Site</li>
  <li>To protect the security and integrity of the Site</li>
  <li>To comply with legal obligations</li>
</ul>

<h2>Cookies and analytics</h2>
<p>We may use cookies and similar technologies to help the Site function and to measure traffic. Most browsers let you refuse or delete cookies through their settings; doing so may affect how the Site works.</p>

<h2>How we share information</h2>
<p>We do not sell your personal information. We may share information with trusted service providers who help us operate the Site (for example, hosting or analytics providers), when required by law, or to protect our rights and the safety of others.</p>

<h2>Third-party links and services</h2>
<p>The Site may link to or embed third-party services, such as Google Maps and our social media pages. Those services have their own privacy policies, and we are not responsible for their practices.</p>

<h2>Data security</h2>
<p>We use reasonable measures to protect information submitted through the Site. However, no method of transmission over the Internet is completely secure, and we cannot guarantee absolute security.</p>

<h2>Children\u2019s privacy</h2>
<p>The Site is intended for a general audience and is not directed at children under 13. We do not knowingly collect personal information from children under 13 through the Site.</p>

<h2>Your choices</h2>
<p>You may choose not to provide information through the Site, and you can adjust your browser\u2019s cookie settings. To ask about information you\u2019ve sent us, please contact our office.</p>

<h2>Changes to this policy</h2>
<p>We may update this Privacy Policy from time to time. Changes will be posted on this page with a revised \u201cLast updated\u201d date.</p>

<h2>Contact us</h2>
<p>Questions about this policy? Call us at <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> or visit our <a href="contact.html">Contact</a> page. Square Lake Family Dentistry, 6053 Rochester Rd, Troy, MI 48085.</p>
'''),

    # -------------------- TERMS OF USE --------------------
    legal(
        "terms.html",
        "Terms of Use | Square Lake Family Dentistry | Troy, MI",
        "Terms of Use for the Square Lake Family Dentistry website, including an important note that the Site\u2019s content is for general information and is not medical advice.",
        "Terms of Use", "The fine print",
        "Please read these terms carefully. By using this website, you agree to them.",
        f'''
<p>These Terms of Use (\u201cTerms\u201d) govern your use of <strong>squarelakefamilydentistry.com</strong> (the \u201cSite\u201d), operated by Square Lake Family Dentistry. By accessing or using the Site, you agree to these Terms. If you do not agree, please do not use the Site.</p>

<h2>Not medical advice</h2>
<p>The information on this Site is provided for general educational purposes only and is <strong>not a substitute for professional dental or medical advice, diagnosis, or treatment</strong>. Using the Site does not create a dentist\u2013patient relationship. Always seek the advice of a qualified dental or health provider with any questions about your condition, and never disregard professional advice or delay seeking it because of something you read here. If you have a medical emergency, call 911 or seek immediate care.</p>

<h2>Use of the Site</h2>
<p>You agree to use the Site only for lawful purposes and not to interfere with its operation, attempt to gain unauthorized access, or use it in any way that could harm the Site or other users.</p>

<h2>Intellectual property</h2>
<p>The content on this Site, including text, graphics, logos, and design, is owned by or licensed to Square Lake Family Dentistry and is protected by applicable laws. You may view and print pages for your personal, non-commercial use, but you may not otherwise copy, reproduce, or distribute Site content without our permission.</p>

<h2>Third-party links</h2>
<p>The Site may contain links to third-party websites and services for your convenience. We do not control and are not responsible for their content, policies, or practices.</p>

<h2>Disclaimer of warranties</h2>
<p>The Site is provided on an \u201cas is\u201d and \u201cas available\u201d basis without warranties of any kind, whether express or implied. We do not warrant that the Site will be uninterrupted, error-free, or free of harmful components, or that the information on it is complete or current.</p>

<h2>Limitation of liability</h2>
<p>To the fullest extent permitted by law, Square Lake Family Dentistry will not be liable for any damages arising out of or related to your use of, or inability to use, the Site.</p>

<h2>Governing law</h2>
<p>These Terms are governed by the laws of the State of Michigan, without regard to its conflict-of-law principles.</p>

<h2>Changes to these Terms</h2>
<p>We may update these Terms from time to time. Continued use of the Site after changes are posted constitutes acceptance of the revised Terms.</p>

<h2>Contact us</h2>
<p>Questions about these Terms? Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> or visit our <a href="contact.html">Contact</a> page.</p>
'''),

    # -------------------- ACCESSIBILITY STATEMENT --------------------
    legal(
        "accessibility.html",
        "Accessibility Statement | Square Lake Family Dentistry | Troy, MI",
        "Square Lake Family Dentistry is committed to digital accessibility and aims to meet WCAG 2.1 Level AA. Learn how to request assistance or report an issue.",
        "Accessibility Statement", "Accessible to everyone",
        "We want everyone to be able to use our website comfortably, including people who rely on assistive technologies.",
        f'''
<p>Square Lake Family Dentistry is committed to ensuring that our website is accessible to people with disabilities. We strive to provide a website that everyone can use, and we work to improve the experience for all visitors.</p>

<h2>Our standard</h2>
<p>We aim to conform to the <strong>Web Content Accessibility Guidelines (WCAG) 2.1, Level AA</strong>, the widely recognized standard for web accessibility. These guidelines help make web content more accessible to people with a range of disabilities, including visual, auditory, physical, and cognitive disabilities.</p>

<h2>What we\u2019ve done</h2>
<ul>
  <li>Built the site with semantic, structured HTML and clear page landmarks</li>
  <li>Provided a \u201cskip to content\u201d link and full keyboard navigation</li>
  <li>Added visible focus indicators for keyboard users</li>
  <li>Chosen color combinations intended to meet AA contrast levels</li>
  <li>Used descriptive labels on form fields and links</li>
  <li>Made the site responsive and usable across devices and zoom levels</li>
  <li>Honored \u201creduced motion\u201d preferences for users sensitive to animation</li>
</ul>

<h2>Known limitations</h2>
<p>Some content provided by third parties, such as the embedded Google Map, may not fully meet accessibility standards because it is outside our direct control. If any such content prevents you from getting the information you need, please contact us and we\u2019ll be glad to help directly.</p>

<h2>Need help or want to report a problem?</h2>
<p>If you have difficulty using any part of this website, or if you need information in an alternative format, please let us know \u2014 we\u2019ll do our best to help and to provide what you need in another way.</p>
<p>Call us at <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> during office hours, or reach us through our <a href="contact.html">Contact</a> page. We welcome your feedback, and we use it to keep improving.</p>

<h2>Ongoing effort</h2>
<p>Accessibility is an ongoing commitment. We review our site periodically and make improvements as standards and technologies evolve.</p>
'''),

    # -------------------- HIPAA NOTICE OF PRIVACY PRACTICES --------------------
    legal(
        "notice-of-privacy-practices.html",
        "Notice of Privacy Practices (HIPAA) | Square Lake Family Dentistry",
        "A summary of how Square Lake Family Dentistry may use and disclose your protected health information and your rights under HIPAA. The full notice is available at our office.",
        "Notice of Privacy Practices", "Your health information",
        "This summary explains how your health information may be used and disclosed, and how you can access it. Our complete, official notice is available at our office.",
        f'''
<p>This notice describes, in summary form, how medical and dental information about you may be used and disclosed by Square Lake Family Dentistry, and how you can get access to this information. Our <strong>complete Notice of Privacy Practices</strong> is provided at your first visit and is available at our office on request. Please review it carefully.</p>

<h2>How we may use and disclose your health information</h2>
<p>We may use and disclose your protected health information (\u201cPHI\u201d) for the following purposes:</p>
<ul>
  <li><strong>Treatment</strong> \u2014 to provide, coordinate, and manage your dental care, including sharing information with other providers involved in your treatment.</li>
  <li><strong>Payment</strong> \u2014 to bill and obtain payment for the services we provide, including verifying insurance coverage.</li>
  <li><strong>Health care operations</strong> \u2014 to support the business activities of our practice, such as quality assessment, staff training, and scheduling.</li>
  <li><strong>As required or permitted by law</strong> \u2014 for example, for public health activities or when required by court order.</li>
</ul>
<p>We may also contact you to provide appointment reminders or information about treatment options. Other uses and disclosures will be made only with your written authorization, which you may revoke at any time.</p>

<h2>Your rights regarding your health information</h2>
<p>You have the right to:</p>
<ul>
  <li>Request access to and a copy of your records</li>
  <li>Request a correction or amendment to your records</li>
  <li>Request restrictions on certain uses and disclosures</li>
  <li>Request to receive confidential communications by a certain method or at a certain location</li>
  <li>Receive an accounting of certain disclosures of your information</li>
  <li>Receive a paper copy of our full Notice of Privacy Practices</li>
</ul>

<h2>Our responsibilities</h2>
<p>We are required by law to maintain the privacy of your PHI, to provide you with this notice of our legal duties and privacy practices, and to follow the terms of our notice currently in effect. We will let you know promptly if a breach occurs that may have compromised the privacy or security of your information.</p>

<h2>Complaints</h2>
<p>If you believe your privacy rights have been violated, you may file a complaint with our office or with the U.S. Department of Health and Human Services. You will not be penalized or retaliated against for filing a complaint.</p>

<h2>How to reach us</h2>
<p>To exercise any of your rights, request our full notice, or ask a question, contact our office at <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> or visit us at 6053 Rochester Rd, Troy, MI 48085.</p>

<p style="color:var(--ink-soft);font-size:.92rem;margin-top:28px;padding-top:18px;border-top:1px solid var(--line)">This page is a plain-language summary for your convenience and is not a substitute for our official Notice of Privacy Practices, which governs and is available at our office.</p>
'''),
]
