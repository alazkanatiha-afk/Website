// script.js

// Language Changer
function changeLanguage(lang) {
    const languageFiles = {
        'tr': 'index.html',
        'en': 'index_en.html',
        'ru': 'index_ru.html',
        'de': 'index_de.html'
    };
    
    // Save theme preference before changing page
    const currentTheme = document.body.classList.contains('light-mode') ? 'light' : 'dark';
    localStorage.setItem('theme', currentTheme);
    
    // Redirect to language file
    window.location.href = languageFiles[lang];
}

// Theme Toggle Functionality
const themeToggle = document.getElementById('themeToggle');
const body = document.body;

// Check for saved theme preference or default to dark mode
const currentTheme = localStorage.getItem('theme') || 'dark';
if (currentTheme === 'light') {
    body.classList.add('light-mode');
    themeToggle.textContent = '🌙 Night';
} else {
    themeToggle.textContent = '☀️ Day';
}

themeToggle.addEventListener('click', () => {
    body.classList.toggle('light-mode');
    
    if (body.classList.contains('light-mode')) {
        themeToggle.textContent = '🌙 Night';
        localStorage.setItem('theme', 'light');
    } else {
        themeToggle.textContent = '☀️ Day';
        localStorage.setItem('theme', 'dark');
    }
});

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add active state to navigation on scroll
window.addEventListener('scroll', () => {
    let current = '';
    const sections = document.querySelectorAll('section, .hero');
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (scrollY >= (sectionTop - 200)) {
            current = section.getAttribute('id');
        }
    });

    document.querySelectorAll('nav a').forEach(link => {
        const isLightMode = body.classList.contains('light-mode');
        link.style.color = isLightMode ? '#2d3748' : '#e0e0e0';
        if (link.getAttribute('href') === `#${current}`) {
            link.style.color = isLightMode ? '#0077cc' : '#00aeff';
        }
    });
});