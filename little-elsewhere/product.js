(() => {
  'use strict';
  const dialog = document.querySelector('.preview-dialog');
  if (!dialog || typeof dialog.showModal !== 'function') return;
  const image = dialog.querySelector('.preview-image');
  const caption = dialog.querySelector('#preview-caption');
  const close = dialog.querySelector('.preview-close');
  let opener;

  document.querySelectorAll('[data-preview]').forEach(link => {
    link.addEventListener('click', event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      opener = link;
      const thumbnail = link.querySelector("img");
      dialog.classList.toggle("is-landscape", Number(thumbnail.getAttribute("width")) > Number(thumbnail.getAttribute("height")));
      image.src = link.href;
      image.alt = link.querySelector('img').alt;
      caption.textContent = link.dataset.caption;
      dialog.showModal();
      const viewport = dialog.querySelector(".preview-image-wrap");
      image.decode().then(() => {
        if (dialog.open) viewport.scrollLeft = (viewport.scrollWidth - viewport.clientWidth) / 2;
      }).catch(() => {});
      close.focus();
    });
  });
  close.addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const bounds = dialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
  });
  dialog.addEventListener('close', () => {
    image.removeAttribute('src');
    opener?.focus({ preventScroll: true });
  });
})();
