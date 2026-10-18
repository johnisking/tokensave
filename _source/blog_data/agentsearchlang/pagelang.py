"""Language of cited pages, checked by hand (URL path, page title in the search results)."""
from urllib.parse import urlparse
PATH_RULES = [("tabelog.com/cn", "zh"), ("tabelog.com/en", "en"), ("tykyiv.com/en", "en"), ("tokyometro.jp/lang_en", "en"), ("tokyometro.jp/en", "en"),
              ("guide.michelin.com/kr/ko", "ko"), ("guide.michelin.com/jp/ja", "ja"), ("guide.michelin.com/us/en", "en"), ("guide.michelin.com/en", "en"),
              ("rfa.org/korean", "ko"), ("news.un.org/en", "en"), ("note.com/yoshi_foodie_jp", "en"), ("timeout.es/madrid/es", "es"),
              ("kiev.vgorode.ua/ukr", "uk"), ("nv.ua/ukr", "uk"), ("kyivmaps.com/en", "en"), ("es.euronews.com", "es"), ("longbridge.com/en", "en"),
              ("tokyoramenoftheyear.com/ja", "ja")]
HOSTS = {
 "ko": "v.daum.net kbthink.com blog.namanecard.com news.seoul.go.kr jab-guyver.co.kr core.asiae.co.kr mt.co.kr wikitree.co.kr biz.sbs.co.kr newspim.com hankookilbo.com sidae.com magazine.hankyung.com allurekorea.com",
 "ja": "tokyometro.jp kumanichi.com mod.go.jp jma.go.jp minkabu.jp jiji.com jimin.jp tabelog.com award.tabelog.com ugatech.jp ramendb.supleks.jp nlab.itmedia.co.jp retty.me appbank.net kyodonewsprwire.jp walkerplus.com adrim.co.jp roote.ekispert.net tbladvisory.com ramental.net",
 "zh": "etnet.com.hk stheadline.com",
 "es": "elespanol.com moncloa.com rtvc.es infobae.com periodistadigital.com libertaddigital.com ifema.es gastroactitud.com losviajeros.com neo2.com eldiario.es guiadelocio.es unbuendiaenmadrid.com muchoturismo.com cocidomadrid.com losmejoresdemadrid.com miradormadrid.com comunidad.madrid gacetinmadrid.com crtm.es esdiario.com esmadrid.com hola.com merca2.es lasrecetasdecarol.com",
 "uk": "epravda.com.ua pro.kyiv.ua grani.kiev.ua ipress.ua ukrinform.ua nashkiev.ua dovidnik.com.ua 44.ua tykyiv.com suspilne.media",
 "pl": "viamichelin.pl",
 "unknown": "yandex.com",
}
H = {h: l for l, hs in HOSTS.items() for h in hs.split()}

def page_lang(u):
    low = u.lower().split('://', 1)[-1]
    low = low[4:] if low.startswith('www.') else low
    for p, l in PATH_RULES:
        if low.startswith(p): return l
    h = urlparse(u).netloc.lower(); h = h[4:] if h.startswith('www.') else h
    return H.get(h, 'en')
