import os

with open("app.js", "r", encoding="utf-8") as f:
    js = f.read()

old_code = """    document.getElementById("modal-desc").innerText = desc;
    document.getElementById("meet-eb-btn").href = "#eb-" + title;"""

new_code = """    document.getElementById("modal-desc").innerText = desc;
    const meetBtn = document.getElementById("meet-eb-btn");
    meetBtn.href = "javascript:void(0)";
    meetBtn.onclick = function(e) {
        e.preventDefault();
        closeCommitteeModal();
        window.location.hash = "#executive-board";
        setTimeout(() => {
            const ebSection = document.getElementById("eb-" + title);
            if(ebSection) {
                const headerOffset = 100;
                const elementPosition = ebSection.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                window.scrollTo({ top: offsetPosition, behavior: "smooth" });
            }
        }, 50);
    };"""

js = js.replace(old_code, new_code)

with open("app.js", "w", encoding="utf-8") as f:
    f.write(js)

# Remove the old onclick from index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace('onclick="closeCommitteeModal()"><i class="fa-solid fa-users"', '><i class="fa-solid fa-users"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Fixed modal redirect logic")
