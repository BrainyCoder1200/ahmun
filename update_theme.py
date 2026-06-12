with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Meta and basic replacements
html = html.replace("Fractures of Time", "Fractures Before Midnight")
html = html.replace('data-text="Fractures">Fractures</span>', 'data-text="Fractures Before">Fractures Before</span>')
html = html.replace('<span class="theme-of">of</span>', '')
html = html.replace('<span class="glitch" data-text="Time">Time</span>', '<br><span class="glitch" style="font-family: var(--font-head); font-style: italic; color: var(--gold);" data-text="Midnight">Midnight</span>')

html = html.replace('<p class="theme-tagline">When the clock shatters, every fragment tells a different story.</p>', '<p class="theme-tagline" style="text-transform: uppercase; letter-spacing: 2px;">Some fault lines can\'t be ignored anymore.</p>')

# Fix any stray occurrences
html = html.replace("Fractures Before Midnight Before Midnight", "Fractures Before Midnight")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated theme text in HTML")
