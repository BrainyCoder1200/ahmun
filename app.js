/* AHMUN 8.0 — "Fractures of Time" — App Controller */

document.addEventListener("DOMContentLoaded", () => {

    // ========== 1. SCROLL ANIMATIONS (must be first) ==========
    const animObs = new IntersectionObserver((entries) => {
        entries.forEach(e => {
            if (e.isIntersecting) { e.target.classList.add("visible"); animObs.unobserve(e.target); }
        });
    }, { threshold: 0.08, rootMargin: "0px 0px -30px 0px" });

    function observeAll() {
        document.querySelectorAll(".animate-trigger").forEach(el => animObs.observe(el));
    }

    function triggerSectionAnimations(section) {
        observeAll();
        section.querySelectorAll(".animate-trigger").forEach(el => {
            setTimeout(() => {
                if (el.getBoundingClientRect().top < window.innerHeight) el.classList.add("visible");
            }, 60);
        });
    }

    // ========== 2. PARTICLE BACKGROUND ==========
    const canvas = document.getElementById("particle-bg");
    if (canvas) {
        const ctx = canvas.getContext("2d");
        let particles = [];
        function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
        resizeCanvas();
        window.addEventListener("resize", resizeCanvas);

        class Particle {
            constructor() { this.reset(); }
            reset() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 1.8 + 0.3;
                this.speedX = (Math.random() - 0.5) * 0.3;
                this.speedY = (Math.random() - 0.5) * 0.3;
                this.opacity = Math.random() * 0.35 + 0.08;
            }
            update() {
                this.x += this.speedX;
                this.y += this.speedY;
                if (this.x < 0 || this.x > canvas.width || this.y < 0 || this.y > canvas.height) this.reset();
            }
            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(253,201,52,${this.opacity})`;
                ctx.fill();
            }
        }
        for (let i = 0; i < 50; i++) particles.push(new Particle());

        function animateParticles() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach(p => { p.update(); p.draw(); });
            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 110) {
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.strokeStyle = `rgba(66,115,148,${0.06 * (1 - dist / 110)})`;
                        ctx.lineWidth = 0.5;
                        ctx.stroke();
                    }
                }
            }
            requestAnimationFrame(animateParticles);
        }
        animateParticles();
    }

    // ========== 3. SPA HASH ROUTING ==========
    const sections = document.querySelectorAll(".route-section");
    const navLinks = document.querySelectorAll(".nav-link");
    const mobileMenuBtn = document.getElementById("mobile-menu-btn");
    const navLinksList = document.getElementById("nav-links-list");

    function navigateToHash() {
        const hash = window.location.hash || "#home";
        let target = document.querySelector(hash);
        if (!target) { window.location.hash = "#home"; return; }

        sections.forEach(s => s.classList.remove("active"));
        if (navLinksList) navLinksList.classList.remove("mobile-open");
        if (mobileMenuBtn) mobileMenuBtn.classList.remove("open");
        target.classList.add("active");

        navLinks.forEach(link => {
            link.classList.toggle("active", link.getAttribute("href") === hash);
        });

        window.scrollTo({ top: 0, behavior: "instant" });
        triggerSectionAnimations(target);
        if (hash === "#theme") initRiftCanvas();
    }

    window.addEventListener("hashchange", navigateToHash);

    // ========== 4. MOBILE MENU ==========
    if (mobileMenuBtn && navLinksList) {
        mobileMenuBtn.addEventListener("click", () => {
            mobileMenuBtn.classList.toggle("open");
            navLinksList.classList.toggle("mobile-open");
        });
        navLinksList.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", () => {
                mobileMenuBtn.classList.remove("open");
                navLinksList.classList.remove("mobile-open");
            });
        });
    }

    // ========== 5. HEADER SCROLL ==========
    const header = document.getElementById("main-header");
    if (header) {
        window.addEventListener("scroll", () => {
            header.classList.toggle("scrolled", window.scrollY > 50);
        });
    }

    // ========== 6. COUNTDOWN (July 11, 2026 08:00 AM) ==========
    const targetDate = new Date("2026-07-11T08:00:00").getTime();
    const daysEl = document.getElementById("days");
    const hoursEl = document.getElementById("hours");
    const minsEl = document.getElementById("minutes");
    const secsEl = document.getElementById("seconds");

    function updateCountdown() {
        const gap = targetDate - Date.now();
        if (gap <= 0) {
            [daysEl, hoursEl, minsEl, secsEl].forEach(el => { if (el) el.innerText = "00"; });
            return;
        }
        const d = Math.floor(gap / 86400000);
        const h = Math.floor((gap % 86400000) / 3600000);
        const m = Math.floor((gap % 3600000) / 60000);
        const s = Math.floor((gap % 60000) / 1000);
        if (daysEl) daysEl.innerText = String(d).padStart(2, "0");
        if (hoursEl) hoursEl.innerText = String(h).padStart(2, "0");
        if (minsEl) minsEl.innerText = String(m).padStart(2, "0");
        if (secsEl) secsEl.innerText = String(s).padStart(2, "0");
    }
    updateCountdown();
    setInterval(updateCountdown, 1000);

    // ========== 7. ANIMATED STAT COUNTERS ==========
    const statNumbers = document.querySelectorAll(".stat-number");
    let statsAnimated = false;
    function animateStats() {
        if (statsAnimated) return;
        statsAnimated = true;
        statNumbers.forEach(el => {
            const target = parseInt(el.dataset.target);
            const duration = 1500;
            const start = performance.now();
            function step(now) {
                const progress = Math.min((now - start) / duration, 1);
                const eased = 1 - Math.pow(1 - progress, 3);
                el.innerText = Math.round(target * eased);
                if (progress < 1) requestAnimationFrame(step);
            }
            requestAnimationFrame(step);
        });
    }
    const statsRibbon = document.querySelector(".stats-ribbon");
    if (statsRibbon) {
        const statsObs = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) { animateStats(); statsObs.unobserve(statsRibbon); }
        }, { threshold: 0.3 });
        statsObs.observe(statsRibbon);
    }

    // ========== 8. CAROUSEL ==========
    const track = document.getElementById("past-mun-track");
    if (track) {
        const slides = Array.from(track.querySelectorAll(".carousel-slide"));
        const nextBtn = document.getElementById("carousel-next");
        const prevBtn = document.getElementById("carousel-prev");
        const dotsContainer = document.getElementById("carousel-dots");
        let current = 0;
        let autoTimer;

        slides.forEach((_, i) => {
            const dot = document.createElement("div");
            dot.classList.add("carousel-dot");
            if (i === 0) dot.classList.add("active");
            dot.addEventListener("click", () => { current = i; update(); resetAuto(); });
            dotsContainer.appendChild(dot);
        });
        const dots = Array.from(dotsContainer.querySelectorAll(".carousel-dot"));

        function update() {
            slides.forEach((s, i) => { s.classList.toggle("active", i === current); });
            dots.forEach((d, i) => { d.classList.toggle("active", i === current); });
        }
        function next() { current = (current + 1) % slides.length; update(); }
        function prev() { current = (current - 1 + slides.length) % slides.length; update(); }
        function resetAuto() { clearInterval(autoTimer); autoTimer = setInterval(next, 4500); }

        if (nextBtn) nextBtn.addEventListener("click", () => { next(); resetAuto(); });
        if (prevBtn) prevBtn.addEventListener("click", () => { prev(); resetAuto(); });
        resetAuto();
    }

    // ========== 9. FAQ ACCORDION ==========
    const faqItems = document.querySelectorAll(".faq-item");
    faqItems.forEach(item => {
        const trigger = item.querySelector(".faq-trigger");
        if (trigger) {
            trigger.addEventListener("click", () => {
                const isActive = item.classList.contains("active");
                faqItems.forEach(other => other.classList.remove("active"));
                if (!isActive) item.classList.add("active");
            });
        }
    });

    // ========== 10. FAQ SEARCH ==========
    const faqSearch = document.getElementById("faq-search-input");
    const faqClear = document.getElementById("faq-search-clear");
    const faqEmpty = document.getElementById("faq-empty-state");
    if (faqSearch) {
        faqSearch.addEventListener("input", () => {
            const q = faqSearch.value.toLowerCase().trim();
            if (faqClear) faqClear.style.display = q.length > 0 ? "block" : "none";
            let matches = 0;
            faqItems.forEach(item => {
                const text = item.textContent.toLowerCase();
                const kw = (item.dataset.keywords || "").toLowerCase();
                const match = text.includes(q) || kw.includes(q);
                item.classList.toggle("hidden", !match);
                if (match) matches++;
            });
            if (faqEmpty) faqEmpty.classList.toggle("hidden", matches > 0);
        });
        if (faqClear) faqClear.addEventListener("click", () => {
            faqSearch.value = "";
            faqSearch.dispatchEvent(new Event("input"));
            faqSearch.focus();
        });
    }



    // ========== 12. RIFT CANVAS (Theme page) ==========
    let riftInitialized = false;
    function initRiftCanvas() {
        if (riftInitialized) return;
        const rc = document.getElementById("rift-canvas");
        if (!rc) return;
        riftInitialized = true;
        const rctx = rc.getContext("2d");
        function sizeRift() {
            const p = rc.parentElement;
            rc.width = p.offsetWidth;
            rc.height = p.offsetHeight;
        }
        sizeRift();
        window.addEventListener("resize", sizeRift);

        const rp = [];
        for (let i = 0; i < 70; i++) {
            rp.push({
                x: Math.random() * rc.width, y: Math.random() * rc.height,
                size: Math.random() * 2 + 0.5, speedX: (Math.random() - 0.5) * 0.5,
                speedY: (Math.random() - 0.5) * 0.5, opacity: Math.random() * 0.4 + 0.1,
                color: Math.random() > 0.5 ? "253,201,52" : "122,165,199"
            });
        }

        function drawRift() {
            rctx.clearRect(0, 0, rc.width, rc.height);
            const grd = rctx.createRadialGradient(rc.width / 2, rc.height / 2, 0, rc.width / 2, rc.height / 2, rc.width * 0.4);
            grd.addColorStop(0, "rgba(253,201,52,0.03)");
            grd.addColorStop(1, "transparent");
            rctx.fillStyle = grd;
            rctx.fillRect(0, 0, rc.width, rc.height);

            const time = Date.now() * 0.001;
            // Main rift line
            rctx.beginPath();
            rctx.moveTo(rc.width / 2, 0);
            for (let y = 0; y < rc.height; y += 3) {
                const offset = Math.sin(y * 0.02 + time) * 15 + Math.sin(y * 0.005 + time * 0.5) * 30;
                rctx.lineTo(rc.width / 2 + offset, y);
            }
            rctx.strokeStyle = "rgba(253,201,52,0.1)";
            rctx.lineWidth = 1.5;
            rctx.stroke();

            // Particles
            rp.forEach(p => {
                p.x += p.speedX; p.y += p.speedY;
                if (p.x < 0 || p.x > rc.width) p.speedX *= -1;
                if (p.y < 0 || p.y > rc.height) p.speedY *= -1;
                rctx.beginPath();
                rctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                rctx.fillStyle = `rgba(${p.color},${p.opacity})`;
                rctx.fill();
            });
            requestAnimationFrame(drawRift);
        }
        drawRift();
    }

    // ========== 13. FRACTURE TEXT EFFECT ==========
    // Animate crack SVG lines on theme title when visible
    const themeHero = document.getElementById("theme-hero");
    if (themeHero) {
        const thObs = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                themeHero.classList.add("revealed");
                thObs.unobserve(themeHero);
            }
        }, { threshold: 0.2 });
        thObs.observe(themeHero);
    }

    // ========== INIT ROUTING (must be last) ==========
    observeAll();
    navigateToHash();
});
