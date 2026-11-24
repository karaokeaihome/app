# -*- coding: utf-8 -*-
# Website 6 ngon ngu: trang chu = luoi bieu tuong, moi tinh nang 1 trang rieng.
# Sua chu trong content.py roi chay: python3 build.py  -> ../website-cai-dat/public
import os, html, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import C, LANGS, NAMES, SAY, PRICE, PRICE_LABEL, PRICE_NOTE, UI
from pages import P, APK, IOS, SITE, LEGAL
from legal import L as LG, DEL_ID
from features import rich, CSS as RCSS
from account import T as AT, page as acc_page, CSS as ACSS, JS as AJS
from upgrade import U as UP, TRIAL, REMOTE
from warranty import T as WT, page as wty_page, CSS as WCSS, JS as WJS
from cailoa import T as CL, UI as CLUI, UPG, WIN, MAC, WIN_LATEST, MAC_LATEST
import qrcode, qrcode.image.svg
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'..','public') if os.path.isdir(os.path.join(HERE,'..','public')) else os.path.join(HERE,'..','website-cai-dat','public')  # repo GitHub: website/src -> website/public
e=html.escape
TAB={'vi': ('Mua & tải app', 'Mua loa và tải app'), 'en': ('Buy & app', 'Buy the speaker & get the app'), 'ja': ('購入・アプリ', 'スピーカー購入とアプリ'), 'ko': ('구매·앱', '스피커 구매 및 앱 받기'), 'fr': ('Achat & app', 'Acheter l’enceinte et l’app'), 'zh': ('购买与应用', '购买音箱与下载应用')}
# Hinh co chu: ban tieng Viet o /img/<ten>.jpg, ngon ngu khac o /img/<lang>/<ten>.jpg (tao bang mockups/render.py)
LOC={'home','entertain','phone','translate','fitness','theme-kids','theme-elder','theme-women','theme-tech'}
def im(l,n): return '/img/%s.jpg'%n if (l=='vi' or n not in LOC) else '/img/%s/%s.jpg'%(l,n)
CSS=open(os.path.join(HERE,'page.css'),encoding='utf-8').read()+"""
nav{position:relative}nav a.nb{padding:6px 12px;border-radius:999px;border:1px solid var(--acc);color:var(--acc)!important;font-weight:700;white-space:nowrap}.dls{max-width:820px;width:calc(100% - 32px);box-sizing:border-box;margin:22px auto 0;padding:18px;border-radius:18px;background:#141417;border:1px solid #2a2a30;text-align:center}.dls>b{display:block;font-size:1.15rem;margin-bottom:12px}.dlr{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}.dli{display:flex;flex-direction:column;align-items:center;gap:10px}.dli img{width:120px;height:120px;background:#fff;border-radius:10px;padding:6px}.dlm{display:inline-block;margin-top:12px;color:var(--acc)}@media(max-width:700px){.dli img{display:none}.dli,.dli .btn{width:100%}.dlr{flex-direction:column}}.star{display:flex;align-items:center;gap:16px;margin:0 0 22px;padding:18px 20px;border-radius:20px;background:linear-gradient(135deg,#5b1d7a,#a1185a);color:#fff;text-decoration:none;box-shadow:0 10px 30px #a1185a40}.star .si{font-size:3rem;line-height:1}.star b{display:block;font-size:1.35rem}.star small{display:block;opacity:.9;margin-top:4px;line-height:1.45}.star em{font-style:normal;font-size:2rem;opacity:.8}.upb{display:flex;align-items:center;gap:12px;max-width:820px;width:calc(100% - 32px);box-sizing:border-box;margin:18px auto 0;padding:14px 18px;border-radius:16px;background:linear-gradient(135deg,#3a2a08,#1c1a14);border:1px solid #6b4a1a;color:var(--fg);text-decoration:none}.upb span{font-size:1.8rem}.upb b{flex:1}.upb em{font-style:normal;color:var(--acc);font-weight:700;white-space:nowrap}h2.ust{display:flex;align-items:center;gap:10px}h2.ust .n{flex:none;width:34px;height:34px;border-radius:50%;background:var(--acc);color:#111;display:inline-flex;align-items:center;justify-content:center;font-size:1.1rem}nav .lg{position:relative}nav .lg summary{list-style:none;cursor:pointer;font-size:1.35rem;color:var(--fg);display:flex;line-height:1;padding:4px 6px;border-radius:999px;user-select:none}nav .lg summary::-webkit-details-marker{display:none}nav .lg[open] summary{background:#222}nav .lg>div{position:absolute;right:0;top:calc(100% + 8px);background:#17171a;border:1px solid #2a2a30;border-radius:14px;padding:6px;min-width:160px;z-index:50;box-shadow:0 10px 30px #0008}nav .lg>div a{display:block!important;padding:9px 12px;border-radius:10px;color:var(--fg);text-decoration:none;white-space:nowrap}nav .lg>div a:hover{background:#222}nav .lg>div a.on{color:var(--acc);font-weight:700}


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
.lgrow{margin:10px 0;padding:14px 16px}.lgrow dl{margin:6px 0 0;display:grid;grid-template-columns:auto 1fr;gap:4px 12px;font-size:.92rem}.lgrow dt{color:var(--mute)}.lgrow dd{margin:0}
.pcc{margin-top:18px}.pcc .btns{justify-content:flex-start;margin:6px 0 4px}.pcc ol{margin-top:12px}
.gs{display:grid;gap:14px;grid-template-columns:1fr;margin:14px 0}.gs figure{margin:0;background:var(--card);border:1px solid #2a2a30;border-radius:16px;padding:12px}
.gs figure img{width:100%;border-radius:10px;display:block;margin:0}.gs figcaption{margin-top:8px}.gs figcaption b{color:var(--acc)}.gs .n{color:var(--acc);font-weight:800;margin-right:6px}
@media(min-width:860px){.gs.two{grid-template-columns:1fr 1fr}}
"""+RCSS+ACSS+WCSS+"""
.gal{display:grid;gap:12px;grid-template-columns:1fr 1fr;max-width:760px;margin:24px auto 0}.gal .main{grid-column:1/3}.gal img{border-radius:16px}
"""
# (slug, group key, list key, index)  group headings reuse section tags
GROUPS=[('k_tag',[('san-hat','san',0),('goi-bai','K',None),('phong-thu','stu',0),('tong-vang-mic','k_f',0),('hang-cho','k_f',1),('cham-diem','k_f',2),('radio','k_f',3)]),
 ('a_tag',[('tro-ly-ai','A',None),('lich-thoi-tiet','a_f',0),('tin-hom-nay','a_f',1),('dich-noi','a_f',2)]),
 ('f_tag',[('be-hoc','f_f',0),('ong-ba','f_f',1),('chi-em','f_f',2),('anh-em','f_f',3),('the-duc','f_f',4),('giai-tri','f_f',5),('giao-dien','T',None)]),
 ('m_tag',[('bao-tien','m_f',0),('dam-thoai','m_f',1),('loi-nhac','m_f',2),('nha-thong-minh','m_f',3),('camera','m_f',4),('kho-ung-dung','m_f',5)]),
 ('p_tag',[('app','P',None),('dieu-khien','p_f',0),('micro-dien-thoai','p_f',1),('tiec-chia-se','p_f',2),('chieu-man-hinh','p_f',3)]),
 ('w_tag',[('bao-hanh','w_f',0),('cap-nhat','w_f',1),('rieng-tu','w_f',2)])]
IMG={'goi-bai':'loa-phong-khach','tong-vang-mic':'loa-ban-lam-viec','bao-hanh':'phu-kien','hang-cho':'home','cham-diem':'entertain','radio':'entertain','giai-tri':'entertain',
 'tro-ly-ai':'translate','dich-noi':'translate','lich-thoi-tiet':'home','the-duc':'fitness','app':'phone','dieu-khien':'phone','tiec-chia-se':'phone'}
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
<nav><b><a href="{url(l)}" style="color:var(--fg)">Karaoke AI Home</a></b><a href="{url(l)}#tinh-nang">{e(UI[l]['all'])}</a><a href="{url(l,'download/')}">{e(P[l]['dl'])}</a><a href="{url(l,'nang-cap/')}">{e(UP[l]['nav'])}</a><a href="{url(l,'mua/')}#lien-he">{e(c['nav'][3])}</a><a href="{url(l,'support/')}">{e(c['nav'][4])}</a><a href="{url(l,'bao-hanh/')}">{e(WT[l]['nav'])}</a><a class="nb" href="{url(l,'mua/')}">{e(TAB[l][0])}</a><details class="lg"><summary title="{e(NAMES[l])}" aria-label="Language"><svg class="ic-globe" viewBox="0 0 24 24" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" style="vertical-align:-.15em"><circle cx="12" cy="12" r="9.2"/><ellipse cx="12" cy="12" rx="4" ry="9.2"/><path d="M3 12h18M4.6 7.3h14.8M4.6 16.7h14.8"/></svg></summary><div>{''.join('<a href="%s" class="%s" lang="%s">%s</a>'%(url(x,path),'on' if x==l else '',x,NAMES[x]) for x in LANGS)}</div></details><a class="nl" href="{url(l,'account/')}">{e(AT[l]['nav'])}</a></nav><script>document.addEventListener('click',function(_e){{var d=document.querySelector('nav .lg');if(d&&d.open&&!d.contains(_e.target))d.open=false}});try{{if(localStorage.getItem('kah_acct')){{var _a=document.querySelector('nav a.nl');_a.textContent=localStorage.getItem('kah_nm')||{json.dumps(AT[l]['my'],ensure_ascii=False)}}}}}catch(_e){{}}</script>
'''
def foot(l,c):
    return f'''<footer>© 2026 Karaoke AI Home · info@karaokeaihome.com<br><a href="{url(l,'download/')}">{e(P[l]['dl'])}</a> · <a href="{url(l,'support/')}">{e(c['legal'][2])}</a> · <a href="{url(l,'bao-hanh/')}">{e(WT[l]['h'])}</a></footer></body></html>'''
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
<div class="price"><div class="l">{e(PRICE_LABEL[l])}</div><div class="v">{e(PRICE[l])}</div><div class="n">{e(PRICE_NOTE[l])}</div></div></header>
<div class="wrap"><div class="gal"><img class="shot main" src="/img/loa-ban-lam-viec.jpg" alt="Karaoke AI Home"><img class="shot" src="/img/loa-phong-khach.jpg" alt="Karaoke AI Home" loading="lazy"><img class="shot" src="/img/phu-kien.jpg" alt="Karaoke AI Home" loading="lazy"></div>
<p class="tap" style="margin-top:28px">{e(c['alt_home'])}</p><img class="shot" src="{im(l,'home')}" alt="{e(c['alt_home'])}" loading="lazy"></div>
<main class="wrap"><section id="tinh-nang" style="border-top:0"><a class="star" href="{url(l,'f/san-hat/')}"><span class="si">{c['san'][0][0]}</span><span><b>{e(c['san'][0][1])}</b><small>{e(c['san'][0][2])}</small></span><em>›</em></a><p class="tap">{e(UI[l]['tap'])}</p>{grid}</section></main>'''+foot(l,c)
def detail(l,slug,gkey,key,idx,others):
    c=C[l]; i,t,d=feat(c,key,idx)
    img=''
    if slug=='giao-dien':
        img='<div class="themes">'+''.join('<figure><img class="shot" src="%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>'%(im(l,f),e(x),e(x)) for f,x in zip(['theme-kids','theme-elder','theme-women','theme-tech'],c['themes']))+'</div>'
    elif slug in ('phong-thu','san-hat'): img=rich(l,slug)
    elif slug in IMG: img='<img class="shot" src="%s" alt="%s" loading="lazy">'%(im(l,IMG[slug]),e(t))
    say=''
    if slug in ('goi-bai','tong-vang-mic'):
        say='<p class="mute" style="margin:14px 0 0;font-size:.9rem">%s</p><div class="say">%s</div>'%(e(c['say_label']),''.join('<span>%s</span>'%e(s) for s in SAY[l]))
    if slug=='bao-hanh': say+='<p style="margin:18px 0 0"><a class="btn" href="%s">%s ›</a></p>'%(url(l,'bao-hanh/'),e(WT[l]['h']))
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
    p=P[l]; vr=REMOTE[l][2]
    va=open(os.path.join(HERE,'..','..','VERSION')).read().strip() if os.path.exists(os.path.join(HERE,'..','..','VERSION')) else ''
    vp=open(os.path.join(HERE,'..','..','cai-loa','VERSION')).read().strip() if os.path.exists(os.path.join(HERE,'..','..','cai-loa','VERSION')) else ''
    def card(h,btn,href,q,steps,note=''):
        return ('<div class="dlc"><h2>%s</h2><div class="qr"><img src="/img/%s" alt="QR %s"><div><a class="btn" href="%s">%s</a></div></div><ol>%s</ol>%s</div>'
                %(e(h),q,e(h),href,e(btn),''.join('<li>%s</li>'%x for x in steps),('<p class="note">%s</p>'%e(note)) if note else ''))
    b='<h1>%s</h1><p class="lead">%s</p><div class="card" style="border-color:#6b4a1a"><b>🎟️ %s</b><p style="margin:6px 0 0">%s</p></div><div class="dlg">%s%s</div>'%(e(p['dl_title']),e(p['dl_lead']),e(TRIAL[l][0]),e(TRIAL[l][1]),
        card(p['and_h'],p['and_btn'],APK,'qr-android.svg',p['and_steps'],('%s %s'%(vr,va)) if va else ''),card(p['ios_h'],p['ios_btn'],IOS,'qr-iphone.svg',p['ios_steps'],p['ios_note']))
    t=CL[l]
    b+=('<div class="dlc pcc" id="may-tinh"><h2>%s</h2><p>%s</p><div class="btns"><a class="btn" href="%s">%s</a><a class="btn" href="%s">%s</a></div>'
        '<ol>%s</ol><p class="note">'+e(('%s %s'%(vr,vp)) if vp else '')+'</p><p><a href="%s">%s →</a></p></div>')%(e(t['card_h']),e(t['card_p']),WIN,e(t['win']),MAC,e(t['mac']),
        ''.join('<li>%s</li>'%x for x in t['card_steps']),url(l,'cai-loa/'),e(t['guide']))
    return simple(l,'download/',p['dl'],b)
def cailoa_page(l):
    t=CL[l]; u=CLUI[l]; im=lambda n:'/img/cai-loa/%s/%s.jpg'%(l,n)
    b='<h1>%s</h1><p class="lead">%s</p><p class="note">%s</p>'%(e(t['g_title']),e(t['g_lead']),e(t['need']))
    b+='<div class="btns" style="justify-content:flex-start"><a class="btn" href="%s">%s</a><a class="btn" href="%s">%s</a></div>'%(WIN,e(t['win']),MAC,e(t['mac']))
    uh,ul=UPG[l]; b+='<h2 id="nang-cap">🚀 %s</h2><ul>%s</ul>'%(e(uh),''.join('<li>%s</li>'%x for x in ul))
    b+='<h2>%s</h2><div class="dlg"><div class="dlc"><h2>%s</h2><ol>%s</ol></div><div class="dlc"><h2>%s</h2><ol>%s</ol></div></div>'%(e(t['h1']),
        e(t['win_h']),''.join('<li>%s</li>'%x for x in t['win_s']),e(t['mac_h']),''.join('<li>%s</li>'%x for x in t['mac_s']))
    b+='<h2>%s</h2><p>%s</p><div class="gs two">%s</div>'%(e(t['h2']),e(t['h2_p']),''.join(
        '<figure><img src="%s" alt="%s" loading="lazy" width="800" height="420"><figcaption><span class="n">%d</span>%s</figcaption></figure>'%(im('g%d'%n),e(t['alt_g'].format(n=n)),n,u['g'][n-1]) for n in range(1,6)))
    b+='<h2>%s</h2><div class="gs">%s</div>'%(e(t['h3']),''.join(
        '<figure><img src="%s" alt="%s" loading="lazy" width="1000"><figcaption><span class="n">%d</span>%s</figcaption></figure>'%(im('app-'+k),e(t['alt_app']),i+1,t['s3'][i]) for i,k in enumerate(['found','busy','done'])))
    b+='<h2>%s</h2><p>%s</p>'%(e(t['ci_h']),t['ci_p'])
    b+='<h2>%s</h2><p>%s</p>'%(e(t['h4']),t['p4'])
    b+='<h2>%s</h2><ol>%s</ol>'%(e(t['h5']),''.join('<li>%s</li>'%e(x) for x in u['none_tips']))
    b+='<h2>%s</h2><ul>%s</ul>'%(e(t['h6']),''.join('<li>%s</li>'%x for x in t['p6']))
    return simple(l,'cai-loa/',t['g_title'],b)
def support(l):
    p=P[l]; g=LG[l]; qa=list(p['qa'][:-1])+[g['del_q']]
    b='<h1>%s</h1><p>%s</p><div class="card"><p><b>Email:</b> <a href="mailto:info@karaokeaihome.com">info@karaokeaihome.com</a></p></div><h2>%s</h2>%s'%(
        e(p['sup']),e(p['sup_lead']),e(p['faq']),''.join('<p><b>%s</b> %s</p>'%(e(q),a.format(dl=url(l,'download/'))) for q,a in qa))
    uh,ul=UPG[l]; b+='<h2>🚀 %s</h2><ul>%s</ul>'%(e(uh),''.join('<li>%s</li>'%x for x in ul))
    b+='<h2 id="%s">%s</h2><ul>%s</ul>'%(DEL_ID,e(g['del_h']),''.join('<li>%s</li>'%e(x) for x in g['del_b']))
    return simple(l,'support/',p['sup'],b)
def blocks(l,secs):
    g=LG[l]; out=''
    for h,items in secs:
        out+='<h2>%s</h2>'%e(h)
        for it in items:
            if isinstance(it,tuple) and it[0]=='rows':
                out+=''.join('<div class="card lgrow"><b>%s</b><dl><dt>%s</dt><dd>%s</dd><dt>%s</dt><dd>%s</dd><dt>%s</dt><dd>%s</dd></dl></div>'%(
                    e(r[0]),e(g['cols'][0]),e(r[1]),e(g['cols'][1]),e(r[2]),e(g['cols'][2]),e(r[3])) for r in it[1])
            elif isinstance(it,list): out+='<ul>%s</ul>'%''.join('<li>%s</li>'%x.format(legal=e(LEGAL)) for x in it)
            else: out+='<p>%s</p>'%it.format(legal=e(LEGAL))
    return out
def account(l):
    return simple(l,'account/',AT[l]['h'],acc_page(l,e),True)
def warranty(l):
    return simple(l,'bao-hanh/',WT[l]['h'],wty_page(l,e))
def upgrade(l):
    t=UP[l]; cl=CL[l]; u=CLUI[l]; im=lambda n:'/img/cai-loa/%s/%s.jpg'%(l,n)
    ol=lambda xs:'<ol>%s</ol>'%''.join('<li>%s</li>'%x for x in xs)
    st=lambda n,h:'<h2 class="ust"><span class="n">%d</span>%s</h2>'%(n,e(h))
    b='<h1>🚀 %s</h1><p class="lead">%s</p><p class="note">%s</p><div class="card" style="border-color:#6b4a1a"><b>%s</b></div>'%(e(t['h1']),e(t['lead']),e(t['need']),e(t['ios']))
    b+=st(1,t['s1h'])+ol(t['s1'])
    b+=st(2,t['s2h'])+'<p>%s</p><div class="gs two">%s</div>'%(e(t['s2p']),''.join('<figure><img src="%s" alt="%s" loading="lazy" width="800" height="420"><figcaption><span class="n">%d</span>%s</figcaption></figure>'%(im('g%d'%n),e(t['alt'].format(n=n)),n,u['g'][n-1]) for n in range(1,6)))
    b+=st(3,t['s3h'])+'<div class="dlg"><div class="dlc"><h2>%s</h2>%s<p><a class="btn" href="%s">%s</a></p></div><div class="dlc"><h2>%s</h2>%s<p class="btns" style="justify-content:flex-start"><a class="btn" href="%s">%s</a><a class="btn" href="%s">%s</a></p><p><a href="%s">%s ›</a></p></div></div>'%(
        e(t['a_h']),ol(t['a']),url(l,'download/'),e(t['a_btn']),e(t['b_h']),ol(t['b']),WIN,e(cl['win']),MAC,e(cl['mac']),url(l,'cai-loa/'),e(t['b_more']))
    b+='<div class="gs">%s</div>'%''.join('<figure><img src="%s" alt="%s" loading="lazy" width="1000"><figcaption>%s</figcaption></figure>'%(im('app-'+k),e(cl['alt_app']),cl['s3'][i]) for i,k in enumerate(['found','busy','done']))
    rh,rs,_=REMOTE[l]; b+='<div class="dlc" id="tu-xa" style="margin-top:18px;border-color:#6b4a1a"><h2>🛟 %s</h2>%s<p class="btns" style="justify-content:flex-start"><a class="btn" href="%s">%s</a><a class="btn" href="%s">%s</a></p></div>'%(e(rh),ol(rs),WIN,e(cl['win']),MAC,e(cl['mac']))
    b+=st(4,t['s4h'])+'<p>%s</p>'%e(t['s4'])
    b+=st(5,t['s5h'])+ol(t['s5'])+'<p class="note">%s</p>'%e(t['help'])
    return simple(l,'nang-cap/',t['h1'],b)
def buy(l):
    c=C[l]
    return head(l,c,'%s – Karaoke AI Home'%TAB[l][1],TAB[l][1],'mua/')+f'''<main class="wrap"><h1 style="text-align:center">{e(TAB[l][1])}</h1><div class="dls"><b>{e(P[l]['dl_title'])}</b><div class="dlr"><div class="dli"><img src="/img/qr-android.svg" alt="QR Android"><a class="btn" href="{APK}">{e(P[l]['and_btn'])}</a></div><div class="dli"><img src="/img/qr-iphone.svg" alt="QR iPhone"><a class="btn o" href="{IOS}">{e(P[l]['ios_btn'])}</a></div></div><a class="dlm" href="{url(l,'download/')}">{e(P[l]['dl'])} ›</a></div>
<a class="upb" href="{url(l,'nang-cap/')}"><span>🚀</span><b>{e(UP[l]['banner'])}</b><em>{e(UP[l]['banner_btn'])} ›</em></a>
{contact(l,c)}</main>'''+foot(l,c)
def privacy(l):
    p=P[l]
    b='<h1>%s</h1><p class="mute">%s</p>%s'%(e(p['pv_title']),e(p['pv_eff']),blocks(l,LG[l]['pv']))
    return simple(l,'privacy/',p['pv_title'],b,True)
def terms(l):
    p=P[l]
    b='<h1>%s</h1><p class="mute">%s</p>%s'%(e(p['tm_title']),e(p['pv_eff']),blocks(l,LG[l]['tm']))
    return simple(l,'terms/',p['tm_title'],b,True)
os.makedirs(os.path.join(OUT,'img'),exist_ok=True)
qr(SITE+APK,'qr-android.svg'); qr(SITE+IOS,'qr-iphone.svg')
n=0
for l in LANGS:
    d=OUT if l=='vi' else os.path.join(OUT,l)
    os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(home(l)); n+=1
    for sub,fn in (('download',download),('support',support),('privacy',privacy),('terms',terms),('cai-loa',cailoa_page),('account',account),('nang-cap',upgrade),('mua',buy),('bao-hanh',warranty)):
        p=os.path.join(d,sub); os.makedirs(p,exist_ok=True)
        open(os.path.join(p,'index.html'),'w',encoding='utf-8').write(fn(l)); n+=1
    for g,items in GROUPS:
        for slug,key,idx in items:
            p=os.path.join(d,'f',slug); os.makedirs(p,exist_ok=True)
            open(os.path.join(p,'index.html'),'w',encoding='utf-8').write(detail(l,slug,g,key,idx,items)); n+=1
print('pages',n)
open(os.path.join(OUT,'account.js'),'w',encoding='utf-8').write(AJS)
open(os.path.join(OUT,'bao-hanh.js'),'w',encoding='utf-8').write(WJS)

# sitemap (khong co privacy/terms), robots, 404, chuyen huong iPhone
urls=[]
for l in LANGS:
    urls.append(url(l)); urls+= [url(l,'mua/'),url(l,'download/'),url(l,'nang-cap/'),url(l,'cai-loa/'),url(l,'support/'),url(l,'bao-hanh/')]
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
for k,v in (('windows',WIN_LATEST),('mac',MAC_LATEST)):  # phan mem cai loa cho may tinh: ban moi nhat trong repo app/cai-loa/
    os.makedirs(os.path.join(OUT,'tai',k),exist_ok=True)
    open(os.path.join(OUT,'tai',k,'index.html'),'w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url=%s"><title>Karaoke AI Home</title></head><body><a href="%s">%s</a><script>location.replace("%s")</script></body></html>'%(v,v,v.rsplit('/',1)[1],v))
open(os.path.join(OUT,'_redirects'),'w').write('/iphone https://app.karaokeaihome.com/app/ 302\n/tai/android %s 302\n%s %s 302\n%s %s 302\n'%(APK_LATEST,WIN,WIN_LATEST,MAC,MAC_LATEST))
print('pages',n,'sitemap',len(urls))
