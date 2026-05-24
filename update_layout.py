import os
import re

files = {
    'index.html': {'nav_type': 'light', 'active': 'NAV_PROCESS'},
    'story.html': {'nav_type': 'dark', 'active': 'NAV_STORY'},
    'artisans.html': {'nav_type': 'dark', 'active': 'NAV_ARTISANS'},
    'collection.html': {'nav_type': 'light', 'active': 'NAV_COLLECTION'},
    'impact.html': {'nav_type': 'light', 'active': 'NAV_IMPACT'},
    'connect.html': {'nav_type': 'light', 'active': 'NAV_CONTACT'},
}

nav_dark_hero = """<!-- TopNavBar -->
<nav class="fixed top-0 left-0 w-full z-50 flex flex-col pt-8 pb-4 px-margin-mobile md:px-margin-desktop bg-transparent transition-all duration-700 border-b border-outline-variant/0" id="main-nav">
    <div class="max-w-container-max w-full mx-auto flex items-center justify-between">
        <a href="index.html" class="flex-shrink-0 flex items-center h-8 md:h-12 overflow-hidden relative w-[120px] md:w-[160px]">
            <img src="logo-sheet.png" alt="ALOHA" class="w-full h-[200%] object-cover object-bottom transition-all duration-700" id="nav-logo" />
        </a>
        <div class="hidden md:flex items-center gap-10 font-label-ui text-label-ui uppercase tracking-widest" id="nav-links">
            <a class="NAV_STORY" href="story.html">STORY</a>
            <a class="NAV_PROCESS" href="index.html#process">CRAFT PROCESS</a>
            <a class="NAV_ARTISANS" href="artisans.html">ARTISANS</a>
            <a class="NAV_COLLECTION" href="collection.html">COLLECTION</a>
            <a class="NAV_IMPACT" href="impact.html">IMPACT</a>
            <a class="NAV_CONTACT" href="connect.html">CONTACT</a>
        </div>
        <div class="md:hidden">
            <span class="material-symbols-outlined text-3xl text-[#FDF6EC] nav-mobile-icon transition-colors duration-700">menu</span>
        </div>
    </div>
</nav>"""

nav_light_hero = """<!-- TopNavBar -->
<nav class="fixed top-0 left-0 w-full z-50 flex flex-col pt-8 pb-4 px-margin-mobile md:px-margin-desktop bg-background/90 backdrop-blur-sm transition-all duration-700 border-b border-outline-variant/30" id="main-nav">
    <div class="max-w-container-max w-full mx-auto flex items-center justify-between">
        <a href="index.html" class="flex-shrink-0 flex items-center h-8 md:h-12 overflow-hidden relative w-[120px] md:w-[160px]">
            <img src="logo-sheet.png" alt="ALOHA" class="w-full h-[200%] object-cover object-top transition-all duration-700" id="nav-logo" />
        </a>
        <div class="hidden md:flex items-center gap-10 font-label-ui text-label-ui uppercase tracking-widest" id="nav-links">
            <a class="NAV_STORY" href="story.html">STORY</a>
            <a class="NAV_PROCESS" href="index.html#process">CRAFT PROCESS</a>
            <a class="NAV_ARTISANS" href="artisans.html">ARTISANS</a>
            <a class="NAV_COLLECTION" href="collection.html">COLLECTION</a>
            <a class="NAV_IMPACT" href="impact.html">IMPACT</a>
            <a class="NAV_CONTACT" href="connect.html">CONTACT</a>
        </div>
        <div class="md:hidden">
            <span class="material-symbols-outlined text-3xl text-on-surface nav-mobile-icon transition-colors duration-700">menu</span>
        </div>
    </div>
</nav>"""

footer = """<!-- Footer -->
<footer class="bg-surface-container border-t border-outline-variant pt-24 pb-12 overflow-hidden relative w-full mt-auto text-left">
    <div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop relative z-10 w-full">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-16 mb-24">
            <div>
                <h3 class="font-display-lg text-[48px] text-primary mb-6" style="font-family: 'Libre Caslon Text', serif; font-weight: 300;">Stay Connected.</h3>
                <p class="font-body-main text-on-surface-variant mb-8 max-w-md">Subscribe to our journal for stories from the villages, new collection drops, and the history of Dhokra.</p>
                <form class="flex border-b border-primary pb-2 max-w-md">
                    <input type="email" placeholder="ENTER YOUR EMAIL" class="bg-transparent border-none outline-none flex-grow font-label-ui text-label-ui placeholder:text-on-surface-variant/50 focus:ring-0 px-0 text-primary">
                    <button type="submit" class="font-button-text text-button-text text-primary hover:text-secondary transition-colors tracking-widest">SUBSCRIBE</button>
                </form>
            </div>
            <div class="grid grid-cols-2 gap-8 md:justify-items-end">
                <div class="flex flex-col gap-4 text-left md:text-right">
                    <span class="font-label-ui text-label-ui text-secondary mb-2 tracking-widest">EXPLORE</span>
                    <a href="story.html" class="font-jost text-[14px] text-on-surface-variant hover:text-primary transition-colors tracking-widest uppercase">Our Story</a>
                    <a href="artisans.html" class="font-jost text-[14px] text-on-surface-variant hover:text-primary transition-colors tracking-widest uppercase">The Artisans</a>
                    <a href="collection.html" class="font-jost text-[14px] text-on-surface-variant hover:text-primary transition-colors tracking-widest uppercase">Collection</a>
                    <a href="impact.html" class="font-jost text-[14px] text-on-surface-variant hover:text-primary transition-colors tracking-widest uppercase">Impact Report</a>
                </div>
                <div class="flex flex-col gap-4 text-left md:text-right">
                    <span class="font-label-ui text-label-ui text-secondary mb-2 tracking-widest">SUPPORT</span>
                    <a href="connect.html" class="font-jost text-[14px] text-on-surface-variant hover:text-primary transition-colors tracking-widest uppercase">Contact Us</a>
                    <a href="#" class="font-jost text-[14px] text-on-surface-variant hover:text-primary transition-colors tracking-widest uppercase">Shipping & Returns</a>
                    <a href="#" class="font-jost text-[14px] text-on-surface-variant hover:text-primary transition-colors tracking-widest uppercase">Care Guide</a>
                    <a href="#" class="font-jost text-[14px] text-on-surface-variant hover:text-primary transition-colors tracking-widest uppercase">Terms of Service</a>
                </div>
            </div>
        </div>
        <div class="flex flex-col md:flex-row items-center justify-between border-t border-outline-variant pt-8">
            <div class="flex items-center justify-center h-8 md:h-12 overflow-hidden relative w-[120px] md:w-[160px] mb-8 md:mb-0">
                <img src="logo-sheet.png" alt="ALOHA" class="w-full h-[200%] object-cover object-top" />
            </div>
            <p class="font-jost text-[12px] tracking-[0.1em] text-on-surface-variant/70 text-center md:text-left">
                © 2024 ALOHA HERITAGE. PRESERVING THE DHOKRA LEGACY.<br/>
                <span class="italic font-body-main text-[16px] tracking-normal">Made in Odisha. Present everywhere.</span>
            </p>
            <div class="flex gap-6 mt-8 md:mt-0 font-jost text-[12px] tracking-[0.1em] uppercase">
                <a href="https://instagram.com/aloha.heritage" class="text-on-surface-variant hover:text-primary transition-colors">Instagram</a>
                <a href="#" class="text-on-surface-variant hover:text-primary transition-colors">Journal</a>
            </div>
        </div>
    </div>
</footer>"""

js_dark = """
<script>
    // GLOBAL NAV SCROLL LOGIC
    window.addEventListener('scroll', () => {
        const header = document.getElementById('main-nav');
        const logo = document.getElementById('nav-logo');
        const links = document.querySelectorAll('.nav-link-text');
        const mobileIcon = document.querySelector('.nav-mobile-icon');
        
        if (window.scrollY > 50) {
            header.classList.remove('bg-transparent', 'border-outline-variant/0');
            header.classList.add('bg-[#F5EAD0]', 'border-outline-variant/30', 'shadow-sm');
            if(logo) {
                logo.classList.remove('object-bottom');
                logo.classList.add('object-top');
            }
            links.forEach(link => {
                if(!link.classList.contains('text-secondary')) {
                    link.classList.remove('text-[#FDF6EC]');
                    link.classList.add('text-on-surface');
                }
            });
            if(mobileIcon) {
                mobileIcon.classList.remove('text-[#FDF6EC]');
                mobileIcon.classList.add('text-on-surface');
            }
        } else {
            header.classList.add('bg-transparent', 'border-outline-variant/0');
            header.classList.remove('bg-[#F5EAD0]', 'border-outline-variant/30', 'shadow-sm');
            if(logo) {
                logo.classList.add('object-bottom');
                logo.classList.remove('object-top');
            }
            links.forEach(link => {
                if(!link.classList.contains('text-secondary')) {
                    link.classList.remove('text-on-surface');
                    link.classList.add('text-[#FDF6EC]');
                }
            });
            if(mobileIcon) {
                mobileIcon.classList.add('text-[#FDF6EC]');
                mobileIcon.classList.remove('text-on-surface');
            }
        }
    });
</script>
</body>"""

js_light = """
<script>
    // GLOBAL NAV SCROLL LOGIC
    window.addEventListener('scroll', () => {
        const header = document.getElementById('main-nav');
        if (window.scrollY > 50) {
            header.classList.remove('bg-background/90', 'border-outline-variant/30');
            header.classList.add('bg-[#F5EAD0]', 'shadow-sm', 'border-outline-variant/30');
        } else {
            header.classList.remove('bg-[#F5EAD0]', 'shadow-sm');
            header.classList.add('bg-background/90', 'border-outline-variant/30');
        }
    });
</script>
</body>"""

def get_styled_nav(nav_template, active_link, is_dark):
    links = ["NAV_STORY", "NAV_PROCESS", "NAV_ARTISANS", "NAV_COLLECTION", "NAV_IMPACT", "NAV_CONTACT"]
    styled_nav = nav_template
    for link in links:
        if link == active_link:
            styled_nav = styled_nav.replace(link, "text-secondary border-b border-secondary transition-colors duration-300 nav-link-text")
        else:
            if is_dark:
                styled_nav = styled_nav.replace(link, "text-[#FDF6EC] hover:text-secondary transition-colors duration-300 nav-link-text")
            else:
                styled_nav = styled_nav.replace(link, "text-on-surface hover:text-secondary transition-colors duration-300 nav-link-text")
    return styled_nav

for file, config in files.items():
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace Nav
    # Match from <nav> or <header> to </nav> or </header>
    content = re.sub(r'<(nav|header).*?(?=id="top-nav"|id="main-nav"|class=".*?sticky.*?"|class=".*?fixed.*?").*?</\1>', 
                     get_styled_nav(nav_dark_hero if config['nav_type'] == 'dark' else nav_light_hero, config['active'], config['nav_type'] == 'dark'), 
                     content, flags=re.DOTALL | re.IGNORECASE)

    # 2. Replace Footer
    content = re.sub(r'<footer.*?>.*?</footer>', footer, content, flags=re.DOTALL | re.IGNORECASE)

    # 3. Inject JS
    if 'GLOBAL NAV SCROLL LOGIC' not in content:
        js = js_dark if config['nav_type'] == 'dark' else js_light
        content = re.sub(r'</body>', js, content, flags=re.IGNORECASE)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
