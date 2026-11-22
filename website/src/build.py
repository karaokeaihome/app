# -*- coding: utf-8 -*-
# Website 6 ngon ngu: trang chu = luoi bieu tuong, moi tinh nang 1 trang rieng.
# Sua chu trong content.py roi chay: python3 build.py  -> ../website-cai-dat/public
import os, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import C, LANGS, NAMES, SAY, PRICE, PRICE_LABEL, PRICE_NOTE, UI
from pages import P, APK, IOS, SITE, LEGAL
import qrcode, qrcode.image.svg
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'..','public') if os.path.isdir(os.path.join(HERE,'..','public')) else os.path.join(HERE,'..','website-cai-dat','public')  # repo GitHub: website/src -> website/public
e=html.escape
# Hinh co chu: ban tieng Viet o /img/<ten>.jpg, ngon ngu khac o /img/<lang>/<ten>.jpg (tao bang mockups/render.py)
LOC={'home','entertain','phone','translate','fitness','theme-kids','theme-elder','theme-women','theme-tech'}
def im(l,n): return '/img/%s.jpg'%n if (l=='vi' or n not in LOC) else '/img/%s/%s.jpg'%(l,n)
CSS=open(os.path.join(HERE,'page.css'),encoding='utf-8').read()+"""
.lang{display:flex;gap:6px;flex-wrap:wrap;justify-content:center;padding:8px 16px 0;max-width:1100px;margin:0 auto}
.lang a{font-size:.85rem;padding:4px 10px;border-radius:999px;border:1px solid #2a2a30;color:var(--mute);text-decoration:none}
.lang a.on{border-color:var(--acc);color:var(--acc)}
.price{max-width:520px;margin:24px auto 0;background:linear-gradient(135deg,#2a2210,#141416);border:1px solid #4a3d18;border-radius:18px;padding:18px;text-align:center}
.price .l{color:var(--mute);font-size:.95rem}.price .v{font-size:2.3rem;font-weight:800;color:var(--acc);line-height:1.2}.price .n{color:var(--mute);font-size:.9rem}
.grp{margin:28px 0 6px;color:var(--acc);font-size:.85rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.icons{display:grid;gap:14px 10px;grid-template-columns:repeat(4,1fr)}
@media(min-width:700px){.icons{grid-template-columns:repeat(6,1fr)}}
@media(min-width:1000px){.icons{grid-template-columns:repeat(8,1fr)}}
.ic{display:flex;flex-direction:column;align-items:center;text-decoration:none;color:var(--fg);text-align:center;font-size:.82rem;line-height:1.25}
.ic .b{width:64px;height:64px;border-radius:18px;background:linear-gradient(160deg,#26221a,#141416);border:1px solid #3a3220;display:flex;align-items:center;justify-content:center;font-size:1.9rem;margin-bottom:6px;transition:transform .15s,border-color .15s}
.ic:hover .b,.ic:focus .b{transform:translateY(-2px);border-color:var(--acc)}
.tap{color:var(--mute);text-align:center;font-size:.9rem;margin:22px 0 0}
.detail{max-width:820px;margin:0 auto;padding:16px}
.detail .bk{display:inline-block;margin:8px 0 18px;text-decoration:none}
.detail .big{width:96px;height:96px;border-radius:26px;background:linear-gradient(160deg,#2a2210,#141416);border:1px solid #4a3d18;display:flex;align-items:center;justify-content:center;font-size:3rem}
.detail h1{font-size:clamp(1.8rem,5vw,2.6rem);margin:16px 0 4px}
.detail .tag{color:var(--acc);font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:.85rem}
.detail p.d{font-size:1.15rem;color:var(--fg);opacity:.9}
.detail img{margin:20px 0}
.dlg{display:grid;gap:18px;grid-template-columns:1fr}@media(min-width:760px){.dlg{grid-template-columns:1fr 1fr}}
.dlc{background:var(--card);border:1px solid #2a2a30;border-radius:18px;padding:20px}.dlc h2{margin:0 0 12px}
.qr{display:flex;gap:16px;align-items:center;flex-wrap:wrap}.qr img{width:150px;height:150px;background:#fff;border-radius:12px;padding:8px;margin:0}
.dlc ol{padding-left:1.2em}.dlc li{margin:6px 0}.note{font-size:.9rem;color:var(--mute);border-left:3px solid var(--acc);padding-left:10px}
.gal{display:grid;gap:12px;grid-template-columns:1fr 1fr;max-width:760px;margin:24px auto 0}.gal .main{grid-column:1/3}.gal img{border-radius:16px}
"""
# (slug, group key, list key, index)  group headings reuse section tags
GROUPS=[('k_tag',[('goi-bai','K',None),('san-hat','san',0),('phong-thu','stu',0),('tong-vang-mic','k_f',0),('hang-cho','k_f',1),('cham-diem','k_f',2),('radio','k_f',3)]),
 ('a_tag',[('tro-ly-ai','A',None),('lich-thoi-tiet','a_f',0),('tin-hom-nay','a_f',1),('dich-noi','a_f',2)]),
 ('f_tag',[('be-hoc','f_f',0),('ong-ba','f_f',1),('chi-em','f_f',2),('anh-em','f_f',3),('the-duc','f_f',4),('giai-tri','f_f',5),('giao-dien','T',None)]),
 ('m_tag',[('bao-tien','m_f',0),('dam-thoai','m_f',1),('loi-nhac','m_f',2),('nha-thong-minh','m_f',3),('camera','m_f',4),('kho-ung-dung','m_f',5)]),
 ('p_tag',[('app','P',None),('dieu-khien','p_f',0),('micro-dien-thoai','p_f',1),('tiec-chia-se','p_f',2),('chieu-man-hinh','p_f',3)]),
 ('w_tag',[('bao-hanh','w_f',0),('cap-nhat','w_f',1),('rieng-tu','w_f',2)])]
IMG={'goi-bai':'loa-phong-khach','tong-vang-mic':'loa-ban-lam-viec','bao-hanh':'phu-kien','hang-cho':'home','cham-diem':'entertain','radio':'entertain','giai-tri':'entertain',
 'tro-ly-ai':'translate','dich-noi':'translate','lich-thoi-tiet':'home','the-duc':'fitness','app':'phone','dieu-khien':'phone','tiec-chia-se':'phone','phong-thu':'phone','san-hat':'phone'}
SPECIAL={'K':('🎤','k_h','k_p'),'A':('🤖','a_h','a_p'),'T':('🎨','t_h','t_p'),'P':('📲','p_h','p_p')}
def feat(c,key,idx):
    if key in SPECIAL:
        i,h,p=SPECIAL[key]; return i,c[h],e(c[p])
    return c[key][idx]
def url(l,p=''): return ('/' if l=='vi' else '/%s/'%l)+p
def head(l,c,title,desc,path,noidx=False):
    alts=''.join('<link rel="alternate" hreflang="%s" href="https://karaokeaihome.com%s">'%(x,url(x,path)) for x in LANGS)
    return f'''<!doctype html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:image" content="https://karaokeaihome.com/img/home.jpg">
{alts}{'<meta name="robots" content="noindex">' if noidx else ''}<link rel="icon" href="/favicon.svg"><link rel="stylesheet" href="/style.css"><style>{CSS}</style></head><body>
<nav><b><a href="{url(l)}" style="color:var(--fg)">Karaoke AI Home</a></b><a href="{url(l)}#tinh-nang">{e(UI[l]['all'])}</a><a href="{url(l,'download/')}">{e(P[l]['dl'])}</a><a href="{url(l)}#lien-he">{e(c['nav'][3])}</a><a href="{url(l,'support/')}">{e(c['nav'][4])}</a></nav>
<div class="lang">{''.join('<a href="%s" class="%s" lang="%s">%s</a>'%(url(x,path),'on' if x==l else '',x,NAMES[x]) for x in LANGS)}</div>'''
def foot(l,c):
    return f'''<footer>© 2026 Karaoke AI Home · info@karaokeaihome.com<br><a href="{url(l,'download/')}">{e(P[l]['dl'])}</a> · <a href="{url(l,'support/')}">{e(c['legal'][2])}</a></footer></body></html>'''
def contact(l,c):
    return f'''<section id="lien-he"><div class="contact"><h2 style="margin-top:0">{e(c['c_h'])}</h2><p class="lead" style="margin:0 auto 12px">{e(c['c_p'])}</p>
<a class="mail" href="mailto:info@karaokeaihome.com">info@karaokeaihome.com</a></div></section>'''
def tile(l,c,slug,key,idx):
    i,t,_=feat(c,key,idx)
    return '<a class="ic" href="%s"><span class="b">%s</span>%s</a>'%(url(l,'f/%s/'%slug),i,e(t))
def home(l):
    c=C[l]
    grid=''.join('<div class="grp">%s</div><div class="icons">%s</div>'%(e(c[g]),''.join(tile(l,c,*it) for it in items)) for g,items in GROUPS)
    return head(l,c,c['title'],c['desc'],'')+f'''
<header class="hero"><h1>{e(c['h1a'])} <span>{e(c['h1b'])}</span><br>{e(c['h1c'])}</h1><p>{e(c['hero'])}</p>
<div class="btns"><a class="btn" href="#lien-he">{e(c['cta1'])}</a><a class="btn o" href="#tinh-nang">{e(c['cta2'])}</a></div>
<div class="price"><div class="l">{e(PRICE_LABEL[l])}</div><div class="v">{e(PRICE[l])}</div><div class="n">{e(PRICE_NOTE[l])}</div></div></header>
<div class="wrap"><div class="gal"><img class="shot main" src="/img/loa-ban-lam-viec.jpg" alt="Karaoke AI Home"><img class="shot" src="/img/loa-phong-khach.jpg" alt="Karaoke AI Home" loading="lazy"><img class="shot" src="/img/phu-kien.jpg" alt="Karaoke AI Home" loading="lazy"></div>
<p class="tap" style="margin-top:28px">{e(c['alt_home'])}</p><img class="shot" src="{im(l,'home')}" alt="{e(c['alt_home'])}" loading="lazy"></div>
<main class="wrap"><section id="tinh-nang" style="border-top:0"><p class="tap">{e(UI[l]['tap'])}</p>{grid}</section>{contact(l,c)}</main>'''+foot(l,c)
def detail(l,slug,gkey,key,idx,others):
    c=C[l]; i,t,d=feat(c,key,idx)
    img=''
    if slug=='giao-dien':
        img='<div class="themes">'+''.join('<figure><img class="shot" src="%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>'%(im(l,f),e(x),e(x)) for f,x in zip(['theme-kids','theme-elder','theme-women','theme-tech'],c['themes']))+'</div>'
    elif slug in IMG: img='<img class="shot" src="%s" alt="%s" loading="lazy">'%(im(l,IMG[slug]),e(t))
    say=''
    if slug in ('goi-bai','tong-vang-mic'):
        say='<p class="mute" style="margin:14px 0 0;font-size:.9rem">%s</p><div class="say">%s</div>'%(e(c['say_label']),''.join('<span>%s</span>'%e(s) for s in SAY[l]))
    more='<div class="grp">%s</div><div class="icons">%s</div>'%(e(UI[l]['more']),''.join(tile(l,c,*o) for o in others if o[0]!=slug))
    return head(l,c,'%s – Karaoke AI Home'%t,t,'f/%s/'%slug)+f'''
<main class="detail"><a class="bk" href="{url(l)}#tinh-nang">{e(UI[l]['back'])}</a>
<div class="big">{i}</div><div class="tag" style="margin-top:14px">{e(c[gkey])}</div><h1>{e(t)}</h1><p class="d">{d}</p>{say}{img}
{more}
<div style="margin-top:32px">{contact(l,c)}</div></main>'''+foot(l,c)
def simple(l,path,title,body,noidx=False):
    c=C[l]; return head(l,c,'%s – Karaoke AI Home'%title,title,path,noidx)+'<main>'+body+'</main>'+foot(l,c)
def qr(data,fn):
    img=qrcode.make(data,image_factory=qrcode.image.svg.SvgPathImage,border=1)
    img.save(os.path.join(OUT,'img',fn))
def download(l):
    p=P[l]
    def card(h,btn,href,q,steps,note=''):
        return ('<div class="dlc"><h2>%s</h2><div class="qr"><img src="/img/%s" alt="QR %s"><div><a class="btn" href="%s">%s</a></div></div><ol>%s</ol>%s</div>'
                %(e(h),q,e(h),href,e(btn),''.join('<li>%s</li>'%x for x in steps),('<p class="note">%s</p>'%e(note)) if note else ''))
    b='<h1>%s</h1><p class="lead">%s</p><div class="dlg">%s%s</div>'%(e(p['dl_title']),e(p['dl_lead']),
        card(p['and_h'],p['and_btn'],APK,'qr-android.svg',p['and_steps']),card(p['ios_h'],p['ios_btn'],IOS,'qr-iphone.svg',p['ios_steps'],p['ios_note']))
    return simple(l,'download/',p['dl'],b)
def support(l):
    p=P[l]
    b='<h1>%s</h1><p>%s</p><div class="card"><p><b>Email:</b> <a href="mailto:info@karaokeaihome.com">info@karaokeaihome.com</a></p></div><h2>%s</h2>%s'%(
        e(p['sup']),e(p['sup_lead']),e(p['faq']),''.join('<p><b>%s</b> %s</p>'%(e(q),a.format(dl=url(l,'download/'))) for q,a in p['qa']))
    return simple(l,'support/',p['sup'],b)
def privacy(l):
    p=P[l]
    b='<h1>%s</h1><p class="mute">%s</p>%s'%(e(p['pv_title']),e(p['pv_eff']),''.join('<h2>%s</h2><p>%s</p>'%(e(h),e(t.format(legal=LEGAL))) for h,t in p['pv']))
    return simple(l,'privacy/',p['pv_title'],b,True)
def terms(l):
    p=P[l]; return simple(l,'terms/',p['tm_title'],'<h1>%s</h1><p>%s</p>'%(e(p['tm_title']),e(p['tm'].format(legal=LEGAL))),True)
os.makedirs(os.path.join(OUT,'img'),exist_ok=True)
qr(SITE+APK,'qr-android.svg'); qr(SITE+IOS,'qr-iphone.svg')
n=0
for l in LANGS:
    d=OUT if l=='vi' else os.path.join(OUT,l)
    os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(home(l)); n+=1
    for sub,fn in (('download',download),('support',support),('privacy',privacy),('terms',terms)):
        p=os.path.join(d,sub); os.makedirs(p,exist_ok=True)
        open(os.path.join(p,'index.html'),'w',encoding='utf-8').write(fn(l)); n+=1
    for g,items in GROUPS:
        for slug,key,idx in items:
            p=os.path.join(d,'f',slug); os.makedirs(p,exist_ok=True)
            open(os.path.join(p,'index.html'),'w',encoding='utf-8').write(detail(l,slug,g,key,idx,items)); n+=1
print('pages',n)

# sitemap (khong co privacy/terms), robots, 404, chuyen huong iPhone
urls=[]
for l in LANGS:
    urls.append(url(l)); urls+= [url(l,'download/'),url(l,'support/')]
    urls+=[url(l,'f/%s/'%slug) for g,items in GROUPS for slug,k,i in items]
open(os.path.join(OUT,'sitemap.xml'),'w',encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>%s%s</loc></url>\n'%(SITE,u) for u in urls)+'</urlset>\n')
open(os.path.join(OUT,'robots.txt'),'w').write('User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n'%SITE)  # privacy/terms: an bang meta noindex
nf=' · '.join('<a href="%s">%s</a>'%(url(l),e(P[l]['home'])) for l in LANGS)
open(os.path.join(OUT,'404.html'),'w',encoding='utf-8').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>404</title><link rel="stylesheet" href="/style.css"></head><body><main><h1>404</h1><p>%s</p><p>%s</p></main></body></html>'%(e(' / '.join(P[l]['nf'] for l in LANGS)),nf))
# /iphone/index.html (du phong) cung chuyen toi web app iPhone
# Noi chua APK moi nhat. Khi co kho GitHub Releases thi doi thanh https://github.com/<to-chuc>/<kho>/releases/latest/download/KaraokeAIHome.apk
APK_LATEST='https://raw.githubusercontent.com/karaokeaihome/app/main/KaraokeAIHome.apk'  # kho GitHub karaokeaihome/app: ban moi chi can day file len
os.makedirs(os.path.join(OUT,'tai','android'),exist_ok=True)
open(os.path.join(OUT,'tai','android','index.html'),'w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url=%s"><title>Karaoke AI Home</title></head><body><a href="%s">KaraokeAIHome.apk</a><script>location.replace("%s")</script></body></html>'%(APK_LATEST,APK_LATEST,APK_LATEST))
open(os.path.join(OUT,'_redirects'),'w').write('/iphone https://app.karaokeaihome.com/app/ 302\n/tai/android %s 302\n'%APK_LATEST)
print('pages',n,'sitemap',len(urls))
