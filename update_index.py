import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Define descriptions
desc = {
    "UNSC": "The UNSC is the premier forum for international crisis management. It holds the primary responsibility for the maintenance of international peace and security, wielding the unique power to issue binding resolutions, impose sanctions, and authorize military action.",
    "AIPPM": "The AIPPM serves as a dynamic platform for diverse political leaders to engage in intense debate over national policies. It simulates the chaotic yet crucial process of consensus-building in the world's largest democracy, focusing on internal security, economic reform, and social justice.",
    "GDWC": "A specialized crisis committee dedicated to navigating the complex landscape of modern warfare and international defense strategy. Delegates must respond rapidly to escalating military conflicts, intelligence leaks, and geopolitical shifts to prevent global catastrophe.",
    "UNODC": "The UNODC is a global leader in the fight against illicit drugs and international crime. This committee addresses the interconnected threats of transnational organized crime, corruption, and terrorism, working to establish robust legal frameworks and cooperative enforcement strategies.",
    "UNHRC": "Dedicated to the promotion and protection of human rights globally. The UNHRC investigates human rights violations, addresses systemic discrimination, and formulates international standards to protect the most vulnerable populations across borders.",
    "IAEA": "The world's central intergovernmental forum for scientific and technical co-operation in the nuclear field. The IAEA works for the safe, secure, and peaceful uses of nuclear science and technology, while critically preventing the proliferation of nuclear weapons."
}

# The new HTML for Committees
committees_html = f"""<!-- ==================== COMMITTEES SECTION ==================== -->
        <section id="committees" class="route-section">
            <div class="container section-padding">
                <div class="section-header text-center animate-trigger">
                    <span class="section-subtitle">THE DEBATE ROOMS</span>
                    <h2 class="section-title">Committees</h2>
                    <div class="section-line"></div>
                </div>

                <div class="committees-grid animate-trigger">
                    <!-- UNSC -->
                    <div class="glass-card committee-card" onclick="openCommitteeModal('UNSC', 'United Nations Security Council', '<i class=\\'fa-solid fa-globe\\'></i>', 'Addressing the Crisis in the Democratic Republic of the Congo with Special Emphasis on Illicit Mineral Trade and Foreign Intervention in the African continent.', `{desc['UNSC']}`)">
                        <div class="committee-header">
                            <div class="committee-icon"><i class="fa-solid fa-globe"></i></div>
                            <h3>UNSC</h3>
                            <p class="committee-full-name">United Nations Security Council</p>
                        </div>
                        <div class="committee-agenda">
                            <h4 class="text-gold">Agenda</h4>
                            <p>Addressing the Crisis in the Democratic Republic of the Congo...</p>
                            <span class="read-more">Click to read more</span>
                        </div>
                    </div>

                    <!-- AIPPM -->
                    <div class="glass-card committee-card" onclick="openCommitteeModal('AIPPM', 'All India Political Parties Meet', '<i class=\\'fa-solid fa-scale-balanced\\'></i>', 'Discussing Labour Law Reforms Amid Rising Cost of Living and Mass Civil Unrest in the NCR.', `{desc['AIPPM']}`)">
                        <div class="committee-header">
                            <div class="committee-icon"><i class="fa-solid fa-scale-balanced"></i></div>
                            <h3>AIPPM</h3>
                            <p class="committee-full-name">All India Political Parties Meet</p>
                        </div>
                        <div class="committee-agenda">
                            <h4 class="text-gold">Agenda</h4>
                            <p>Discussing Labour Law Reforms Amid Rising Cost of Living...</p>
                            <span class="read-more">Click to read more</span>
                        </div>
                    </div>

                    <!-- GDWC -->
                    <div class="glass-card committee-card" onclick="openCommitteeModal('GDWC', 'Global Defense and War Council', '<i class=\\'fa-solid fa-jet-fighter\\'></i>', 'Deliberating upon the Escalation of the US–Iran–Israel Conflict with Special Emphasis on Regional Destabilisation and Strategic Military Response.', `{desc['GDWC']}`)">
                        <div class="committee-header">
                            <div class="committee-icon"><i class="fa-solid fa-jet-fighter"></i></div>
                            <h3>GDWC</h3>
                            <p class="committee-full-name">Global Defense and War Council</p>
                        </div>
                        <div class="committee-agenda">
                            <h4 class="text-gold">Agenda</h4>
                            <p>Deliberating upon the Escalation of the US–Iran–Israel Conflict...</p>
                            <span class="read-more">Click to read more</span>
                        </div>
                    </div>

                    <!-- UNODC -->
                    <div class="glass-card committee-card" onclick="openCommitteeModal('UNODC', 'United Nations Office on Drugs and Crime', '<i class=\\'fa-solid fa-handcuffs\\'></i>', 'Discussing the Threat Posed by Transnational Organised Crime with Special Emphasis on Gang Violence, Arms Smuggling, and Criminal Governance.', `{desc['UNODC']}`)">
                        <div class="committee-header">
                            <div class="committee-icon"><i class="fa-solid fa-handcuffs"></i></div>
                            <h3>UNODC</h3>
                            <p class="committee-full-name">United Nations Office on Drugs and Crime</p>
                        </div>
                        <div class="committee-agenda">
                            <h4 class="text-gold">Agenda</h4>
                            <p>Discussing the Threat Posed by Transnational Organised Crime...</p>
                            <span class="read-more">Click to read more</span>
                        </div>
                    </div>

                    <!-- UNHRC -->
                    <div class="glass-card committee-card" onclick="openCommitteeModal('UNHRC', 'United Nations Human Rights Council', '<i class=\\'fa-solid fa-hands-holding-child\\'></i>', 'Deliberating upon Human Rights Violations in the Global Migration Crisis with Special Emphasis on Forced Deportations, Xenophobia, and Refugee Protection.', `{desc['UNHRC']}`)">
                        <div class="committee-header">
                            <div class="committee-icon"><i class="fa-solid fa-hands-holding-child"></i></div>
                            <h3>UNHRC</h3>
                            <p class="committee-full-name">United Nations Human Rights Council</p>
                        </div>
                        <div class="committee-agenda">
                            <h4 class="text-gold">Agenda</h4>
                            <p>Deliberating upon Human Rights Violations in the Global Migration Crisis...</p>
                            <span class="read-more">Click to read more</span>
                        </div>
                    </div>

                    <!-- IAEA -->
                    <div class="glass-card committee-card" onclick="openCommitteeModal('IAEA', 'International Atomic Energy Agency', '<i class=\\'fa-solid fa-radiation\\'></i>', 'Addressing the Threat of Nuclear Terrorism with Special Emphasis on Illicit Trafficking of Radioactive Materials and Non-State Actors.', `{desc['IAEA']}`)">
                        <div class="committee-header">
                            <div class="committee-icon"><i class="fa-solid fa-radiation"></i></div>
                            <h3>IAEA</h3>
                            <p class="committee-full-name">International Atomic Energy Agency</p>
                        </div>
                        <div class="committee-agenda">
                            <h4 class="text-gold">Agenda</h4>
                            <p>Addressing the Threat of Nuclear Terrorism with Special Emphasis...</p>
                            <span class="read-more">Click to read more</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

# Replace the entire committees section
start_tag = "<!-- ==================== COMMITTEES SECTION ==================== -->"
end_tag = "<!-- ==================== EXECUTIVE BOARD SECTION ==================== -->"

start_idx = content.find(start_tag)
end_idx = content.find(end_tag)

if start_idx == -1 or end_idx == -1:
    print("Could not find sections!")
    exit()

# Add Modal HTML at the very end before </body>
modal_html = """

    <!-- Committee Modal -->
    <div class="modal-overlay" id="committee-modal">
        <div class="modal-content glass-card">
            <button class="modal-close" onclick="closeCommitteeModal()"><i class="fa-solid fa-xmark"></i></button>
            <div class="modal-header">
                <div class="modal-icon" id="modal-icon"></div>
                <div>
                    <h3 id="modal-title"></h3>
                    <p id="modal-fullname"></p>
                </div>
            </div>
            <div class="modal-body">
                <div class="modal-section">
                    <h4 class="text-gold"><i class="fa-solid fa-bullseye"></i> Agenda</h4>
                    <p id="modal-agenda"></p>
                </div>
                <div class="modal-section">
                    <h4 class="text-gold"><i class="fa-solid fa-circle-info"></i> About the Committee</h4>
                    <p id="modal-desc"></p>
                </div>
            </div>
        </div>
    </div>
"""

new_content = content[:start_idx] + committees_html + "\n\n        " + content[end_idx:]

if "<!-- Committee Modal -->" not in new_content:
    new_content = new_content.replace("</body>", modal_html + "\n</body>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("HTML modified successfully.")
