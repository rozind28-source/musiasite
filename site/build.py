# -*- coding: utf-8 -*-
"""Генератор многостраничного сайта «Шар&Ко» (демо-дизайн в духе mrsair.ru).
Запуск: python3 build.py  ->  создаёт index.html, shop.html, soberisam.html,
delivery.html, about.html, contacts.html, privacy.html, offer.html,
catalog/*.html, product/*.html"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, 'src', 'style.css'), encoding='utf-8').read()
JS = open(os.path.join(HERE, 'src', 'main.js'), encoding='utf-8').read()

PHONE = '+7 (900) 000-00-00'
PHONE_HREF = 'tel:+79000000000'
EMAIL = 'hello@sharandco.ru'

# ---------------------------------------------------------------- данные
CATS = [
    ('readykids',      'Детские дни рождения',  'set-kids.jpg',    'Облака и фонтаны из шаров для главного детского праздника: от нежной пастели до ярких героев.'),
    ('readyadult',     'Взрослые дни рождения', 'set-adult.jpg',   'Стильные композиции для взрослого праздника: хром, фольга и благородные сочетания.'),
    ('newborn',        'Выписка из роддома',    'set-newborn.jpg',  'Трогательные наборы для встречи малыша: нежные оттенки, бабблсы и банты.'),
    ('genderballoons', 'Гендер-пати',           'gender.jpg',      'Розовый или голубой? Наборы для вечеринки, где всё решит один шарик с конфетти.'),
    ('devichnik',      'Шары на девичник',      'devichnik.jpg',    'Розовое золото, сердца и блеск — для самой весёлой девичьей вечеринки.'),
    ('edinorogi',      'Единороги',             'unicorn.jpg',     'Волшебные наборы с фольгированными единорогами — мечта любого ребёнка.'),
    ('bantiki',        'Шары с бантиками',      'bantiki.jpg',     'Аккуратные атласные бантики на каждом шарике — милый акцент для любого повода.'),
    ('shkola',         '1 сентября',            'school.jpg',      'Праздничные букеты из шаров для первоклассников и выпускников детского сада.'),
    ('newyear',        'Новый год',             'newyear.jpg',     'Зимние композиции с мишурой, снежинками и металлическим блеском.'),
    ('valentine',      '14 февраля',            'valentine.jpg',    'Сердца, красный и розовый — готовый способ сказать «люблю» без слов.'),
    ('den-papy',       'День папы',             'fathers.jpg',     'Сдержанные мужские композиции: графит, синий хром и серебро.'),
    ('den-mamy',       'День мамы',             'mothers.jpg',     'Нежные наборы для мам и бабушек: пудровые оттенки и цветы из фольги.'),
    ('easter',         'Пасха',                 'easter.jpg',      'Весенние пастельные композиции с зайцами и крапинками-яйцами.'),
    ('lions',          'Наборы со львами',      'lions.jpg',       'Сафари-стиль: фольгированный лев, песочные тона и пампасная трава.'),
    ('formen',         'Для него',              'formen.jpg',      'Строгие премиальные наборы для мужчин: матовый чёрный и золото.'),
    ('forwomen',       'Для неё',               'forwomen.jpg',    'Эстетичные композиции для неё: нюд, шампань и жемчужный перламутр.'),
]
CAT_T = {s: t for s, t, _, _ in CATS}
CAT_I = {s: i for s, _, i, _ in CATS}

P = lambda slug, name, cats, price, img, alts, desc, comp, badge='', old=0, date=0, hit=0: \
    dict(slug=slug, name=name, cats=cats, price=price, img=img, alts=alts, desc=desc,
         comp=comp, badge=badge, old=old, date=date, hit=hit)

PRODUCTS = [
    P('nabor-pervyj-prazdnik', 'Набор «Первый праздник»', ['readykids'], 3900, 'set-kids.jpg', ['hero.jpg', 'bantiki.jpg'],
      'Пастельные латексные шары и фольгированная цифра — трогательный акцент для первого дня рождения.',
      ['10 латексных шаров 12″ с гелием', 'Фольгированная цифра на выбор', 'Атласные ленты и грузик', 'Транспортировочный пакет'],
      badge='Хит', date=5, hit=1),
    P('nabor-pastelnoe-oblako', 'Набор «Пастельное облако»', ['readykids', 'newborn', 'genderballoons', 'easter'], 8900, 'hero.jpg', ['set-newborn.jpg', 'bantiki.jpg'],
      'Плотное облако из 25 пастельных шаров с бабблсами и конфетти — выглядит как кадр из pinterest.',
      ['18 латексных шаров 12″ и 14″', '4 бабблса с конфетти', 'Бусины и ленты в тон', 'Упаковка для перевозки'],
      badge='−9%', old=9800, date=12, hit=1),
    P('nabor-zolotoj-vecher', 'Набор «Золотой вечер»', ['readyadult', 'newyear'], 6500, 'set-adult.jpg', ['formen.jpg', 'newyear.jpg'],
      'Чёрный хром, золото и фольгированные звёзды — строгий и нарядный сет для взрослого юбилея.',
      ['12 шаров хром и металлик', '3 фольгированные звезды', 'Ленты-спиральки', 'Транспортировочный пакет'],
      badge='Хит', date=8, hit=1),
    P('nabor-oblako-nezhnosti', 'Набор «Облако нежности»', ['newborn', 'bantiki'], 4900, 'set-newborn.jpg', ['bantiki.jpg', 'hero.jpg'],
      'Мятно-голубое облако с бабблсом и пёрышками внутри — классика встречи из роддома.',
      ['12 латексных шаров пастель', '1 бабблс 18″ с наполнением', 'Ленты и грузик', 'Упаковка для перевозки'],
      date=3),
    P('nabor-malchik-ili-devochka', 'Набор «Мальчик или девочка?»', ['genderballoons'], 6100, 'gender.jpg', ['hero.jpg', 'valentine.jpg'],
      'Розово-голубое облако с бабблсом-конфетти: момент объявления пола получится эффектным.',
      ['14 шаров розовый/голубой', 'Бабблс 18″ с двойным конфетти', 'Чёрный шар-сюрприз в подарок', 'Ленты, грузик, пакет'],
      badge='Хит', date=10, hit=1),
    P('nabor-utro-nevesty', 'Набор «Утро невесты»', ['devichnik', 'forwomen', 'valentine'], 6800, 'devichnik.jpg', ['forwomen.jpg', 'valentine.jpg'],
      'Розовое золото и blush-оттенки с фольгированным сердцем — идеален для фото утра невесты.',
      ['14 шаров нюд и розовое золото', 'Фольгированное сердце 1 шт', 'Гирлянда-дождик 2 м', 'Ленты и упаковка'],
      date=7),
    P('nabor-edinorog-mechta', 'Набор «Единорог-мечта»', ['edinorogi', 'readykids'], 5200, 'unicorn.jpg', ['easter.jpg', 'hero.jpg'],
      'Фольгированный единорог в окружении пастельных шаров и звёзд — готовая фотозона.',
      ['Фольгированный единорог 32″', '10 латексных шаров пастель', '3 фольгированные звезды', 'Ленты, грузик, пакет'],
      badge='Хит', date=9, hit=1),
    P('nabor-bantiki', 'Набор «Бантики»', ['bantiki', 'newborn', 'den-mamy'], 4300, 'bantiki.jpg', ['set-newborn.jpg', 'mothers.jpg'],
      'На каждом шарике — аккуратный атласный бантик. Мило настолько, насколько звучит.',
      ['10 латексных шаров 12″', '10 атласных бантиков ручной работы', 'Ленты и грузик', 'Транспортировочный пакет'],
      date=2),
    P('nabor-pervyj-zvonok', 'Набор «Первый звонок»', ['shkola'], 3700, 'school.jpg', ['hero.jpg', 'lions.jpg'],
      'Бордово-белое облако с колокольчиком — праздничное настроение для линейки 1 сентября.',
      ['10 шаров бордо/белый/золото', 'Плюшевый колокольчик', 'Ленты и грузик', 'Упаковка для перевозки'],
      date=4),
    P('nabor-zimnyaya-skazka', 'Набор «Зимняя сказка»', ['newyear'], 7900, 'newyear.jpg', ['set-adult.jpg', 'valentine.jpg'],
      'Серебро, глубокий красный и мишура-дождик — новогоднее настроение с первого взгляда.',
      ['14 шаров металлик и красный', 'Фольгированная снежинка', 'Мишура-дождик 3 м', 'Ленты и упаковка'],
      date=11),
    P('nabor-dvoe-serdtsa', 'Набор «Два сердца»', ['valentine', 'devichnik'], 5600, 'valentine.jpg', ['devichnik.jpg', 'hero.jpg'],
      'Фольгированные сердца и красное облако с конфетти-бабблсом — признание в любви без слов.',
      ['2 фольгированных сердца 18″', '8 красных латексных шаров', 'Бабблс с конфетти-сердечками', 'Ленты, грузик, пакет'],
      date=6),
    P('nabor-papin-den', 'Набор «Папин день»', ['den-papy', 'formen', 'readyadult'], 5400, 'fathers.jpg', ['formen.jpg', 'set-adult.jpg'],
      'Графит, синий хром и фольгированная медаль — сдержанно, стильно, по-мужски.',
      ['12 шаров графит и синий хром', 'Фольгированная медаль 1 шт', 'Ленты и грузик', 'Транспортировочный пакет'],
      date=13),
    P('nabor-mamin-den', 'Набор «Мамин день»', ['den-mamy', 'forwomen', 'newborn'], 5800, 'mothers.jpg', ['bantiki.jpg', 'forwomen.jpg'],
      'Пудровые шары с фольгированным тюльпаном и плюшевым сердцем — тепло и нежность в одном наборе.',
      ['12 шаров пудра и крем', 'Фольгированный тюльпан 1 шт', 'Плюшевое сердце', 'Ленты и упаковка'],
      date=14),
    P('nabor-paskhalnoe-utro', 'Набор «Пасхальное утро»', ['easter', 'edinorogi'], 4600, 'easter.jpg', ['unicorn.jpg', 'hero.jpg'],
      'Солнечная пастель, ушки-зайчик и декоративные яйца — весенняя композиция для светлого праздника.',
      ['10 пастельных шаров', 'Фольгированные ушки 1 шт', 'Декоративные яйца 3 шт', 'Ленты, грузик, пакет'],
      date=1),
    P('nabor-korol-savanny', 'Набор «Король саванны»', ['lions', 'readykids'], 6900, 'lions.jpg', ['school.jpg', 'hero.jpg'],
      'Фольгированный лев, песочные тона и пампасная трава — сафари-вечеринка готова.',
      ['Фольгированный лев 30″', '10 шаров терракота/песок', 'Пампасная трава (сухоцвет)', 'Ленты и упаковка'],
      badge='New', date=17),
    P('nabor-status', 'Набор «Статус»', ['formen', 'readyadult'], 7200, 'formen.jpg', ['set-adult.jpg', 'fathers.jpg'],
      'Матовый чёрный, изумруд и золотая фольга — премиальный сет для серьёзного повода.',
      ['14 шаров матовый чёрный/изумруд', 'Фольгированная цифра золотая', '3 фольгированные звезды', 'Ленты и упаковка'],
      date=15),
    P('nabor-shampanskoe-shik', 'Набор «Шампань-шик»', ['forwomen', 'readyadult', 'devichnik'], 7400, 'forwomen.jpg', ['devichnik.jpg', 'mothers.jpg'],
      'Нюд, шампань и жемчужный перламутр с фольгированным бокалом — эстетика дорогого праздника.',
      ['14 шаров нюд и перламутр', 'Фольгированное шампанское 1 шт', 'Пампасная трава (сухоцвет)', 'Ленты и упаковка'],
      badge='New', date=16),
]
PROD = {p['slug']: p for p in PRODUCTS}

SWATCHES = ['#F8C9D4', '#BFE6DA', '#CFC4F7', '#F7E3AE', '#2E2436']

# ---------------------------------------------------------------- helpers
def f(n):
    return f'{n:,}'.replace(',', ' ') + ' ₽'

def img(px, name):
    if name.endswith('.png') and not name.startswith('icon'):
        name = name[:-4] + '.jpg'
    return px + 'img/' + name

def prod_card(p, px):
    badge = f'<span class="prod__tag">{p["badge"]}</span>' if p['badge'] else ''
    old = f'<small>{f(p["old"])}</small>' if p['old'] else ''
    return f'''<article class="prod" data-price="{p['price']}" data-date="{p['date']}" data-hit="{p['hit']}" data-cats="{','.join(p['cats'])}">
  <a class="prod__media" href="{px}product/{p['slug']}.html">{badge}<img src="{img(px, p['img'])}" alt="{p['name']}" loading="lazy"></a>
  <div class="prod__body">
    <span class="prod__cat">{CAT_T[p['cats'][0]]}</span>
    <a class="prod__name" href="{px}product/{p['slug']}.html">{p['name']}</a>
    <p class="prod__desc">{p['desc']}</p>
    <div class="prod__foot">
      <span class="prod__price">{f(p['price'])}{old}</span>
      <button class="buy" type="button" data-slug="{p['slug']}" data-name="{p['name']}" data-price="{p['price']}" data-img="{img(px, p['img'])}">Купить →</button>
    </div>
  </div>
</article>'''

def grid(products, px, gid='gridCat'):
    return f'<div class="grid" id="{gid}">' + '\n'.join(prod_card(p, px) for p in products) + '</div>'

SORT = '''<select class="select" data-sort="#gridCat" aria-label="Сортировка">
  <option value="rec">Сортировка: рекомендуем</option>
  <option value="price-desc">Цена по убыванию</option>
  <option value="price-asc">Цена по возрастанию</option>
  <option value="newest">Сначала новинки</option>
</select>'''

ICONS = {
    'truck': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M2 6h11v10H2zM13 9h4.5L21 12.5V16h-8z" fill="#F4436C"/><circle cx="6.5" cy="18" r="2" fill="#2E2436"/><circle cx="16.5" cy="18" r="2" fill="#2E2436"/></svg>',
    'shield': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5l-8-3Z" fill="#59C9AE"/><path d="m8.5 11.5 2.4 2.4 4.6-4.6" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>',
    'card': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><rect x="2" y="5" width="20" height="14" rx="3" fill="#9B8CF2"/><path d="M2 10h20" stroke="#fff" stroke-width="2"/></svg>',
    'plus': '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>',
}

# ---------------------------------------------------------------- layout
def head(title, desc, px):
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="manifest" href="{px}manifest.webmanifest">
<meta name="theme-color" content="#F4436C">
<link rel="icon" type="image/png" sizes="192x192" href="{px}img/icons/icon-192.png">
<link rel="apple-touch-icon" href="{px}img/icons/apple-touch-icon.png">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Шар&amp;Ко">
<style>
{CSS}
</style>
</head>
<body>
'''

LOGO = '''<svg class="logo__mark" viewBox="0 0 64 64" fill="none" aria-hidden="true">
  <ellipse cx="24" cy="24" rx="13" ry="16" fill="#F4436C"/>
  <ellipse cx="41" cy="20" rx="11" ry="14" fill="#59C9AE" opacity=".9"/>
  <ellipse cx="34" cy="34" rx="10" ry="13" fill="#F7C860" opacity=".95"/>
  <path d="M24 40c2 6-2 10 0 16M41 34c1 8-3 12-1 20M34 47c1 5-1 8 0 12" stroke="#2E2436" stroke-width="2" stroke-linecap="round"/>
</svg>'''

def header(px, active=''):
    def a(key, href, label):
        cls = ' class="active"' if active == key else ''
        return f'<a href="{px}{href}"{cls}>{label}</a>'
    menu = '\n'.join(f'          <a href="{px}catalog/{s}.html">{t}</a>' for s, t, _, _ in CATS)
    return f'''<header class="header">
  <div class="container header__in">
    <a class="logo" href="{px}index.html" aria-label="На главную">
      {LOGO}
      <span class="logo__text">
        <span class="logo__name">Шар<span>&amp;</span>Ко</span>
        <span class="logo__tag">воздушные шары · москва</span>
      </span>
    </a>
    <nav class="nav" id="nav">
      <div class="drop" id="drop">
        <button type="button" aria-expanded="false">Готовые наборы
          <svg width="12" height="8" viewBox="0 0 12 8" fill="none"><path d="M1 1.5 6 6.5 11 1.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        </button>
        <div class="drop__menu">
{menu}
        </div>
      </div>
      {a('shop', 'shop.html', 'Все товары')}
      {a('soberisam', 'soberisam.html', 'Собери сам')}
      {a('delivery', 'delivery.html', 'Доставка и оплата')}
      {a('about', 'about.html', 'О нас')}
      {a('contacts', 'contacts.html', 'Контакты')}
    </nav>
    <div class="header__actions">
      <a class="phone" href="{PHONE_HREF}">{PHONE}</a>
      <button class="cart-btn install-btn" id="installBtn" type="button" hidden aria-label="Установить приложение">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 3v11m0 0 4-4m-4 4-4-4M4 19h16" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span class="txt">Установить</span>
      </button>
      <button class="cart-btn" id="cartOpen" type="button">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M3 4h2.4l2.2 11.2a2 2 0 0 0 2 1.6h7.9a2 2 0 0 0 2-1.6L21 8H6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="10" cy="20" r="1.6" fill="currentColor"/><circle cx="17.5" cy="20" r="1.6" fill="currentColor"/></svg>
        <span class="txt">Корзина</span>
        <span class="cart-btn__count" id="cartCount">0</span>
      </button>
      <button class="burger" id="burger" type="button" aria-label="Меню"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
'''

def footer(px):
    cat_links = '\n'.join(f'        <a href="{px}catalog/{s}.html">{t}</a>' for s, t, _, _ in CATS[:6])
    return f'''<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <div class="footer__logo">{LOGO}<span class="logo__name">Шар<span style="color:var(--accent)">&amp;</span>Ко</span></div>
        <p class="footer__note">Воздушные шары и конфетти с доставкой по Москве и Московской области. Соберём композицию под любой повод — от выписки до корпоратива.</p>
      </div>
      <div>
        <h4>Каталог</h4>
{cat_links}
        <a href="{px}shop.html">Все товары</a>
      </div>
      <div>
        <h4>Страницы</h4>
        <a href="{px}soberisam.html">Собери сам</a>
        <a href="{px}delivery.html">Доставка и оплата</a>
        <a href="{px}about.html">О нас</a>
        <a href="{px}contacts.html">Контакты</a>
        <a href="{px}privacy.html">Политика конфиденциальности</a>
        <a href="{px}offer.html">Публичная оферта</a>
      </div>
      <div>
        <h4>Контакты</h4>
        <a href="{PHONE_HREF}">{PHONE}</a>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <p class="footer__note" style="margin-top:8px">Ежедневно с 9:00 до 21:00<br>Москва, ул. Лётчиков, 12<br>доставка по Москве и МО</p>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© 2026 Шар&amp;Ко · ИП Иванов И. И. · демонстрационный макет дизайна</span>
      <span>Сделано с ♥ и гелием</span>
    </div>
  </div>
</footer>
'''

def cart_block(px):
    return f'''<div class="overlay" id="overlay"></div>
<aside class="drawer" id="drawer" aria-label="Корзина">
  <div class="drawer__head">
    <h3>Ваши товары (<span id="drawerCount">0</span>)</h3>
    <button class="drawer__close" id="cartClose" type="button" aria-label="Закрыть">✕</button>
  </div>
  <div class="drawer__body" id="drawerBody"></div>
  <div class="drawer__foot">
    <div class="drawer__total"><span>Итого</span><span id="drawerTotal">0 ₽</span></div>
    <button class="btn btn--accent" type="button" id="checkout">Оформить заказ</button>
  </div>
</aside>
<div class="toast" id="toast"></div>
<script>
{JS}
</script>
<script>
if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {{
  window.addEventListener('load', function () {{
    navigator.serviceWorker.register('{px}sw.js').catch(function () {{}});
  }});
}}
</script>
</body>
</html>
'''

def page(fname, title, desc, px, active, body):
    html = head(title, desc, px) + header(px, active) + body + footer(px) + cart_block(px)
    path = os.path.join(HERE, fname)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(html)
    PAGES.append(fname)
    print('ok', fname)

def crumbs(px, items):
    parts = [f'<a href="{px}index.html">Главная</a>']
    for href, label in items:
        parts.append('<span>/</span>')
        parts.append(f'<a href="{px}{href}">{label}</a>' if href else f'<span style="opacity:.85;color:var(--ink)">{label}</span>')
    return f'<div class="container"><nav class="breadcrumbs">{" ".join(parts)}</nav></div>'

def cta_banner(px, h, p, btn_href, btn_label, image):
    return f'''<section class="section" style="padding-top:20px">
  <div class="container">
    <div class="cta__card">
      <div class="cta__body">
        <h2>{h}</h2>
        <p>{p}</p>
        <div class="cta__btns">
          <a class="btn btn--accent" href="{px}{btn_href}">{btn_label}</a>
          <a class="btn btn--ghost" href="{PHONE_HREF}">{PHONE}</a>
        </div>
      </div>
      <div class="cta__media"><img src="{img(px, image)}" alt="" loading="lazy"></div>
    </div>
  </div>
</section>'''

def social_block(px):
    return f'''<section class="section">
  <div class="container">
    <div class="social__card">
      <div>
        <h2>Следите за нами!</h2>
        <p>Каждый день показываем процесс сборки композиций, делимся новинками и разыгрываем наборы среди подписчиков. Подписывайтесь, чтобы не пропустить обновления!</p>
      </div>
      <div class="social__links">
        <a class="soc soc--tg" href="#" aria-label="Telegram"><svg width="26" height="26" viewBox="0 0 24 24" fill="none"><path d="M21.5 4.5 2.8 11.7c-.8.3-.8 1.4 0 1.7l4.6 1.6 1.7 4.9c.3.8 1.3.9 1.8.2l2.3-2.9 4.6 3.4c.7.5 1.6.1 1.8-.7l3-14c.2-.9-.7-1.7-1.6-1.4Z" fill="#fff"/></svg></a>
        <a class="soc soc--vk" href="#" aria-label="VK"><svg width="26" height="26" viewBox="0 0 24 24" fill="none"><path d="M3 7c.4 6 4 10.5 9.2 10.5h.9v-3.6c1.8.2 3.2 1.6 3.8 3.6H20c-.7-2.6-2.4-4.2-4-4.9 1.6-.9 3.1-2.7 3.6-5.6h-2.5c-.5 2.2-2 3.9-3.9 4.1V7h-2.6v6.4C8.6 12.9 6.4 10.6 5.6 7H3Z" fill="#fff"/></svg></a>
        <a class="soc soc--wa" href="#" aria-label="WhatsApp"><svg width="26" height="26" viewBox="0 0 24 24" fill="none"><path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3Zm4.2 12.4c-.2.6-1.2 1.1-1.7 1.2-.4.1-1 .1-1.6-.1-3.2-1.1-5.3-3.7-6-5.2-.3-.7-.3-1.5.2-2.1.2-.3.5-.6.8-.6h.6c.2 0 .4 0 .6.5l.8 1.9c.1.2 0 .4-.1.6l-.5.6c-.1.2-.2.3 0 .6.6 1 1.6 2 2.9 2.5.3.1.5.1.6-.1l.7-.8c.2-.2.4-.2.6-.1l1.9.9c.3.1.4.3.4.5 0 .2 0 .5-.2.7Z" fill="#fff"/></svg></a>
      </div>
    </div>
  </div>
</section>'''

# ---------------------------------------------------------------- pages
def build_home():
    px = ''
    chips = ''.join(f'<a class="chip chip--{i % 5 + 1}" href="catalog/{s}.html">{t}</a>'
                    for i, (s, t, _, _d) in enumerate(CATS[:10]))
    hits = [p for p in PRODUCTS if p['hit']][:4]
    gal_imgs = ['unicorn.jpg', 'gender.jpg', 'newyear.jpg', 'lions.jpg', 'devichnik.jpg', 'valentine.jpg', 'mothers.jpg', 'formen.jpg']
    gal = '\n'.join(f'<img src="img/{g}" alt="Пример композиции" loading="lazy">' for g in gal_imgs)
    body = f'''<section class="hero">
  <div class="container hero__grid">
    <div>
      <span class="badge"><i></i> Доставляем ежедневно с 8:00 до 23:00</span>
      <h1>Воздушные шары<br>с доставкой <em>по Москве</em></h1>
      <p class="hero__sub">Соберём и привезём композицию к нужному часу — праздник не будет ждать.</p>
      <a class="hero__phone" href="{PHONE_HREF}">{PHONE}</a>
      <p class="chips-title">Выбери из готовых наборов</p>
      <div class="chips">{chips}</div>
    </div>
    <div class="hero__media">
      <img src="img/hero.jpg" alt="Облако из пастельных воздушных шаров с лентами">
      <div class="hero__float hero__float--1">
        <svg width="34" height="34" viewBox="0 0 24 24" fill="none"><path d="M12 21s-7-4.6-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.4-7 10-7 10Z" fill="#F4436C"/></svg>
        <span><b>4 800+</b> счастливых клиентов</span>
      </div>
      <div class="hero__float hero__float--2">
        <svg width="34" height="34" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="#59C9AE" stroke-width="2"/><path d="M12 7v5l3.5 2" stroke="#59C9AE" stroke-width="2" stroke-linecap="round"/></svg>
        <span><b>до 60 дней</b> полёт шаров</span>
      </div>
    </div>
  </div>
</section>
{cta_banner('', 'Или собери свою собственную композицию', 'Расскажи менеджеру повод, цвета и бюджет — пришлём 2–3 варианта композиции с фото и расчётом за 15 минут.', 'soberisam.html', 'Собрать свой набор', 'build-your-own.jpg')}
<section class="section">
  <div class="container">
    <div class="adv__grid">
      <div class="adv__card"><div class="adv__icon"><svg width="30" height="30" viewBox="0 0 24 24" fill="none"><path d="M20 4c-9 0-15 4-15 11 0 3 2 5 5 5 7 0 10-7 10-16Z" fill="#59C9AE"/><path d="M5 20C8 14 12 10 17 7" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg></div>
        <h3>Экологичность</h3><p>Работаем с шарами из натурального латекса и материалами, которые легко перерабатываются и не вредят окружающей среде.</p></div>
      <div class="adv__card"><div class="adv__icon"><svg width="30" height="30" viewBox="0 0 24 24" fill="none"><ellipse cx="12" cy="9" rx="6" ry="7.5" fill="#9B8CF2"/><path d="M12 16.5 10.5 19h3L12 16.5Z" fill="#9B8CF2"/><path d="M12 20c1.5 1.5-1.5 2.5 0 4" stroke="#9B8CF2" stroke-width="1.6" stroke-linecap="round"/></svg></div>
        <h3>Долгий полёт</h3><p>95% наших латексных шаров летают больше месяца, а бабблсы в сезон отопления держат форму до полугода.</p></div>
      <div class="adv__card"><div class="adv__icon">{ICONS['truck'].replace('width="20" height="20"', 'width="30" height="30"')}</div>
        <h3>Быстрая доставка</h3><p>Аккуратно соберём, упакуем в транспортировочный пакет и привезём заказ на автомобиле точно к сроку.</p></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:10px">
  <div class="container">
    <div class="shead"><div><h2>Популярные товары</h2><p>Наборы, которые заказывают чаще всего</p></div><a href="shop.html">Все товары →</a></div>
    {grid(hits, '', 'gridHome')}
  </div>
</section>
<section class="section" style="padding-top:10px">
  <div class="container">
    <div class="shead"><div><h2>Как мы работаем</h2><p>Четыре шага от заявки до праздника</p></div></div>
    <div class="steps">
      <div class="step"><div class="num">01</div><h3>Заявка</h3><p>Выбираете готовый набор или рассказываете идею в мессенджере.</p></div>
      <div class="step"><div class="num">02</div><h3>Эскиз и расчёт</h3><p>За 15 минут присылаем фото-варианты композиции и точную цену.</p></div>
      <div class="step"><div class="num">03</div><h3>Сборка</h3><p>Надуваем и собираем заказ в день доставки, чтобы шары летали дольше.</p></div>
      <div class="step"><div class="num">04</div><h3>Доставка</h3><p>Курьер привозит шары в защитном пакете к нужному интервалу.</p></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:10px">
  <div class="container">
    <div class="shead"><div><h2>Наши работы</h2><p>Немного вдохновения из последних заказов</p></div><a href="shop.html">Смотреть каталог →</a></div>
    <div class="gal">{gal}</div>
  </div>
</section>
{social_block('')}'''
    page('index.html', 'Воздушные шары с доставкой по Москве — Шар&Ко',
         'Готовые наборы воздушных шаров с доставкой по Москве: дни рождения, выписка, гендер-пати и другие поводы.', px, 'home', body)

def build_shop():
    px = ''
    chips = '<button class="fchip active" data-filter="all">Все</button>' + ''.join(
        f'<button class="fchip" data-filter="{s}">{t}</button>' for s, t, _, _ in CATS)
    body = f'''{crumbs(px, [('', 'Все товары')])}
<section class="pagehead">
  <div class="container pagehead__grid">
    <div>
      <h1>Все наборы шаров</h1>
      <p class="pagehead__lead">Полный каталог готовых композиций: фильтруйте по поводу, сортируйте по цене и добавляйте в корзину в один клик.</p>
      <div class="pagehead__chips"><a class="btn btn--light" href="soberisam.html">Не нашли нужное? Соберём своё →</a></div>
    </div>
    <img class="pagehead__img" src="img/workshop.jpg" alt="Мастерская воздушных шаров">
  </div>
</section>
<section class="section" style="padding-top:16px">
  <div class="container">
    <div class="filters">{chips}</div>
    <div class="toolbar">
      <span class="toolbar__count">Наборов: <b id="shopCount">{len(PRODUCTS)}</b></span>
      {SORT.replace('#gridCat', '#gridShop')}
    </div>
    {grid(PRODUCTS, '', 'gridShop')}
    <div class="pager"><button class="cur">1</button><button>2</button><button>3</button><button>Далее →</button></div>
  </div>
</section>'''
    page('shop.html', 'Все наборы воздушных шаров — каталог Шар&Ко',
         'Полный каталог готовых наборов воздушных шаров с ценами и доставкой по Москве.', px, 'shop', body)

def build_category(slug, title, image, descr):
    px = '../'
    own = [p for p in PRODUCTS if slug in p['cats']]
    others = [p for p in PRODUCTS if slug not in p['cats']][:4]
    sib = ''.join(f'<a class="chip" href="{s}.html">{t}</a>' for s, t, _, _ in [c for c in CATS if c[0] != slug][:8])
    body = f'''{crumbs(px, [('shop.html', 'Каталог'), ('', title)])}
<section class="pagehead">
  <div class="container pagehead__grid">
    <div>
      <h1>{title}</h1>
      <p class="pagehead__lead">{descr}</p>
      <div class="pagehead__chips">{sib}</div>
    </div>
    <img class="pagehead__img" src="{img(px, image)}" alt="{title}">
  </div>
</section>
<section class="section" style="padding-top:16px">
  <div class="container">
    <div class="toolbar">
      <span class="toolbar__count">Наборов в категории: <b>{len(own)}</b></span>
      {SORT}
    </div>
    {grid(own, px)}
    <div class="pager"><button class="cur">1</button><button>2</button><button>3</button></div>
  </div>
</section>
<section class="section" style="padding-top:6px">
  <div class="container">
    <div class="shead"><div><h2>Похожие наборы</h2><p>Может понравиться из соседних категорий</p></div><a href="{px}shop.html">Все товары →</a></div>
    {grid(others, px, 'gridSim')}
  </div>
</section>
{cta_banner(px, 'Хочется чего-то особенного?', 'Соберём уникальную композицию по вашим цветам и бюджету — пришлём эскиз за 15 минут.', 'soberisam.html', 'Собрать свой набор', 'build-your-own.jpg')}'''
    page(f'catalog/{slug}.html', f'{title} — купить набор шаров в Москве | Шар&Ко',
         descr, px, 'catalog', body)

def build_product(p):
    px = '../'
    thumbs = [p['img']] + p['alts']
    th = '\n'.join(f'<button type="button" class="{"active" if i == 0 else ""}" data-img="{img(px, t)}"><img src="{img(px, t)}" alt="Фото {i + 1}"></button>' for i, t in enumerate(thumbs))
    sw = '\n'.join(f'<button type="button" class="sw{" active" if i == 0 else ""}" style="background:{c}" aria-label="Палитра {i + 1}"></button>' for i, c in enumerate(SWATCHES))
    comp = '\n'.join(f'<li>{c}</li>' for c in p['comp'])
    save = ''
    if p['old']:
        pct = round((1 - p['price'] / p['old']) * 100)
        save = f'<span class="save">выгода {pct}%</span>'
    badge = f'<span class="badge"><i></i> {p["badge"]}</span>' if p['badge'] else ''
    cat_links = ' · '.join(f'<a href="{px}catalog/{c}.html" style="color:var(--accent)">{CAT_T[c]}</a>' for c in p['cats'])
    same = [x for x in PRODUCTS if x['slug'] != p['slug'] and set(x['cats']) & set(p['cats'])]
    sim = (same or [x for x in PRODUCTS if x['slug'] != p['slug']])[:4]
    body = f'''{crumbs(px, [('shop.html', 'Каталог'), ('catalog/' + p['cats'][0] + '.html', CAT_T[p['cats'][0]]), ('', p['name'])])}
<section class="container pcard">
  <div class="gallery">
    <img class="gallery__main" id="galleryMain" src="{img(px, p['img'])}" alt="{p['name']}">
    <div class="thumbs">{th}</div>
  </div>
  <div class="pinfo">
    {badge}
    <h1>{p['name']}</h1>
    <p class="muted" style="margin-top:8px;font-size:14px">Категории: {cat_links}</p>
    <div class="pprice"><b>{f(p['price'])}</b>{('<s>' + f(p['old']) + '</s>') if p['old'] else ''}{save}</div>
    <p class="muted">{p['desc']}</p>
    <ul class="plist">{comp}</ul>
    <div class="opts">
      <div>
        <div class="opts__label">Палитра лент</div>
        <div class="swatches">{sw}</div>
      </div>
      <div>
        <div class="opts__label">Количество</div>
        <div class="stepper" data-key="qty"><button type="button" data-d="-">−</button><b id="qtyVal">1</b><button type="button" data-d="+">+</button></div>
      </div>
    </div>
    <div class="pbuy">
      <button class="btn btn--accent" id="addProduct" type="button" data-slug="{p['slug']}" data-name="{p['name']}" data-price="{p['price']}" data-img="{img(px, p['img'])}">В корзину</button>
      <button class="btn btn--dark" id="buyProduct" type="button" data-slug="{p['slug']}" data-name="{p['name']}" data-price="{p['price']}" data-img="{img(px, p['img'])}">Купить в 1 клик</button>
    </div>
    <div class="pmeta">
      <div>{ICONS['truck']}<span>Доставка по Москве от 900 ₽, интервалы 4 часа; самовывоз из студии ежедневно.</span></div>
      <div>{ICONS['shield']}<span>Гарантия 24 часа: если с шарами что-то случится — заменим или вернём деньги.</span></div>
      <div>{ICONS['card']}<span>Оплата онлайн: картой на сайте, по ссылке-счёту или безналом для юрлиц.</span></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:6px">
  <div class="container" style="max-width:860px">
    <div class="acc open">
      <button class="acc__btn" type="button">Доставка и интервалы {ICONS['plus']}</button>
      <div class="acc__body"><div class="acc__in"><p>Собираем заказ в день доставки и привозим в большом транспортировочном пакете на автомобиле. Интервалы: 10:00–14:00, 14:00–18:00, 18:00–22:00 и 22:00–00:00. Точное время и ранняя доставка — по согласованию.</p></div></div>
    </div>
    <div class="acc">
      <button class="acc__btn" type="button">Гарантия на шары {ICONS['plus']}</button>
      <div class="acc__body"><div class="acc__in"><p>Гарантия действует 24 часа после доставки курьером. Если бабблс или фольгированная фигура потеряли вид — привезём новую, вернём деньги или перенесём стоимость на следующий заказ.</p></div></div>
    </div>
    <div class="acc">
      <button class="acc__btn" type="button">Как ухаживать за шарами {ICONS['plus']}</button>
      <div class="acc__body"><div class="acc__in"><ul>
        <li>Комфортная температура — 20–23 °C, без резких перепадов.</li>
        <li>Держите подальше от прямых солнца, сквозняков и влажности.</li>
        <li>Не оставляйте шары в машине дольше 2–3 часов.</li>
        <li>Берегите от шершавых стен, веток и когтей домашних питомцев.</li>
      </ul></div></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:6px">
  <div class="container">
    <div class="shead"><div><h2>Похожие наборы</h2></div><a href="{px}shop.html">Все товары →</a></div>
    {grid(sim, px, 'gridSim')}
  </div>
</section>'''
    page(f'product/{p["slug"]}.html', f'{p["name"]} — купить в Москве | Шар&Ко', p['desc'], px, 'catalog', body)

def build_soberisam():
    px = ''
    occ = ['День рождения', 'Выписка из роддома', 'Гендер-пати', 'Девичник', 'Новый год', 'Просто так']
    pal = ['Пастель', 'Моно-белый', 'Чёрное золото', 'Розовое облако', 'Мята и небо', 'Радуга']
    occ_chips = ''.join(f'<button type="button" class="chip{" sel" if i == 0 else ""}" data-val="{o}">{o}</button>' for i, o in enumerate(occ))
    pal_chips = ''.join(f'<button type="button" class="chip{" sel" if i == 0 else ""}" data-val="{o}">{o}</button>' for i, o in enumerate(pal))
    gal = '\n'.join(f'<img src="img/{g}" alt="Идея композиции" loading="lazy">' for g in
                    ['unicorn.jpg', 'gender.jpg', 'lions.jpg', 'newyear.jpg', 'devichnik.jpg', 'easter.jpg', 'formen.jpg', 'valentine.jpg'])
    body = f'''{crumbs(px, [('', 'Собери сам')])}
<section class="pagehead">
  <div class="container pagehead__grid">
    <div>
      <h1>Собери свою композицию</h1>
      <p class="pagehead__lead">Придумайте набор, которого ещё ни у кого не было: выберите повод, палитру и состав — мы посчитаем ориентировочную стоимость сразу, а менеджер пришлёт эскиз и точный расчёт.</p>
    </div>
    <img class="pagehead__img" src="img/build-your-own.jpg" alt="Шары разных оттенков для своей композиции">
  </div>
</section>
<section class="section" style="padding-top:20px" id="builder">
  <div class="container builder">
    <div>
      <div class="bstep">
        <h3>Шаг 1. Повод</h3><p>Для какого праздника собираем?</p>
        <div class="chips" data-group="occasion">{occ_chips}</div>
      </div>
      <div class="bstep">
        <h3>Шаг 2. Палитра</h3><p>Какое настроение цветов вам близко?</p>
        <div class="chips" data-group="palette">{pal_chips}</div>
      </div>
      <div class="bstep">
        <h3>Шаг 3. Состав</h3><p>Сколько и каких шаров положить в облако?</p>
        <div class="brow"><div class="brow__t"><b>Латексные шары</b><span>12–14″, 190 ₽/шт</span></div>
          <div class="stepper" data-key="latex"><button type="button" data-d="-">−</button><b id="q-latex">10</b><button type="button" data-d="+">+</button></div></div>
        <div class="brow"><div class="brow__t"><b>Фольгированные</b><span>фигуры и цифры, 450 ₽/шт</span></div>
          <div class="stepper" data-key="foil"><button type="button" data-d="-">−</button><b id="q-foil">1</b><button type="button" data-d="+">+</button></div></div>
        <div class="brow"><div class="brow__t"><b>Бабблс с конфетти</b><span>прозрачные, 18″, 950 ₽/шт</span></div>
          <div class="stepper" data-key="bubbles"><button type="button" data-d="-">−</button><b id="q-bubbles">0</b><button type="button" data-d="+">+</button></div></div>
      </div>
      <div class="bstep">
        <h3>Шаг 4. Комментарий</h3><p>Любые детали: любимые цвета, герои, надписи.</p>
        <form class="form" data-mock>
          <div class="field"><textarea placeholder="Например: хочу облако в оттенках лаванды с фольгированной луной…"></textarea></div>
        </form>
      </div>
    </div>
    <aside class="summary">
      <h3>Ваша композиция</h3>
      <div id="sumRows"></div>
      <div class="summary__total"><span>Ориентировочно</span><b id="sumTotal">0 ₽</b></div>
      <button class="btn btn--accent" id="sendBuilder" type="button">Отправить менеджеру</button>
      <p class="summary__note">Расчёт предварительный: точную цену подтвердит менеджер после эскиза. Доставка считается отдельно.</p>
    </aside>
  </div>
</section>
<section class="section" style="padding-top:6px">
  <div class="container">
    <div class="shead"><div><h2>Идеи для вдохновения</h2><p>Работы, которые мы собирали по заявкам «собери сам»</p></div></div>
    <div class="gal">{gal}</div>
  </div>
</section>
<section class="section" style="padding-top:6px">
  <div class="container split">
    <div>
      <h2 style="font-size:clamp(24px,2.6vw,34px);font-weight:800;margin-bottom:12px">Оставьте номер — перезвоним</h2>
      <p class="muted" style="margin-bottom:20px">Обсудим идею, подскажем по сочетаниям и забронируем удобный интервал доставки.</p>
      <form class="form" data-mock>
        <div class="field"><input type="tel" required placeholder="Телефон *"></div>
        <label class="check"><input type="checkbox" required> Нажимая кнопку, я соглашаюсь с <a href="privacy.html">политикой конфиденциальности</a> и <a href="offer.html">публичной офертой</a></label>
        <button class="btn btn--accent" type="submit">Жду звонка</button>
      </form>
    </div>
    <img src="img/courier.jpg" alt="Курьер с пакетом шаров" style="border-radius:28px;aspect-ratio:4/3;object-fit:cover;box-shadow:var(--shadow-hover)">
  </div>
</section>'''
    page('soberisam.html', 'Собери сам — воздушные шары на заказ | Шар&Ко',
         'Конструктор собственной композиции из воздушных шаров с онлайн-расчётом.', px, 'soberisam', body)

def build_delivery():
    px = ''
    body = f'''{crumbs(px, [('', 'Доставка и оплата')])}
<section class="pagehead">
  <div class="container pagehead__grid">
    <div>
      <h1>Доставка и оплата</h1>
      <p class="pagehead__lead">Наша цель — ваш идеальный праздник: привозим шары в защитных пакетах на автомобиле и берём на себя всё, что может пойти не так.</p>
    </div>
    <img class="pagehead__img" src="img/courier.jpg" alt="Курьер с большим пакетом шаров">
  </div>
</section>
<section class="section" style="padding-top:24px">
  <div class="container">
    <div class="shead"><div><h2>Интервалы и тарифы</h2><p>Доставка по Москве и до 10 км за МКАД</p></div></div>
    <div class="tablewrap"><table class="table">
      <tr><th>Интервал</th><th>В пределах МКАД</th><th>За МКАД до 10 км</th></tr>
      <tr><td>10:00 – 14:00</td><td><b>900 ₽</b></td><td><b>1 400 ₽</b></td></tr>
      <tr><td>14:00 – 18:00</td><td><b>900 ₽</b></td><td><b>1 400 ₽</b></td></tr>
      <tr><td>18:00 – 22:00</td><td><b>1 200 ₽</b></td><td><b>1 700 ₽</b></td></tr>
      <tr><td>22:00 – 00:00</td><td><b>900 ₽</b></td><td><b>1 400 ₽</b></td></tr>
      <tr><td>Точное время / до 10:00 / после 00:00</td><td><b>2 000 ₽</b></td><td><b>2 000 ₽ + 50 ₽/км</b></td></tr>
    </table></div>
    <p class="muted" style="margin-top:16px;font-size:14px">Заказы от 25 шаров и коробки 60–70 см рассчитываем индивидуально. Самовывоз из студии — ежедневно с 9:00 до 21:00 по предварительному звонку (гарантия при самовывозе не действует).</p>
  </div>
</section>
<section class="section" style="padding-top:6px">
  <div class="container">
    <div class="shead"><div><h2>Оплата</h2><p>Работаем полностью по онлайн-оплате — это быстро и безопасно</p></div></div>
    <div class="adv__grid">
      <div class="adv__card"><div class="adv__icon">{ICONS['card'].replace('width="20" height="20"', 'width="30" height="30"')}</div>
        <h3>Картой на сайте</h3><p>Visa, Mastercard и МИР при 100% оплате заказа — чек приходит на почту мгновенно.</p></div>
      <div class="adv__card"><div class="adv__icon"><svg width="30" height="30" viewBox="0 0 24 24" fill="none"><path d="M4 6h16v12H4z" fill="#59C9AE"/><path d="m4 7 8 6 8-6" stroke="#fff" stroke-width="2"/></svg></div>
        <h3>Ссылкой-счётом</h3><p>Выставим счёт в мессенджер или на почту — оплатите в два касания с телефона.</p></div>
      <div class="adv__card"><div class="adv__icon"><svg width="30" height="30" viewBox="0 0 24 24" fill="none"><rect x="3" y="6" width="18" height="13" rx="2.5" fill="#F7C860"/><path d="M7 11h6M7 14.5h4" stroke="#2E2436" stroke-width="2" stroke-linecap="round"/></svg></div>
        <h3>Безнал для юрлиц</h3><p>Договор, счёт и закрывающие документы онлайн. Работаем по упрощёнке.</p></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:6px">
  <div class="container" style="max-width:860px">
    <div class="acc open">
      <button class="acc__btn" type="button">Гарантия 24 часа {ICONS['plus']}</button>
      <div class="acc__body"><div class="acc__in"><p>Если в течение суток после доставки с шарами что-то случилось — не переживайте, вопрос решим. Для больших шаров (бабблсы, гиганты, фольгированные фигуры) привезём замену, вернём деньги или перенесём стоимость на следующий заказ. Для стандартных шаров — вернём стоимость или перенесём на следующий заказ. Гарантия действует только при доставке нашим курьером.</p></div></div>
    </div>
    <div class="acc">
      <button class="acc__btn" type="button">Как продлить полёт шаров {ICONS['plus']}</button>
      <div class="acc__body"><div class="acc__in"><ul>
        <li>Идеальная температура — 20–23 °C: жара и холод одинаково вредны.</li>
        <li>Проветриваемое помещение без прямых солнечных лучей.</li>
        <li>Высокая влажность сокращает время полёта.</li>
        <li>Не оставляйте шары в машине дольше 2–3 часов в любую погоду.</li>
      </ul></div></div>
    </div>
    <div class="acc">
      <button class="acc__btn" type="button">Самовывоз из студии {ICONS['plus']}</button>
      <div class="acc__body"><div class="acc__in"><p>Ежедневно с 9:00 до 21:00 по предварительной договорённости — позвоните за час до приезда, и мы упакуем заказ к вашему визиту. Обратите внимание: при самовывозе гарантия на шары не действует.</p></div></div>
    </div>
  </div>
</section>
{cta_banner(px, 'Остались вопросы?', 'Позвоните или напишите в мессенджер — подскажем по срокам, цветам и любому поводу.', 'contacts.html', 'Написать нам', 'hero.jpg')}'''
    page('delivery.html', 'Доставка и оплата — Шар&Ко',
         'Тарифы и интервалы доставки воздушных шаров по Москве и МО, способы оплаты и гарантия.', px, 'delivery', body)

def build_about():
    px = ''
    gal = '\n'.join(f'<img src="img/{g}" alt="Наша работа" loading="lazy">' for g in
                    ['workshop.jpg', 'hero.jpg', 'build-your-own.jpg', 'courier.jpg'])
    body = f'''{crumbs(px, [('', 'О нас')])}
<section class="pagehead">
  <div class="container pagehead__grid">
    <div>
      <h1>Шар&amp;Ко — шары для счастливых людей</h1>
      <p class="pagehead__lead">Мы начинали с одного гелиевого баллона и стола на кухне, а теперь собираем по 40 композиций в день и всё равно относимся к каждому заказу как к первому.</p>
    </div>
    <img class="pagehead__img" src="img/workshop.jpg" alt="Наша мастерская">
  </div>
</section>
<section class="section" style="padding-top:24px">
  <div class="container">
    <div class="stats">
      <div class="stat"><b>6 лет</b><span>дарим Москве праздники</span></div>
      <div class="stat"><b>12 400</b><span>композиций собрано</span></div>
      <div class="stat"><b>95%</b><span>шаров летают больше месяца</span></div>
      <div class="stat"><b>4,9</b><span>средняя оценка заказов</span></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:10px">
  <div class="container split">
    <img src="img/build-your-own.jpg" alt="Шары и ленты в мастерской">
    <div>
      <h2 style="font-size:clamp(24px,2.6vw,34px);font-weight:800;margin-bottom:14px">Почему нам доверяют</h2>
      <p class="muted" style="margin-bottom:12px">Мы покупаем латекс и фольгу только у официальных поставщиков с сертификатами: Бельгия, Испания, Польша, Турция, США и Россия. Каждое облако собираем в день доставки — поэтому шары прилетают к вам максимально «свежими».</p>
      <p class="muted">А ещё мы честно предупреждаем, если идея не сработает: подскажем, как получить тот же эффект за меньший бюджет, и никогда не добавим в чек лишнего.</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:6px">
  <div class="container">
    <div class="shead"><div><h2>Наши принципы</h2></div></div>
    <div class="adv__grid">
      <div class="adv__card"><div class="adv__icon"><svg width="30" height="30" viewBox="0 0 24 24" fill="none"><path d="M12 21s-7-4.6-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.4-7 10-7 10Z" fill="#F4436C"/></svg></div>
        <h3>С любовью к деталям</h3><p>Ровные ленты, подобранные оттенки и ни одной случайной бусины — композиция должна выглядеть дорого даже на фото с телефона.</p></div>
      <div class="adv__card"><div class="adv__icon"><svg width="30" height="30" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="#9B8CF2" stroke-width="2"/><path d="M12 7v5l3.5 2" stroke="#9B8CF2" stroke-width="2" stroke-linecap="round"/></svg></div>
        <h3>Пунктуальность</h3><p>97% заказов приезжают в первой половине выбранного интервала. Опаздываем только по погоде — и всегда предупреждаем.</p></div>
      <div class="adv__card"><div class="adv__icon"><svg width="30" height="30" viewBox="0 0 24 24" fill="none"><path d="M20 4c-9 0-15 4-15 11 0 3 2 5 5 5 7 0 10-7 10-16Z" fill="#59C9AE"/></svg></div>
        <h3>Честная экологичность</h3><p>Латекс разлагается как листва, а бабблсы и ленты мы учим клиентов возвращать в студию на переработку.</p></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:6px">
  <div class="container">
    <div class="shead"><div><h2>Заглянуть в мастерскую</h2></div></div>
    <div class="gal">{gal}</div>
  </div>
</section>
{social_block(px)}'''
    page('about.html', 'О нас — Шар&Ко', 'История мастерской воздушных шаров Шар&Ко: цифры, принципы и фотографии мастерской.', px, 'about', body)

def build_contacts():
    px = ''
    body = f'''{crumbs(px, [('', 'Контакты')])}
<section class="pagehead">
  <div class="container pagehead__grid">
    <div>
      <h1>Контакты</h1>
      <p class="pagehead__lead">Пишите и звоните ежедневно с 9:00 до 21:00 — отвечаем в мессенджерах в среднем за 7 минут.</p>
    </div>
    <img class="pagehead__img" src="img/hero.jpg" alt="Шары студии Шар&Ко">
  </div>
</section>
<section class="section" style="padding-top:24px">
  <div class="container contactcards">
    <div class="ccard"><h3>Телефон</h3><b><a href="{PHONE_HREF}">{PHONE}</a></b><p>Ежедневно с 9:00 до 21:00</p></div>
    <div class="ccard"><h3>Почта</h3><b><a href="mailto:{EMAIL}">{EMAIL}</a></b><p>Для заказов и документов</p></div>
    <div class="ccard"><h3>Студия</h3><b>Москва, ул. Лётчиков, 12</b><p>Самовывоз по предварительному звонку</p></div>
    <div class="ccard"><h3>Мессенджеры</h3><b>Telegram · WhatsApp · VK</b><p>Присылайте референсы — соберём похожее</p></div>
  </div>
</section>
<section class="section" style="padding-top:10px">
  <div class="container split">
    <div>
      <h2 style="font-size:clamp(24px,2.6vw,34px);font-weight:800;margin-bottom:12px">Напишите нам</h2>
      <p class="muted" style="margin-bottom:20px">Оставьте контакты и пару слов о празднике — вернёмся с идеями и расчётом.</p>
      <form class="form" data-mock>
        <div class="field"><input type="text" required placeholder="Как вас зовут?"></div>
        <div class="field"><input type="tel" required placeholder="Телефон или ник в мессенджере *"></div>
        <div class="field"><textarea placeholder="Повод, дата и пара слов о любимых цветах"></textarea></div>
        <label class="check"><input type="checkbox" required> Согласен(на) с <a href="privacy.html">политикой конфиденциальности</a></label>
        <button class="btn btn--accent" type="submit">Отправить</button>
      </form>
    </div>
    <div class="map">
      <div class="map__pin">
        <svg width="52" height="52" viewBox="0 0 24 24" fill="none"><path d="M12 22s-8-5.3-8-11.5A8 8 0 0 1 12 2a8 8 0 0 1 8 8.5C20 16.7 12 22 12 22Z" fill="#F4436C"/><circle cx="12" cy="10.5" r="3.2" fill="#fff"/></svg>
        <span class="map__label">Студия Шар&amp;Ко · ул. Лётчиков, 12</span>
      </div>
    </div>
  </div>
</section>'''
    page('contacts.html', 'Контакты — Шар&Ко', 'Телефон, почта, адрес студии и форма обратной связи мастерской воздушных шаров.', px, 'contacts', body)

def build_legal():
    px = ''
    privacy = f'''{crumbs(px, [('', 'Политика конфиденциальности')])}
<section class="pagehead"><div class="container"><h1>Политика конфиденциальности</h1></div></section>
<section class="section" style="padding-top:20px"><div class="container prose">
  <p>Демонстрационный текст для макета: замените его на актуальную редакцию документа вашего юридического лица.</p>
  <h2>1. Какие данные мы собираем</h2>
  <p>Имя, телефон, e-mail и адрес доставки — только то, что вы сами оставили в формах сайта или сообщили менеджеру для оформления заказа.</p>
  <h2>2. Зачем они нужны</h2>
  <ul><li>оформить и доставить заказ;</li><li>связаться по вопросам заказа;</li><li>прислать подборку новинок, если вы подписались на рассылку.</li></ul>
  <h2>3. Как мы их храним</h2>
  <p>Данные хранятся в защищённой CRM мастерской и не передаются третьим лицам, кроме службы доставки и платёжного провайдера.</p>
  <h2>4. Ваши права</h2>
  <p>Вы можете запросить копию своих данных или попросить удалить их, написав на {EMAIL} — ответим в течение 3 рабочих дней.</p>
</div></section>'''
    offer = f'''{crumbs(px, [('', 'Публичная оферта')])}
<section class="pagehead"><div class="container"><h1>Публичный договор (оферта)</h1></div></section>
<section class="section" style="padding-top:20px"><div class="container prose">
  <p>Демонстрационный текст для макета: замените его на актуальную редакцию оферты вашего юридического лица.</p>
  <h2>1. Предмет договора</h2>
  <p>Продавец изготавливает и передаёт покупателю композиции из воздушных шаров, а покупатель оплачивает и принимает их на условиях, опубликованных на сайте.</p>
  <h2>2. Момент заключения договора</h2>
  <p>Договор считается заключённым с момента подтверждения заказа менеджером и 100% онлайн-оплаты.</p>
  <h2>3. Доставка и приёмка</h2>
  <p>Заказ передаётся в транспортировочном пакете в согласованный интервал. Проверьте композицию при курьере: после его отъезда претензии по внешнему виду принимаются в рамках гарантии 24 часа.</p>
  <h2>4. Возвраты</h2>
  <p>При отмене заказа ранее чем за 48 часов до доставки возвращаем 100% оплаты; при отмене заказа «день в день» предоплата не возвращается, так как материалы уже собраны.</p>
</div></section>'''
    page('privacy.html', 'Политика конфиденциальности — Шар&Ко', 'Политика обработки персональных данных (демо).', px, '', privacy)
    page('offer.html', 'Публичная оферта — Шар&Ко', 'Публичный договор оферты (демо).', px, '', offer)

# ---------------------------------------------------------------- PWA
PAGES = []

def build_manifest():
    import json
    manifest = {
        'name': 'Шар&Ко — воздушные шары с доставкой по Москве',
        'short_name': 'Шар&Ко',
        'description': 'Готовые наборы воздушных шаров и конструктор собственной композиции с доставкой по Москве и МО.',
        'lang': 'ru',
        'start_url': './index.html',
        'scope': './',
        'display': 'standalone',
        'orientation': 'portrait-primary',
        'background_color': '#FFF7F3',
        'theme_color': '#F4436C',
        'categories': ['shopping', 'lifestyle'],
        'icons': [
            {'src': 'img/icons/icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
            {'src': 'img/icons/icon-512.png', 'sizes': '512x512', 'type': 'image/png'},
            {'src': 'img/icons/icon-maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'},
        ],
    }
    open(os.path.join(HERE, 'manifest.webmanifest'), 'w', encoding='utf-8').write(
        json.dumps(manifest, ensure_ascii=False, indent=2))
    print('ok manifest.webmanifest')

def build_sw():
    import glob, time
    images = sorted('img/' + os.path.basename(p) for p in glob.glob(os.path.join(HERE, 'img', '*.jpg')))
    icons = sorted('img/icons/' + os.path.basename(p) for p in glob.glob(os.path.join(HERE, 'img', 'icons', '*.png')))
    core = ['./', './offline.html', './manifest.webmanifest'] + ['./' + p for p in PAGES] + icons + images
    core_js = ',\n  '.join(f"'{c}'" for c in core)
    sw = f'''/* Шар&Ко PWA service worker */
const CACHE = 'sharco-v{int(time.time())}';
const CORE = [
  {core_js}
];

self.addEventListener('install', (e) => {{
  e.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(CORE)).then(() => self.skipWaiting())
  );
}});

self.addEventListener('activate', (e) => {{
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
}});

self.addEventListener('fetch', (e) => {{
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;

  /* страницы: сеть -> кэш -> офлайн-страница */
  if (req.mode === 'navigate') {{
    e.respondWith(
      fetch(req)
        .then((res) => {{
          if (res.ok) {{
            const copy = res.clone();
            caches.open(CACHE).then((c) => c.put(req, copy));
          }}
          return res;
        }})
        .catch(() => caches.match(req).then((hit) => hit || caches.match('./offline.html')))
    );
    return;
  }}

  /* остальное: кэш -> сеть (и положим в кэш на будущее) */
  e.respondWith(
    caches.match(req).then((hit) => hit ||
      fetch(req).then((res) => {{
        if (res.ok) {{
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(req, copy));
        }}
        return res;
      }}).catch(() => new Response('', {{ status: 404, statusText: 'offline' }})))
  );
}});
'''
    open(os.path.join(HERE, 'sw.js'), 'w', encoding='utf-8').write(sw)
    print('ok sw.js (precache: %d файлов)' % len(core))

def build_offline():
    html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Нет соединения — Шар&amp;Ко</title>
<meta name="theme-color" content="#F4436C">
<link rel="icon" type="image/png" sizes="192x192" href="img/icons/icon-192.png">
<style>
  body{{margin:0;font-family:"Manrope","Segoe UI",system-ui,sans-serif;background:#FFF7F3;color:#2E2436;display:grid;place-items:center;min-height:100vh;text-align:center;padding:24px}}
  .card{{background:#fff;border-radius:28px;box-shadow:0 16px 40px rgba(46,36,54,.12);padding:48px 40px;max-width:420px}}
  h1{{font-size:26px;margin:18px 0 10px}}
  p{{color:#6E6478;font-size:15px;line-height:1.6;margin:0 0 24px}}
  button{{background:#F4436C;color:#fff;border:0;border-radius:14px;padding:14px 28px;font:inherit;font-weight:800;cursor:pointer}}
  button:hover{{background:#D92C58}}
  a{{display:block;margin-top:16px;color:#F4436C;font-weight:700;text-decoration:none}}
</style>
</head>
<body>
<div class="card">
  <svg width="72" height="72" viewBox="0 0 64 64" fill="none" aria-hidden="true">
    <ellipse cx="24" cy="24" rx="13" ry="16" fill="#F4436C"/>
    <ellipse cx="41" cy="20" rx="11" ry="14" fill="#59C9AE" opacity=".9"/>
    <ellipse cx="34" cy="34" rx="10" ry="13" fill="#F7C860" opacity=".95"/>
    <path d="M24 40c2 6-2 10 0 16M41 34c1 8-3 12-1 20M34 47c1 5-1 8 0 12" stroke="#2E2436" stroke-width="2" stroke-linecap="round"/>
  </svg>
  <h1>Пока нет соединения</h1>
  <p>Вы офлайн. Уже открытые страницы и каталог доступны из кэша приложения, а как только сеть вернётся — всё обновится само.</p>
  <button type="button" onclick="location.reload()">Попробовать снова</button>
  <a href="index.html">Открыть главную из кэша</a>
</div>
</body>
</html>
'''
    open(os.path.join(HERE, 'offline.html'), 'w', encoding='utf-8').write(html)
    print('ok offline.html')

# ---------------------------------------------------------------- deploy (Netlify)
DEPLOY = os.path.join(HERE, '..', 'deploy')

def build_404():
    html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>404 — страница не найдена | Шар&amp;Ко</title>
<meta name="theme-color" content="#F4436C">
<link rel="icon" type="image/png" sizes="192x192" href="img/icons/icon-192.png">
<link rel="manifest" href="manifest.webmanifest">
<style>
  body{{margin:0;font-family:"Manrope","Segoe UI",system-ui,sans-serif;background:#FFF7F3;color:#2E2436;display:grid;place-items:center;min-height:100vh;text-align:center;padding:24px}}
  .card{{background:#fff;border-radius:28px;box-shadow:0 16px 40px rgba(46,36,54,.12);padding:48px 40px;max-width:460px}}
  .code{{font-size:64px;font-weight:800;color:#F4436C;line-height:1}}
  h1{{font-size:26px;margin:14px 0 10px}}
  p{{color:#6E6478;font-size:15px;line-height:1.6;margin:0 0 24px}}
  a.btn{{display:inline-block;background:#F4436C;color:#fff;border:0;border-radius:14px;padding:14px 28px;font-weight:800;text-decoration:none}}
  a.btn:hover{{background:#D92C58}}
  a.alt{{display:block;margin-top:16px;color:#F4436C;font-weight:700;text-decoration:none}}
</style>
</head>
<body>
<div class="card">
  <div class="code">404</div>
  <h1>Такой страницы нет</h1>
  <p>Возможно, набор улетел вместе с шариками. Загляните в каталог — там точно что-то праздничное найдётся.</p>
  <a class="btn" href="index.html">На главную</a>
  <a class="alt" href="shop.html">Открыть каталог наборов →</a>
</div>
</body>
</html>
'''
    open(os.path.join(HERE, '404.html'), 'w', encoding='utf-8').write(html)
    print('ok 404.html')

def build_headers():
    open(os.path.join(HERE, '_headers'), 'w', encoding='utf-8').write('''/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
/sw.js
  Cache-Control: no-cache
/manifest.webmanifest
  Cache-Control: no-cache
/*.html
  Cache-Control: no-cache
/catalog/*.html
  Cache-Control: no-cache
/product/*.html
  Cache-Control: no-cache
/img/*
  Cache-Control: public, max-age=604800
''')
    print('ok _headers')

def build_deploy():
    import shutil
    deploy = os.path.normpath(DEPLOY)
    shutil.rmtree(deploy, ignore_errors=True)
    os.makedirs(os.path.join(deploy, 'catalog'))
    os.makedirs(os.path.join(deploy, 'product'))
    files = list(PAGES) + ['offline.html', '404.html', 'sw.js', 'manifest.webmanifest', '_headers']
    for fname in files:
        src = os.path.join(HERE, fname)
        dst = os.path.join(deploy, fname)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
    shutil.copytree(os.path.join(HERE, 'img'), os.path.join(deploy, 'img'),
                    ignore=shutil.ignore_patterns('icon-src.png'))
    open(os.path.join(deploy, 'README.md'), 'w', encoding='utf-8').write('''# Папка для деплоя на Netlify

Это готовый статический сайт-PWA «Шар&Ко». Чтобы опубликовать:

1. Зайдите на https://app.netlify.com (Sites → Add new site → Deploy manually,
   или сразу https://app.netlify.com/drop).
2. Перетащите ЭТУ папку (deploy) в окно загрузки — или заархивируйте её в ZIP и выберите файл.
3. Netlify раздаст сайт по адресу вида https://<имя>.netlify.app с HTTPS —
   PWA, service worker и установка на телефон заработают сразу.

Дополнительно уже настроено:
- 404.html — фирменная страница ошибки Netlify;
- _headers — кэш-политика (html и sw.js без кэша, картинки на неделю);
- sw.js прекэширует всё приложение для офлайн-работы.

Чтобы обновить сайт после правок: в папке site выполните `python3 build.py`,
затем `python3 build.py --deploy` (или просто запустите build.py — папка deploy
пересобирается автоматически), и загрузите новую папку deploy тем же способом
(Netlify → Deploys → drag&drop поверх старого сайта).
''')
    n = sum(len(fs) for _, _, fs in os.walk(deploy))
    size = sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(deploy) for f in fs)
    print(f'ok deploy/ ({n} файлов, {size / 1e6:.1f} MB)')

# ---------------------------------------------------------------- run
if __name__ == '__main__':
    build_home()
    build_shop()
    for slug, title, image, descr in CATS:
        build_category(slug, title, image, descr)
    for p in PRODUCTS:
        build_product(p)
    build_soberisam()
    build_delivery()
    build_about()
    build_contacts()
    build_legal()
    build_manifest()
    build_sw()
    build_offline()
    build_404()
    build_headers()
    build_deploy()
    print('total pages:', len(PAGES))
