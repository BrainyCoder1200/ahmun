import os

css_code = """
/* ============================================================
   MODALS
   ============================================================ */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(11, 17, 32, 0.85);
    backdrop-filter: blur(10px);
    z-index: 2000;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.4s var(--ease);
}
.modal-overlay.active {
    opacity: 1;
    pointer-events: auto;
}
.modal-content {
    background: var(--glass);
    border: 1px solid var(--gold-border);
    box-shadow: var(--gold-glow);
    border-radius: var(--radius);
    width: 100%;
    max-width: 600px;
    max-height: 90vh;
    overflow-y: auto;
    position: relative;
    transform: translateY(30px);
    transition: transform 0.4s var(--ease);
    padding: 40px;
}
.modal-overlay.active .modal-content {
    transform: translateY(0);
}
.modal-close {
    position: absolute;
    top: 20px;
    right: 20px;
    background: transparent;
    border: none;
    color: var(--text-muted);
    font-size: 1.5rem;
    cursor: pointer;
    transition: color 0.2s;
}
.modal-close:hover {
    color: var(--gold);
}
.modal-header {
    display: flex;
    align-items: center;
    gap: 20px;
    margin-bottom: 30px;
    border-bottom: 1px solid var(--glass-border);
    padding-bottom: 20px;
}
.modal-icon {
    width: 60px;
    height: 60px;
    background: rgba(253, 201, 52, 0.1);
    color: var(--gold);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    border: 1px solid var(--gold-border);
    flex-shrink: 0;
}
#modal-title {
    font-size: 2rem;
    font-family: var(--font-head);
    color: var(--text);
    margin-bottom: 4px;
}
#modal-fullname {
    font-size: 0.9rem;
    color: var(--text-sec);
    text-transform: uppercase;
    letter-spacing: 1px;
}
.modal-section {
    margin-bottom: 24px;
}
.modal-section:last-child {
    margin-bottom: 0;
}
.modal-section h4 {
    font-size: 1.1rem;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.modal-section p {
    font-size: 0.95rem;
    line-height: 1.7;
    color: var(--text);
}
.read-more {
    display: inline-block;
    margin-top: 12px;
    font-size: 0.85rem;
    color: var(--gold);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    cursor: pointer;
    transition: color 0.3s;
}
.committee-card {
    cursor: pointer;
}
.committee-card:hover .read-more {
    text-decoration: underline;
}

@media(max-width: 600px) {
    .modal-content { padding: 24px; }
    .modal-header { flex-direction: column; text-align: center; gap: 12px; }
}
"""

js_code = """
// ========== MODALS ==========
function openCommitteeModal(title, fullname, iconHtml, agenda, desc) {
    document.getElementById("modal-title").innerText = title;
    document.getElementById("modal-fullname").innerText = fullname;
    document.getElementById("modal-icon").innerHTML = iconHtml;
    document.getElementById("modal-agenda").innerText = agenda;
    document.getElementById("modal-desc").innerText = desc;
    
    document.getElementById("committee-modal").classList.add("active");
    document.body.style.overflow = "hidden"; // Prevent background scrolling
}

function closeCommitteeModal() {
    document.getElementById("committee-modal").classList.remove("active");
    document.body.style.overflow = "";
}

// Close modal when clicking outside of the content
document.getElementById("committee-modal").addEventListener("click", function(e) {
    if (e.target === this) {
        closeCommitteeModal();
    }
});
"""

# Append CSS before the RESPONSIVE section to ensure media queries override correctly
with open("style.css", "r", encoding="utf-8") as f:
    css_content = f.read()

responsive_marker = "/* ============================================================\n   RESPONSIVE"
if responsive_marker in css_content:
    css_content = css_content.replace(responsive_marker, css_code + "\n" + responsive_marker)
else:
    css_content += "\n" + css_code

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

# Append JS at the end
with open("app.js", "a", encoding="utf-8") as f:
    f.write("\n" + js_code)

print("Appended Modal CSS and JS.")
