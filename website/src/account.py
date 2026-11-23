# -*- coding: utf-8 -*-
# Trang Đăng nhập (/<lang>/account/): chỉ đăng nhập tài khoản đã có, KHÔNG có đăng ký (tài khoản tạo trong app khi kết nối loa).
# Gọi máy chủ https://api.karaokeaihome.com/w/acct/* và /w/san/* (repo karaokeaihome/sever, worker.js + acct.js).
T = {
 'vi': dict(nav="Đăng nhập", h="Đăng nhập tài khoản", lead="Đăng nhập để nghe lại và quản lý các bài hát bạn đã đăng lên Sàn hát.",
  email="Email", send="Gửi mã đăng nhập", code="Mã 6 số trong email", login="Đăng nhập", other="Dùng email khác", resend="Gửi lại mã",
  sent="Đã gửi mã tới {e}. Mở email và nhập mã (hiệu lực 10 phút).",
  noacct="Email này chưa có tài khoản. Tài khoản được tạo trong app Karaoke AI Home khi điện thoại kết nối với loa. Mở app → Tài khoản để tạo.",
  e_email="Email chưa đúng.", e_wait="Vừa gửi mã rồi, chờ 1 phút rồi gửi lại nhé.", e_limit="Đã gửi quá nhiều mã hôm nay, mai thử lại nhé.",
  e_expired="Mã đã hết hạn, bấm Gửi lại mã.", e_tries="Nhập sai quá nhiều lần, bấm Gửi lại mã.", e_wrong="Mã chưa đúng (còn {n} lần).", e_net="Không kết nối được máy chủ, thử lại sau nhé.",
  hi="Xin chào", acct="Tài khoản", name="Tên hiển thị", save="Lưu", saved="Đã lưu", e_name="Tên cần ít nhất 2 chữ và không có từ ngữ xấu.",
  warranty="Bảo hành loa", wcode="Mã bảo hành", wend="Hết hạn", nowarranty="Chưa gắn với loa.",
  avatar="Ảnh đại diện", pick="Chọn ảnh", rmav="Bỏ ảnh",
  songs="Bài hát của tôi trên Sàn hát", empty="Bạn chưa đăng bài nào. Hát trong Phòng thu của app rồi bấm Đăng lên Sàn hát.",
  play="▶ Nghe", stop="■ Dừng", dele="Xoá", delq="Xoá vĩnh viễn bài này khỏi Sàn hát?", duet="hát đôi", hidden="Đang tạm ẩn chờ duyệt",
  voice="Âm lượng giọng", logout="Đăng xuất", delacct="Xoá tài khoản",
  delacctq="Xoá vĩnh viễn tài khoản và mọi bài hát, bình luận, tim, hoa? Không thể khôi phục.", deleted="Tài khoản đã được xoá.",
  note="Chưa có tài khoản? Tài khoản chỉ tạo được trong app Karaoke AI Home sau khi kết nối với loa."),
 'en': dict(nav="Sign in", h="Sign in to your account", lead="Sign in to listen to and manage the songs you posted on the Singing Stage.",
  email="Email", send="Send sign‑in code", code="6‑digit code from the email", login="Sign in", other="Use another email", resend="Resend code",
  sent="We sent a code to {e}. Open the email and enter the code (valid for 10 minutes).",
  noacct="There is no account for this email. Accounts are created in the Karaoke AI Home app once your phone is connected to a speaker. Open the app → Account to create one.",
  e_email="Please check the email address.", e_wait="A code was just sent. Please wait a minute before resending.", e_limit="Too many codes today. Please try again tomorrow.",
  e_expired="The code has expired. Tap Resend code.", e_tries="Too many wrong attempts. Tap Resend code.", e_wrong="Wrong code ({n} tries left).", e_net="Can’t reach the server. Please try again later.",
  hi="Hello", acct="Account", name="Display name", save="Save", saved="Saved", e_name="The name needs at least 2 characters and no bad words.",
  warranty="Speaker warranty", wcode="Warranty code", wend="Expires", nowarranty="Not linked to a speaker yet.",
  avatar="Profile photo", pick="Choose photo", rmav="Remove photo",
  songs="My songs on the Singing Stage", empty="You haven’t posted any songs yet. Sing in the app’s Recording Studio and tap Post to the Singing Stage.",
  play="▶ Play", stop="■ Stop", dele="Delete", delq="Permanently delete this song from the Singing Stage?", duet="duet", hidden="Hidden pending review",
  voice="Voice volume", logout="Sign out", delacct="Delete account",
  delacctq="Permanently delete your account and all songs, comments, hearts and flowers? This cannot be undone.", deleted="Your account has been deleted.",
  note="No account yet? Accounts can only be created in the Karaoke AI Home app after connecting to a speaker."),
 'ja': dict(nav="ログイン", h="アカウントにログイン", lead="ログインすると、歌のステージに投稿した歌を聴き直したり管理したりできます。",
  email="メールアドレス", send="ログインコードを送信", code="メールに届いた6桁のコード", login="ログイン", other="別のメールを使う", resend="コードを再送信",
  sent="{e} にコードを送信しました。メールを開いてコードを入力してください（有効期限10分）。",
  noacct="このメールアドレスのアカウントはありません。アカウントはスマホをスピーカーに接続したあと、Karaoke AI Home アプリで作成します。アプリ → アカウント から作成してください。",
  e_email="メールアドレスをご確認ください。", e_wait="コードを送信したばかりです。1分ほどお待ちください。", e_limit="本日の送信回数の上限に達しました。明日お試しください。",
  e_expired="コードの有効期限が切れました。「コードを再送信」を押してください。", e_tries="入力ミスが多すぎます。「コードを再送信」を押してください。", e_wrong="コードが違います（残り{n}回）。", e_net="サーバーに接続できません。しばらくしてからお試しください。",
  hi="こんにちは", acct="アカウント", name="表示名", save="保存", saved="保存しました", e_name="名前は2文字以上で、不適切な言葉は使えません。",
  warranty="スピーカー保証", wcode="保証コード", wend="保証期限", nowarranty="まだスピーカーと連携していません。",
  avatar="プロフィール画像", pick="画像を選ぶ", rmav="画像を削除",
  songs="歌のステージの自分の歌", empty="まだ投稿がありません。アプリのレコーディングスタジオで歌って「ステージに投稿」を押してください。",
  play="▶ 再生", stop="■ 停止", dele="削除", delq="この歌を歌のステージから完全に削除しますか？", duet="デュエット", hidden="審査のため一時非表示",
  voice="歌声の音量", logout="ログアウト", delacct="アカウントを削除",
  delacctq="アカウントとすべての歌、コメント、ハート、花を完全に削除しますか？元に戻せません。", deleted="アカウントを削除しました。",
  note="アカウントをお持ちでない方：アカウントはスピーカーに接続したあと、Karaoke AI Home アプリでのみ作成できます。"),
 'ko': dict(nav="로그인", h="계정 로그인", lead="로그인하면 노래 무대에 올린 노래를 다시 듣고 관리할 수 있습니다.",
  email="이메일", send="로그인 코드 보내기", code="이메일로 받은 6자리 코드", login="로그인", other="다른 이메일 사용", resend="코드 다시 보내기",
  sent="{e}(으)로 코드를 보냈습니다. 이메일을 열고 코드를 입력하세요(10분간 유효).",
  noacct="이 이메일로 된 계정이 없습니다. 계정은 휴대폰을 스피커에 연결한 뒤 Karaoke AI Home 앱에서 만듭니다. 앱 → 계정에서 만들어 주세요.",
  e_email="이메일 주소를 확인해 주세요.", e_wait="방금 코드를 보냈습니다. 1분 뒤에 다시 보내 주세요.", e_limit="오늘 보낼 수 있는 코드 수를 넘었습니다. 내일 다시 시도해 주세요.",
  e_expired="코드가 만료되었습니다. 코드 다시 보내기를 누르세요.", e_tries="잘못 입력한 횟수가 너무 많습니다. 코드 다시 보내기를 누르세요.", e_wrong="코드가 틀렸습니다({n}번 남음).", e_net="서버에 연결할 수 없습니다. 잠시 후 다시 시도해 주세요.",
  hi="안녕하세요", acct="계정", name="표시 이름", save="저장", saved="저장했습니다", e_name="이름은 2자 이상이어야 하며 나쁜 말은 쓸 수 없습니다.",
  warranty="스피커 보증", wcode="보증 코드", wend="만료일", nowarranty="아직 스피커와 연결되지 않았습니다.",
  avatar="프로필 사진", pick="사진 선택", rmav="사진 삭제",
  songs="노래 무대의 내 노래", empty="아직 올린 노래가 없습니다. 앱의 녹음실에서 노래한 뒤 무대에 올리기를 누르세요.",
  play="▶ 재생", stop="■ 정지", dele="삭제", delq="이 노래를 노래 무대에서 영구 삭제할까요?", duet="듀엣", hidden="검토를 위해 숨김",
  voice="목소리 볼륨", logout="로그아웃", delacct="계정 삭제",
  delacctq="계정과 모든 노래, 댓글, 하트, 꽃을 영구 삭제할까요? 되돌릴 수 없습니다.", deleted="계정이 삭제되었습니다.",
  note="계정이 없으신가요? 계정은 스피커에 연결한 뒤 Karaoke AI Home 앱에서만 만들 수 있습니다."),
 'fr': dict(nav="Connexion", h="Connexion à votre compte", lead="Connectez‑vous pour réécouter et gérer les chansons publiées sur la Scène karaoké.",
  email="E‑mail", send="Recevoir un code de connexion", code="Code à 6 chiffres reçu par e‑mail", login="Se connecter", other="Utiliser un autre e‑mail", resend="Renvoyer le code",
  sent="Un code a été envoyé à {e}. Ouvrez l’e‑mail et saisissez le code (valable 10 minutes).",
  noacct="Aucun compte pour cet e‑mail. Les comptes se créent dans l’application Karaoke AI Home une fois le téléphone connecté à une enceinte. Ouvrez l’application → Compte.",
  e_email="Vérifiez l’adresse e‑mail.", e_wait="Un code vient d’être envoyé. Patientez une minute avant de renvoyer.", e_limit="Trop de codes aujourd’hui. Réessayez demain.",
  e_expired="Le code a expiré. Touchez Renvoyer le code.", e_tries="Trop d’essais erronés. Touchez Renvoyer le code.", e_wrong="Code incorrect ({n} essais restants).", e_net="Serveur injoignable. Réessayez plus tard.",
  hi="Bonjour", acct="Compte", name="Nom affiché", save="Enregistrer", saved="Enregistré", e_name="Le nom doit comporter au moins 2 caractères, sans grossièretés.",
  warranty="Garantie de l’enceinte", wcode="Code de garantie", wend="Fin de garantie", nowarranty="Pas encore lié à une enceinte.",
  avatar="Photo de profil", pick="Choisir une photo", rmav="Retirer la photo",
  songs="Mes chansons sur la Scène", empty="Vous n’avez encore rien publié. Chantez dans le Studio de l’application puis touchez Publier sur la Scène.",
  play="▶ Écouter", stop="■ Arrêter", dele="Supprimer", delq="Supprimer définitivement cette chanson de la Scène ?", duet="duo", hidden="Masquée en attente d’examen",
  voice="Volume de la voix", logout="Se déconnecter", delacct="Supprimer le compte",
  delacctq="Supprimer définitivement le compte et toutes vos chansons, commentaires, cœurs et fleurs ? Action irréversible.", deleted="Votre compte a été supprimé.",
  note="Pas encore de compte ? Les comptes se créent uniquement dans l’application Karaoke AI Home après connexion à une enceinte."),
 'zh': dict(nav="登录", h="登录账户", lead="登录后可以重听和管理你发布到歌唱舞台的歌曲。",
  email="邮箱", send="发送登录验证码", code="邮件中的 6 位验证码", login="登录", other="换个邮箱", resend="重新发送",
  sent="验证码已发送到 {e}。请打开邮件并输入验证码（10 分钟内有效）。",
  noacct="该邮箱还没有账户。账户需在手机连接音箱后，在 Karaoke AI Home 应用中创建。请打开应用 → 账户 进行创建。",
  e_email="请检查邮箱地址。", e_wait="刚刚已发送验证码，请 1 分钟后再试。", e_limit="今天发送次数过多，请明天再试。",
  e_expired="验证码已过期，请点击重新发送。", e_tries="输错次数过多，请点击重新发送。", e_wrong="验证码错误（还剩 {n} 次）。", e_net="无法连接服务器，请稍后再试。",
  hi="你好", acct="账户", name="显示名称", save="保存", saved="已保存", e_name="名称至少 2 个字，且不能含不文明用语。",
  warranty="音箱保修", wcode="保修码", wend="到期", nowarranty="尚未绑定音箱。",
  avatar="头像", pick="选择图片", rmav="移除头像",
  songs="我在歌唱舞台的歌曲", empty="你还没有发布歌曲。在应用的录音棚演唱后点击发布到歌唱舞台。",
  play="▶ 播放", stop="■ 停止", dele="删除", delq="确定从歌唱舞台永久删除这首歌？", duet="合唱", hidden="待审核，暂时隐藏",
  voice="人声音量", logout="退出登录", delacct="删除账户",
  delacctq="确定永久删除账户及所有歌曲、评论、爱心和鲜花？此操作无法恢复。", deleted="账户已删除。",
  note="还没有账户？账户只能在连接音箱后，在 Karaoke AI Home 应用中创建。"),
}

# Nút vào Sàn hát / Phòng thu: mở app web (app.karaokeaihome.com) đã đăng nhập sẵn tài khoản
GO = {
 'vi': dict(go_h="Hát & nghe ngay trên web", go_san="Vào Sàn hát", go_stu="Vào Phòng thu", go_note="Mở bản web của app Karaoke AI Home, đã đăng nhập sẵn tài khoản của bạn. Thu âm cần cho phép dùng micro; dùng tai nghe để bản thu sạch hơn."),
 'en': dict(go_h="Sing & listen right on the web", go_san="Open Singing Stage", go_stu="Open Recording Studio", go_note="Opens the web version of the Karaoke AI Home app, already signed in to your account. Recording needs microphone permission; use headphones for a cleaner take."),
 'ja': dict(go_h="Webでそのまま歌う・聴く", go_san="歌のステージへ", go_stu="レコーディングスタジオへ", go_note="Karaoke AI Home アプリのWeb版を、ログインした状態で開きます。録音にはマイクの許可が必要です。ヘッドホンを使うとよりきれいに録れます。"),
 'ko': dict(go_h="웹에서 바로 노래하고 듣기", go_san="노래 무대 열기", go_stu="녹음 스튜디오 열기", go_note="Karaoke AI Home 앱의 웹 버전을 로그인된 상태로 엽니다. 녹음하려면 마이크 권한이 필요하며, 헤드폰을 쓰면 더 깨끗하게 녹음됩니다."),
 'fr': dict(go_h="Chanter et écouter directement sur le web", go_san="Ouvrir la Scène", go_stu="Ouvrir le Studio", go_note="Ouvre la version web de l’app Karaoke AI Home, déjà connectée à votre compte. L’enregistrement demande l’accès au micro ; utilisez un casque pour un son plus propre."),
 'zh': dict(go_h="在网页上直接唱歌和收听", go_san="进入歌唱舞台", go_stu="进入录音室", go_note="打开 Karaoke AI Home 应用的网页版，已自动登录你的账号。录音需要允许使用麦克风；戴耳机录音效果更干净。"),
}
for _l in T: T[_l].update(GO[_l])
for _l,_v in {'vi': {'vip': 'Nâng cấp VIP', 'vip_h': 'Gói VIP', 'vip_sub': 'Gói nâng cao', 'vip_on': 'Bạn đang dùng gói VIP.', 'vip_free': 'Năm đầu bạn đang được dùng miễn phí các quyền lợi VIP. Nâng cấp để giữ tiếp sau năm đầu.', 'vip_ben': 'Quyền lợi', 'b1': 'Phòng thu đầy đủ', 'b1n': 'thu âm với hiệu ứng giọng, nhạc nền, lưu bản thu không giới hạn', 'b2': 'Sàn hát không giới hạn', 'b2n': 'đăng bài, hát đôi, nhận hoa và bình luận, lên Top tuần', 'b3': 'Dùng chung cả nhà', 'b3n': 'gói tính theo loa: mọi điện thoại đã kết nối với loa đều được VIP', 'b4': 'Huy hiệu vương miện', 'b4n': 'hiện cạnh tên bạn ở Tài khoản và trên Sàn hát', 'py': 'mỗi năm', 'pm': 'mỗi tháng', 'vip_soon': 'Sắp mở bán. Hiện bạn vẫn dùng VIP miễn phí năm đầu.', 'p1': '199.000đ', 'p2': '29.000đ'}, 'en': {'vip': 'Upgrade to VIP', 'vip_h': 'VIP plan', 'vip_sub': 'Advanced plan', 'vip_on': 'You are on the VIP plan.', 'vip_free': 'You enjoy all VIP benefits free for the first year. Upgrade to keep them after that.', 'vip_ben': 'Benefits', 'b1': 'Full Recording Studio', 'b1n': 'record with voice effects and backing tracks, keep unlimited recordings', 'b2': 'Unlimited Singing Stage', 'b2n': 'post songs, sing duets, receive flowers and comments, reach the weekly Top', 'b3': 'Shared by the whole family', 'b3n': 'the plan follows the speaker: every phone connected to it gets VIP', 'b4': 'Crown badge', 'b4n': 'shown next to your name in Account and on the Singing Stage', 'py': 'per year', 'pm': 'per month', 'vip_soon': 'Coming soon. You still have free VIP for your first year.', 'p1': '$7.99', 'p2': '$1.49'}, 'ja': {'vip': 'VIPにアップグレード', 'vip_h': 'VIPプラン', 'vip_sub': 'アドバンスプラン', 'vip_on': 'VIPプランをご利用中です。', 'vip_free': '1年目はVIP特典を無料でご利用いただけます。2年目以降も続けるにはアップグレードしてください。', 'vip_ben': '特典', 'b1': 'フル機能のレコーディングスタジオ', 'b1n': '声のエフェクトや伴奏付きで録音、録音は無制限に保存', 'b2': '歌のステージ無制限', 'b2n': '投稿、デュエット、花やコメント、週間トップ入り', 'b3': '家族みんなで共有', 'b3n': 'プランはスピーカー単位：接続したすべてのスマホがVIPに', 'b4': '王冠バッジ', 'b4n': 'アカウントと歌のステージで名前の横に表示', 'py': '年額', 'pm': '月額', 'vip_soon': 'まもなく販売開始。1年目は引き続き無料でVIPをご利用いただけます。', 'p1': '¥1,200', 'p2': '¥200'}, 'ko': {'vip': 'VIP 업그레이드', 'vip_h': 'VIP 플랜', 'vip_sub': '고급 플랜', 'vip_on': 'VIP 플랜을 이용 중입니다.', 'vip_free': '첫해에는 VIP 혜택을 무료로 이용합니다. 이후에도 유지하려면 업그레이드하세요.', 'vip_ben': '혜택', 'b1': '전체 녹음 스튜디오', 'b1n': '음성 효과와 반주로 녹음, 녹음 무제한 저장', 'b2': '노래 무대 무제한', 'b2n': '게시, 듀엣, 꽃과 댓글 받기, 주간 톱 진입', 'b3': '온 가족이 함께', 'b3n': '플랜은 스피커 단위: 연결된 모든 휴대폰이 VIP', 'b4': '왕관 배지', 'b4n': '계정과 노래 무대에서 이름 옆에 표시', 'py': '연간', 'pm': '월간', 'vip_soon': '곧 판매를 시작합니다. 첫해에는 계속 무료로 VIP를 이용할 수 있습니다.', 'p1': '₩9,900', 'p2': '₩1,500'}, 'fr': {'vip': 'Passer VIP', 'vip_h': 'Offre VIP', 'vip_sub': 'Offre avancée', 'vip_on': 'Vous avez l’offre VIP.', 'vip_free': 'Vous profitez gratuitement des avantages VIP la première année. Passez VIP pour les garder ensuite.', 'vip_ben': 'Avantages', 'b1': 'Studio complet', 'b1n': 'enregistrez avec effets de voix et accompagnements, enregistrements illimités', 'b2': 'Scène illimitée', 'b2n': 'publiez, chantez en duo, recevez fleurs et commentaires, entrez dans le Top de la semaine', 'b3': 'Partagé en famille', 'b3n': 'l’offre suit l’enceinte : chaque téléphone connecté devient VIP', 'b4': 'Badge couronne', 'b4n': 'affiché à côté de votre nom dans le compte et sur la Scène', 'py': 'par an', 'pm': 'par mois', 'vip_soon': 'Bientôt disponible. Vous gardez le VIP gratuit la première année.', 'p1': '6,99 €', 'p2': '1,29 €'}, 'zh': {'vip': '升级 VIP', 'vip_h': 'VIP 套餐', 'vip_sub': '高级套餐', 'vip_on': '你正在使用 VIP 套餐。', 'vip_free': '第一年你可免费享受 VIP 权益。升级后第一年之后也能继续使用。', 'vip_ben': '权益', 'b1': '完整录音室', 'b1n': '带人声效果和伴奏录音，录音无限保存', 'b2': '歌唱舞台无限制', 'b2n': '发布歌曲、合唱、收花和评论、登上每周排行', 'b3': '全家共享', 'b3n': '套餐按音箱计算：连接该音箱的所有手机都是 VIP', 'b4': '皇冠徽章', 'b4n': '显示在账户和歌唱舞台的名字旁边', 'py': '每年', 'pm': '每月', 'vip_soon': '即将开售。第一年你仍可免费使用 VIP。', 'p1': '¥58', 'p2': '¥9'}}.items(): T[_l].update(_v)
for _l,(_a,_b,_c,_d) in {'vi': ('Gửi mã xác nhận về email', 'Xoá vĩnh viễn', 'Không xoá nữa', 'Đã gửi mã tới email của bạn. Nhập mã để xác nhận xoá.'), 'en': ('Email me a confirmation code', 'Delete permanently', 'Cancel', 'We sent a code to your email. Enter it to confirm deletion.'), 'ja': ('確認コードをメールで送る', '完全に削除', 'やめる', 'メールにコードを送りました。削除を確定するにはコードを入力してください。'), 'ko': ('확인 코드를 이메일로 받기', '영구 삭제', '취소', '이메일로 코드를 보냈습니다. 삭제를 확인하려면 코드를 입력하세요.'), 'fr': ('Recevoir un code de confirmation par e-mail', 'Supprimer définitivement', 'Annuler', 'Un code a été envoyé à votre e-mail. Saisissez-le pour confirmer la suppression.'), 'zh': ('发送确认码到邮箱', '永久删除', '取消', '确认码已发送到你的邮箱。输入确认码以确认删除。')}.items(): T[_l].update(del_send=_a,del_go=_b,del_no=_c,del_sent=_d)
for _l,_v in {'vi': {'tools': 'Loa và ứng dụng', 'upd': 'Cập nhật phần mềm loa', 'updn': 'Tải phần mềm máy tính, cập nhật loa qua Wi-Fi bằng một nút bấm', 'setup': 'Cài loa mới', 'setupn': 'Loa mới mua: hướng dẫn bằng hình và phần mềm cài qua Wi-Fi', 'guiden': 'Bắt đầu nhanh và hướng dẫn chi tiết từng tính năng', 'nt_h': 'Thông báo qua email', 'nt_n': 'Mặc định chỉ gửi thư bảo mật (mã xác minh, điện thoại lạ kết nối loa, xoá tài khoản). Bật thêm loại bạn muốn nhận:', 'k_san': 'Hoạt động Sàn hát (tóm tắt mỗi ngày)', 'k_top': 'Bài của bạn lọt Top tuần', 'k_upd': 'Loa có bản cập nhật mới', 'k_promo': 'Khuyến mãi, sản phẩm mới'}, 'en': {'tools': 'Speaker & app', 'upd': 'Update speaker software', 'updn': 'Download the computer app and update the speaker over Wi-Fi with one click', 'setup': 'Set up a new speaker', 'setupn': 'New speaker: picture guide and Wi-Fi installer', 'guiden': 'Quick start and step-by-step guides for every feature', 'nt_h': 'Email notifications', 'nt_n': 'By default we only send security emails (verification codes, an unknown phone connecting to your speaker, account deletion). Turn on anything else you want:', 'k_san': 'Singing Stage activity (daily summary)', 'k_top': 'Your song made the weekly Top', 'k_upd': 'New speaker update available', 'k_promo': 'Promotions and new products'}, 'ja': {'tools': 'スピーカーとアプリ', 'upd': 'スピーカーのソフト更新', 'updn': 'パソコン用ソフトをダウンロードし、Wi-Fi経由でワンクリック更新', 'setup': '新しいスピーカーの設定', 'setupn': '新品スピーカー：画像ガイドとWi-Fiインストーラー', 'guiden': 'クイックスタートと各機能の詳しいガイド', 'nt_h': 'メール通知', 'nt_n': '通常はセキュリティメール（確認コード、不明なスマホの接続、アカウント削除）のみ送信します。受け取りたい通知をオンにしてください：', 'k_san': '歌のステージの活動（毎日のまとめ）', 'k_top': 'あなたの曲が週間トップ入り', 'k_upd': 'スピーカーの新しい更新', 'k_promo': 'キャンペーン・新製品'}, 'ko': {'tools': '스피커 및 앱', 'upd': '스피커 소프트웨어 업데이트', 'updn': '컴퓨터 프로그램을 내려받아 Wi-Fi로 한 번에 업데이트', 'setup': '새 스피커 설치', 'setupn': '새 스피커: 그림 안내와 Wi-Fi 설치 프로그램', 'guiden': '빠른 시작과 기능별 자세한 안내', 'nt_h': '이메일 알림', 'nt_n': '기본적으로 보안 메일(인증 코드, 낯선 휴대폰의 스피커 연결, 계정 삭제)만 보냅니다. 받고 싶은 알림을 켜세요:', 'k_san': '노래 무대 활동(매일 요약)', 'k_top': '내 노래가 주간 톱에 진입', 'k_upd': '스피커 새 업데이트', 'k_promo': '프로모션 및 신제품'}, 'fr': {'tools': 'Enceinte et application', 'upd': 'Mettre à jour l’enceinte', 'updn': 'Téléchargez le logiciel pour ordinateur et mettez à jour l’enceinte en Wi-Fi en un clic', 'setup': 'Installer une nouvelle enceinte', 'setupn': 'Enceinte neuve : guide illustré et installateur Wi-Fi', 'guiden': 'Démarrage rapide et guides détaillés de chaque fonction', 'nt_h': 'Notifications par e-mail', 'nt_n': 'Par défaut, nous n’envoyons que les e-mails de sécurité (codes de vérification, téléphone inconnu connecté à l’enceinte, suppression du compte). Activez ce que vous souhaitez recevoir :', 'k_san': 'Activité de la Scène (résumé quotidien)', 'k_top': 'Votre chanson est dans le Top de la semaine', 'k_upd': 'Nouvelle mise à jour de l’enceinte', 'k_promo': 'Promotions et nouveaux produits'}, 'zh': {'tools': '音箱与应用', 'upd': '更新音箱软件', 'updn': '下载电脑软件，通过 Wi-Fi 一键更新音箱', 'setup': '安装新音箱', 'setupn': '新音箱：图文指南与 Wi-Fi 安装程序', 'guiden': '快速入门和各项功能的详细指南', 'nt_h': '邮件通知', 'nt_n': '默认只发送安全邮件（验证码、陌生手机连接音箱、删除账号）。打开你想接收的通知：', 'k_san': '歌唱舞台动态（每日摘要）', 'k_top': '你的歌进入每周排行', 'k_upd': '音箱有新更新', 'k_promo': '优惠与新产品'}}.items(): T[_l].update(_v)
for _l,(_a,_b,_c) in [(k,(v[0],v[1],v[2]+' '+{'vi': 'Mỗi loa có 5 lượt kết nối điện thoại miễn phí.', 'en': 'Each speaker includes 5 free phone connections.', 'ja': 'スピーカー1台につき無料のスマホ接続が5回あります。', 'ko': '스피커마다 무료 휴대폰 연결 5회가 제공됩니다.', 'fr': 'Chaque enceinte inclut 5 connexions de téléphone gratuites.', 'zh': '每台音箱有 5 次免费手机连接。'}[k])) for k,v in  {'vi': ('Kích hoạt loa', 'Hướng dẫn sử dụng', 'Kích hoạt: cho máy tính hoặc điện thoại chung Wi-Fi với loa, rồi nhập mã 4 số hiện trên TV.'), 'en': ('Activate speaker', 'User guide', 'To activate: put your computer or phone on the same Wi-Fi as the speaker, then enter the 4-digit code shown on the TV.'), 'ja': ('スピーカーを有効化', '使い方ガイド', '有効化：パソコンやスマホをスピーカーと同じWi-Fiにつなぎ、テレビに表示される4桁のコードを入力します。'), 'ko': ('스피커 활성화', '사용 설명서', '활성화: 컴퓨터나 휴대폰을 스피커와 같은 Wi-Fi에 연결한 뒤 TV에 표시된 4자리 코드를 입력하세요.'), 'fr': ('Activer l’enceinte', 'Guide d’utilisation', 'Activation : connectez votre ordinateur ou téléphone au même Wi-Fi que l’enceinte, puis saisissez le code à 4 chiffres affiché sur la TV.'), 'zh': ('激活音箱', '使用指南', '激活：让电脑或手机与音箱连接同一个 Wi-Fi，然后输入电视上显示的 4 位数代码。')}.items()]: T[_l].update(go_spk=_a,go_guide=_b,go_spkn=_c)
for _l,_v in {'vi': 'Tài khoản của tôi', 'en': 'My account', 'ja': 'マイアカウント', 'ko': '내 계정', 'fr': 'Mon compte', 'zh': '我的账号'}.items(): T[_l]['my']=_v
for _l,_v in {'vi': 'Đã có mã', 'en': 'I have a code', 'ja': 'コードを持っている', 'ko': '코드가 있어요', 'fr': 'J’ai déjà un code', 'zh': '我已有验证码'}.items(): T[_l]['have']=_v

CSS = """
.acc{max-width:760px;margin:0 auto;padding:16px}.acc .card{margin:14px 0}
.acc input{width:100%;box-sizing:border-box;padding:12px 14px;border-radius:12px;border:1px solid #333;background:#111;color:var(--fg);font-size:1.05rem;margin:6px 0 10px}
.acc button{cursor:pointer;border:0;border-radius:12px;padding:11px 16px;font-weight:700;font-size:1rem;background:var(--acc);color:#111}
.acc button.o{background:#222;color:var(--fg);border:1px solid #333}.acc button.r{background:#5a1d22;color:#fff}
.acc .row{display:flex;gap:8px;flex-wrap:wrap;align-items:center}.acc .msg{min-height:1.4em;color:var(--acc);margin:6px 0}.acc .err{color:#ff8a8a}
.acc .me{display:flex;gap:14px;align-items:center}.acc .av{width:64px;height:64px;border-radius:50%;background:#222 center/cover;flex:none;display:flex;align-items:center;justify-content:center;font-size:28px}
.acc .song{display:flex;gap:12px;align-items:center;padding:10px 0;border-top:1px solid #222}.acc .song img{width:112px;height:63px;object-fit:cover;border-radius:10px;flex:none}
.acc .song .t{flex:1;min-width:0}.acc .song .t b{display:block}.acc .song small{color:var(--mute);display:block}
.acc .player{position:sticky;top:0;z-index:5;background:#0b0b0c;padding:8px 0}.acc .player .v{position:relative;padding-top:56.25%;border-radius:12px;overflow:hidden;background:#000}.acc .player .v iframe,.acc .player .v>div{position:absolute;inset:0;width:100%;height:100%;border:0}
.acc .hide{display:none!important}.acc .mute{color:var(--mute)}
"""

CSS += """.acc a.li{display:flex;gap:14px;align-items:center;padding:12px 4px;border-top:1px solid #2a2a30;color:inherit;text-decoration:none}.acc a.li:first-of-type{border-top:0}.acc a.li i{font-style:normal;font-size:1.6rem;width:2rem;text-align:center}.acc a.li span{flex:1}.acc a.li b{display:block}.acc a.li small{color:var(--mute)}.acc a.li:hover b{color:var(--acc)}
.acc a.delx{color:#e06666;font-size:.85rem;text-decoration:underline;opacity:.8}.acc .vipb{display:inline-flex;align-items:center;gap:6px;margin-top:8px;background:linear-gradient(135deg,#f5d76e,#c99a1e);color:#3a2a00;border:0;border-radius:999px;padding:8px 14px;font-weight:800;cursor:pointer}.acc .vben{display:flex;gap:12px;align-items:center;padding:10px 0;border-top:1px solid #2a2a30}.acc .vben i{font-style:normal;font-size:1.5rem}.acc .vben b{display:block}.acc .vben small{color:var(--mute)}.acc .vpr{flex:1;text-align:center;background:#1c1c20;border:1px solid #333;border-radius:14px;padding:10px}.acc .vpr.on{border:2px solid #d4af37}.acc .vpr b{display:block;font-size:1.3rem}.acc .vpr small{color:var(--mute)}.acc .sw{display:flex;align-items:center;gap:12px;padding:10px 0;border-top:1px solid #2a2a30;cursor:pointer}.acc .sw span{flex:1}.acc .sw input{width:22px;height:22px;accent-color:var(--acc)}
"""

JS = r"""
(function(){var A='https://api.karaokeaihome.com',L=window.ACC_L,LG=window.ACC_LANG,$=function(i){return document.getElementById(i)};
var tok=null;try{tok=localStorage.getItem('kah_acct')}catch(e){}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return'&#'+c.charCodeAt(0)+';'})}
function msg(id,t,bad){var m=$(id);m.textContent=t||'';m.className='msg'+(bad?' err':'')}
function api(p,o){o=o||{};var h={};if(tok)h['X-Acct']=tok;if(o.json!==undefined){h['Content-Type']='application/json';o.body=JSON.stringify(o.json)}
  return fetch(A+p,{method:o.method||(o.body?'POST':'GET'),headers:h,body:o.body}).then(function(r){return r.json().catch(function(){return{}}).then(function(j){j._s=r.status;return j})})}
function errText(j){var c=j.code;if(j.noacct)return L.noacct;if(c==='email')return L.e_email;if(c==='wait')return L.e_wait;if(c==='limit')return L.e_limit;
  if(c==='expired')return L.e_expired;if(c==='tries')return L.e_tries;if(c==='wrong')return L.e_wrong.replace('{n}',j.left);return L.e_net}
var email='';
function hdr(n){var a=document.querySelector('nav a.nl');try{if(n)localStorage.setItem('kah_nm',n);else localStorage.removeItem('kah_nm')}catch(x){}if(a)a.textContent=tok?(n||L.my):L.nav;$('accH').textContent=tok?L.my:L.h;document.querySelector('.acc .lead').style.display=tok?'none':''}
function show(s){['stEmail','stCode','stIn'].forEach(function(x){$(x).classList.toggle('hide',x!==s)})}
$('bSend').onclick=$('bResend').onclick=function(){email=($('iEmail').value||'').trim().toLowerCase();if(!email)return msg('m1',L.e_email,1);
  msg('m1','…');msg('m2','');api('/w/acct/code',{json:{email:email,lang:LG}}).then(function(j){if(j.ok||j.code==='wait'){pend(email);toCode()}
  else{show('stEmail');msg('m1',errText(j),1)}}).catch(function(){msg('m1',L.e_net,1)})};
// Safari iPhone hay tải lại trang khi khách sang app Mail lấy mã → nhớ email đang chờ mã 10 phút
function pend(m){try{if(m)localStorage.setItem('kah_pend',JSON.stringify({e:m,t:Date.now()}));else localStorage.removeItem('kah_pend')}catch(x){}}
function pending(){try{var o=JSON.parse(localStorage.getItem('kah_pend')||'null');if(o&&Date.now()-o.t<600000)return o.e}catch(x){}return ''}
function toCode(){show('stCode');msg('m2',L.sent.replace('{e}',email));try{$('iCode').focus()}catch(x){}}
$('bHave').onclick=function(){email=($('iEmail').value||'').trim().toLowerCase()||pending();if(!email)return msg('m1',L.e_email,1);msg('m1','');toCode()};
$('bOther').onclick=function(){pend('');show('stEmail');msg('m1','')};
$('bLogin').onclick=function(){api('/w/acct/verify',{json:{email:email,code:($('iCode').value||'').trim()}}).then(function(j){if(j.acct){pend('');tok=j.acct;try{localStorage.setItem('kah_acct',tok)}catch(e){}load()}else msg('m2',errText(j),1)}).catch(function(){msg('m2',L.e_net,1)})};
$('iCode').onkeydown=function(e){if(e.key==='Enter')$('bLogin').click()};$('iEmail').onkeydown=function(e){if(e.key==='Enter')$('bSend').click()};
function logout(){tok=null;try{localStorage.removeItem('kah_acct')}catch(e){}hdr('');stopPlay();show('stEmail')}
$('bOut').onclick=logout;
function fmt(t){var d=new Date(t);return d.toLocaleDateString(LG==='vi'?'vi-VN':LG)}
var me=null;
function load(){api('/w/acct/me').then(function(a){if(a._s===401){logout();return}me=a;show('stIn');vipDraw(a);notifs(a.notif);hdr(a.name||a.email.split('@')[0]);$('uName').textContent=a.name||a.email;$('uMail').textContent=a.email;$('iName').value=a.name||'';
  if(a.warranty&&a.warranty.start){$('uW').innerHTML=esc(L.wcode)+': <b>'+esc(a.warranty.code)+'</b><br>'+esc(L.wend)+': <b>'+fmt(a.warranty.start+365*864e5)+'</b>'}else $('uW').textContent=L.nowarranty;
  api('/w/san/me').then(function(s){setAv(s.uid,s.av);if(!a.name&&s.name)$('iName').value=s.name});songs()}).catch(function(){msg('m1',L.e_net,1)})}
function setAv(uid,av){var e=$('uAv');if(av){e.style.backgroundImage='url('+A+'/w/san/av?u='+encodeURIComponent(uid)+'&v='+av+')';e.textContent=''}else{e.style.backgroundImage='';e.textContent='🙂'}}
$('bName').onclick=function(){var n=$('iName').value;api('/w/acct/name',{json:{name:n}}).then(function(j){if(!j.ok)return msg('m3',L.e_name,1);
  api('/w/san/me',{json:{name:n}}).then(function(){msg('m3',L.saved);$('uName').textContent=j.name;hdr(j.name)})})};
$('fAv').onchange=function(){var f=this.files[0];if(!f)return;var img=new Image();img.onload=function(){var c=document.createElement('canvas'),s=256,w=img.width,h=img.height,m=Math.min(w,h);c.width=c.height=s;
  c.getContext('2d').drawImage(img,(w-m)/2,(h-m)/2,m,m,0,0,s,s);c.toBlob(function(b){api('/w/san/avatar',{body:b}).then(function(j){if(j.ok)api('/w/san/me').then(function(s){setAv(s.uid,s.av)});else msg('m3',j.error||L.e_net,1)})},'image/jpeg',0.82)};img.src=URL.createObjectURL(f)};
$('bRmAv').onclick=function(){api('/w/san/avatar',{body:new Blob([])}).then(function(){setAv('',0)})};
$('bDel').onclick=function(e){e.preventDefault();$('delBox').classList.toggle('hide');$('delBox').scrollIntoView({behavior:'smooth',block:'center'})};
$('bDelNo').onclick=function(){$('delBox').classList.add('hide');$('delStep').classList.add('hide');msg('m5','')};
$('bDelCode').onclick=function(){msg('m5','…');api('/w/acct/delcode',{json:{lang:LG}}).then(function(j){if(j.ok||j.code==='wait'){$('delStep').classList.remove('hide');msg('m5',L.del_sent);$('iDelCode').focus()}else msg('m5',errText(j),1)}).catch(function(){msg('m5',L.e_net,1)})};
$('bDelGo').onclick=function(){var c=($('iDelCode').value||'').trim();if(c.length!==6)return msg('m5',L.e_wrong.replace('{n}','5'),1);
  api('/w/acct/delete',{json:{code:c}}).then(function(j){if(j.deleted){$('delBox').classList.add('hide');logout();msg('m1',L.deleted)}else msg('m5',j.code==='need'?L.del_sent:errText(j),1)}).catch(function(){msg('m5',L.e_net,1)})};
function songs(){api('/w/san/list?tab=mine').then(function(j){var it=j.items||[];$('songs').innerHTML=it.length?it.map(function(p){
  return '<div class="song"><img src="https://i.ytimg.com/vi/'+esc(p.vid)+'/mqdefault.jpg" alt=""><div class="t"><b>'+esc(p.title)+(p.parent?' · 👫 '+esc(L.duet):'')+'</b>'+
  '<small>'+fmt(p.at)+' · ❤️ '+p.likes+' · 🌹 '+p.flowers+' · 💬 '+p.cmts+' · ▶ '+p.plays+'</small>'+(p.hidden?'<small class="err">'+esc(L.hidden)+'</small>':'')+
  '<div class="row" style="margin-top:6px"><button data-p="'+esc(p.id)+'">'+esc(L.play)+'</button><button class="o" data-d="'+esc(p.id)+'">'+esc(L.dele)+'</button></div></div></div>'}).join(''):'<p class="mute">'+esc(L.empty)+'</p>';
  window._songs={};it.forEach(function(p){window._songs[p.id]=p})})}
$('songs').onclick=function(e){var b=e.target.closest('button');if(!b)return;if(b.dataset.p)playSong(window._songs[b.dataset.p]);
  if(b.dataset.d&&confirm(L.delq))api('/w/san/del',{json:{id:b.dataset.d}}).then(function(){if(cur&&cur.id===b.dataset.d)stopPlay();songs()})};
// ---- phát: video karaoke YouTube + giọng hát khớp theo d (giây trong bản thu = giờ video + d) ----
var yt=null,ytReady=false,cur=null,tracks=[],timer=0;
function ytLoad(cb){if(ytReady)return cb();window.onYouTubeIframeAPIReady=function(){ytReady=true;cb()};var s=document.createElement('script');s.src='https://www.youtube.com/iframe_api';document.head.appendChild(s)}
function stopPlay(){clearInterval(timer);tracks.forEach(function(t){t.a.pause()});tracks=[];if(yt&&yt.stopVideo)try{yt.stopVideo()}catch(e){}$('player').classList.add('hide');cur=null}
$('bStop').onclick=stopPlay;$('vol').oninput=function(){tracks.forEach(function(t){t.a.volume=$('vol').value/100})};
function playSong(p){stopPlay();cur=p;$('player').classList.remove('hide');$('pTitle').textContent=p.title;
  tracks=[{a:new Audio(A+'/w/san/a?id='+encodeURIComponent(p.id)),d:p.d||0}];
  if(p.parent&&p.pok)tracks.push({a:new Audio(A+'/w/san/a?id='+encodeURIComponent(p.parent)),d:p.pd||0});
  tracks.forEach(function(t){t.a.preload='auto';t.a.volume=$('vol').value/100});
  api('/w/san/play',{json:{id:p.id}});
  ytLoad(function(){if(yt){yt.loadVideoById(p.vid);return}yt=new YT.Player('yt',{videoId:p.vid,playerVars:{playsinline:1,rel:0,autoplay:1},events:{onReady:function(){yt.playVideo()}}})});
  clearInterval(timer);timer=setInterval(sync,300)}
function sync(){if(!yt||!yt.getPlayerState)return;var st=yt.getPlayerState(),vt=yt.getCurrentTime();
  tracks.forEach(function(t){var tgt=vt+t.d;if(st!==1||tgt<0||(t.a.duration&&tgt>t.a.duration)){if(!t.a.paused)t.a.pause();return}
    if(Math.abs(t.a.currentTime-tgt)>0.3)t.a.currentTime=tgt;if(t.a.paused)t.a.play().catch(function(){})})}
function badge(t,sz){var P={free:['#2ecc71','#14873f'],basic:['#d9dee5','#8a929c'],adv:['#f5d76e','#b8860b'],exp:['#8d8d93','#55555a']},p=P[t]||P.free,g='pg'+t+sz;
  var inner=t==='adv'?'<path d="M7 15.5 6 9l3.3 2.6L12 7l2.7 4.6L18 9l-1 6.5z" fill="#fff8d6" stroke="#8a6508" stroke-width=".8"/>':t==='basic'?'<path d="M12 6.5l1.6 3.3 3.6.5-2.6 2.5.6 3.6-3.2-1.7-3.2 1.7.6-3.6-2.6-2.5 3.6-.5z" fill="#fff" stroke="#6b7280" stroke-width=".7"/>':t==='exp'?'<path d="M9 9l6 6M15 9l-6 6" stroke="#eee" stroke-width="2" stroke-linecap="round"/>':'<path d="M8 12.2l2.7 2.7L16.3 9" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>';
  return '<svg viewBox="0 0 24 24" width="'+sz+'" height="'+sz+'" style="vertical-align:-3px"><defs><linearGradient id="'+g+'" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="'+p[0]+'"/><stop offset="1" stop-color="'+p[1]+'"/></linearGradient></defs><path d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5z" fill="url(#'+g+')" stroke="'+p[1]+'" stroke-width="1.2"/>'+inner+'</svg>'}
function plan(m){var pl=m&&m.plan;if(pl&&pl.tier)return pl;var w=m&&m.warranty;if(w&&w.start){var u=w.start+365*864e5;return {tier:Date.now()>u?'exp':'free',until:u}}return {tier:'free',until:0}}
function vipDraw(m){var t=plan(m).tier;$('vipIc').innerHTML=badge('adv',18);$('vipBig').innerHTML=badge('adv',64);$('uBadge').innerHTML=badge(t,24);
  $('vipState').textContent=t==='adv'?L.vip_on:t==='free'?L.vip_free:'';$('bVip').classList.toggle('hide',t==='adv')}
$('bVip').onclick=function(){$('vipBox').classList.toggle('hide')};$('bVipBuy').onclick=function(){msg('m6',L.vip_soon)};
function goApp(w){if(!tok||!me)return;window.open('https://app.karaokeaihome.com/app/#acct='+encodeURIComponent(tok)+'&em='+encodeURIComponent(me.email||'')+'&nm='+encodeURIComponent(me.name||'')+'&go='+w+'&lang='+LG,'_blank')}
$('bGoSan').onclick=function(){goApp('san')};$('bGoStu').onclick=function(){goApp('stu')};$('bGoGuide').onclick=function(e){e.preventDefault();goApp('guide')};
function notifs(n){n=n||{};$('notifs').innerHTML=['san','top','upd','promo'].map(function(k){return '<label class="sw"><span>'+esc(L['k_'+k])+'</span><input type="checkbox" data-k="'+k+'"'+(n[k]?' checked':'')+'></label>'}).join('')}
$('notifs').onchange=function(){var n={};[].forEach.call($('notifs').querySelectorAll('input'),function(i){n[i.dataset.k]=i.checked?1:0});api('/w/acct/notif',{json:{notif:n}}).then(function(j){msg('m4',j.ok?L.saved:L.e_net,!j.ok)})};
if(tok)load();else if(pending()){email=pending();$('iEmail').value=email;toCode()}else show('stEmail');
})();
"""

def page(l, e):
    t = T[l]
    import json
    t['cai'] = ('/' if l=='vi' else '/%s/'%l)+'cai-loa/'
    return ('<div class="acc"><h1 id="accH">%s</h1><p class="lead">%s</p>'
     '<div id="stEmail" class="card"><label>%s</label><input id="iEmail" type="email" autocomplete="email" inputmode="email"><button id="bSend">%s</button><button class="o" id="bHave" style="margin-left:8px">%s</button><div id="m1" class="msg"></div><p class="mute" style="font-size:.9rem">%s</p></div>'
     '<div id="stCode" class="card hide"><div id="m2" class="msg"></div><label>%s</label><input id="iCode" inputmode="numeric" autocomplete="one-time-code" maxlength="6"><div class="row"><button id="bLogin">%s</button><button class="o" id="bResend">%s</button><button class="o" id="bOther">%s</button></div></div>'
     '<div id="stIn" class="hide"><div class="card"><div class="me"><span style="position:relative;flex:none"><div class="av" id="uAv">🙂</div><span id="uBadge" style="position:absolute;right:-4px;bottom:-4px;background:#17171a;border-radius:50%%;padding:2px;display:flex"></span></span><div><div class="mute">%s</div><b id="uName" style="font-size:1.3rem"></b><div class="mute" id="uMail"></div><button id="bVip" class="vipb"><span id="vipIc"></span> %s</button></div></div>'
     '<div id="vipBox" class="hide" style="margin-top:14px;border-top:1px solid #2a2a30;padding-top:14px"><div style="text-align:center"><span id="vipBig"></span><div class="mute">%s</div></div><p id="vipState" style="text-align:center"></p><h3>%s</h3>'
     '<div class="vben"><i>🎛️</i><span><b>%s</b><small>%s</small></span></div><div class="vben"><i>🪩</i><span><b>%s</b><small>%s</small></span></div><div class="vben"><i>🏡</i><span><b>%s</b><small>%s</small></span></div><div class="vben"><i>🎖️</i><span><b>%s</b><small>%s</small></span></div>'
     '<div class="row" style="margin:14px 0"><div class="vpr on"><b>%s</b><small>%s</small></div><div class="vpr"><b>%s</b><small>%s</small></div></div><button id="bVipBuy" class="vipb" style="width:100%%;justify-content:center">%s</button><div id="m6" class="msg"></div></div></div>'
     '<div class="card"><h2 style="margin-top:0">%s</h2><div class="row"><button id="bGoSan">🎪 %s</button><button id="bGoStu">🎙️ %s</button></div><p class="mute" style="font-size:.9rem;margin-bottom:0">%s</p></div>'
     '<div class="card"><h2 style="margin-top:0">%s</h2>'
     '<a class="li" href="%s"><i>🔄</i><span><b>%s</b><small>%s</small></span></a>'
     '<a class="li" href="%s"><i>🧰</i><span><b>%s</b><small>%s</small></span></a>'
     '<a class="li" id="bGoGuide" href="#"><i>📘</i><span><b>%s</b><small>%s</small></span></a></div>'
     '<div class="card"><h2 style="margin-top:0">📬 %s</h2><p class="mute" style="font-size:.9rem">%s</p><div id="notifs"></div><div id="m4" class="msg"></div></div>'
     '<div class="card"><h2 style="margin-top:0">%s</h2><div id="player" class="player hide"><b id="pTitle"></b><div class="v"><div id="yt"></div></div><div class="row" style="margin-top:8px"><label class="mute">%s</label><input id="vol" type="range" min="0" max="100" value="90" style="flex:1;margin:0"><button class="o" id="bStop">%s</button></div></div><div id="songs"></div></div>'
     '<div class="card"><h2 style="margin-top:0">%s</h2><label>%s</label><div class="row"><input id="iName" maxlength="30" style="flex:1;margin:0"><button id="bName">%s</button></div>'
     '<p style="margin:14px 0 6px">%s</p><div class="row"><label class="o" style="display:inline-block;padding:11px 16px;border-radius:12px;background:#222;border:1px solid #333;cursor:pointer;font-weight:700">%s<input id="fAv" type="file" accept="image/*" class="hide"></label><button class="o" id="bRmAv">%s</button></div><div id="m3" class="msg"></div>'
     '<p style="margin:14px 0 6px">%s</p><p id="uW" class="mute"></p>'
     '<div class="row" style="margin-top:16px"><button class="o" id="bOut">%s</button></div></div>'
     '<div style="margin:56px 0 8px;text-align:center"><a href="#" id="bDel" class="delx">%s</a></div>'
     '<div id="delBox" class="card hide" style="border:1px solid #6b2a2a"><p>%s</p><button class="r" id="bDelCode">%s</button><div id="delStep" class="hide"><label>%s</label><input id="iDelCode" inputmode="numeric" autocomplete="one-time-code" maxlength="6"><div class="row"><button class="r" id="bDelGo">%s</button><button class="o" id="bDelNo">%s</button></div></div><div id="m5" class="msg"></div></div></div></div>'
     '<script>window.ACC_L=%s;window.ACC_LANG=%s;</script><script src="/account.js"></script>') % (
        e(t['h']), e(t['lead']), e(t['email']), e(t['send']), e(t['have']), e(t['note']), e(t['code']), e(t['login']), e(t['resend']), e(t['other']),
        e(t['hi']), e(t['vip']), e(t['vip_sub']), e(t['vip_ben']), e(t['b1']), e(t['b1n']), e(t['b2']), e(t['b2n']), e(t['b3']), e(t['b3n']), e(t['b4']), e(t['b4n']), e(t['p1']), e(t['py']), e(t['p2']), e(t['pm']), e(t['vip']), e(t['go_h']), e(t['go_san']), e(t['go_stu']), e(t['go_note']), e(t['tools']), t['cai'], e(t['upd']), e(t['updn']), t['cai'], e(t['setup']), e(t['setupn']), e(t['go_guide']), e(t['guiden']), e(t['nt_h']), e(t['nt_n']), e(t['songs']), e(t['voice']), e(t['stop']), e(t['acct']), e(t['name']), e(t['save']), e(t['avatar']), e(t['pick']), e(t['rmav']),
        e(t['warranty']), e(t['logout']), e(t['delacct']), e(t['delacctq']), e(t['del_send']), e(t['code']), e(t['del_go']), e(t['del_no']), json.dumps(t, ensure_ascii=False).replace('</', '<\\/'), json.dumps(l))
