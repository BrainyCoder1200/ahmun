import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace in Committees Modal clicks
html = html.replace("<i class=\\'fa-solid fa-globe\\'></i>", "<img src=\\'./ICONS/UNSC.svg\\' class=\\'committee-img\\'>")
html = html.replace("<i class=\\'fa-solid fa-scale-balanced\\'></i>", "<img src=\\'./ICONS/AIPPM.svg\\' class=\\'committee-img\\'>")
html = html.replace("<i class=\\'fa-solid fa-jet-fighter\\'></i>", "<img src=\\'./ICONS/GDWC.svg\\' class=\\'committee-img\\'>")
html = html.replace("<i class=\\'fa-solid fa-handcuffs\\'></i>", "<img src=\\'./ICONS/UNODC.svg\\' class=\\'committee-img\\'>")
html = html.replace("<i class=\\'fa-solid fa-hands-holding-child\\'></i>", "<img src=\\'./ICONS/UNHRC.svg\\' class=\\'committee-img\\'>")
html = html.replace("<i class=\\'fa-solid fa-radiation\\'></i>", "<img src=\\'./ICONS/IAEA.svg\\' class=\\'committee-img\\'>")

# Replace in Committee Headers and EB Headers
html = html.replace('<div class="committee-icon"><i class="fa-solid fa-globe"></i></div>', '<div class="committee-icon"><img src="./ICONS/UNSC.svg" class="committee-img"></div>')
html = html.replace('<div class="committee-icon"><i class="fa-solid fa-scale-balanced"></i></div>', '<div class="committee-icon"><img src="./ICONS/AIPPM.svg" class="committee-img"></div>')
html = html.replace('<div class="committee-icon"><i class="fa-solid fa-jet-fighter"></i></div>', '<div class="committee-icon"><img src="./ICONS/GDWC.svg" class="committee-img"></div>')
html = html.replace('<div class="committee-icon"><i class="fa-solid fa-handcuffs"></i></div>', '<div class="committee-icon"><img src="./ICONS/UNODC.svg" class="committee-img"></div>')
html = html.replace('<div class="committee-icon"><i class="fa-solid fa-hands-holding-child"></i></div>', '<div class="committee-icon"><img src="./ICONS/UNHRC.svg" class="committee-img"></div>')
html = html.replace('<div class="committee-icon"><i class="fa-solid fa-radiation"></i></div>', '<div class="committee-icon"><img src="./ICONS/IAEA.svg" class="committee-img"></div>')

# EB Headers
html = html.replace('<h3 class="eb-group-title"><i class="fa-solid fa-globe"></i> United Nations Security Council</h3>', '<h3 class="eb-group-title"><img src="./ICONS/UNSC.svg" class="eb-title-img"> United Nations Security Council</h3>')
html = html.replace('<h3 class="eb-group-title"><i class="fa-solid fa-scale-balanced"></i> All India Political Parties Meet</h3>', '<h3 class="eb-group-title"><img src="./ICONS/AIPPM.svg" class="eb-title-img"> All India Political Parties Meet</h3>')
html = html.replace('<h3 class="eb-group-title"><i class="fa-solid fa-jet-fighter"></i> Global Defense and War Council</h3>', '<h3 class="eb-group-title"><img src="./ICONS/GDWC.svg" class="eb-title-img"> Global Defense and War Council</h3>')
html = html.replace('<h3 class="eb-group-title"><i class="fa-solid fa-handcuffs"></i> United Nations Office on Drugs and Crime</h3>', '<h3 class="eb-group-title"><img src="./ICONS/UNODC.svg" class="eb-title-img"> United Nations Office on Drugs and Crime</h3>')
html = html.replace('<h3 class="eb-group-title"><i class="fa-solid fa-hands-holding-child"></i> United Nations Human Rights Council</h3>', '<h3 class="eb-group-title"><img src="./ICONS/UNHRC.svg" class="eb-title-img"> United Nations Human Rights Council</h3>')
html = html.replace('<h3 class="eb-group-title"><i class="fa-solid fa-radiation"></i> International Atomic Energy Agency</h3>', '<h3 class="eb-group-title"><img src="./ICONS/IAEA.svg" class="eb-title-img"> International Atomic Energy Agency</h3>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated icons in HTML")
