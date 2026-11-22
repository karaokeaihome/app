import sys; sys.path.insert(0,'.')
from tv import *
SRC='src/entertain.jpg'
VI=dict(hdr="GIẢI TRÍ",cards=[("Âm thanh ru ngủ","mưa, sóng, quạt, ru bé"),("Tin hôm nay","xổ số, giá vàng, tỷ giá"),("Bảng xếp hạng","vua karaoke tuần này"),("Radio","VOV, nhạc thư giãn"),("Cờ caro","chơi với máy"),("2048","trượt và gộp số"),("Sudoku","rèn trí nhớ"),("Đố vui","10 câu mỗi lượt")],
 tip='Mẹo: nói với Trợ lý AI "đố vui", "chơi Ai là triệu phú", "kể chuyện cổ tích" để chơi bằng giọng nói.')
T={
'vi':dict(cards=[None,(None,"giá vàng, tỷ giá, tin tức")]+[None]*6,tip='Mẹo: nói với Lambo "đố vui", "chơi Ai là triệu phú", "kể chuyện cổ tích" để chơi bằng giọng nói.'),
'en':dict(hdr="ENTERTAINMENT",cards=[("Sleep sounds","rain, waves, fan, lullabies"),("Today’s news","gold, exchange rates, news"),("Leaderboard","this week’s karaoke king"),("Radio","live radio, relaxing music"),("Gomoku","play against the computer"),("2048","slide and merge"),("Sudoku","train your memory"),("Quiz","10 questions per round")],
  tip='Tip: say “quiz”, “millionaire game” or “tell me a fairy tale” to Lambo to play by voice.'),
'ja':dict(hdr="エンタメ",cards=[("睡眠サウンド","雨・波・扇風機・子守歌"),("今日のニュース","金価格・為替・ニュース"),("ランキング","今週のカラオケ王"),("ラジオ","ラジオ・リラックス音楽"),("五目並べ","コンピューターと対戦"),("2048","スライドして合体"),("数独","記憶力トレーニング"),("クイズ","1回10問")],
  tip='ヒント：Lamboに「クイズ」「ミリオネア」「昔話して」と話しかけると音声で遊べます。'),
'ko':dict(hdr="엔터테인먼트",cards=[("수면 사운드","빗소리, 파도, 선풍기, 자장가"),("오늘의 뉴스","금 시세, 환율, 뉴스"),("랭킹","이번 주 노래왕"),("라디오","라디오, 힐링 음악"),("오목","컴퓨터와 대결"),("2048","밀어서 숫자 합치기"),("스도쿠","기억력 훈련"),("퀴즈","한 판에 10문제")],
  tip='팁: Lambo에게 “퀴즈”, “백만장자 게임”, “옛날이야기 해 줘”라고 말하면 음성으로 즐길 수 있어요.'),
'fr':dict(hdr="DIVERTISSEMENT",cards=[("Sons pour dormir","pluie, vagues, ventilateur"),("Infos du jour","or, taux de change, actualités"),("Classement","le roi du karaoké de la semaine"),("Radio","radio, musique relaxante"),("Morpion","contre l’ordinateur"),("2048","glisser et fusionner"),("Sudoku","entraîner sa mémoire"),("Quiz","10 questions par partie")],
  tip='Astuce : dites « quiz », « jeu du millionnaire » ou « raconte un conte » à Lambo pour jouer à la voix.'),
'zh':dict(hdr="娱乐",cards=[("助眠声音","雨声、海浪、风扇、摇篮曲"),("今日资讯","金价、汇率、新闻"),("排行榜","本周K歌之王"),("电台","电台、放松音乐"),("五子棋","与电脑对战"),("2048","滑动合并数字"),("数独","锻炼记忆力"),("问答","每轮10题")],
  tip='提示：对Lambo说“问答”“百万富翁”或“讲个童话”，即可用语音来玩。'),
}
CX=[213,538,862,1186]
def one(lang,out):
    img=Img(SRC); ops=[]; t=T[lang]
    if 'hdr' in t: replace(img,ops,(48,30,400,66),VI['hdr'],t['hdr'],lang,kind='bi',maxw=600,thr=40)
    TS=tile_size(img,(862-95,150,862+120,184),"Bảng xếp hạng",'bold'); SS=tile_size(img,(862-95,186,862+120,208),"vua karaoke tuần này",'sans')
    TB=[base_of(img,(862-95,150+r,862+120,184+r),"Bảng xếp hạng",'bold',TS) for r in (0,180)]
    SB=[base_of(img,(862-95,186+r,862+120,208+r),"vua karaoke tuần này",'sans',SS) for r in (0,180)]
    for i,c in enumerate(t['cards']):
        if not c: continue
        cx=CX[i%4]; ry=0 if i<4 else 180
        tt,st=c
        if tt and tt!=VI['cards'][i][0]:
            replace(img,ops,(cx-95,150+ry,cx+120,184+ry),VI['cards'][i][0],tt,lang,kind='bold',align='center',center=cx+3,maxw=250,fixsize=TS,fixbase=TB[i//4])
        if st:
            replace(img,ops,(cx-95,186+ry,cx+120,208+ry),VI['cards'][i][1],st,lang,align='center',center=cx+3,maxw=250,fixsize=SS,fixbase=SB[i//4])
    replace(img,ops,(44,452,1360,478),VI['tip'],t['tip'],lang,maxw=1290)
    render(img,ops,out)
for lang in sys.argv[1].split(','):
    out='out/%s/entertain.jpg'%lang; one(lang,out); print(out)
