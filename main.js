// Cursor glow
const glow = document.getElementById('cursorGlow');
if (glow) {
  document.addEventListener('mousemove', e => {
    glow.style.left = e.clientX + 'px';
    glow.style.top  = e.clientY + 'px';
  });
}

// Navbar scroll effect
const navbar = document.getElementById('navbar');
if (navbar) {
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 20);
  });
}

// Mobile menu
const menuToggle = document.getElementById('menuToggle');
const mobileMenu = document.getElementById('mobileMenu');
if (menuToggle && mobileMenu) {
  menuToggle.addEventListener('click', () => mobileMenu.classList.toggle('open'));
}

// Scroll animations
const obs = new IntersectionObserver(entries => {
  entries.forEach((e, i) => {
    if (e.isIntersecting) {
      setTimeout(() => e.target.classList.add('visible'), i * 80);
    }
  });
}, { threshold: 0.08 });
document.querySelectorAll('.animate').forEach(el => obs.observe(el));

// Animated counters
function animateCounter(el, target, duration = 1800) {
  let start = null;
  const step = ts => {
    if (!start) start = ts;
    const prog = Math.min((ts - start) / duration, 1);
    const ease = 1 - Math.pow(1 - prog, 3);
    el.textContent = Math.floor(ease * target).toLocaleString();
    if (prog < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}
const counterObs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting && !e.target.dataset.counted) {
      e.target.dataset.counted = '1';
      animateCounter(e.target, parseInt(e.target.dataset.target));
    }
  });
}, { threshold: 0.4 });
document.querySelectorAll('[data-target]').forEach(el => counterObs.observe(el));
