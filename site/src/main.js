/* Shared behaviour: cart, menus, sorting, filters, accordions, builder, forms */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------- cart (localStorage, shared across pages) ---------- */
  var cart = [];
  try { cart = JSON.parse(localStorage.getItem('sharco_cart') || '[]'); } catch (e) { cart = []; }
  function save() { try { localStorage.setItem('sharco_cart', JSON.stringify(cart)); } catch (e) {} }
  function fmt(n) { return n.toLocaleString('ru-RU') + ' ₽'; }

  var toast = $('#toast'), toastTimer;
  function showToast(msg) {
    if (!toast) return;
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toast.classList.remove('show'); }, 2400);
  }

  function renderCart() {
    var count = cart.reduce(function (s, i) { return s + i.qty; }, 0);
    var cc = $('#cartCount'), dc = $('#drawerCount');
    if (cc) cc.textContent = count;
    if (dc) dc.textContent = count;
    var body = $('#drawerBody');
    if (!body) return;
    body.innerHTML = '';
    if (!cart.length) {
      body.innerHTML = '<div class="drawer__empty">Корзина пуста...<br>Добавьте набор из каталога</div>';
    } else {
      cart.forEach(function (item, i) {
        var el = document.createElement('div');
        el.className = 'ci';
        el.innerHTML =
          '<img src="' + item.img + '" alt="">' +
          '<div class="ci__info"><div class="ci__name">' + item.name + '</div>' +
          '<div class="ci__qty">' + item.qty + ' шт.</div>' +
          '<div class="ci__price">' + fmt(item.price * item.qty) + '</div></div>' +
          '<button class="ci__rm" data-i="' + i + '" aria-label="Убрать">✕</button>';
        body.appendChild(el);
      });
      $$('.ci__rm', body).forEach(function (btn) {
        btn.addEventListener('click', function () {
          cart.splice(+btn.getAttribute('data-i'), 1);
          save(); renderCart();
        });
      });
    }
    var total = cart.reduce(function (s, i) { return s + i.price * i.qty; }, 0);
    var dt = $('#drawerTotal');
    if (dt) dt.textContent = fmt(total);
  }

  function addToCart(item) {
    var found = null;
    cart.forEach(function (c) { if (c.slug === item.slug) found = c; });
    if (found) found.qty += item.qty || 1;
    else cart.push({ slug: item.slug, name: item.name, price: item.price, img: item.img, qty: item.qty || 1 });
    save(); renderCart();
    showToast(item.name + ' — в корзине');
  }

  var drawer = $('#drawer'), overlay = $('#overlay');
  function openCart() { drawer.classList.add('show'); overlay.classList.add('show'); }
  function closeCart() { drawer.classList.remove('show'); overlay.classList.remove('show'); }
  if ($('#cartOpen')) $('#cartOpen').addEventListener('click', openCart);
  if ($('#cartClose')) $('#cartClose').addEventListener('click', closeCart);
  if (overlay) overlay.addEventListener('click', closeCart);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeCart(); });

  $$('.buy').forEach(function (btn) {
    btn.addEventListener('click', function () {
      addToCart({ slug: btn.getAttribute('data-slug'), name: btn.getAttribute('data-name'), price: +btn.getAttribute('data-price'), img: btn.getAttribute('data-img'), qty: 1 });
    });
  });

  var checkout = $('#checkout');
  if (checkout) checkout.addEventListener('click', function () {
    if (!cart.length) { showToast('Корзина пуста'); return; }
    showToast('Спасибо! Менеджер свяжется с вами 💌');
    cart = []; save(); renderCart();
    setTimeout(closeCart, 600);
  });

  /* ---------- burger & dropdown ---------- */
  var burger = $('#burger'), nav = $('#nav');
  if (burger) burger.addEventListener('click', function () {
    burger.classList.toggle('open'); nav.classList.toggle('open');
  });
  if (nav) nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A' && window.innerWidth <= 1020) {
      burger.classList.remove('open'); nav.classList.remove('open');
    }
  });
  var drop = $('#drop');
  if (drop) {
    var dropBtn = drop.querySelector('button');
    dropBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      drop.classList.toggle('open');
    });
    document.addEventListener('click', function (e) {
      if (!drop.contains(e.target)) drop.classList.remove('open');
    });
  }

  /* ---------- sorting of product grids ---------- */
  $$('[data-sort]').forEach(function (sel) {
    sel.addEventListener('change', function () {
      var grid = document.querySelector(sel.getAttribute('data-sort'));
      if (!grid) return;
      var cards = $$('.prod', grid);
      cards.sort(function (a, b) {
        var pa = +a.getAttribute('data-price'), pb = +b.getAttribute('data-price');
        var da = +a.getAttribute('data-date'), db = +b.getAttribute('data-date');
        switch (sel.value) {
          case 'price-asc': return pa - pb;
          case 'price-desc': return pb - pa;
          case 'newest': return db - da;
          default: return (+b.getAttribute('data-hit')) - (+a.getAttribute('data-hit'));
        }
      });
      cards.forEach(function (c) { grid.appendChild(c); });
    });
  });

  /* ---------- category filters (shop) ---------- */
  $$('.fchip').forEach(function (chip) {
    chip.addEventListener('click', function () {
      $$('.fchip').forEach(function (c) { c.classList.remove('active'); });
      chip.classList.add('active');
      var f = chip.getAttribute('data-filter');
      $$('.prod').forEach(function (card) {
        var cats = (card.getAttribute('data-cats') || '').split(',');
        card.style.display = (f === 'all' || cats.indexOf(f) > -1) ? '' : 'none';
      });
      var cnt = $('#shopCount');
      if (cnt) cnt.textContent = $$('.prod').filter(function (c) { return c.style.display !== 'none'; }).length;
    });
  });

  /* ---------- pager (demo) ---------- */
  $$('.pager button').forEach(function (b) {
    b.addEventListener('click', function () {
      if (!b.classList.contains('cur')) showToast('В демо-версии пагинация отключена 🙂');
    });
  });

  /* ---------- accordions ---------- */
  $$('.acc__btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      btn.parentNode.classList.toggle('open');
    });
  });

  /* ---------- product page: gallery + qty + options ---------- */
  var mainImg = $('#galleryMain');
  if (mainImg) {
    $$('.thumbs button').forEach(function (t) {
      t.addEventListener('click', function () {
        $$('.thumbs button').forEach(function (x) { x.classList.remove('active'); });
        t.classList.add('active');
        mainImg.src = t.getAttribute('data-img');
      });
    });
  }
  var qty = 1, qtyEl = $('#qtyVal');
  $$('.stepper button').forEach(function (b) {
    b.addEventListener('click', function () {
      qty = Math.min(20, Math.max(1, qty + (b.getAttribute('data-d') === '+' ? 1 : -1)));
      if (qtyEl) qtyEl.textContent = qty;
    });
  });
  $$('.sw').forEach(function (s) {
    s.addEventListener('click', function () {
      $$('.sw').forEach(function (x) { x.classList.remove('active'); });
      s.classList.add('active');
    });
  });
  var addBtn = $('#addProduct');
  if (addBtn) addBtn.addEventListener('click', function () {
    addToCart({ slug: addBtn.getAttribute('data-slug'), name: addBtn.getAttribute('data-name'), price: +addBtn.getAttribute('data-price'), img: addBtn.getAttribute('data-img'), qty: qty });
  });
  var buyBtn = $('#buyProduct');
  if (buyBtn) buyBtn.addEventListener('click', function () {
    addToCart({ slug: buyBtn.getAttribute('data-slug'), name: buyBtn.getAttribute('data-name'), price: +buyBtn.getAttribute('data-price'), img: buyBtn.getAttribute('data-img'), qty: qty });
    openCart();
  });

  /* ---------- builder (soberisam) ---------- */
  var builder = $('#builder');
  if (builder) {
    var state = { occasion: 'День рождения', palette: 'Пастель', latex: 10, foil: 1, bubbles: 0 };
    var PRICES = { latex: 190, foil: 450, bubbles: 950 };
    var BASE = 500;
    function recalc() {
      var sum = BASE + state.latex * PRICES.latex + state.foil * PRICES.foil + state.bubbles * PRICES.bubbles;
      var rows = $('#sumRows');
      if (rows) rows.innerHTML =
        '<div class="summary__row"><span>Повод</span><span>' + state.occasion + '</span></div>' +
        '<div class="summary__row"><span>Палитра</span><span>' + state.palette + '</span></div>' +
        '<div class="summary__row"><span>Латекс ' + state.latex + ' шт</span><span>' + fmt(state.latex * PRICES.latex) + '</span></div>' +
        '<div class="summary__row"><span>Фольга ' + state.foil + ' шт</span><span>' + fmt(state.foil * PRICES.foil) + '</span></div>' +
        '<div class="summary__row"><span>Бабблс ' + state.bubbles + ' шт</span><span>' + fmt(state.bubbles * PRICES.bubbles) + '</span></div>' +
        '<div class="summary__row"><span>Сборка и упаковка</span><span>' + fmt(BASE) + '</span></div>';
      var t = $('#sumTotal');
      if (t) t.textContent = fmt(sum);
    }
    $$('#builder .chips .chip').forEach(function (ch) {
      ch.addEventListener('click', function () {
        var group = ch.parentNode.getAttribute('data-group');
        $$('#builder .chips .chip').forEach(function (c) {
          if (c.parentNode.getAttribute('data-group') === group) c.classList.remove('sel');
        });
        ch.classList.add('sel');
        state[group] = ch.getAttribute('data-val');
        recalc();
      });
    });
    $$('#builder .stepper button').forEach(function (b) {
      b.addEventListener('click', function () {
        var k = b.parentNode.getAttribute('data-key');
        state[k] = Math.min(60, Math.max(0, state[k] + (b.getAttribute('data-d') === '+' ? 1 : -1)));
        var el = $('#q-' + k);
        if (el) el.textContent = state[k];
        recalc();
      });
    });
    var sendBtn = $('#sendBuilder');
    if (sendBtn) sendBtn.addEventListener('click', function () {
      showToast('Заявка отправлена! Менеджер пришлёт эскиз и точный расчёт.');
    });
    recalc();
  }

  /* ---------- mock forms ---------- */
  $$('form[data-mock]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      showToast('Спасибо! Мы свяжемся с вами в ближайшее время 💌');
      f.reset();
    });
  });

  /* ---------- PWA: install prompt & network state ---------- */
  var installBtn = $('#installBtn'), deferredPrompt = null;
  window.addEventListener('beforeinstallprompt', function (e) {
    e.preventDefault();
    deferredPrompt = e;
    if (installBtn) installBtn.hidden = false;
  });
  if (installBtn) installBtn.addEventListener('click', function () {
    if (!deferredPrompt) { showToast('Приложение уже установлено 🙂'); return; }
    deferredPrompt.prompt();
    deferredPrompt.userChoice.then(function () {
      deferredPrompt = null;
      installBtn.hidden = true;
    });
  });
  window.addEventListener('appinstalled', function () {
    showToast('Приложение установлено 🎉');
    if (installBtn) installBtn.hidden = true;
  });
  window.addEventListener('offline', function () { showToast('Нет сети — сайт работает из кэша'); });
  window.addEventListener('online', function () { showToast('Снова в сети!'); });

  renderCart();
})();
