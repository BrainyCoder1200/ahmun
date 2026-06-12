import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Info bar
html = html.replace('<span class="info-value text-gold">TBA</span>', '<span class="info-value text-gold">₹2,200</span>')

# 2. Brochure detail text
html = html.replace(
    '<p>The official brochure with fee details, schedule, and committee slots will be published here once registration dates are announced.</p>',
    '<p>The official brochure with schedule and committee slots will be published here once registration dates are announced. The delegation fee is ₹2,200.</p>'
)

# 3. FAQ answer
html = html.replace(
    '<div class="faq-content"><p>Registrations for AHMUN 8.0 have not opened yet, and the delegate fee is currently undecided. Once registration goes live, links and payment portals will be accessible on this site.</p></div>',
    '<div class="faq-content"><p>Registrations for AHMUN 8.0 have not opened yet. The delegate fee is ₹2,200. Once registration goes live, links and payment portals will be accessible on this site.</p></div>'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Fee updated successfully")
