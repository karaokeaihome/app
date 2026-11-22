import sys; sys.path.insert(0,'../mk')
from PIL import Image, ImageDraw
from tv import font
CAP={'vi':["Trang chủ","Điều khiển loa","Bài hát","Trợ lý Lambo","Tiện ích"],
'en':["Home","Speaker control","Songs","Lambo assistant","Tools"],
'ja':["ホーム","スピーカー操作","曲","Lamboアシスタント","ツール"],
'ko':["홈","스피커 제어","노래","Lambo 비서","도구"],
'fr':["Accueil","Contrôle de l’enceinte","Chansons","Assistant Lambo","Outils"],
'zh':["首页","音箱控制","歌曲","Lambo 助手","工具"]}
BG=(12,12,14)
def phone(l,n,w):
    im=Image.open('shots/%s-%s.png'%(l,n)).convert('RGB'); h=int(im.height*w/im.width); im=im.resize((w,h),Image.LANCZOS)
    fr=Image.new('RGB',(w+12,h+12),(40,40,44)); m=Image.new('L',fr.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,fr.width-1,fr.height-1),radius=int(w*0.09),fill=255)
    fr.paste(im,(6,6)); out=Image.new('RGB',fr.size,BG); out.paste(fr,(0,0),m)
    m2=Image.new('L',im.size,0); ImageDraw.Draw(m2).rounded_rectangle((0,0,w-1,h-1),radius=int(w*0.08),fill=255); out.paste(im,(6,6),m2)
    return out
def row(l,names,w,gap,width,caps=None,top=30):
    ps=[phone(l,n,w) for n in names]; pw=ps[0].width; ph=ps[0].height
    H=top+ph+(70 if caps else 30); W=Image.new('RGB',(width,H),BG); d=ImageDraw.Draw(W)
    x=(width-(len(ps)*pw+(len(ps)-1)*gap))//2
    for i,p in enumerate(ps):
        W.paste(p,(x,top))
        if caps:
            f=font('sans',22,l); t=caps[i]; d.text((x+pw/2,top+ph+38),t,font=f,fill=(205,200,190),anchor='mm')
        x+=pw+gap
    return W
import os
for l in CAP:
    os.makedirs('out/%s'%l,exist_ok=True)
    row(l,['home','remote','songs','ai','more'],250,24,1400,CAP[l]).save('out/%s/phone.jpg'%l,quality=86)
    row(l,['dich','ai'],560,60,1400).save('out/%s/translate.jpg'%l,quality=86)
    row(l,['fit1','fit2','fit3'],390,40,1400).save('out/%s/fitness.jpg'%l,quality=86)
print('ok')
