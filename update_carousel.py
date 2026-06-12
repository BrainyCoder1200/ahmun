import re

# 1. Update CSS
with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Remove old carousel CSS
old_css_pattern = r'\.carousel-wrapper\{.*?\.carousel-dot\.active\{.*?\}'
# Actually, it's safer to just replace from .carousel-wrapper to .carousel-dot.active
start_idx = css.find('.carousel-wrapper')
end_idx = css.find('}', css.find('.carousel-dot.active')) + 1
if start_idx != -1 and end_idx != -1:
    css = css[:start_idx] + css[end_idx:]

new_css = """
.carousel-wrapper {
    max-width: 1000px;
    margin: 0 auto 50px;
    perspective: 1200px;
    position: relative;
}
.carousel-container {
    position: relative;
    width: 100%;
    height: 450px;
    display: flex;
    justify-content: center;
    align-items: center;
    transform-style: preserve-3d;
}
.carousel-track {
    width: 100%;
    height: 100%;
    position: absolute;
    transform-style: preserve-3d;
}
.carousel-slide {
    position: absolute;
    width: 550px;
    height: 350px;
    left: 50%;
    top: 50%;
    margin-left: -275px;
    margin-top: -175px;
    opacity: 0;
    transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.6s ease, filter 0.6s ease;
    border-radius: var(--radius);
    box-shadow: 0 15px 45px rgba(0,0,0,0.6);
    cursor: pointer;
    filter: blur(4px) brightness(0.4);
    border: 1px solid var(--glass-border);
    -webkit-box-reflect: below 5px linear-gradient(transparent 70%, rgba(255,255,255,0.2));
}
.carousel-slide.active {
    opacity: 1;
    z-index: 5;
    transform: translateX(0) scale(1) translateZ(0) rotateY(0deg);
    filter: blur(0px) brightness(1);
    box-shadow: 0 0 35px rgba(206,172,105,0.35);
    border-color: var(--gold);
    cursor: default;
}
.carousel-slide.prev {
    opacity: 0.8;
    z-index: 4;
    transform: translateX(-45%) scale(0.85) translateZ(-150px) rotateY(25deg);
}
.carousel-slide.next {
    opacity: 0.8;
    z-index: 4;
    transform: translateX(45%) scale(0.85) translateZ(-150px) rotateY(-25deg);
}
.carousel-slide.hidden-left {
    opacity: 0;
    z-index: 1;
    transform: translateX(-65%) scale(0.6) translateZ(-300px) rotateY(45deg);
}
.carousel-slide.hidden-right {
    opacity: 0;
    z-index: 1;
    transform: translateX(65%) scale(0.6) translateZ(-300px) rotateY(-45deg);
}
.carousel-slide img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: calc(var(--radius) - 1px);
}
.carousel-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(11,17,32,0.85);
    color: var(--gold);
    border: 1px solid var(--gold-border);
    width: 50px; height: 50px;
    border-radius: 50%;
    cursor: pointer;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    transition: all 0.3s;
}
.carousel-btn:hover { background: var(--gold); color: var(--bg-deep); box-shadow: var(--gold-glow); }
.prev-btn { left: -20px; }
.next-btn { right: -20px; }
.carousel-dots {
    position: absolute;
    bottom: -40px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 10px;
    z-index: 10;
}
.carousel-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    background: rgba(255,255,255,0.2);
    cursor: pointer;
    transition: all 0.3s;
}
.carousel-dot.active { background: var(--gold); transform: scale(1.4); box-shadow: 0 0 10px var(--gold); }
"""

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css + new_css)


# 2. Update JS
with open("app.js", "r", encoding="utf-8") as f:
    js = f.read()

# Find the carousel section
start_idx = js.find('// ========== 7. PAST MUN CAROUSEL ==========')
end_idx = js.find('// ========== 8. OBSERVERS', start_idx)

new_js = """// ========== 7. PAST MUN CAROUSEL ==========
    const track = document.getElementById("past-mun-track");
    const slides = Array.from(document.querySelectorAll(".carousel-slide"));
    const nextBtn = document.getElementById("carousel-next");
    const prevBtn = document.getElementById("carousel-prev");
    const dotsNav = document.getElementById("carousel-dots");
    let currentIndex = 0;
    let autoPlayInterval;

    if (slides.length > 0) {
        // Create dots
        slides.forEach((_, i) => {
            const dot = document.createElement("div");
            dot.classList.add("carousel-dot");
            if (i === 0) dot.classList.add("active");
            dot.addEventListener("click", () => {
                currentIndex = i;
                updateCarousel();
                resetAutoPlay();
            });
            dotsNav.appendChild(dot);
        });

        const dots = Array.from(document.querySelectorAll(".carousel-dot"));

        function updateCarousel() {
            slides.forEach((slide, i) => {
                slide.className = 'carousel-slide'; // Reset
                if (i === currentIndex) {
                    slide.classList.add('active');
                } else if (i === (currentIndex - 1 + slides.length) % slides.length) {
                    slide.classList.add('prev');
                } else if (i === (currentIndex + 1) % slides.length) {
                    slide.classList.add('next');
                } else if (i < currentIndex) {
                    slide.classList.add('hidden-left');
                } else {
                    slide.classList.add('hidden-right');
                }
            });

            dots.forEach(d => d.classList.remove('active'));
            dots[currentIndex].classList.add('active');
        }

        // Make side slides clickable to rotate
        slides.forEach((slide, i) => {
            slide.addEventListener('click', () => {
                if(i !== currentIndex) {
                    currentIndex = i;
                    updateCarousel();
                    resetAutoPlay();
                }
            });
        });

        nextBtn.addEventListener("click", () => {
            currentIndex = (currentIndex + 1) % slides.length;
            updateCarousel();
            resetAutoPlay();
        });

        prevBtn.addEventListener("click", () => {
            currentIndex = (currentIndex - 1 + slides.length) % slides.length;
            updateCarousel();
            resetAutoPlay();
        });

        // AutoPlay
        function resetAutoPlay() {
            clearInterval(autoPlayInterval);
            autoPlayInterval = setInterval(() => {
                currentIndex = (currentIndex + 1) % slides.length;
                updateCarousel();
            }, 4000);
        }

        // Initialize
        updateCarousel();
        resetAutoPlay();
        
        // Pause on hover
        const carouselContainer = document.querySelector('.carousel-wrapper');
        carouselContainer.addEventListener('mouseenter', () => clearInterval(autoPlayInterval));
        carouselContainer.addEventListener('mouseleave', resetAutoPlay);
    }

    """

if start_idx != -1 and end_idx != -1:
    js = js[:start_idx] + new_js + js[end_idx:]
    with open("app.js", "w", encoding="utf-8") as f:
        f.write(js)

print("Updated 3D Carousel CSS and JS")
