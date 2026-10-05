"""Social preview images (1200x630) for every tool page, one per tool and language.

Each tool gets its own drawn icon; title and description are the page's own
localized h1/desc, sized per language so nothing is cut off.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
FD = os.path.join(HERE, 'fonts')
CJK = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
CJK_R = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
CJK_FACE = {'ja': 0, 'ko': 1, 'zh-CN': 2, 'zh-TW': 3}
SCRIPT = {'ar': 'arabic', 'fa': 'arabic', 'ur': 'arabic', 'he': 'hebrew', 'th': 'thai',
          'bn': 'bengali', 'hi': 'devanagari', 'mr': 'devanagari', 'gu': 'gujarati',
          'pa': 'gurmukhi', 'kn': 'kannada', 'ml': 'malayalam', 'ta': 'tamil', 'te': 'telugu'}
RTL = {'ar', 'fa', 'ur', 'he'}
TALL = {'arabic', 'thai', 'bengali', 'devanagari', 'gujarati', 'gurmukhi', 'kannada', 'malayalam', 'tamil', 'telugu'}
NO_BREAK_START = set('、。，．！？」）ー・…：；,.!?)%')
W, H = 1200, 630
WHITE, GREY, VIOLET = (245, 243, 255), (168, 166, 186), (167, 139, 250)
_cache = {}


def _font(lang, size, bold):
    k = (lang, size, bold)
    if k in _cache:
        return _cache[k]
    if lang in CJK_FACE:
        f = ImageFont.truetype(CJK if bold else CJK_R, size, index=CJK_FACE[lang])
    else:
        f = ImageFont.truetype(os.path.join(FD, f"{SCRIPT.get(lang, 'base')}-{'700' if bold else '400'}.ttf"), size,
                               layout_engine=ImageFont.Layout.RAQM)
    _cache[k] = f
    return f


def _dir(lang):
    return 'rtl' if lang in RTL else 'ltr'


def _len(d, text, font, lang):
    return d.textlength(text, font=font, direction=_dir(lang)) if lang not in CJK_FACE else d.textlength(text, font=font)


def _split_long(d, word, font, lang, maxw):
    """Break a single over-long word (e.g. Thai run without spaces) between base characters."""
    import unicodedata
    parts, cur = [], ''
    for ch in word:
        if cur and unicodedata.category(ch)[0] != 'M' and _len(d, cur + ch, font, lang) > maxw:
            parts.append(cur); cur = ch
        else:
            cur += ch
    parts.append(cur)
    return parts


def _tokens(text, lang):
    """Unbreakable units joined without separators (spaces are their own tokens)."""
    import re
    if lang in ('ja', 'zh-TW'):
        try:
            import budoux
            parser = budoux.load_default_japanese_parser() if lang == 'ja' else budoux.load_default_traditional_chinese_parser()
            return [t for chunk in parser.parse(text) for t in re.split(r"( )", chunk) if t]
        except ImportError:
            pass
    if lang in ('ja', 'zh-CN', 'zh-TW'):
        return re.findall(r"[A-Za-z0-9][A-Za-z0-9.\-]*|\s|.", text)
    if lang == 'th':
        try:
            from pythainlp.tokenize import word_tokenize
            return word_tokenize(text, engine='newmm', keep_whitespace=True)
        except ImportError:
            pass
    return re.split(r"( )", text)


def _wrap(d, text, font, lang, maxw, split_long=True):
    toks = []
    for t in _tokens(text, lang):
        if split_long and t.strip() and _len(d, t, font, lang) > maxw:
            if lang in ('ja', 'zh-CN', 'zh-TW'):
                import re
                toks += re.findall(r"[A-Za-z0-9][A-Za-z0-9.\-]*|\s|.", t)
            else:
                toks += _split_long(d, t, font, lang, maxw)
        elif t:
            toks.append(t)
    lines, line = [], ''
    for t in toks:
        cand = line + t
        if line.strip() and t.strip() and _len(d, cand.rstrip(), font, lang) > maxw and t[0] not in NO_BREAK_START:
            lines.append(line.rstrip()); line = t
        else:
            line = cand if (line or t.strip()) else ''
    lines.append(line.rstrip())
    return [l for l in lines if l]


def _longest_word(d, text, font, lang):
    import re
    return max((_len(d, t.replace('\u200b', ''), font, lang) for t in _tokens(re.sub(r'(\w{5,})-(?=\w)', '\\1-\u200b ', text), lang) if t.strip()), default=0)


def _wrap_title(d, text, font, lang, maxw):
    # allow a break after a hyphen only inside long compounds ("Spielekosten-Rechner"),
    # never right after a short prefix like "KI-" / "AI-"
    if lang not in CJK_FACE:
        import re
        marked = re.sub(r"(\w{5,})-(?=\w)", "\\1-\u200b ", text)
        lines = _wrap(d, marked, font, lang, maxw)
        return [l.replace('-\u200b ', '-').replace('\u200b', '') for l in lines]
    return _wrap(d, text, font, lang, maxw)


# ---------- icons (drawn at centre cx, cy) ----------
def _ic_token(d, cx, cy):
    d.rounded_rectangle([cx - 150, cy - 95, cx + 150, cy + 75], radius=28, fill=(39, 30, 80), outline=VIOLET, width=5)
    d.polygon([(cx - 90, cy + 72), (cx - 40, cy + 72), (cx - 100, cy + 125)], fill=VIOLET)
    d.polygon([(cx - 84, cy + 70), (cx - 48, cy + 70), (cx - 91, cy + 108)], fill=(39, 30, 80))
    cols = [(250, 204, 21), (52, 211, 153), (244, 114, 182), (96, 165, 250), (167, 139, 250)]
    x = cx - 115
    for i, w in enumerate([62, 40, 75, 45]):
        d.rounded_rectangle([x, cy - 55, x + w, cy - 25], radius=8, fill=cols[i])
        x += w + 10
    x = cx - 115
    for i, w in enumerate([55, 90, 40]):
        d.rounded_rectangle([x, cy - 5, x + w, cy + 25], radius=8, fill=cols[(i + 2) % 5])
        x += w + 10


def _ic_video(d, cx, cy):
    d.rounded_rectangle([cx - 150, cy - 70, cx + 150, cy + 110], radius=22, fill=(39, 30, 80), outline=VIOLET, width=5)
    d.rounded_rectangle([cx - 150, cy - 120, cx + 150, cy - 70], radius=12, fill=VIOLET)
    for i in range(5):
        x = cx - 138 + i * 56
        d.polygon([(x, cy - 72), (x + 26, cy - 72), (x + 46, cy - 118), (x + 20, cy - 118)], fill=(39, 30, 80))
    d.polygon([(cx - 30, cy - 25), (cx - 30, cy + 75), (cx + 55, cy + 25)], fill=(244, 114, 182))


def _ic_image(d, cx, cy):
    d.rounded_rectangle([cx - 150, cy - 110, cx + 150, cy + 110], radius=22, fill=(39, 30, 80), outline=VIOLET, width=5)
    d.ellipse([cx + 40, cy - 75, cx + 95, cy - 20], fill=(250, 204, 21))
    d.polygon([(cx - 130, cy + 90), (cx - 40, cy - 30), (cx + 40, cy + 90)], fill=(52, 211, 153))
    d.polygon([(cx - 10, cy + 90), (cx + 60, cy + 5), (cx + 130, cy + 90)], fill=(96, 165, 250))


def _ic_plans(d, cx, cy):
    for k, (dx, dy, col) in enumerate([(-55, 20, (60, 50, 120)), (55, -20, (39, 30, 80))]):
        x, y = cx + dx, cy + dy
        d.rounded_rectangle([x - 95, y - 110, x + 95, y + 110], radius=22, fill=col, outline=VIOLET, width=5)
    x, y = cx + 55, cy - 20
    d.text((x, y - 45), '$', font=ImageFont.truetype(os.path.join(FD, 'base-700.ttf'), 80), fill=(250, 204, 21), anchor='mm')
    for i, w in enumerate([110, 80, 95]):
        d.rounded_rectangle([x - 60, y + 15 + i * 26, x - 60 + w, y + 29 + i * 26], radius=7, fill=VIOLET if i else (52, 211, 153))


def _ic_agents(d, cx, cy):
    d.line([cx, cy - 115, cx, cy - 80], fill=VIOLET, width=6)
    d.ellipse([cx - 14, cy - 132, cx + 14, cy - 104], fill=(244, 114, 182))
    d.rounded_rectangle([cx - 130, cy - 80, cx + 130, cy + 110], radius=40, fill=(39, 30, 80), outline=VIOLET, width=5)
    d.rounded_rectangle([cx - 165, cy - 10, cx - 130, cy + 50], radius=10, fill=VIOLET)
    d.rounded_rectangle([cx + 130, cy - 10, cx + 165, cy + 50], radius=10, fill=VIOLET)
    for ex in (-55, 55):
        d.ellipse([cx + ex - 26, cy - 30, cx + ex + 26, cy + 22], fill=(96, 165, 250))
    d.rounded_rectangle([cx - 55, cy + 50, cx + 55, cy + 70], radius=10, fill=(52, 211, 153))


def _ic_game(d, cx, cy):
    d.rounded_rectangle([cx - 150, cy - 85, cx + 150, cy + 85], radius=85, fill=(39, 30, 80), outline=VIOLET, width=5)
    d.rectangle([cx - 100, cy - 10, cx - 50, cy + 10], fill=VIOLET)
    d.rectangle([cx - 85, cy - 25, cx - 65, cy + 25], fill=VIOLET)
    for dx, dy, c in [(70, -22, (250, 204, 21)), (100, 8, (52, 211, 153)), (40, 8, (244, 114, 182)), (70, 38, (96, 165, 250))]:
        d.ellipse([cx + dx - 13, cy + dy - 13, cx + dx + 13, cy + dy + 13], fill=c)


ICONS = dict(token=_ic_token, video=_ic_video, image=_ic_image, plans=_ic_plans, agents=_ic_agents, game=_ic_game)


def _layout(d, lang, title, sub, maxw, top, bottom, strict=True):
    """Largest title/sub sizes where every word fits, with no truncation."""
    lh = 1.42 if (SCRIPT.get(lang) in TALL) else 1.22
    slh = 1.55 if (SCRIPT.get(lang) in TALL) else 1.42
    best = None
    for ts in range(76, 33, -2):
        tf = _font(lang, ts, True)
        if strict and _longest_word(d, title, tf, lang) > maxw:
            continue
        tl = _wrap_title(d, title, tf, lang, maxw)
        if len(tl) > 3 or any(_len(d, l, tf, lang) > maxw for l in tl):
            continue
        th = int(ts * lh) * len(tl)
        for ss in range(30, 19, -1):
            sf = _font(lang, ss, False)
            sl = _wrap(d, sub, sf, lang, maxw)
            sh = int(ss * slh) * len(sl)
            if top + th + 18 + sh <= bottom and all(_len(d, l, sf, lang) <= maxw for l in sl):
                score = ts * 1.0 + ss * 2.2 - (len(tl) - 1) * 6
                if best is None or score > best[0]:
                    best = (score, ts, tl, ss, sl, lh, slh)
                break
    if best is None and strict:  # no size keeps every word whole: allow breaks inside long words
        return _layout(d, lang, title, sub, maxw, top, bottom, strict=False)
    if best is None:  # last resort: smallest sizes, still full text
        print("og_tool: tight fit", lang, title)
        ts, ss = 40, 20
        best = (0, ts, _wrap_title(d, title, _font(lang, ts, True), lang, maxw), ss,
                _wrap(d, sub, _font(lang, ss, False), lang, maxw), lh, slh)
    return best[1:]


def render(lang, key, title, sub, out_path, icon_path=None):
    img = Image.new('RGB', (W, H), (11, 11, 15))
    glow = Image.new('RGB', (W, H), (0, 0, 0))
    ImageDraw.Draw(glow).ellipse([250, -380, 950, 320], fill=(60, 52, 140))
    img = Image.blend(img, glow.filter(ImageFilter.GaussianBlur(140)), 0.75)
    d = ImageDraw.Draw(img)
    rtl = lang in RTL
    L, R = 90, W - 90
    maxw = 615
    # text column on the left (LTR) or right (RTL); icon on the other side
    tx = R if rtl else L
    icx = 285 if rtl else 915
    ICONS.get(key, _ic_token)(d, icx, 300)

    brand = _font('en', 34, True)
    if icon_path and os.path.exists(icon_path):
        ic = Image.open(icon_path).convert('RGBA').resize((56, 56))
        m = Image.new('L', (56, 56), 0)
        ImageDraw.Draw(m).rounded_rectangle([0, 0, 55, 55], radius=13, fill=255)
        img.paste(ic, (R - 56 if rtl else L, 92), m)
    bx = R - 56 - 22 if rtl else L + 78
    d.text((bx, 120), 'TokenSave', font=brand, fill=(222, 220, 235), anchor='rm' if rtl else 'lm')

    top, bottom = 180, 528
    ts, tl, ss, sl, lh, slh = _layout(d, lang, title, sub, maxw, top, bottom)
    anchor = 'ra' if rtl else 'la'
    kw = {} if lang in CJK_FACE else {'direction': _dir(lang)}
    tf, sf = _font(lang, ts, True), _font(lang, ss, False)
    block = int(ts * lh) * len(tl) + 18 + int(ss * slh) * len(sl)
    y = max(top, min(bottom - block, 315 - block // 2))
    for ln in tl:
        d.text((tx, y), ln, font=tf, fill=WHITE, anchor=anchor, **kw)
        y += int(ts * lh)
    y += 18
    for ln in sl:
        d.text((tx, y), ln, font=sf, fill=GREY, anchor=anchor, **kw)
        y += int(ss * slh)
    d.text((tx, 572), 'tokensave.app', font=_font('en', 30, True), fill=VIOLET, anchor='rm' if rtl else 'lm')
    img.save(out_path, quality=88)
