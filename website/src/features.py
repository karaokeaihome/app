# -*- coding: utf-8 -*-
# Trang chi tiết Phòng thu và Sàn hát: danh sách chức năng + hình minh hoạ dựng bằng HTML (tự dịch theo ngôn ngữ).
# Biểu tượng con không trùng nhau và không trùng 32 biểu tượng ở trang chủ.
R = {}
R['vi'] = {
 'badge': "Bản miễn phí: 10 bài mỗi ngày · VIP: không giới hạn",
 'how': "Cách dùng",
 'phong-thu': dict(
  items=[("🎬","Hát theo video karaoke","Tìm bài ngay trong app. Nửa trên màn hình hiện video có lời, nửa dưới là nút thu âm."),
   ("🔁","Hát theo bài đang phát trên loa","Loa phát karaoke trên TV, điện thoại thu giọng của bạn. Thu xong có thể phát giọng cùng video ngay trên loa."),
   ("🎧","Hát với nhạc beat của bạn","Chọn file nhạc mp3, m4a có sẵn trong máy, app ghép giọng khớp chính xác với nhạc. Nên đeo tai nghe để nhạc không lọt vào bản thu."),
   ("🎼","Tông nam, tông nữ","Chọn tông hợp giọng trước khi hát, có đếm ngược để bạn kịp chuẩn bị."),
   ("🪄","Chỉnh giọng như phòng thu","Chỉnh trầm, bổng, vang, echo, làm sạch giọng (bớt ù, bớt tiếng ồn) hoặc chọn mẫu chỉnh nhanh chỉ một chạm."),
   ("⏪","Nghe lại khớp nhạc","Giọng và nhạc phát lại khớp nhau, tua tới lui được, chỉnh riêng âm lượng nhạc nền và giọng."),
   ("💾","Lưu file MP3","Lưu bản thu thành MP3 về máy hoặc gửi ngay qua Zalo, Messenger cho người thân."),
   ("🌟","Đăng lên Sàn hát","Thích bản thu nào, bấm một nút là đăng lên Sàn hát cho mọi người cùng nghe.")],
  steps=["Mở app → Tiện ích → Phòng thu.","Chọn nguồn nhạc: video karaoke, bài trên loa hoặc nhạc trong máy.","Chọn tông, bấm ● Bắt đầu thu và hát.","Nghe lại, chỉnh giọng, rồi lưu MP3 hoặc đăng lên Sàn hát."],
  mock=dict(title="Phòng thu", song="Mùa thu Hà Nội", lyric="♪ Hà Nội mùa thu, cây cơm nguội vàng…", key=("Tông nam","Tông nữ"),
   knobs=("Trầm","Bổng","Vang","Echo"), rec="● Bắt đầu thu", save="💾 Lưu MP3", post="🌟 Đăng lên Sàn hát")),
 'san-hat': dict(
  items=[("🆕","Bài mới mỗi ngày","Nghe những bài hát mới nhất mọi người vừa đăng, bấm vào là nghe ngay cùng video karaoke."),
   ("❤️","Thả tim","Thích giọng hát nào, thả tim để động viên người hát."),
   ("🌹","Tặng hoa","Tặng hoa cho giọng hát bạn yêu thích. Hoa giúp bài hát lên cao trên bảng xếp hạng."),
   ("💬","Bình luận","Khen, góp ý, trò chuyện ngay dưới mỗi bài hát."),
   ("👫","Hát đôi","Mời mọi người hát đôi cùng bài của bạn. Người hát sau nghe giọng bạn cùng video, thu giọng của mình, nghe thử bản song ca rồi đăng."),
   ("🥇","Top tuần","Bảng xếp hạng 7 ngày qua, tính theo tim, hoa và số người nghe. Hát hay là lên top."),
   ("👤","Trang của tôi","Đặt tên hiển thị, ảnh đại diện, xem lại các bài đã đăng và xoá bài bất cứ lúc nào."),
   ("🚩","An toàn cho cả nhà","Mỗi bài và bình luận đều có nút báo cáo, chặn được người làm phiền. Nội dung bị báo cáo được tạm ẩn chờ duyệt."),
   ("🎵","Nhạc nền chính thức","Bài đăng chỉ chứa giọng hát, nhạc nền phát từ video karaoke chính thức trên YouTube nên bài nhẹ, mở nhanh.")],
  steps=["Mở app → Tiện ích → Sàn hát.","Tạo tài khoản bằng email (miễn phí) và đặt tên của bạn.","Hát trong Phòng thu rồi bấm 🌟 Đăng lên Sàn hát.","Nghe mọi người hát, thả tim, tặng hoa, bình luận và mời hát đôi."],
  mock=dict(title="Sàn hát", tabs=("🆕 Mới","🥇 Top tuần","👫 Hát đôi","👤 Của tôi"),
   posts=(("Biển nhớ","Chị Lan"),("Tình ca quê hương","Anh Phong"),("Mùa thu Hà Nội","Bà Tư")), duet="👫 mời hát đôi")),
}
R['en'] = {
 'badge': "Free: 10 a day · VIP: unlimited",
 'how': "How it works",
 'phong-thu': dict(
  items=[("🎬","Sing along to karaoke videos","Search for a song in the app. The top half shows the lyric video, the bottom half has the record button."),
   ("🔁","Sing to the song on the speaker","The speaker plays karaoke on the TV while your phone records your voice. Afterwards you can play your voice with the video right on the speaker."),
   ("🎧","Sing over your own backing track","Pick an mp3 or m4a file on your phone and the app lines your voice up exactly with the music. Wear headphones so the music doesn’t leak into the recording."),
   ("🎼","Male or female key","Choose the key that suits your voice before you start, with a countdown so you are ready."),
   ("🪄","Studio‑style voice tuning","Adjust bass, treble, reverb and echo, clean up your voice (less hum and noise), or pick a one‑tap preset."),
   ("⏪","Playback in perfect sync","Voice and music play back in sync, you can seek back and forth, and set the music and voice volume separately."),
   ("💾","Save as MP3","Save your recording as an MP3 on your phone or share it straight to your favourite messaging apps."),
   ("🌟","Post to the Singing Stage","Happy with a take? One tap posts it to the Singing Stage for everyone to hear.")],
  steps=["Open the app → Utilities → Recording Studio.","Choose the music: karaoke video, song on the speaker or music on your phone.","Pick a key, tap ● Start recording and sing.","Listen back, tune your voice, then save an MP3 or post it to the Singing Stage."],
  mock=dict(title="Recording Studio", song="Autumn Breeze", lyric="♪ Golden leaves are falling down…", key=("Male key","Female key"),
   knobs=("Bass","Treble","Reverb","Echo"), rec="● Start recording", save="💾 Save MP3", post="🌟 Post to the Stage")),
 'san-hat': dict(
  items=[("🆕","New songs every day","Listen to the latest songs people have just posted, playing together with the karaoke video."),
   ("❤️","Hearts","Love a voice? Give it a heart to cheer the singer on."),
   ("🌹","Flowers","Send flowers to the singers you like best. Flowers help a song climb the chart."),
   ("💬","Comments","Praise, give tips or chat under every song."),
   ("👫","Duets","Invite everyone to sing a duet with you. The next singer hears your voice with the video, records their part, previews the duet and posts it."),
   ("🥇","Weekly Top","A chart of the last 7 days based on hearts, flowers and listeners. Sing well and reach the top."),
   ("👤","My page","Set your display name and profile photo, see your posts and delete any of them at any time."),
   ("🚩","Safe for the whole family","Every song and comment has a report button and you can block anyone who bothers you. Reported content is hidden pending review."),
   ("🎵","Official backing music","Posts contain only your voice; the music plays from the official karaoke video on YouTube, so songs are light and open fast.")],
  steps=["Open the app → Utilities → Singing Stage.","Create a free account with your email and choose your name.","Sing in the Recording Studio, then tap 🌟 Post to the Singing Stage.","Listen to others, give hearts and flowers, comment and invite duets."],
  mock=dict(title="Singing Stage", tabs=("🆕 New","🥇 Weekly Top","👫 Duets","👤 Mine"),
   posts=(("Ocean Memories","Linda"),("Country Road Home","Peter"),("Autumn Breeze","Grandma Rose")), duet="👫 duet invite")),
}
R['ja'] = {
 'badge': "無料版：1日10曲 · VIP：無制限",
 'how': "使い方",
 'phone-thu': None,
 'phong-thu': dict(
  items=[("🎬","カラオケ動画に合わせて歌う","アプリ内で曲を検索。画面の上半分に歌詞付き動画、下半分に録音ボタンが表示されます。"),
   ("🔁","スピーカーで流れている曲に合わせて歌う","スピーカーがテレビでカラオケを再生し、スマホがあなたの声を録音。録音後は動画と一緒に声をスピーカーで再生できます。"),
   ("🎧","自分の伴奏で歌う","スマホ内の mp3・m4a を選ぶと、声と音楽をぴったり合わせます。音楽が録音に入らないようイヤホンの使用をおすすめします。"),
   ("🎼","男性キー・女性キー","歌う前に声に合ったキーを選択。カウントダウン付きで準備も安心。"),
   ("🪄","スタジオ並みの声の調整","低音・高音・リバーブ・エコーの調整、声のクリーンアップ（ハムやノイズを軽減）、ワンタップのプリセット。"),
   ("⏪","ぴったり合った再生","声と音楽が同期して再生され、早送り・巻き戻しも可能。伴奏と声の音量を個別に調整できます。"),
   ("💾","MP3 で保存","録音を MP3 としてスマホに保存したり、メッセージアプリですぐに共有したりできます。"),
   ("🌟","歌のステージに投稿","気に入ったテイクはワンタップで歌のステージに投稿し、みんなに聴いてもらえます。")],
  steps=["アプリを開く → ユーティリティ → レコーディングスタジオ。","伴奏を選ぶ：カラオケ動画、スピーカーの曲、スマホ内の音楽。","キーを選んで ● 録音開始 を押して歌う。","聴き直して声を調整し、MP3 で保存するかステージに投稿。"],
  mock=dict(title="レコーディングスタジオ", song="秋のそよ風", lyric="♪ 金色の葉が舞い落ちる…", key=("男性キー","女性キー"),
   knobs=("低音","高音","リバーブ","エコー"), rec="● 録音開始", save="💾 MP3 保存", post="🌟 ステージに投稿")),
 'san-hat': dict(
  items=[("🆕","毎日届く新しい歌","みんなが投稿したばかりの歌を、カラオケ動画と一緒にすぐ聴けます。"),
   ("❤️","ハート","好きな歌声にハートを送って応援しましょう。"),
   ("🌹","花を贈る","お気に入りの歌い手に花を贈れます。花はランキングを押し上げます。"),
   ("💬","コメント","それぞれの歌の下で感想やアドバイス、おしゃべりを。"),
   ("👫","デュエット","みんなをデュエットに招待。次の人はあなたの声と動画を聴きながら自分のパートを録音し、デュエットを試聴して投稿します。"),
   ("🥇","週間トップ","ハート・花・リスナー数による直近7日間のランキング。上手に歌ってトップを目指そう。"),
   ("👤","マイページ","表示名とプロフィール画像を設定し、投稿を確認・いつでも削除できます。"),
   ("🚩","家族みんなで安心","すべての歌とコメントに報告ボタンがあり、迷惑なユーザーはブロック可能。報告された内容は審査まで非表示になります。"),
   ("🎵","公式の伴奏","投稿には歌声だけを保存し、伴奏は YouTube の公式カラオケ動画から再生するので、軽くてすぐ開けます。")],
  steps=["アプリを開く → ユーティリティ → 歌のステージ。","メールで無料アカウントを作成し、名前を設定。","スタジオで歌って 🌟 ステージに投稿 を押す。","みんなの歌を聴いて、ハートや花、コメント、デュエットの招待を。"],
  mock=dict(title="歌のステージ", tabs=("🆕 新着","🥇 週間トップ","👫 デュエット","👤 マイ"),
   posts=(("海の思い出","ユキ"),("ふるさとの道","タロウ"),("秋のそよ風","ハナおばあちゃん")), duet="👫 デュエット募集")),
}
R['ko'] = {
 'badge': "무료: 하루 10곡 · VIP: 무제한",
 'how': "사용 방법",
 'phong-thu': dict(
  items=[("🎬","노래방 영상에 맞춰 부르기","앱에서 바로 곡을 찾으세요. 화면 위쪽에는 가사 영상, 아래쪽에는 녹음 버튼이 있습니다."),
   ("🔁","스피커에서 나오는 곡에 맞춰 부르기","스피커가 TV로 노래방을 틀고 휴대폰이 목소리를 녹음합니다. 녹음 후 영상과 함께 목소리를 스피커로 재생할 수 있습니다."),
   ("🎧","내 반주로 부르기","휴대폰의 mp3, m4a 파일을 고르면 목소리를 반주에 정확히 맞춥니다. 반주가 녹음에 섞이지 않도록 이어폰을 권장합니다."),
   ("🎼","남성 키, 여성 키","부르기 전에 목소리에 맞는 키를 고르세요. 카운트다운으로 준비할 시간을 줍니다."),
   ("🪄","스튜디오처럼 목소리 보정","저음, 고음, 리버브, 에코 조절, 목소리 정리(웅웅거림·잡음 감소), 원터치 프리셋."),
   ("⏪","딱 맞는 다시 듣기","목소리와 반주가 맞춰 재생되고 앞뒤로 이동할 수 있으며, 반주와 목소리 볼륨을 따로 조절합니다."),
   ("💾","MP3로 저장","녹음을 MP3로 휴대폰에 저장하거나 메신저로 바로 공유하세요."),
   ("🌟","노래 무대에 올리기","마음에 드는 녹음은 한 번만 누르면 노래 무대에 올라가 모두가 들을 수 있습니다.")],
  steps=["앱 열기 → 유틸리티 → 녹음실.","반주 선택: 노래방 영상, 스피커의 곡, 휴대폰의 음악.","키를 고르고 ● 녹음 시작을 눌러 노래하세요.","다시 듣고 목소리를 보정한 뒤 MP3로 저장하거나 무대에 올리세요."],
  mock=dict(title="녹음실", song="가을 바람", lyric="♪ 노란 잎이 떨어지네…", key=("남성 키","여성 키"),
   knobs=("저음","고음","리버브","에코"), rec="● 녹음 시작", save="💾 MP3 저장", post="🌟 무대에 올리기")),
 'san-hat': dict(
  items=[("🆕","매일 새 노래","방금 올라온 노래를 노래방 영상과 함께 바로 들어 보세요."),
   ("❤️","하트","마음에 드는 목소리에 하트를 보내 응원하세요."),
   ("🌹","꽃 선물","좋아하는 가수에게 꽃을 선물하세요. 꽃은 노래를 순위 위로 올려 줍니다."),
   ("💬","댓글","노래마다 칭찬, 조언, 대화를 남기세요."),
   ("👫","듀엣","모두를 듀엣에 초대하세요. 다음 사람은 영상과 함께 내 목소리를 들으며 자기 파트를 녹음하고, 듀엣을 미리 들은 뒤 올립니다."),
   ("🥇","주간 Top","하트, 꽃, 청취자 수로 매긴 최근 7일 순위. 잘 부르면 Top에 오릅니다."),
   ("👤","내 페이지","표시 이름과 프로필 사진을 정하고, 올린 노래를 보고 언제든 삭제할 수 있습니다."),
   ("🚩","온 가족이 안심","모든 노래와 댓글에 신고 버튼이 있고 불편한 사용자는 차단할 수 있습니다. 신고된 콘텐츠는 검토 전까지 숨겨집니다."),
   ("🎵","공식 반주","게시물에는 목소리만 저장되고 반주는 YouTube 공식 노래방 영상에서 재생되어 가볍고 빨리 열립니다.")],
  steps=["앱 열기 → 유틸리티 → 노래 무대.","이메일로 무료 계정을 만들고 이름을 정하세요.","녹음실에서 노래한 뒤 🌟 무대에 올리기를 누르세요.","다른 사람의 노래를 듣고 하트, 꽃, 댓글, 듀엣 초대를 해 보세요."],
  mock=dict(title="노래 무대", tabs=("🆕 최신","🥇 주간 Top","👫 듀엣","👤 내 노래"),
   posts=(("바다의 추억","지은"),("고향 가는 길","민수"),("가을 바람","순자 할머니")), duet="👫 듀엣 초대")),
}
R['fr'] = {
 'badge': "Gratuit : 10 par jour · VIP : illimité",
 'how': "Comment ça marche",
 'phong-thu': dict(
  items=[("🎬","Chanter sur une vidéo karaoké","Cherchez une chanson dans l’application : la moitié haute de l’écran affiche la vidéo avec les paroles, la moitié basse le bouton d’enregistrement."),
   ("🔁","Chanter sur le morceau de l’enceinte","L’enceinte lance le karaoké sur la TV pendant que le téléphone enregistre votre voix. Ensuite, réécoutez votre voix avec la vidéo directement sur l’enceinte."),
   ("🎧","Chanter sur votre propre instrumental","Choisissez un fichier mp3 ou m4a du téléphone : l’application cale votre voix exactement sur la musique. Mettez un casque pour que la musique ne s’entende pas dans l’enregistrement."),
   ("🎼","Tonalité homme ou femme","Choisissez la tonalité adaptée à votre voix avant de chanter, avec un compte à rebours pour être prêt."),
   ("🪄","Réglages de voix comme en studio","Graves, aigus, réverbération, écho, nettoyage de la voix (moins de souffle et de bruit) ou réglage rapide en une touche."),
   ("⏪","Réécoute parfaitement synchronisée","Voix et musique sont synchronisées, vous pouvez avancer ou reculer et régler séparément le volume de la musique et de la voix."),
   ("💾","Export MP3","Enregistrez votre prise en MP3 sur le téléphone ou partagez‑la directement dans vos messageries."),
   ("🌟","Publier sur la Scène","Une prise vous plaît ? Une touche suffit pour la publier sur la Scène karaoké.")],
  steps=["Ouvrez l’application → Outils → Studio d’enregistrement.","Choisissez la musique : vidéo karaoké, morceau de l’enceinte ou musique du téléphone.","Choisissez la tonalité, touchez ● Enregistrer et chantez.","Réécoutez, réglez votre voix, puis enregistrez en MP3 ou publiez sur la Scène."],
  mock=dict(title="Studio", song="Brise d’automne", lyric="♪ Les feuilles dorées tombent…", key=("Ton homme","Ton femme"),
   knobs=("Graves","Aigus","Réverb","Écho"), rec="● Enregistrer", save="💾 Enregistrer MP3", post="🌟 Publier sur la Scène")),
 'san-hat': dict(
  items=[("🆕","Nouveautés chaque jour","Écoutez les dernières chansons publiées, avec la vidéo karaoké."),
   ("❤️","Cœurs","Une voix vous plaît ? Offrez un cœur pour encourager le chanteur."),
   ("🌹","Fleurs","Offrez des fleurs à vos chanteurs préférés. Les fleurs font monter la chanson dans le classement."),
   ("💬","Commentaires","Compliments, conseils ou discussion sous chaque chanson."),
   ("👫","Duos","Invitez tout le monde à chanter en duo avec vous. Le chanteur suivant entend votre voix avec la vidéo, enregistre sa partie, écoute le duo puis le publie."),
   ("🥇","Top de la semaine","Classement des 7 derniers jours selon les cœurs, les fleurs et le nombre d’auditeurs."),
   ("👤","Ma page","Choisissez votre nom et votre photo, retrouvez vos publications et supprimez‑les quand vous voulez."),
   ("🚩","Sûr pour toute la famille","Chaque chanson et commentaire a un bouton de signalement, et vous pouvez bloquer les gêneurs. Le contenu signalé est masqué en attente d’examen."),
   ("🎵","Accompagnement officiel","Les publications ne contiennent que votre voix ; la musique est lue depuis la vidéo karaoké officielle sur YouTube, donc les chansons sont légères et s’ouvrent vite.")],
  steps=["Ouvrez l’application → Outils → Scène karaoké.","Créez un compte gratuit avec votre e‑mail et choisissez votre nom.","Chantez dans le Studio puis touchez 🌟 Publier sur la Scène.","Écoutez les autres, offrez cœurs et fleurs, commentez et lancez des duos."],
  mock=dict(title="Scène karaoké", tabs=("🆕 Nouveau","🥇 Top","👫 Duos","👤 Moi"),
   posts=(("Souvenirs de la mer","Claire"),("Le chemin du village","Paul"),("Brise d’automne","Mamie Rose")), duet="👫 invitation en duo")),
}
R['zh'] = {
 'badge': "免费版：每天 10 首 · VIP：不限",
 'how': "使用方法",
 'phong-thu': dict(
  items=[("🎬","跟着卡拉OK视频唱","在应用中直接搜歌。屏幕上半部分显示带歌词的视频，下半部分是录音按钮。"),
   ("🔁","跟着音箱正在播放的歌唱","音箱在电视上播放卡拉OK，手机录下你的声音。录完可以在音箱上把人声和视频一起播放。"),
   ("🎧","用自己的伴奏唱","选择手机里的 mp3、m4a 文件，应用会把人声与伴奏精准对齐。建议戴耳机，避免伴奏漏进录音。"),
   ("🎼","男调、女调","开唱前选择适合自己的调，并有倒计时让你做好准备。"),
   ("🪄","录音棚级人声调节","调节低音、高音、混响、回声，人声降噪（减少嗡嗡声和杂音），或一键选择预设。"),
   ("⏪","同步回放","人声与伴奏同步回放，可前后拖动，伴奏和人声音量可分别调节。"),
   ("💾","保存为 MP3","把录音保存为 MP3 到手机，或直接分享到聊天应用。"),
   ("🌟","发布到歌唱舞台","满意的录音一键发布到歌唱舞台，让大家都来听。")],
  steps=["打开应用 → 工具 → 录音棚。","选择伴奏：卡拉OK视频、音箱上的歌或手机里的音乐。","选调，点击 ● 开始录音 并演唱。","回放并调节人声，然后保存 MP3 或发布到歌唱舞台。"],
  mock=dict(title="录音棚", song="秋风", lyric="♪ 金黄的叶子飘落…", key=("男调","女调"),
   knobs=("低音","高音","混响","回声"), rec="● 开始录音", save="💾 保存 MP3", post="🌟 发布到舞台")),
 'san-hat': dict(
  items=[("🆕","每天都有新歌","收听大家刚发布的新歌，与卡拉OK视频一起播放。"),
   ("❤️","点赞爱心","喜欢某个歌声，就送一颗爱心为他加油。"),
   ("🌹","送花","给喜欢的歌手送花，鲜花能让歌曲在排行榜上升。"),
   ("💬","评论","在每首歌下面称赞、建议或聊天。"),
   ("👫","合唱","邀请大家和你合唱。下一位歌手边看视频边听你的声音，录下自己的部分，试听合唱后发布。"),
   ("🥇","每周榜单","按爱心、鲜花和收听人数统计的近 7 天排行榜，唱得好就能上榜。"),
   ("👤","我的主页","设置显示名称和头像，查看自己发布的作品，随时删除。"),
   ("🚩","全家安心","每首歌和评论都有举报按钮，可以屏蔽打扰你的人。被举报的内容在审核前会暂时隐藏。"),
   ("🎵","官方伴奏","作品只保存人声，伴奏来自 YouTube 官方卡拉OK视频，因此作品小、打开快。")],
  steps=["打开应用 → 工具 → 歌唱舞台。","用邮箱免费注册并设置名字。","在录音棚演唱后点击 🌟 发布到歌唱舞台。","收听大家的歌，送爱心、送花、评论并邀请合唱。"],
  mock=dict(title="歌唱舞台", tabs=("🆕 最新","🥇 每周榜","👫 合唱","👤 我的"),
   posts=(("海的回忆","小雨"),("回家的路","阿明"),("秋风","王奶奶")), duet="👫 邀请合唱")),
}
for _l in R: R[_l].pop('phone-thu', None)

def mock_studio(m):
    e = __import__('html').escape
    knobs = ''.join('<div class="kn"><span>%s</span><i style="--v:%d%%"></i></div>' % (e(k), v) for k, v in zip(m['knobs'], (55, 62, 70, 35)))
    return ('<div class="mock"><div class="mh">🎙️ %s</div><div class="mv"><b>KARAOKE</b><small>%s</small><em>%s</em></div>'
            '<div class="wave">%s</div><div class="chips"><span class="on">%s</span><span>%s</span></div>%s'
            '<div class="mrec">%s</div><div class="mrow"><span>%s</span><span class="g">%s</span></div></div>') % (
        e(m['title']), e(m['song']), e(m['lyric']), '<i></i>' * 28, e(m['key'][0]), e(m['key'][1]), knobs, e(m['rec']), e(m['save']), e(m['post']))

def mock_stage(m):
    e = __import__('html').escape
    tabs = ''.join('<span class="%s">%s</span>' % ('on' if i == 1 else '', e(t)) for i, t in enumerate(m['tabs']))
    cols = ('#7a2e2e', '#2e4f7a', '#4f2e7a')
    nums = ((236, 41, 18), (198, 33, 12), (152, 20, 9))
    posts = ''.join('<div class="pc"><b class="rk">%d</b><div class="th" style="background:linear-gradient(135deg,%s,#111)">KARAOKE</div><div class="pt"><b>%s</b><small>%s%s</small><small>❤️ %d · 🌹 %d · 💬 %d</small></div></div>' % (
        i + 1, cols[i], e(t), e(s), (' · <span class="du">%s</span>' % e(m['duet'])) if i == 1 else '', *nums[i]) for i, (t, s) in enumerate(m['posts']))
    return '<div class="mock"><div class="mh">🎪 %s</div><div class="tabs4">%s</div>%s</div>' % (e(m['title']), tabs, posts)

CSS = """
.richwrap{display:grid;gap:22px;align-items:start;margin-top:18px}@media(min-width:800px){.richwrap{grid-template-columns:300px 1fr}}
.mock{width:280px;margin:0 auto;background:#0b0b0c;border:8px solid #222;border-radius:36px;padding:16px 12px 18px;box-shadow:0 10px 40px #0008;font-size:13px}
.mock .mh{font-weight:800;color:#f3d77a;font-size:17px;margin:2px 4px 10px}
.mock .mv{border-radius:12px;background:linear-gradient(135deg,#3a1c4a,#101018);padding:14px 12px;display:flex;flex-direction:column;gap:4px;min-height:96px}
.mock .mv b{color:#fff8;letter-spacing:.2em;font-size:12px}.mock .mv small{color:#fff;font-weight:700;font-size:14px}.mock .mv em{color:#f3d77a;font-style:normal}
.mock .wave{display:flex;gap:3px;align-items:center;height:44px;margin:10px 4px}.mock .wave i{flex:1;background:#d4af37;border-radius:2px;height:30%}
.mock .wave i:nth-child(3n){height:80%}.mock .wave i:nth-child(4n+1){height:55%}.mock .wave i:nth-child(5n+2){height:95%}.mock .wave i:nth-child(7n){height:40%}
.mock .chips{display:flex;gap:6px;margin:4px 0 8px}.mock .chips span{flex:1;text-align:center;background:#1f1f23;border-radius:10px;padding:6px}.mock .chips .on{background:#d4af37;color:#111;font-weight:700}
.mock .kn{display:flex;align-items:center;gap:8px;margin:6px 2px}.mock .kn span{width:64px;color:#9b978f}.mock .kn i{flex:1;height:6px;border-radius:3px;background:linear-gradient(90deg,#d4af37 var(--v),#2a2a2f var(--v))}
.mock .mrec{margin:12px 0 8px;background:#e5484d;color:#fff;text-align:center;border-radius:14px;padding:11px;font-weight:800;font-size:15px}
.mock .mrow{display:flex;gap:6px}.mock .mrow span{flex:1;text-align:center;background:#1f1f23;border-radius:12px;padding:9px 4px;font-size:12px}.mock .mrow .g{background:#d4af37;color:#111;font-weight:700}
.mock .tabs4{display:grid;grid-template-columns:repeat(4,1fr);gap:4px;margin-bottom:8px}.mock .tabs4 span{background:#17171a;border-radius:10px;padding:6px 2px;text-align:center;font-size:11px;line-height:1.2}.mock .tabs4 .on{background:#d4af37;color:#111;font-weight:700}
.mock .pc{display:flex;gap:8px;align-items:center;background:#17171a;border-radius:14px;padding:8px;margin-top:8px}
.mock .rk{color:#f3d77a;font-size:20px;width:18px;text-align:center}.mock .th{width:70px;height:42px;border-radius:8px;color:#fff6;font-size:9px;font-weight:800;letter-spacing:.15em;display:flex;align-items:center;justify-content:center;flex:none}
.mock .pt{min-width:0}.mock .pt b{display:block;font-size:13px}.mock .pt small{display:block;color:#9b978f;font-size:11px}.mock .du{color:#3ecf8e}
.subf{display:grid;gap:12px}@media(min-width:560px){.subf{grid-template-columns:1fr 1fr}}
.subf .card{display:flex;gap:12px;padding:14px;margin:0}.subf .si{font-size:1.6rem;line-height:1;flex:none}.subf b{display:block;margin-bottom:3px}.subf p{margin:0;font-size:.95rem;opacity:.9}
.badge{display:inline-block;margin:10px 0 0;padding:6px 12px;border-radius:999px;border:1px solid #4a3d18;background:#2a2210;color:var(--acc);font-weight:700;font-size:.9rem}
.steps{counter-reset:s;list-style:none;padding:0}.steps li{counter-increment:s;position:relative;padding:8px 0 8px 40px}.steps li:before{content:counter(s);position:absolute;left:0;top:6px;width:28px;height:28px;border-radius:50%;background:var(--acc);color:#111;font-weight:800;display:flex;align-items:center;justify-content:center}
"""

def rich(l, slug):
    import html
    e = html.escape
    d = R[l][slug]
    mock = mock_studio(d['mock']) if slug == 'phong-thu' else mock_stage(d['mock'])
    cards = ''.join('<div class="card"><span class="si">%s</span><div><b>%s</b><p>%s</p></div></div>' % (i, e(t), e(x)) for i, t, x in d['items'])
    steps = '<h2>%s</h2><ol class="steps">%s</ol>' % (e(R[l]['how']), ''.join('<li>%s</li>' % e(s) for s in d['steps']))
    return '<div class="badge">%s</div><div class="richwrap"><div>%s</div><div><div class="subf">%s</div>%s</div></div>' % (e(R[l]['badge']), mock, cards, steps)
