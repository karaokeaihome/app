import sys; sys.path.insert(0,'.')
from tv import *
SRC='src/'
T={
'en':dict(date="Sunday, November 22, 2026",city="HANOI",wx1="Cloudy, chance of light rain",wx2="Low 19° · High 26° · Hum. 78%",calh="NOVEMBER · SUNDAY",
  lun1="Lunar · Year of the Horse",lun2="Ox day · Auspicious day",remh="TODAY’S REMINDER",
  quote="“An Ox day in harmony with the Rat sign. All goes well: a good day to start something new.”",own="Host born in the Year of the Horse",
  tiles=["Karaoke","YouTube","Lambo AI","Payment alerts","Entertainment","Kids","Women","Horoscope","News","Settings"],hint="Hold the Mic button on the remote to talk to Lambo"),
'ja':dict(date="2026年11月22日 日曜日",city="ハノイ",wx1="くもり、ところにより小雨",wx2="最低19° · 最高26° · 湿度78%",calh="11月 · 日曜日",
  lun1="旧暦 · 丙午年",lun2="乙丑の日 · 吉日",remh="今日のひとこと",
  quote="「丑の日は子年生まれと好相性。物事が順調に進みます。新しいことを始めましょう。」",own="世帯主：午年生まれ",
  tiles=["カラオケ","YouTube","Lambo AI","入金通知","エンタメ","キッズ","女性","占い","ニュース","設定"],hint="リモコンのマイクボタンを長押しして Lambo を呼び出し"),
'ko':dict(date="2026년 11월 22일 일요일",city="하노이",wx1="흐림, 약한 비 가능성",wx2="최저 19° · 최고 26° · 습도 78%",calh="11월 · 일요일",
  lun1="음력 · 병오년",lun2="을축일 · 길일",remh="오늘의 한마디",
  quote="“축일은 쥐띠와 잘 맞는 날. 모든 일이 순조로우니 새로운 일을 시작해 보세요.”",own="세대주: 말띠",
  tiles=["노래방","YouTube","Lambo AI","입금 알림","엔터테인먼트","어린이","여성","운세","뉴스","설정"],hint="리모컨의 마이크 버튼을 길게 눌러 Lambo 호출"),
'fr':dict(date="Dimanche 22 novembre 2026",city="HANOÏ",wx1="Nuageux, petite pluie possible",wx2="Min 19° · Max 26° · Hum. 78 %",calh="NOVEMBRE · DIMANCHE",
  lun1="Lunaire · Année du Cheval",lun2="Jour du Buffle · Jour faste",remh="LE RAPPEL DU JOUR",
  quote="« Jour du Buffle en harmonie avec le Rat. Tout va bien : osez commencer quelque chose de nouveau. »",own="Hôte né l’année du Cheval",
  tiles=["Karaoké","YouTube","Lambo IA","Alertes paiement","Divertissement","Enfants","Femmes","Horoscope","Actualités","Réglages"],hint="Maintenez le bouton Micro de la télécommande pour parler à Lambo"),
'zh':dict(date="2026年11月22日 星期日",city="河内",wx1="多云，可能有小雨",wx2="最低19° · 最高26° · 湿度78%",calh="11月 · 星期日",
  lun1="农历 · 丙午年",lun2="乙丑日 · 黄道吉日",remh="今日提醒",
  quote="“丑日与属鼠相合，诸事顺利，大胆开始新的事情吧。”",own="户主：属马",
  tiles=["卡拉OK","YouTube","Lambo AI","到账播报","娱乐","儿童","女性","运势","今日资讯","设置"],hint="长按遥控器上的麦克风键呼叫 Lambo"),
'vi':dict(tiles={2:"Trợ lý Lambo"},hint="Giữ nút Mic trên điều khiển để gọi Lambo"),
}
VI=dict(date="Chủ Nhật, 22 tháng 11, 2026",city="HÀ NỘI",wx1="Nhiều mây, có thể mưa nhẹ",wx2="Thấp 19° · Cao 26° · Ẩm 78%",calh="THÁNG 11 · CHỦ NHẬT",
  lun1="Âm lịch · Bính Ngọ",lun2="Ngày Ất Sửu · Hoàng đạo",remh="LỜI NHẮC HÔM NAY",quote="“Ngày Sửu lục hợp với tuổi Tý, mọi việc",own="Gia chủ tuổi Canh Ngọ",
  tiles=["Hát Karaoke","YouTube","Trợ lý AI","Loa báo tiền","Giải trí","Bé học","Chị em","Tử vi","Tin hôm nay","Cài đặt"],hint="Giữ nút Mic trên điều khiển để gọi Trợ lý AI")
CX=[127,255,382,509,636,763,890,1017,1145,1272]
def one(name,lang,out):
    img=Img(SRC+name+'.jpg'); ops=[]; t=T[lang]
    big = name=='theme-elder'
    def R(key,box,**kw):
        if key in t: replace(img,ops,box,VI[key],t[key],lang,**kw)
    R('date',(60,118,760,152),maxw=700)
    R('city',(220,198,456,219) if big else (220,200,470,224),caps_sp=True,maxw=230)
    R('wx1',(220,297,466,321),maxw=235)
    R('wx2',(220,324,486,350) if big else (220,324,466,348),maxw=235)
    R('calh',(508,197,790,221),caps_sp=True,maxw=272)
    R('lun1',(577,330,800,354) if big else (568,333,786,354),maxw=205,pad=2)
    R('lun2',(577,355,800,380) if big else (568,356,786,378),maxw=205,pad=2)
    R('remh',(834,196,1300,220),caps_sp=True,maxw=440)
    if 'quote' in t:
        m=img.measure((834,266,1320,300));
        if m: img.ops.append(m[:4])
        replace(img,ops,(834,230,1320,264),VI['quote'],t['quote'],lang,kind='serif',lines=2,maxw=455,lh=37 if not big else 38)
    R('own',(834,356,1150,378),maxw=300)
    if 'tiles' in t:
        import statistics
        sz=[tile_size(img,(CX[i]-63,532,CX[i]+63,562),VI['tiles'][i],'sans') for i in range(1,10) if i!=1]
        ts=statistics.median([x for x in sz if x])
        bs=[base_of(img,(CX[i]-63,532,CX[i]+63,562),VI['tiles'][i],'sans',ts) for i in range(1,10) if i!=1]
        tb=statistics.median([x for x in bs if x])
        tl=t['tiles']; it=tl.items() if isinstance(tl,dict) else enumerate(tl)
        for i,lab in it:
            if VI['tiles'][i]=='YouTube': continue
            replace(img,ops,(CX[i]-63,532,CX[i]+63,562),VI['tiles'][i],lab,lang,kind='bold' if i==0 else 'sans',align='center',center=CX[i],maxw=122,fixsize=ts,fixbase=tb)
    R('hint',(60,668,520,692),maxw=800,fixsize=None if big else 13.2)
    render(img,ops,out)
if __name__=='__main__':
    import sys
    for name in sys.argv[2].split(','):
        for lang in sys.argv[1].split(','):
            out=('out/vi/%s.jpg'%name) if lang=='vi' else 'out/%s/%s.jpg'%(lang,name)
            one(name,lang,out); print(out)
