# Dich chu tren anh chup man hinh loa: xoa chu cu (inpaint) roi ve chu moi cung co chu, cung vi tri.
import cv2, numpy as np, sys, os
from PIL import Image, ImageDraw, ImageFont
F = {
 'sans': '/usr/share/fonts/truetype/inter/Inter-Regular.ttf',
}
def find(pat):
    import subprocess
    return subprocess.check_output(['fc-match','-f','%{file}',pat]).decode()
INTER = find('Inter:style=Regular'); INTER_B = find('Inter:style=SemiBold'); INTER_M=find('Inter:style=Medium'); INTER_BI=find('Inter:style=SemiBold Italic')
SERIF = find('Liberation Serif')
CJK = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
CJK_B = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
CJKS = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc'
IDX = {'ja':0,'ko':1,'zh':2}
def font(kind, size, lang):
    size=max(6,int(round(size)))
    if lang in IDX:
        p={'sans':CJK,'bold':CJK_B,'med':CJK,'serif':CJKS,'bi':CJK_B}[kind]
        return ImageFont.truetype(p,size,index=IDX[lang])
    return ImageFont.truetype({'sans':INTER,'bold':INTER_B,'med':INTER_M,'serif':SERIF,'bi':INTER_BI}[kind],size)

def tw(txt,f,sp=0):
    if not sp: return f.getlength(txt)
    return sum(f.getlength(ch) for ch in txt)+sp*(len(txt)-1)
def draw_text(d,x,y,txt,f,fill,sp=0):
    if not sp: d.text((x,y),txt,font=f,fill=fill,anchor='ls'); return
    for ch in txt:
        d.text((x,y),ch,font=f,fill=fill,anchor='ls'); x+=f.getlength(ch)+sp

class Img:
    def __init__(s,path): s.cv=cv2.imread(path); s.ops=[]
    def measure(s,box,thr=45,bright=True):
        x0,y0,x1,y1=box; g=cv2.cvtColor(s.cv,cv2.COLOR_BGR2GRAY).astype(int)[y0:y1,x0:x1]
        bg=np.median(g); m=(g-bg>thr) if bright else (np.abs(g-bg)>thr)
        ys,xs=np.where(m)
        if len(xs)==0: return None
        col=s.cv[y0:y1,x0:x1][m]; lum=col.sum(axis=1); top=col[lum>=np.percentile(lum,70)]
        c=tuple(int(v) for v in np.median(top,axis=0)[::-1])
        return (x0+xs.min(),y0+ys.min(),x0+xs.max()+1,y0+ys.max()+1,c)
    def erase(s,box,pad=6,thr=14):
        x0,y0,x1,y1=box; x0-=pad;y0-=pad;x1+=pad;y1+=pad
        g=cv2.cvtColor(s.cv,cv2.COLOR_BGR2GRAY).astype(int)
        sub=g[y0:y1,x0:x1]; bg=np.median(sub)
        m=np.zeros(g.shape,np.uint8); m[y0:y1,x0:x1]=(np.abs(sub-bg)>thr).astype(np.uint8)*255
        m=cv2.dilate(m,np.ones((5,5),np.uint8))
        s.cv=cv2.inpaint(s.cv,m,6,cv2.INPAINT_TELEA)

def fit_size(orig,kind,width,sp=0,lang='vi'):
    lo,hi=5.0,120.0
    for _ in range(30):
        mid=(lo+hi)/2
        if tw(orig,font(kind,mid,'vi'),sp)<width: lo=mid
        else: hi=mid
    return lo

def replace(img,d_ops,box,orig,new,lang,kind='sans',align='left',caps_sp=False,maxw=None,lines=1,lh=None,thr=45,color=None,center=None,fixsize=None,fixbase=None,pad=6):
    """box: vung chua chu goc. orig: chu goc (tieng Viet) de do co chu. new: chu moi."""
    m=img.measure(box,thr)
    if not m: print('!! no text',orig); return
    x0,y0,x1,y1,c=m; c=color or c
    first=orig.split('\n')[0]
    if caps_sp:
        lo,hi=5.0,80.0
        for _ in range(30):
            mid=(lo+hi)/2; b=font(kind,mid,'vi').getbbox(first,anchor='ls')
            if b[3]-b[1]<y1-y0: lo=mid
            else: hi=mid
        size=lo; f=font(kind,size,'vi'); n=len(first)
        sp=min(max(0,((x1-x0)-tw(first,f))/(n-1)),0.45*size)
    else:
        sp=0; size=fit_size(first,kind,x1-x0,0)
    if fixsize: size=fixsize
    fv=font(kind,size,'vi')
    # baseline: dong goc ve o (0,0) anchor ls -> bbox top
    bb=fv.getbbox(first,anchor='ls')
    base=y0-bb[1]
    if orig.startswith('“') or orig.startswith('"'): pass
    img.ops.append((x0,y0,x1,y1,pad))
    if fixbase: base=fixbase
    fn=font(kind,size*(0.92 if lang in IDX else 1.0),lang)
    spn=sp if lang not in IDX else max(sp*0.5,1) if sp else 0
    mw=maxw or (x1-x0)
    # chia dong
    def wrap(f):
        if lines==1: return [new]
        words=new.split(' ') if lang not in ('ja','zh') else list(new)
        out=['']
        for w in words:
            t=(out[-1]+(' ' if out[-1] and lang not in ('ja','zh') else '')+w)
            if tw(t,f,spn)<=mw or not out[-1]: out[-1]=t
            else: out.append(w)
        return out
    k=1.0
    while True:
        f=font(kind,size*(0.92 if lang in IDX else 1.0)*k,lang); L=wrap(f)
        if len(L)<=lines and max(tw(t,f,spn) for t in L)<=mw+1: break
        k-=0.03
        if k<0.5: break
    d_ops.append((L,f,spn,x0,base,c,align,center,lh))

def render(img,ops,out):
    for b in img.ops: img.erase(b[:4],*(b[4:5] or [6]))
    pil=Image.fromarray(cv2.cvtColor(img.cv,cv2.COLOR_BGR2RGB)); d=ImageDraw.Draw(pil)
    for L,f,sp,x0,base,c,align,center,lh in ops:
        for i,t in enumerate(L):
            w=tw(t,f,sp); x=x0 if align=='left' else center-w/2
            draw_text(d,x,base+i*(lh or 0),t,f,c,sp)
    os.makedirs(os.path.dirname(out),exist_ok=True)
    pil.save(out,quality=88)

def tile_size(img,box,orig,kind):
    m=img.measure(box,45)
    return fit_size(orig,kind,m[2]-m[0]) if m else None

def base_of(img,box,orig,kind,size):
    m=img.measure(box,45)
    if not m: return None
    return m[1]-font(kind,size,'vi').getbbox(orig,anchor='ls')[1]
