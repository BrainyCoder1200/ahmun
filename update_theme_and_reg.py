import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --- 1. Theme Updates ---
# Theme Quote & Concept Text
old_theme_text = r'<blockquote class="theme-quote">.*?</blockquote>\s*<p>Time is often spoken of as a river.*?<p>"Fractures Before Midnight" invites delegates.*?</p>'
new_theme_text = '''<blockquote class="theme-quote">
                            &ldquo;Collapse is rarely immediate. Beneath every moment of crisis lie years of pressure.&rdquo;
                        </blockquote>
                        <p>Presenting to you the theme for AHMUN 8.0: <strong>Fractures Before Midnight</strong>. At the heart of our theme lies a simple truth, collapse is rarely immediate. Beneath every moment of crisis lie years of pressure, instability, and neglect. The fractures that threaten our world are often invisible, until they become impossible to ignore. As the Doomsday Clock nears midnight, it becomes increasingly urgent to understand these fractures and prevent them from becoming tomorrow’s catastrophe.</p>
                        <p>The world does not break all at once. Every conflict, every disruption, every warning sign is part of a larger story unfolding beneath the surface. With the Doomsday Clock set at just 85 seconds to midnight, which is the closest it has ever been, humanity stands closer than ever to a moment of reckoning. This theme is a call to recognize the pressures building beneath the surface and then come together to set in the reversal of the Doomsday Clock.</p>'''
html = re.sub(r'<blockquote class="theme-quote">[\s\S]*?</blockquote>[\s\S]*?<p>Time is often spoken of as a river[\s\S]*?</p>[\s\S]*?<p>"Fractures Before Midnight" invites delegates[\s\S]*?</p>', new_theme_text, html)

# Theme Visual (Doomsday Clock)
old_clock = r'<div class="shattered-clock">[\s\S]*?</svg>\s*</div>'
new_clock = '''<div class="doomsday-clock animate-trigger">
                            <div class="dd-mark">XII</div>
                            <div class="dd-hand dd-hour"></div>
                            <div class="dd-hand dd-minute"></div>
                            <svg class="dd-crack" viewBox="0 0 300 300">
                                <path d="M150 150 L120 180 L130 220 L100 280" stroke="rgba(206,172,105,0.5)" stroke-width="2" fill="none"/>
                                <path d="M150 150 L180 120 L160 80 L200 40" stroke="rgba(206,172,105,0.5)" stroke-width="2" fill="none"/>
                                <path d="M150 150 L80 140 L40 160 L0 120" stroke="rgba(206,172,105,0.5)" stroke-width="2" fill="none"/>
                            </svg>
                        </div>'''
html = re.sub(old_clock, new_clock, html)

# Timeline Text Updates
old_tl_past = r'<span class="tl-era text-gold">The Past</span>\s*<h4>Decisions That Shattered</h4>\s*<p>History is littered with moments that fractured the status quo.*?<p>'
new_tl_past = '''<span class="tl-era text-gold">The Past</span>
                                <h4>Invisible Fractures</h4>
                                <p>Collapse is rarely immediate. Beneath every moment of crisis lie years of pressure, instability, and neglect. The fractures that threaten our world are often invisible, until they become impossible to ignore.</p>'''
html = re.sub(r'<span class="tl-era text-gold">The Past</span>[\s\S]*?</p>', new_tl_past, html)

old_tl_present = r'<span class="tl-era text-gold">The Present</span>\s*<h4>Living in the Cracks</h4>\s*<p>Today, we stand on fractured ground.*?<p>'
new_tl_present = '''<span class="tl-era text-gold">The Present</span>
                                <h4>85 Seconds to Midnight</h4>
                                <p>Every conflict, every disruption, every warning sign is part of a larger story unfolding beneath the surface. With the Doomsday Clock set at just 85 seconds to midnight, humanity stands closer than ever to a moment of reckoning.</p>'''
html = re.sub(r'<span class="tl-era text-gold">The Present</span>[\s\S]*?</p>', new_tl_present, html)

old_tl_future = r'<span class="tl-era text-gold">The Future</span>\s*<h4>Piecing It Back Together</h4>\s*<p>Can fractured time be mended\? As delegates.*?<p>'
new_tl_future = '''<span class="tl-era text-gold">The Future</span>
                                <h4>Reversing the Clock</h4>
                                <p>This theme is a call to recognize the pressures building beneath the surface and then come together to set in the reversal of the Doomsday Clock.</p>'''
html = re.sub(r'<span class="tl-era text-gold">The Future</span>[\s\S]*?</p>', new_tl_future, html)

# CTA Section Updates
old_cta_title = r'<h3 class="text-gold">The Fracture Is the Invitation</h3>'
new_cta_title = r'<h3 class="text-gold">Some Fault Lines Cannot Be Ignored</h3>'
html = html.replace('<h3 class="text-gold">The Fracture Is the Invitation</h3>', '<h3 class="text-gold">Some Fault Lines Cannot Be Ignored</h3>')
html = html.replace('Every crack lets light in. Every break reveals what was hidden beneath the surface. "Fractures Before Midnight" is not a story of destruction&mdash;it is a story of <strong class="text-gold">revelation</strong>.', 'As the Doomsday Clock nears midnight, it becomes increasingly urgent to understand these fractures and prevent them from becoming tomorrow’s catastrophe.')
html = html.replace('Are you ready to step into the fracture?', 'Are you ready to reverse the clock?')


# --- 2. Registration Updates ---
# Replace `#register` with the form link in Nav and Footer
html = html.replace('<a href="#register"', '<a href="https://forms.gle/HBk9FhtNU1gdoDPh7" target="_blank" rel="noopener noreferrer"')
html = html.replace('>Registration (Opening Soon)</a>', '>Register Now</a>')
html = html.replace('>Register (Opening Soon)</a>', '>Register Now</a>')

# Hero Register Button
html = html.replace('<a href="#register" class="btn btn-gold"><i class="fa-solid fa-file-signature icon-btn"></i> Register (Opening Soon)</a>', '<a href="https://forms.gle/HBk9FhtNU1gdoDPh7" target="_blank" rel="noopener noreferrer" class="btn btn-gold"><i class="fa-solid fa-file-signature icon-btn"></i> Register Now</a>')
html = html.replace('<a href="#register" class="btn btn-gold"><i class="fa-solid fa-file-signature icon-btn"></i> Register Now</a>', '<a href="https://forms.gle/HBk9FhtNU1gdoDPh7" target="_blank" rel="noopener noreferrer" class="btn btn-gold"><i class="fa-solid fa-file-signature icon-btn"></i> Register Now</a>')

# FAQ Answer
old_faq = '<div class="faq-content"><p>Registrations for AHMUN 8.0 have not opened yet. The delegate fee is ₹2,200. Once registration goes live, links and payment portals will be accessible on this site.</p></div>'
new_faq = '<div class="faq-content"><p>Registrations for AHMUN 8.0 are <strong>now open</strong>! The delegate fee is ₹2,200. You can register right now by clicking the "Register Now" button in the navigation bar, or <a href="https://forms.gle/HBk9FhtNU1gdoDPh7" target="_blank" class="link-gold">click here</a>.</p></div>'
html = html.replace(old_faq, new_faq)


with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)


# --- 3. Style Updates for Doomsday Clock ---
with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace shattered clock css with doomsday clock css
css = re.sub(r'\.shattered-clock\{[\s\S]*?\.cracks path\{[\s\S]*?\}', '', css)

doomsday_css = """
.doomsday-clock {
    position: relative;
    width: 280px;
    height: 280px;
    border-radius: 50%;
    border: 4px solid var(--gold);
    background: rgba(11, 17, 32, 0.4);
    box-shadow: 0 0 35px rgba(206,172,105,0.25), inset 0 0 20px rgba(206,172,105,0.15);
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
    backdrop-filter: blur(5px);
}
.doomsday-clock::before {
    content: '';
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 14px; height: 14px;
    border-radius: 50%;
    background: var(--gold);
    z-index: 5;
    box-shadow: 0 0 15px var(--gold);
}
.dd-hand {
    position: absolute;
    bottom: 50%;
    left: 50%;
    transform-origin: bottom center;
    background: var(--gold);
    border-radius: 4px;
    box-shadow: 0 0 12px var(--gold);
}
.dd-minute {
    width: 4px;
    height: 110px;
    margin-left: -2px;
    transform: rotate(351deg); /* 85 Seconds to Midnight */
    animation: tick-tock 1s infinite alternate;
}
.dd-hour {
    width: 6px;
    height: 70px;
    margin-left: -3px;
    transform: rotate(0deg); /* Midnight */
}
.dd-mark {
    position: absolute;
    top: 15px;
    left: 50%;
    transform: translateX(-50%);
    color: var(--gold);
    font-family: var(--font-head);
    font-size: 1.8rem;
    font-weight: bold;
    text-shadow: 0 0 15px var(--gold);
}
.dd-crack {
    position: absolute;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 10;
}
@keyframes tick-tock {
    0% { transform: rotate(351.5deg); }
    100% { transform: rotate(352deg); }
}
"""

if '.doomsday-clock {' not in css:
    css += doomsday_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated Theme & Registration successfully")
