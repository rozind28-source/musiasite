/* Шар&Ко PWA service worker */
const CACHE = 'sharco-v1792079176';
const CORE = [
  './',
  './offline.html',
  './manifest.webmanifest',
  './index.html',
  './shop.html',
  './catalog/readykids.html',
  './catalog/readyadult.html',
  './catalog/newborn.html',
  './catalog/genderballoons.html',
  './catalog/devichnik.html',
  './catalog/edinorogi.html',
  './catalog/bantiki.html',
  './catalog/shkola.html',
  './catalog/newyear.html',
  './catalog/valentine.html',
  './catalog/den-papy.html',
  './catalog/den-mamy.html',
  './catalog/easter.html',
  './catalog/lions.html',
  './catalog/formen.html',
  './catalog/forwomen.html',
  './product/nabor-pervyj-prazdnik.html',
  './product/nabor-pastelnoe-oblako.html',
  './product/nabor-zolotoj-vecher.html',
  './product/nabor-oblako-nezhnosti.html',
  './product/nabor-malchik-ili-devochka.html',
  './product/nabor-utro-nevesty.html',
  './product/nabor-edinorog-mechta.html',
  './product/nabor-bantiki.html',
  './product/nabor-pervyj-zvonok.html',
  './product/nabor-zimnyaya-skazka.html',
  './product/nabor-dvoe-serdtsa.html',
  './product/nabor-papin-den.html',
  './product/nabor-mamin-den.html',
  './product/nabor-paskhalnoe-utro.html',
  './product/nabor-korol-savanny.html',
  './product/nabor-status.html',
  './product/nabor-shampanskoe-shik.html',
  './soberisam.html',
  './delivery.html',
  './about.html',
  './contacts.html',
  './privacy.html',
  './offer.html',
  'img/icons/apple-touch-icon.png',
  'img/icons/icon-192.png',
  'img/icons/icon-512.png',
  'img/icons/icon-maskable-512.png',
  'img/bantiki.jpg',
  'img/build-your-own.jpg',
  'img/courier.jpg',
  'img/devichnik.jpg',
  'img/easter.jpg',
  'img/fathers.jpg',
  'img/formen.jpg',
  'img/forwomen.jpg',
  'img/gender.jpg',
  'img/hero.jpg',
  'img/lions.jpg',
  'img/mothers.jpg',
  'img/newyear.jpg',
  'img/school.jpg',
  'img/set-adult.jpg',
  'img/set-kids.jpg',
  'img/set-newborn.jpg',
  'img/unicorn.jpg',
  'img/valentine.jpg',
  'img/workshop.jpg'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(CORE)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;

  /* страницы: сеть -> кэш -> офлайн-страница */
  if (req.mode === 'navigate') {
    e.respondWith(
      fetch(req)
        .then((res) => {
          if (res.ok) {
            const copy = res.clone();
            caches.open(CACHE).then((c) => c.put(req, copy));
          }
          return res;
        })
        .catch(() => caches.match(req).then((hit) => hit || caches.match('./offline.html')))
    );
    return;
  }

  /* остальное: кэш -> сеть (и положим в кэш на будущее) */
  e.respondWith(
    caches.match(req).then((hit) => hit ||
      fetch(req).then((res) => {
        if (res.ok) {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(req, copy));
        }
        return res;
      }).catch(() => new Response('', { status: 404, statusText: 'offline' })))
  );
});
