/* BILUX TECH — interazioni
   Nessuna dipendenza esterna. Tutto rispetta prefers-reduced-motion. */
(function () {
  'use strict';

  var root = document.documentElement;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Load sequence ---------- */
  function markLoaded() { requestAnimationFrame(function () { root.classList.add('is-loaded'); }); }
  if (document.fonts && document.fonts.ready) {
    Promise.race([document.fonts.ready, new Promise(function (r) { setTimeout(r, 900); })]).then(markLoaded);
  } else { markLoaded(); }

  /* ---------- Header: solid after hero edge, hides on scroll down ---------- */
  var header = document.querySelector('.site-header');
  var lastY = window.scrollY;
  var ticking = false;
  function onScroll() {
    var y = window.scrollY;
    if (header) {
      header.classList.toggle('is-solid', y > 24);
      var goingDown = y > lastY;
      header.classList.toggle('is-hidden', goingDown && y > 480 && !root.classList.contains('menu-open'));
    }
    lastY = y;
    updateMethod();
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });

  /* ---------- Mobile menu ---------- */
  var toggle = document.querySelector('.menu-toggle');
  var menu = document.getElementById('mobile-menu');
  function setMenu(open) {
    root.classList.toggle('menu-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Chiudi il menu' : 'Apri il menu');
    menu.setAttribute('aria-hidden', String(!open));
    if (open) {
      header.classList.add('is-solid');
      var first = menu.querySelector('a');
      if (first) setTimeout(function () { first.focus(); }, 120);
    } else {
      toggle.focus();
    }
  }
  if (toggle && menu) {
    toggle.addEventListener('click', function () { setMenu(!root.classList.contains('menu-open')); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) root.classList.remove('menu-open'), toggle.setAttribute('aria-expanded', 'false'); });
    document.addEventListener('keydown', function (e) {
      if (!root.classList.contains('menu-open')) return;
      if (e.key === 'Escape') { setMenu(false); return; }
      if (e.key === 'Tab') {
        var f = [toggle].concat([].slice.call(menu.querySelectorAll('a')));
        var i = f.indexOf(document.activeElement);
        if (e.shiftKey && i <= 0) { e.preventDefault(); f[f.length - 1].focus(); }
        else if (!e.shiftKey && i === f.length - 1) { e.preventDefault(); f[0].focus(); }
      }
    });
    window.matchMedia('(min-width: 901px)').addEventListener('change', function (m) { if (m.matches && root.classList.contains('menu-open')) setMenu(false); });
  }

  /* ---------- Scroll reveal ---------- */
  var revealEls = document.querySelectorAll('.reveal, .reveal-media');
  if ('IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---------- Method progress (scroll-linked, never hijacks) ---------- */
  var method = document.querySelector('.method');
  var steps = method ? method.querySelectorAll('.method-step') : [];
  function updateMethod() {
    if (!method) return;
    var r = method.getBoundingClientRect();
    var vh = window.innerHeight;
    var p = (vh * 0.7 - r.top) / Math.max(r.height, 1);
    if (window.innerWidth > 900) p = (vh * 0.8 - r.top) / (vh * 0.5);
    p = Math.min(1, Math.max(0, p));
    method.style.setProperty('--p', p.toFixed(3));
    steps.forEach(function (s, i) { s.classList.toggle('is-active', p >= (i / steps.length) + 0.02 || p === 1); });
  }
  updateMethod();

  /* ---------- Torch: one light that reveals the stage ---------- */
  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  document.querySelectorAll('[data-torch]').forEach(function (stage) {
    var lines = [].slice.call(stage.querySelectorAll('.hero-title .line > span'));
    var dust = stage.querySelector('canvas.dust');
    var ctx = dust ? dust.getContext('2d') : null;
    var w = 0, h = 0, offsets = [];
    var s = { x: -200, y: 0, tx: 0, ty: 0, r: 0, tr: 0, t: 0, auto: true, intro: 0 };
    var particles = [];
    var lowPower = (navigator.hardwareConcurrency || 8) <= 4 || (navigator.deviceMemory || 8) <= 4 ||
      (navigator.connection && navigator.connection.saveData) || !finePointer;
    if (lowPower && dust) { dust.remove(); dust = null; ctx = null; }
    var frame = 0;
    var running = false, visible = true, raf = null;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);

    function measure() {
      var sr = stage.getBoundingClientRect();
      w = sr.width; h = sr.height;
      offsets = lines.map(function (el) { var r = el.getBoundingClientRect(); return [r.left - sr.left, r.top - sr.top]; });
      s.tr = Math.max(150, Math.min(380, w * 0.23));
      // text light: smaller than the room light, so only a few letters glow at once
      stage.style.setProperty('--tr', Math.round(Math.max(110, Math.min(250, w * 0.15))) + 'px');
      if (dust) {
        dust.width = Math.round(w * dpr); dust.height = Math.round(h * dpr);
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        if (!particles.length) for (var i = 0; i < 90; i++) particles.push({ x: Math.random() * w, y: Math.random() * h, vx: (Math.random() - .5) * .18, vy: -Math.random() * .22 - .03, s: Math.random() * 1.6 + .4 });
      }
    }
    function autopilot() {
      // drifts across the headline; on phones it stays over the title, slower
      if (w < 700) return [w * (0.5 + 0.34 * Math.sin(s.t * 0.4)), h * (0.5 + 0.08 * Math.sin(s.t * 0.8))];
      return [w * (0.36 + 0.24 * Math.sin(s.t * 0.5)), h * (0.5 + 0.12 * Math.sin(s.t * 0.95))];
    }
    function apply() {
      stage.style.setProperty('--x', s.x.toFixed(1) + 'px');
      stage.style.setProperty('--y', s.y.toFixed(1) + 'px');
      stage.style.setProperty('--r', s.r.toFixed(1) + 'px');
      for (var i = 0; i < lines.length; i++) {
        lines[i].style.setProperty('--lx', (s.x - offsets[i][0]).toFixed(1) + 'px');
        lines[i].style.setProperty('--ly', (s.y - offsets[i][1]).toFixed(1) + 'px');
      }
      if (ctx) {
        ctx.clearRect(0, 0, w, h);
        var R2 = Math.pow(s.r * 1.3, 2);
        for (var k = 0; k < particles.length; k++) {
          var p = particles[k];
          p.x += p.vx; p.y += p.vy;
          if (p.y < -5) { p.y = h + 5; p.x = Math.random() * w; }
          if (p.x < -5) p.x = w + 5; else if (p.x > w + 5) p.x = -5;
          var dx = p.x - s.x, dy = p.y - s.y;
          var a = Math.exp(-(dx * dx + dy * dy) / R2);
          if (a < 0.03) continue;
          ctx.fillStyle = 'rgba(247,247,245,' + (a * 0.75).toFixed(3) + ')';
          ctx.fillRect(p.x, p.y, p.s, p.s);
        }
      }
    }
    function tick() {
      s.t += 0.006;
      var target = s.auto ? autopilot() : [s.tx, s.ty];
      var k = s.intro < 1 ? 0.035 : (s.auto ? 0.025 : 0.3);
      s.intro = Math.min(1, s.intro + 0.006);
      s.x += (target[0] - s.x) * k; s.y += (target[1] - s.y) * k;
      s.r += (s.tr - s.r) * 0.04;
      frame++;
      if (!lowPower || frame % 2 === 0) apply(); // low-power devices: ~30fps
      raf = requestAnimationFrame(tick);
    }
    function start() { if (!running && visible && !document.hidden) { running = true; raf = requestAnimationFrame(tick); } }
    function stop() { running = false; if (raf) cancelAnimationFrame(raf); }

    measure();
    s.y = h * 0.62;
    if (reduceMotion) {
      // no movement: the light rests on the headline, fully lit
      var a = autopilot(); s.x = a[0]; s.y = a[1]; s.r = s.tr * 2.4; apply();
      stage.style.setProperty('--tr', '4000px');
      return;
    }
    stage.addEventListener('pointermove', function (e) {
      if (e.pointerType !== 'mouse') return; // touch handled separately
      var r = stage.getBoundingClientRect();
      s.tx = e.clientX - r.left; s.ty = e.clientY - r.top; s.auto = false; s.intro = 1;
    }, { passive: true });
    stage.addEventListener('pointerleave', function () { s.auto = true; });
    // touch: the light jumps to the finger, never blocks scrolling (passive listeners, no preventDefault)
    var touchTimer;
    function onTouch(e) {
      var t = e.touches && e.touches[0]; if (!t) return;
      var r = stage.getBoundingClientRect();
      s.tx = t.clientX - r.left; s.ty = t.clientY - r.top; s.auto = false; s.intro = 1;
      clearTimeout(touchTimer); touchTimer = setTimeout(function () { s.auto = true; }, 2200);
    }
    stage.addEventListener('touchstart', onTouch, { passive: true });
    stage.addEventListener('touchmove', onTouch, { passive: true });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) { visible = en[0].isIntersecting; visible ? start() : stop(); }).observe(stage);
    }
    document.addEventListener('visibilitychange', function () { document.hidden ? stop() : start(); });
    var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(measure, 120); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { setTimeout(measure, 1200); });
    setTimeout(measure, 1300); // after the title has finished rising
    start();
  });

  /* ---------- Prism: rows light up their ray ---------- */
  var prism = document.querySelector('.prism-wrap');
  if (prism) {
    if ('IntersectionObserver' in window && !reduceMotion) {
      var pio = new IntersectionObserver(function (en) { if (en[0].isIntersecting) { prism.classList.add('is-in'); pio.disconnect(); } }, { threshold: 0.25 });
      pio.observe(prism);
    } else { prism.classList.add('is-in'); }
    prism.querySelectorAll('[data-ray]').forEach(function (row) {
      var i = row.getAttribute('data-ray');
      var parts = prism.querySelectorAll('.prism-svg [data-ray="' + i + '"]');
      var others = prism.querySelectorAll('.prism-svg .p-ray:not([data-ray="' + i + '"])');
      function on() { parts.forEach(function (p) { p.classList.add('is-hot'); }); others.forEach(function (p) { p.classList.add('is-dim'); }); }
      function off() { parts.forEach(function (p) { p.classList.remove('is-hot'); }); others.forEach(function (p) { p.classList.remove('is-dim'); }); }
      row.addEventListener('mouseenter', on); row.addEventListener('mouseleave', off);
      row.addEventListener('focusin', on); row.addEventListener('focusout', off);
    });
  }


  /* ---------- Projects carousel ---------- */
  document.querySelectorAll('.pj-carousel').forEach(function (c) {
    var track = c.querySelector('.pj-track'), prev = c.querySelector('.pj-prev'), next = c.querySelector('.pj-next');
    var bar = c.querySelector('.pj-progress');
    function step() { var card = track.querySelector('.pj-card'); return card ? card.getBoundingClientRect().width + parseFloat(getComputedStyle(track).columnGap || 24) : 400; }
    function update() {
      var max = track.scrollWidth - track.clientWidth;
      var p = max > 0 ? track.scrollLeft / max : 0;
      if (bar) bar.style.setProperty('--pj', p.toFixed(3));
      prev.disabled = track.scrollLeft < 8;
      next.disabled = track.scrollLeft > max - 8;
    }
    prev.addEventListener('click', function () { track.scrollBy({ left: -step(), behavior: reduceMotion ? 'auto' : 'smooth' }); });
    next.addEventListener('click', function () { track.scrollBy({ left: step(), behavior: reduceMotion ? 'auto' : 'smooth' }); });
    track.addEventListener('scroll', function () { requestAnimationFrame(update); }, { passive: true });
    window.addEventListener('resize', update);
    // mouse drag to scroll (touch and trackpads scroll natively)
    var down = false, sx = 0, sl = 0, moved = false;
    track.addEventListener('pointerdown', function (e) { if (e.pointerType !== 'mouse') return; down = true; moved = false; sx = e.clientX; sl = track.scrollLeft; track.style.scrollSnapType = 'none'; track.style.scrollBehavior = 'auto'; });
    window.addEventListener('pointermove', function (e) { if (!down) return; var dx = e.clientX - sx; if (Math.abs(dx) > 5) moved = true; track.scrollLeft = sl - dx; });
    window.addEventListener('pointerup', function () { if (!down) return; down = false; track.style.scrollSnapType = ''; track.style.scrollBehavior = ''; });
    track.addEventListener('click', function (e) { if (moved) { e.preventDefault(); moved = false; } }, true);
    update();
  });

  /* ---------- Mobile sticky CTA: after the hero, hidden near contact forms ---------- */
  var mcta = document.querySelector('.m-cta');
  if (mcta) {
    var onContact = /\/(contatti|grazie)\//.test(location.pathname);
    var forms = document.querySelectorAll('form[data-contact], .site-footer');
    var formVisible = false;
    if ('IntersectionObserver' in window) {
      var fio = new IntersectionObserver(function (en) { en.forEach(function (x) { x.target._vis = x.isIntersecting; }); formVisible = [].some.call(forms, function (f) { return f._vis; }); toggleCta(); });
      forms.forEach(function (f) { fio.observe(f); });
    }
    function toggleCta() { mcta.classList.toggle('is-visible', !onContact && !formVisible && window.scrollY > window.innerHeight * 0.7); }
    window.addEventListener('scroll', function () { requestAnimationFrame(toggleCta); }, { passive: true });
    toggleCta();
  }

  /* ---------- Easter egg: lights off ---------- */
  var sw = document.querySelector('.lights-switch');
  if (sw) {
    var blackout = document.createElement('div');
    blackout.className = 'blackout'; blackout.setAttribute('aria-hidden', 'true');
    document.body.appendChild(blackout);
    function moveTorch(e) {
      root.style.setProperty('--bx', e.clientX + 'px');
      root.style.setProperty('--by', e.clientY + 'px');
    }
    function setLights(off) {
      root.classList.toggle('lights-off', off);
      sw.setAttribute('aria-pressed', String(off));
      sw.querySelector('.sw-label').textContent = off ? 'Riaccendi la luce' : 'Spegni la luce';
      if (off) window.addEventListener('pointermove', moveTorch, { passive: true });
      else window.removeEventListener('pointermove', moveTorch);
    }
    sw.addEventListener('click', function (e) { moveTorch(e); setLights(!root.classList.contains('lights-off')); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && root.classList.contains('lights-off')) setLights(false); });
  }

  /* ---------- Contact form ---------- */
  document.querySelectorAll('form[data-contact]').forEach(function (form) {
    var status = form.querySelector('.form-status');
    var btn = form.querySelector('button[type="submit"]');
    var btnLabel = btn ? btn.textContent : '';
    var endpoint = (form.getAttribute('data-endpoint') || '').trim();
    var mailTo = form.getAttribute('data-mailto') || '';

    function setError(input, msg) {
      var field = input.closest('.field');
      var err = field && field.querySelector('.field-error');
      if (msg) { field.setAttribute('data-invalid', ''); input.setAttribute('aria-invalid', 'true'); }
      else { field.removeAttribute('data-invalid'); input.removeAttribute('aria-invalid'); }
      if (err) err.textContent = msg || '';
    }
    function validate() {
      var first = null;
      [].forEach.call(form.querySelectorAll('[required]'), function (el) {
        var v = el.type === 'checkbox' ? el.checked : el.value.trim();
        var msg = '';
        if (!v) msg = el.type === 'checkbox' ? 'Serve il consenso per poterti rispondere.' : 'Compila questo campo.';
        else if (el.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(el.value.trim())) msg = 'Inserisci un indirizzo email valido, ad esempio nome@azienda.ch.';
        setError(el, msg);
        if (msg && !first) first = el;
      });
      return first;
    }
    form.addEventListener('input', function (e) {
      if (e.target.closest('[data-invalid]')) setError(e.target, '');
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      status.textContent = ''; status.removeAttribute('data-state');
      var invalid = validate();
      if (invalid) { invalid.focus(); return; }
      if (form.querySelector('.hp input').value) return; // bot

      var data = new FormData(form);
      if (!endpoint) {
        // Nessun servizio di invio configurato: apre il client email con il messaggio già compilato.
        var body = 'Nome: ' + data.get('nome') + '\nEmail: ' + data.get('email') +
          (data.get('azienda') ? '\nAzienda: ' + data.get('azienda') : '') +
          '\nServizio: ' + data.get('servizio') + '\n\n' + data.get('messaggio');
        window.location.href = 'mailto:' + mailTo + '?subject=' + encodeURIComponent('Nuovo progetto — ' + data.get('nome')) + '&body=' + encodeURIComponent(body);
        status.dataset.state = 'success';
        status.textContent = 'Si è aperto il tuo programma di posta con il messaggio pronto: premi Invia per spedirlo.';
        return;
      }
      btn.setAttribute('aria-busy', 'true'); btn.textContent = 'Invio in corso…';
      fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(data).toString() })
        .then(function (res) { if (!res.ok) throw new Error(res.status); return res; })
        .then(function () {
          form.reset();
          status.dataset.state = 'success';
          status.textContent = 'Messaggio inviato. Ti rispondiamo entro un giorno lavorativo.';
        })
        .catch(function () {
          status.dataset.state = 'error';
          status.textContent = 'Il messaggio non è partito. Riprova tra poco oppure scrivici a ' + mailTo + '.';
        })
        .finally(function () { btn.removeAttribute('aria-busy'); btn.textContent = btnLabel; status.focus(); });
    });
  });
})();
