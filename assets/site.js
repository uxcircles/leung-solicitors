/* Leung & Co Law concept: menu, hero seam, open-now, enquiry form (mailto), lazy map */
(() => {
  const zh = document.documentElement.lang.startsWith('zh');
  const t = (en, z) => (zh ? z : en);

  // menu
  const btn = document.querySelector('.menu-btn');
  const nav = document.getElementById('nav');
  if (btn && nav) {
    const head = document.querySelector('.site-head');
    const set = (open) => {
      if (open) nav.style.setProperty('--nav-top', Math.max(0, head.getBoundingClientRect().bottom) + 'px');
      btn.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('open', open);
      document.body.classList.toggle('menu-open', open);
    };
    btn.addEventListener('click', () => set(btn.getAttribute('aria-expanded') !== 'true'));
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') set(false); });
    window.matchMedia('(min-width: 901px)').addEventListener('change', (m) => { if (m.matches) set(false); });
  }

  // hero: on phones the seal sits on the seam between the stacked halves
  const hero = document.querySelector('.hero');
  if (hero) {
    const first = hero.querySelector('.half');
    const place = () => hero.style.setProperty('--seam-y', first.offsetHeight + 'px');
    place();
    window.addEventListener('resize', place);
    if (document.fonts) document.fonts.ready.then(place);
  }

  // open now (Europe/London)
  const parts = new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/London', weekday: 'short', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' }).formatToParts(new Date());
  const get = (k) => parts.find((p) => p.type === k).value;
  const day = get('weekday');
  const mins = +get('hour') * 60 + +get('minute');
  const weekday = !['Sat', 'Sun'].includes(day);
  const open = weekday && mins >= 570 && mins < 1080;
  document.querySelectorAll('[data-open-now]').forEach((el) => {
    el.textContent = open
      ? t('Open now, until 6pm UK time', '現正辦公，英國時間下午 6 時止')
      : t('Closed now. Leave a message or email and we will reply on the next working day', '現已休息，歡迎留言或電郵，我們會在下一個工作天回覆');
    if (!open) el.style.color = 'var(--muted)';
    el.hidden = false;
  });

  // enquiry form -> pre-filled email
  const form = document.getElementById('enquiry');
  if (form) {
    const q = new URLSearchParams(location.search).get('matter');
    const sel = form.querySelector('select');
    if (q && sel.querySelector(`option[value="${CSS.escape(q)}"]`)) sel.value = q;
    const err = form.querySelector('.form-err');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      let bad = null;
      form.querySelectorAll('[required]').forEach((f) => {
        const ok = f.value.trim() !== '';
        f.setAttribute('aria-invalid', String(!ok));
        if (!ok && !bad) bad = f;
      });
      if (bad) {
        err.textContent = t('Please fill in the highlighted fields.', '請填寫標示的欄位。');
        err.hidden = false;
        bad.focus();
        return;
      }
      err.hidden = true;
      const d = new FormData(form);
      const matter = sel.options[sel.selectedIndex].text;
      const body = [
        `${t('Name', '姓名')}: ${d.get('name')}`,
        `${t('Phone or email', '電話或電郵')}: ${d.get('contact')}`,
        `${t('Matter', '事項')}: ${matter}`,
        `${t('Preferred language', '語言')}: ${d.get('lang')}`,
        '',
        d.get('message'),
      ].join('\n');
      location.href = `mailto:info@leung-solicitors.co.uk?subject=${encodeURIComponent(t('Enquiry: ', '查詢：') + matter)}&body=${encodeURIComponent(body)}`;
    });
  }

  // map: load MapLibre only when the map comes near the screen
  const box = document.querySelector('[data-map]');
  if (box && 'IntersectionObserver' in window) {
    const root = document.querySelector('link[rel="stylesheet"]').href.replace(/site\.css.*$/, '');
    const load = (src) => new Promise((res, rej) => { const s = document.createElement('script'); s.src = src; s.onload = res; s.onerror = rej; document.head.appendChild(s); });
    const io = new IntersectionObserver((es) => {
      if (!es.some((e) => e.isIntersecting)) return;
      io.disconnect();
      const css = document.createElement('link'); css.rel = 'stylesheet'; css.href = root + 'vendor/maplibre/maplibre-gl.css'; document.head.appendChild(css);
      (window.maplibregl ? Promise.resolve() : load(root + 'vendor/maplibre/maplibre-gl.js'))
        .then(() => load(root + 'map.js?v=11'))
        .then(() => window.lcMap(box))
        .catch(() => {});
    }, { rootMargin: '400px' });
    io.observe(box);
  }
})();
