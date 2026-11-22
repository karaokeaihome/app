import json
K=json.load(open('keys.json'))
COMMON={'🎫':'📻'}
L={}
L['vi']={'Trợ lý AI':'Lambo','Xổ số':'Radio','PH:Hỏi trợ lý…':'Hỏi Lambo…'}
L['en']=["Living room speaker","192.168.1.25 · connected","Good morning","Sunday, Nov 22 · Lunar 10/14, Year of the Horse","📍 Hanoi · Cloudy","Mon","Tue","Wed","On your phone","Lambo","Translate","Football","Radio","Gold · FX","Lunar calendar","Weather","More","Control Living room speaker","Karaoke, volume, photos to TV","Home","Speaker","Songs","Tools",
"Now singing","My Way – Karaoke (male key)","Up next: Yesterday – Karaoke","OK","Back","Talk","Menu","Volume 45%","Key · Echo · Mic","Key","find other versions","Male","Female","Lower","Higher","Echo","Off","Studio","KTV","Stage","Mic volume",
"🎤 Karaoke","🎵 Original","Queue","2 songs in queue","Clear all","Yesterday – Karaoke","🎤 Tom","Sing","Remove","Let It Be – Karaoke (female key)","🎤 Anna","PH:Song, artist…",
"Ask Lambo anything, answers on the speaker","Answer on","📱 Phone","🔈 Speaker","What should I cook for the family tonight?","How about a creamy chicken pasta with a green salad? Quick, easy and everyone loves it. Want me to read the recipe?","Turn on the living room light","Living room light is on.","Will it rain tomorrow?","Tomorrow will be cloudy with light showers in the evening, 22 to 28 degrees. Don’t forget your umbrella.","PH:Ask Lambo…",
"Open on the speaker TV","Health","Fitness","Pickleball","Yoga","Meditation","Tai chi","Party & Sharing","Sing with your phone","Studio","Photo album","Greetings","Party mode","Lucky draw","Scores","Music on phone","News reader",
"Speak into your phone, the speaker reads the translation aloud.","Speak English","translate to Spanish","Hablar español","traducir al inglés","Read translation on","PH:Type an English sentence…",
"‹ Back","💪 Fitness","Start your streak today! · 7 days: 0 days, 0 min","Aerobics","burn fat, have fun","Zumba","dance to the music","Belly dance","toned waist","Dance sport","cha‑cha, rumba, samba","Home gym","no equipment needed","warm‑up, technique, rules","flexible and relaxed","calm mind, better sleep","gentle exercise for seniors","Kids workouts","fun and healthy","Stretching","before and after workouts",
"Exercise images: free-exercise-db (github.com/yuhonas/free-exercise-db), Unlicense (public domain). Music and voice guidance made for this app.",
"‹ Fitness","All","Beginner","Intermediate","Advanced","Full body for beginners","Beginner · 10 min · 6 moves × 2 rounds","Start","📺 To speaker","Flat belly basics","Beginner · 8 min · 5 moves × 2 rounds","Full‑body fat burn","Intermediate · 18 min · 6 moves × 3 rounds","Toned legs and glutes","Intermediate · 14 min · 5 moves × 3 rounds","Arms, chest and shoulders","Intermediate · 15 min · 5 moves × 3 rounds","Advanced HIIT","Advanced · 21 min · 7 moves × 3 rounds","Advanced six‑pack abs","Advanced · 18 min · 6 moves × 3 rounds",
"‹ Home gym","GET READY","Squat","Feet shoulder‑width apart, sit back as if onto a chair, knees behind your toes, then stand up.","Next: Squat","Pause","📺 Play on speaker / TV","🔊 Voice: on","🎵 Music: on"]
L['ja']=["リビングのスピーカー","192.168.1.25 · 接続済み","おはようございます","11月22日(日) · 旧暦10月14日 · 丙午年","📍 ハノイ · くもり","月","火","水","スマホで使う","Lambo","翻訳","サッカー","ラジオ","金 · 為替","旧暦","天気","追加","リビングのスピーカーを操作","カラオケ、音量、写真をテレビへ","ホーム","スピーカー","曲","ツール",
"再生中","乾杯 – カラオケ（男性キー）","次の曲：糸 – カラオケ","OK","戻る","話す","メニュー","音量 45%","キー · エコー · マイク","キー","別バージョンを探す","男性","女性","下げる","上げる","エコー","オフ","スタジオ","KTV","ステージ","マイク音量",
"🎤 カラオケ","🎵 原曲","予約","2曲予約中","すべて削除","糸 – カラオケ","🎤 たろう","歌う","削除","ハナミズキ – カラオケ（女性キー）","🎤 はなこ","PH:曲名、歌手…",
"Lamboに何でも聞いて、スピーカーで答えます","回答先","📱 スマホ","🔈 スピーカー","今夜は家族で何を食べようか？","肉じゃがとお味噌汁はいかがですか？簡単でご飯が進みます。作り方を読み上げましょうか？","リビングの電気をつけて","リビングの電気をつけました。","明日は雨が降る？","明日はくもりで、夕方から小雨の予報です。気温は22度から28度。傘を忘れずに。","PH:Lamboに質問…",
"スピーカーのテレビで開く","健康","フィットネス","ピックルボール","ヨガ","瞑想","太極拳・養生","パーティー＆シェア","スマホで歌う","スタジオ","アルバム","メッセージ","パーティーモード","抽選","採点","スマホの音楽","ニュース読み上げ",
"スマホに話すと、スピーカーが翻訳を読み上げます。","日本語で話す","英語に翻訳","Speak English","日本語に翻訳","翻訳を読み上げる場所","PH:翻訳したい日本語を入力…",
"‹ 戻る","💪 フィットネス","今日から連続記録を始めよう！ · 7日間：0日、0分","エアロビクス","脂肪燃焼、楽しく","ズンバ","音楽に合わせて","ベリーダンス","くびれづくり","ダンススポーツ","チャチャ、ルンバ、サンバ","おうちジム","器具なし","準備運動、技術、ルール","しなやかにリラックス","心を整えぐっすり","シニア向け気功","キッズ体操","楽しく元気に","ストレッチ","運動の前後に",
"動作画像：free-exercise-db (github.com/yuhonas/free-exercise-db)、Unlicense（パブリックドメイン）。音楽と音声ガイドはアプリ用に制作。",
"‹ フィットネス","すべて","初心者","中級","上級","初心者向け全身","初心者 · 10分 · 6種目 × 2セット","開始","📺 スピーカーへ","ぺたんこお腹の基本","初心者 · 8分 · 5種目 × 2セット","全身脂肪燃焼","中級 · 18分 · 6種目 × 3セット","脚とお尻の引き締め","中級 · 14分 · 5種目 × 3セット","腕・胸・肩","中級 · 15分 · 5種目 × 3セット","上級HIIT","上級 · 21分 · 7種目 × 3セット","上級シックスパック","上級 · 18分 · 6種目 × 3セット",
"‹ おうちジム","準備","スクワット","足を肩幅に開き、椅子に座るように腰を下ろします。ひざはつま先より前に出さず、立ち上がります。","次：スクワット","一時停止","📺 スピーカー／テレビで再生","🔊 音声：オン","🎵 音楽：オン"]
L['ko']=["거실 스피커","192.168.1.25 · 연결됨","좋은 아침이에요","11월 22일 일요일 · 음력 10월 14일, 병오년","📍 하노이 · 흐림","월","화","수","휴대폰에서","Lambo","번역","축구","라디오","금 · 환율","음력","날씨","더보기","거실 스피커 제어","노래방, 볼륨, 사진을 TV로","홈","스피커","노래","도구",
"지금 부르는 곡","좋은 날 – 노래방 (남자 키)","다음 곡: 밤편지 – 노래방","OK","뒤로","말하기","메뉴","볼륨 45%","키 · 에코 · 마이크","키","다른 버전 찾기","남성","여성","키 내리기","키 올리기","에코","끄기","스튜디오","KTV","무대","마이크 볼륨",
"🎤 노래방","🎵 원곡","예약","2곡 대기 중","모두 삭제","밤편지 – 노래방","🎤 민준","부르기","삭제","너의 의미 – 노래방 (여자 키)","🎤 서연","PH:곡명, 가수…",
"Lambo에게 무엇이든 물어보세요, 스피커로 답해요","답변 위치","📱 휴대폰","🔈 스피커","오늘 저녁 가족이랑 뭐 먹을까?","김치찌개와 계란말이는 어떠세요? 간단하고 밥반찬으로 좋아요. 레시피를 읽어 드릴까요?","거실 불 켜 줘","거실 불을 켰어요.","내일 비 와?","내일은 흐리고 저녁에 약한 소나기가 있어요. 기온은 22도에서 28도예요. 우산 챙기세요.","PH:Lambo에게 질문…",
"스피커 TV에서 열기","건강","피트니스","피클볼","요가","명상","기공·양생","파티 & 공유","휴대폰으로 노래","스튜디오","앨범","축하 메시지","파티 모드","제비뽑기","점수","휴대폰 음악","뉴스 읽기",
"휴대폰에 말하면 스피커가 번역을 읽어 줘요.","한국어로 말하기","영어로 번역","Speak English","한국어로 번역","번역 읽기 위치","PH:번역할 한국어를 입력…",
"‹ 뒤로","💪 피트니스","오늘부터 연속 기록을 시작해요! · 7일: 0일, 0분","에어로빅","지방 연소, 신나게","줌바","음악에 맞춰 춤","벨리댄스","잘록한 허리","댄스스포츠","차차, 룸바, 삼바","홈짐","도구 없이","준비운동, 기술, 규칙","유연하고 편안하게","마음 안정, 숙면","어르신 기공","어린이 운동","즐겁고 건강하게","스트레칭","운동 전후",
"동작 이미지: free-exercise-db (github.com/yuhonas/free-exercise-db), Unlicense(퍼블릭 도메인). 음악과 음성 안내는 앱 전용으로 제작.",
"‹ 피트니스","전체","초급","중급","고급","초보자 전신 운동","초급 · 10분 · 6동작 × 2세트","시작","📺 스피커로","납작 배 기초","초급 · 8분 · 5동작 × 2세트","전신 지방 연소","중급 · 18분 · 6동작 × 3세트","탄탄한 하체와 엉덩이","중급 · 14분 · 5동작 × 3세트","팔, 가슴, 어깨","중급 · 15분 · 5동작 × 3세트","고급 HIIT","고급 · 21분 · 7동작 × 3세트","고급 식스팩","고급 · 18분 · 6동작 × 3세트",
"‹ 홈짐","준비","스쿼트","발을 어깨너비로 벌리고 의자에 앉듯 엉덩이를 내립니다. 무릎이 발끝을 넘지 않게 한 뒤 일어섭니다.","다음: 스쿼트","일시정지","📺 스피커 / TV에서 재생","🔊 음성: 켜짐","🎵 음악: 켜짐"]
L['fr']=["Enceinte du salon","192.168.1.25 · connectée","Bonjour","Dim. 22 nov. · 14/10 lunaire, année du Cheval","📍 Hanoï · Nuageux","Lun","Mar","Mer","Sur le téléphone","Lambo","Traduction","Football","Radio","Or · Change","Calendrier lunaire","Météo","Plus","Piloter l’enceinte du salon","Karaoké, volume, photos sur la TV","Accueil","Enceinte","Chansons","Outils",
"En cours","La Vie en rose – Karaoké (ton homme)","Ensuite : Alors on danse – Karaoké","OK","Retour","Parler","Menu","Volume 45 %","Tonalité · Écho · Micro","Tonalité","autres versions","Homme","Femme","Baisser","Monter","Écho","Off","Studio","KTV","Scène","Volume micro",
"🎤 Karaoké","🎵 Original","File d’attente","2 chansons en attente","Tout effacer","Alors on danse – Karaoké","🎤 Paul","Chanter","Retirer","Je veux – Karaoké (ton femme)","🎤 Julie","PH:Titre, artiste…",
"Demandez tout à Lambo, réponse sur l’enceinte","Réponse sur","📱 Téléphone","🔈 Enceinte","On mange quoi ce soir en famille ?","Pourquoi pas un gratin de pâtes et une salade verte ? Simple et tout le monde aime. Je lis la recette ?","Allume la lumière du salon","La lumière du salon est allumée.","Il pleut demain ?","Demain, temps nuageux avec quelques averses le soir, de 22 à 28 degrés. Pensez au parapluie.","PH:Demandez à Lambo…",
"Ouvrir sur la TV de l’enceinte","Santé","Sport","Pickleball","Yoga","Méditation","Qi gong","Fête & partage","Chanter au téléphone","Studio","Album photo","Vœux","Mode fête","Tirage au sort","Notes","Musique du téléphone","Lecture d’actus",
"Parlez au téléphone, l’enceinte lit la traduction à voix haute.","Parler français","traduire en anglais","Speak English","traduire en français","Lire la traduction sur","PH:Tapez une phrase en français…",
"‹ Retour","💪 Sport","Commencez votre série aujourd’hui ! · 7 jours : 0 jour, 0 min","Aérobic","brûler, s’amuser","Zumba","danser en rythme","Danse orientale","taille fine","Danse sportive","cha‑cha, rumba, samba","Gym à la maison","sans matériel","échauffement, technique, règles","souplesse et détente","esprit calme, bon sommeil","gym douce seniors","Sport pour enfants","bouger en s’amusant","Étirements","avant et après l’effort",
"Images : free-exercise-db (github.com/yuhonas/free-exercise-db), Unlicense (domaine public). Musique et guidage vocal créés pour l’app.",
"‹ Sport","Tout","Débutant","Intermédiaire","Avancé","Corps entier débutant","Débutant · 10 min · 6 exercices × 2 tours","Go","📺 Sur l’enceinte","Ventre plat de base","Débutant · 8 min · 5 exercices × 2 tours","Brûle‑graisses complet","Intermédiaire · 18 min · 6 exercices × 3 tours","Jambes et fessiers","Intermédiaire · 14 min · 5 exercices × 3 tours","Bras, pecs et épaules","Intermédiaire · 15 min · 5 exercices × 3 tours","HIIT avancé","Avancé · 21 min · 7 exercices × 3 tours","Abdos avancés","Avancé · 18 min · 6 exercices × 3 tours",
"‹ Gym à la maison","PRÉPAREZ‑VOUS","Squat","Pieds écartés largeur d’épaules, descendez comme pour vous asseoir, genoux derrière les orteils, puis remontez.","Ensuite : Squat","Pause","📺 Lire sur l’enceinte / TV","🔊 Voix : on","🎵 Musique : on"]
L['zh']=["客厅音箱","192.168.1.25 · 已连接","早上好","11月22日 周日 · 农历十月十四 · 丙午年","📍 河内 · 多云","周一","周二","周三","手机功能","Lambo","翻译","足球","电台","金价 · 汇率","农历","天气","更多","控制客厅音箱","卡拉OK、音量、照片投到电视","首页","音箱","歌曲","工具",
"正在演唱","月亮代表我的心 – 伴奏（男调）","下一首：甜蜜蜜 – 伴奏","OK","返回","说话","菜单","音量 45%","音调 · 混响 · 麦克风","音调","查找其他版本","男声","女声","降调","升调","混响","关闭","录音棚","KTV","舞台","麦克风音量",
"🎤 卡拉OK","🎵 原唱","已点","2首等待中","全部清除","甜蜜蜜 – 伴奏","🎤 小明","演唱","删除","后来 – 伴奏（女调）","🎤 小红","PH:歌名、歌手…",
"有问题就问 Lambo，在音箱上回答","回答设备","📱 手机","🔈 音箱","今晚全家吃什么好？","试试西红柿炒鸡蛋配紫菜蛋花汤吧，简单又下饭。要我读一下做法吗？","打开客厅的灯","客厅的灯已打开。","明天会下雨吗？","明天多云，傍晚有小阵雨，气温22到28度。记得带伞哦。","PH:问问 Lambo…",
"在音箱电视上打开","健康","健身","匹克球","瑜伽","冥想","养生气功","派对与分享","用手机唱歌","录音棚","相册","祝福","派对模式","抽签","评分","手机音乐","读新闻",
"对着手机说话，音箱朗读译文。","说中文","译成英语","Speak English","译成中文","朗读译文的设备","PH:输入要翻译的中文…",
"‹ 返回","💪 健身","今天开始连续打卡吧！ · 7天：0天，0分钟","有氧操","燃脂，欢乐","尊巴","跟着音乐跳","肚皮舞","纤腰","体育舞蹈","恰恰、伦巴、桑巴","居家健身","无需器械","热身、技巧、规则","柔韧放松","静心助眠","长辈养生功","儿童运动","快乐健康","拉伸","运动前后",
"动作图片：free-exercise-db (github.com/yuhonas/free-exercise-db)，Unlicense（公有领域）。音乐和语音指导为本应用专门制作。",
"‹ 健身","全部","入门","中级","高级","新手全身训练","入门 · 10分钟 · 6个动作 × 2组","开始","📺 投到音箱","平坦小腹入门","入门 · 8分钟 · 5个动作 × 2组","全身燃脂","中级 · 18分钟 · 6个动作 × 3组","紧致腿臀","中级 · 14分钟 · 5个动作 × 3组","手臂、胸和肩","中级 · 15分钟 · 5个动作 × 3组","高级HIIT","高级 · 21分钟 · 7个动作 × 3组","高级六块腹肌","高级 · 18分钟 · 6个动作 × 3组",
"‹ 居家健身","准备","深蹲","双脚与肩同宽，像坐椅子一样下蹲，膝盖不超过脚尖，然后站起。","下一个：深蹲","暂停","📺 在音箱 / 电视播放","🔊 语音：开","🎵 音乐：开"]
for l in ['en','ja','ko','fr','zh']:
    assert L[l][76] in ('Studio','スタジオ','스튜디오','录音棚'),L[l][76]; del L[l][76]
for l,v in L.items():
    if isinstance(v,list):
        assert len(v)==len(K),(l,len(v),len(K))
        d=dict(zip(K,v))
    else: d=v
    d.update(COMMON)
    # extra variants of greeting
    json.dump(d,open('dict-%s.json'%l,'w'),ensure_ascii=False)
print('ok')
