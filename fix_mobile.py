with open("style.css", "a", encoding="utf-8") as f:
    f.write("""
/* Mobile Fixes for 3D Carousel and Clock */
@media(max-width: 768px) {
    .carousel-container {
        height: 300px;
    }
    .carousel-slide {
        width: 80%;
        height: 200px;
        margin-left: -40%;
        margin-top: -100px;
    }
    .doomsday-clock {
        width: 220px;
        height: 220px;
    }
    .dd-minute {
        height: 80px;
    }
    .dd-hour {
        height: 50px;
    }
    .dd-mark {
        font-size: 1.2rem;
        top: 10px;
    }
}
@media(max-width: 480px) {
    .carousel-container {
        height: 250px;
    }
    .carousel-slide {
        width: 90%;
        height: 180px;
        margin-left: -45%;
        margin-top: -90px;
    }
    .doomsday-clock {
        width: 200px;
        height: 200px;
    }
    .dd-minute {
        height: 70px;
    }
    .dd-hour {
        height: 40px;
    }
}
""")
print("Added mobile media queries.")
