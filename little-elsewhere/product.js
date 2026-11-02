// Language is represented by the URL; remember explicit choices without redirecting shared URLs.
try {
  localStorage.setItem('little-elsewhere-language', document.documentElement.lang === 'en' ? 'en' : 'zh-CN');
} catch { /* Navigation remains usable when storage is unavailable. */ }
