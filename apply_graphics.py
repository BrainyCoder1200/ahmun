import re

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add cursor and orbs right after <body>
if 'class="cursor-glow"' not in html:
    injection = """
    <!-- Sleek Graphics Elements -->
    <div class="cursor-glow" id="cursor-glow"></div>
    <div class="ambient-orb orb-1"></div>
    <div class="ambient-orb orb-2"></div>
    <div class="ambient-orb orb-3"></div>
"""
    html = html.replace('<body>', '<body>\n' + injection)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 2. Update style.css
css_injection = """
/* ============================================================
   SLEEK GRAPHICS (Aura, Orbs, Sweeps)
   ============================================================ */
/* Cursor Glow */
.cursor-glow {
    position: fixed;
    top: 0; left: 0;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(206,172,105,0.15) 0%, rgba(0,0,0,0) 70%);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    pointer-events: none;
    z-index: 9999;
    transition: width 0.3s, height 0.3s, background 0.3s;
    mix-blend-mode: screen;
}
body:hover .cursor-glow { opacity: 1; }

/* Ambient Orbs */
.ambient-orb {
    position: fixed;
    border-radius: 50%;
    filter: blur(100px);
    z-index: -1;
    pointer-events: none;
    opacity: 0.4;
    animation: floatOrb 20s infinite alternate ease-in-out;
}
.orb-1 {
    width: 600px; height: 600px;
    background: rgba(16, 32, 64, 0.6);
    top: -100px; left: -100px;
}
.orb-2 {
    width: 500px; height: 500px;
    background: rgba(206, 172, 105, 0.1);
    bottom: -100px; right: -50px;
    animation-delay: -5s;
}
.orb-3 {
    width: 400px; height: 400px;
    background: rgba(16, 40, 80, 0.5);
    top: 40%; left: 60%;
    animation-delay: -10s;
}
@keyframes floatOrb {
    0% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(50px, 30px) scale(1.1); }
    100% { transform: translate(-30px, 60px) scale(0.9); }
}

/* Glass Sweep Reflection */
.committee-card, .eb-card, .glass-card {
    position: relative;
    overflow: hidden;
}
.committee-card::after, .eb-card::after, .glass-card::after {
    content: '';
    position: absolute;
    top: 0; left: -150%;
    width: 50%; height: 100%;
    background: linear-gradient(to right, rgba(255,255,255,0) 0%, rgba(255,255,255,0.05) 50%, rgba(255,255,255,0) 100%);
    transform: skewX(-25deg);
    transition: left 0.7s ease;
    z-index: 1;
    pointer-events: none;
}
.committee-card:hover::after, .eb-card:hover::after, .glass-card:hover::after {
    left: 200%;
}

/* Make contents of cards sit above the sweep */
.committee-card > *, .eb-card > *, .glass-card > * {
    position: relative;
    z-index: 2;
}

/* Glowing Neon Lines */
.section-line {
    width: 120px;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    box-shadow: 0 0 10px var(--gold);
    margin: 20px auto;
    border: none;
}
"""

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace old section-line
if ".section-line{" in css:
    css = re.sub(r'\.section-line\s*\{[^}]+\}', '', css)
if "/* Glowing Neon Lines */" not in css:
    css += "\n" + css_injection

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

# 3. Update app.js
js_injection = """
    // ========== CURSOR GLOW EFFECT ==========
    const cursorGlow = document.getElementById('cursor-glow');
    if (cursorGlow) {
        document.addEventListener('mousemove', (e) => {
            cursorGlow.style.left = e.clientX + 'px';
            cursorGlow.style.top = e.clientY + 'px';
        });
        
        // Expand glow on interactive elements
        const interactives = document.querySelectorAll('a, button, .committee-card, .eb-card');
        interactives.forEach(el => {
            el.addEventListener('mouseenter', () => {
                cursorGlow.style.width = '400px';
                cursorGlow.style.height = '400px';
                cursorGlow.style.background = 'radial-gradient(circle, rgba(206,172,105,0.25) 0%, rgba(0,0,0,0) 70%)';
            });
            el.addEventListener('mouseleave', () => {
                cursorGlow.style.width = '300px';
                cursorGlow.style.height = '300px';
                cursorGlow.style.background = 'radial-gradient(circle, rgba(206,172,105,0.15) 0%, rgba(0,0,0,0) 70%)';
            });
        });
    }
"""

with open("app.js", "r", encoding="utf-8") as f:
    js = f.read()

if "CURSOR GLOW EFFECT" not in js:
    # Append inside DOMContentLoaded
    js = js.replace('observeAll();', js_injection + '\n    observeAll();')

with open("app.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Sleek graphics applied!")
