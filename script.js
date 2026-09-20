(() => {
  'use strict';
  const email = window.JEVAI_CONFIG?.email?.trim();
  if (email && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    document.querySelectorAll('[data-contact]').forEach(container => {
      const link = document.createElement('a');
      link.href = 'mailto:' + email;
      link.dataset.cursor = 'say hello';
      link.textContent = email;
      container.replaceChildren(link);
    });
  }

  // Visual formulas ported from https://cloudesign.space/product/ (2026-09-20).
  // Only lifecycle handling is adapted: redraw on input instead of an idle RAF loop.
  const canvas = document.getElementById('field');
  const ctx = canvas?.getContext('2d');
  if (!ctx) return;
  const cursor = document.querySelector('.cursor-ui');
  const label = document.querySelector('.cursor-label');
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  const finePointer = matchMedia('(any-pointer: fine)');
  const mouse = { x: -9999, y: -9999 };
  let frame = 0;

  function drawMesh() {
    frame = 0;
    if (reducedMotion.matches) return;
    const w = innerWidth, h = innerHeight, step = 26, R = 190;
    ctx.clearRect(0, 0, w, h);
    const mx = mouse.x, my = mouse.y;
    ctx.fillStyle = 'rgba(14,17,22,0.13)';
    for (let x = step / 2; x < w; x += step) {
      const near = Math.abs(x - mx) < R;
      for (let y = step / 2; y < h; y += step) {
        if (!near || Math.abs(y - my) > R) {
          ctx.fillRect(x - 0.9, y - 0.9, 1.8, 1.8); continue;
        }
        const dx = x - mx, dy = y - my;
        const d = Math.sqrt(dx * dx + dy * dy);
        if (d >= R) { ctx.fillRect(x - 0.9, y - 0.9, 1.8, 1.8); continue; }
        const t = 1 - d / R, e = t * t;
        const push = e * 10, inv = d || 1;
        ctx.beginPath();
        ctx.arc(x + (dx / inv) * push, y + (dy / inv) * push, 0.9 + e * 2.2, 0, 6.2832);
        ctx.fillStyle = 'rgba(74,58,214,' + (0.16 + e * 0.7).toFixed(3) + ')';
        ctx.fill();
        ctx.fillStyle = 'rgba(14,17,22,0.13)';
      }
    }
  }

  function schedule() {
    if (!frame && !document.hidden && !reducedMotion.matches) frame = requestAnimationFrame(drawMesh);
  }

  function sizeMesh() {
    const dpr = Math.min(devicePixelRatio || 1, 2);
    canvas.width = innerWidth * dpr;
    canvas.height = innerHeight * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    cancelAnimationFrame(frame);
    drawMesh();
  }

  function leave() {
    mouse.x = -9999; mouse.y = -9999;
    if (cursor) cursor.style.opacity = '0';
    schedule();
  }

  window.addEventListener('pointermove', event => {
    if (event.pointerType === 'touch' || reducedMotion.matches || !finePointer.matches) return;
    mouse.x = event.clientX; mouse.y = event.clientY;
    if (cursor) {
      cursor.style.transform = 'translate(' + event.clientX + 'px,' + event.clientY + 'px)';
      cursor.style.opacity = '1';
    }
    const target = event.target.closest?.('[data-cursor]');
    if (label) label.textContent = target ? target.getAttribute('data-cursor') : 'browse';
    schedule();
  }, { passive: true });
  document.documentElement.addEventListener('pointerleave', leave);
  window.addEventListener('blur', leave);
  window.addEventListener('pointercancel', leave);
  document.addEventListener('visibilitychange', () => {
    cancelAnimationFrame(frame); frame = 0; leave();
  });
  reducedMotion.addEventListener('change', () => { leave(); sizeMesh(); });
  finePointer.addEventListener('change', leave);
  window.addEventListener('resize', sizeMesh, { passive: true });
  document.body.classList.add('field-active');
  sizeMesh();
})();
