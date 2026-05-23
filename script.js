document.addEventListener("DOMContentLoaded", () => {
    const navbar = document.getElementById('navbar');
    
    // Dynamic Navbar styling on scroll
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.remove('transparent');
            navbar.classList.add('solid');
        } else {
            navbar.classList.add('transparent');
            navbar.classList.remove('solid');
        }
    });

    // Intersection Observer for scroll animations
    const faders = document.querySelectorAll('.fade-in, .slide-in-left, .slide-in-right');

    const appearOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const appearOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('appear');
                observer.unobserve(entry.target);
            }
        });
    }, appearOptions);

    faders.forEach(fader => {
        appearOnScroll.observe(fader);
    });
});
