// Language is represented by the URL; remember explicit choices without redirecting shared URLs.
try {
  localStorage.setItem('little-elsewhere-language', document.documentElement.lang === 'en' ? 'en' : 'zh-CN');
} catch { /* Navigation remains usable when storage is unavailable. */ }

// Reveal each part of the landing page once, as it comes into view.
// Observe steps separately so a stacked mobile journey follows the reader.
if (document.body.classList.contains('landing-page') && 'IntersectionObserver' in window) {
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  if (!reducedMotion.matches) {
    const targets = [];
    const register = (selector, delay = 0, stagger = 0) => {
      document.querySelectorAll(selector).forEach((element, index) => {
        element.classList.add('page-reveal');
        element.style.setProperty('--reveal-delay', `${delay + index * stagger}ms`);
        targets.push(element);
      });
    };
    register('.header .brand', 0);
    register('.header nav', 90);
    register('.arrival-copy > *', 80, 120);
    register('.hero-interface', 420);
    register('.experience > h2');
    register('.journey-step', 100, 230);
    register('.journal-record-title', 80);
    register('.journal-record', 260);
    register('.journal-description', 300);
    register('.journal-focus', 480);
    register('.journal-notes-title', 400);
    register('.journal-notes', 650);
    register('.journal-todo', 850);
    register('.worlds-music-title', 80);
    register('.worlds-music-panel', 280);
    register('.worlds-music-copy', 480);
    register('.worlds-map-title', 400);
    register('.worlds-map-panel', 640);
    register('.worlds-map-copy', 800);
    register('.invitation .content > *', 0, 160);
    register('.footer-top, .footer-bottom', 0, 120);

    const reveal = element => {
      element.classList.add('page-revealed');
      observer.unobserve(element);
    };
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const element = entry.target;
        // Start nearby lazy images before the reveal reaches them.
        const images = [...element.querySelectorAll('img')];
        images.forEach(img => { img.loading = 'eager'; });
        Promise.all(images.map(img => img.decode().catch(() => {}))).then(() => {
          requestAnimationFrame(() => requestAnimationFrame(() => reveal(element)));
        });
      });
    }, {threshold: .08});
    targets.forEach(element => observer.observe(element));

    const preload = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.querySelectorAll('img').forEach(img => { img.loading = 'eager'; });
        preload.unobserve(entry.target);
      });
    }, {rootMargin:'500px'});
    targets.forEach(element => preload.observe(element));

    // Keyboard navigation should make an offscreen link immediately available.
    document.addEventListener('focusin', event => {
      const element = event.target.closest('.page-reveal');
      if (element) reveal(element);
    });
    reducedMotion.addEventListener('change', () => {
      if (!reducedMotion.matches) return;
      observer.disconnect();
      preload.disconnect();
      targets.forEach(element => element.classList.add('page-revealed'));
    });
  }
}

document.querySelectorAll('.worlds-scene').forEach(scene => {
  const resize = () => {
    scene.style.setProperty('--worlds-scale', scene.clientWidth / 4177);
    scene.style.setProperty('--worlds-panel-scale', scene.clientWidth * .84 / 1045);
  };
  resize();
  if ('ResizeObserver' in window) new ResizeObserver(resize).observe(scene);
  else window.addEventListener('resize', resize, {passive:true});
});

document.querySelectorAll('.journal-scene').forEach(scene => {
  const visuals = [...scene.querySelectorAll('.journal-visual')];
  const resize = () => {
    visuals.forEach(visual => {
      const sourceWidth = visual.classList.contains('journal-record') ? 563
        : visual.classList.contains('journal-focus') ? 1924 : 738.234;
      visual.style.setProperty('--art-scale', visual.clientWidth / sourceWidth);
    });
  };
  resize();
  if ('ResizeObserver' in window) {
    const observer = new ResizeObserver(resize);
    visuals.forEach(visual => observer.observe(visual));
  }
  else window.addEventListener('resize', resize, {passive:true});
});

// Enhance a fully visible static scene: content remains available without JS.
document.querySelectorAll('.rewards-scene').forEach(scene => {
  const canvas = scene.querySelector('.rewards-canvas');
  const layers = [...scene.querySelectorAll('.reward-layer')];
  layers.forEach(layer => {
    const drift = layer.querySelector('.reward-drift');
    if (layer.classList.contains('reward-decoration')) {
      const source = drift.firstElementChild;
      const x = parseFloat(source.style.left) || 0;
      const y = parseFloat(source.style.top) || 0;
      layer.style.setProperty('--deco-left', `${x / 4177 * 86}%`);
      layer.style.setProperty('--deco-top', `${y < 300 ? 143 : 170 + y / 1514 * 1050}px`);
      layer.style.setProperty('--deco-offset-x', `${-x}px`);
      layer.style.setProperty('--deco-offset-y', `${-y}px`);
    }
  });
  const resize = () => {
    scene.style.setProperty('--scene-scale', scene.clientWidth / 4177);
    scene.style.setProperty('--card-scale', scene.clientWidth * .43 / 552);
    scene.style.setProperty('--note-scale', scene.clientWidth * .47 / 705);
    scene.style.setProperty('--decoration-scale', scene.clientWidth / 4177);
  };
  resize();
  if ('ResizeObserver' in window) new ResizeObserver(resize).observe(scene);
  else window.addEventListener('resize', resize, {passive:true});
  if (!('IntersectionObserver' in window)) return;
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  const reveal = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-revealed');
        reveal.unobserve(entry.target);
      }
    });
  }, {rootMargin:'0px 0px -5% 0px', threshold:.08});
  if (!reducedMotion.matches) scene.classList.add('motion-ready');
  layers.forEach(layer => reveal.observe(layer));
  const active = new IntersectionObserver(([entry]) => {
    scene.classList.toggle('is-active', entry.isIntersecting && !document.hidden);
  });
  active.observe(scene);
  const preload = new IntersectionObserver(([entry]) => {
    if (!entry.isIntersecting) return;
    canvas.querySelectorAll('img').forEach(img => { img.loading = 'eager'; });
    preload.disconnect();
  }, {rootMargin:'500px'});
  preload.observe(scene);
  const preference = () => {
    if (reducedMotion.matches) {
      scene.classList.remove('motion-ready');
      layers.forEach(layer => layer.classList.add('is-revealed'));
    }
  };
  reducedMotion.addEventListener('change', preference);
  document.addEventListener('visibilitychange', () => {
    const bounds = scene.getBoundingClientRect();
    scene.classList.toggle('is-active', !document.hidden && bounds.bottom > 0 && bounds.top < innerHeight);
  });
});
