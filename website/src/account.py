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
function load(){api('/w/acct/me').then(function(a){if(a._s===401){logout();return}me=a;show('stIn');hdr(a.name||a.email.split('@')[0]);$('uName').textContent=a.name||a.email;$('uMail').textContent=a.email;$('iName').value=a.name||'';
  if(a.warranty&&a.warranty.start){$('uW').innerHTML=esc(L.wcode)+': <b>'+esc(a.warranty.code)+'</b><br>'+esc(L.wend)+': <b>'+fmt(a.warranty.start+365*864e5)+'</b>'}else $('uW').textContent=L.nowarranty;
  api('/w/san/me').then(function(s){setAv(s.uid,s.av);if(!a.name&&s.name)$('iName').value=s.name});songs()}).catch(function(){msg('m1',L.e_net,1)})}
function setAv(uid,av){var e=$('uAv');if(av){e.style.backgroundImage='url('+A+'/w/san/av?u='+encodeURIComponent(uid)+'&v='+av+')';e.textContent=''}else{e.style.backgroundImage='';e.textContent='🙂'}}
$('bName').onclick=function(){var n=$('iName').value;api('/w/acct/name',{json:{name:n}}).then(function(j){if(!j.ok)return msg('m3',L.e_name,1);
  api('/w/san/me',{json:{name:n}}).then(function(){msg('m3',L.saved);$('uName').textContent=j.name;hdr(j.name)})})};
$('fAv').onchange=function(){var f=this.files[0];if(!f)return;var img=new Image();img.onload=function(){var c=document.createElement('canvas'),s=256,w=img.width,h=img.height,m=Math.min(w,h);c.width=c.height=s;
  c.getContext('2d').drawImage(img,(w-m)/2,(h-m)/2,m,m,0,0,s,s);c.toBlob(function(b){api('/w/san/avatar',{body:b}).then(function(j){if(j.ok)api('/w/san/me').then(function(s){setAv(s.uid,s.av)});else msg('m3',j.error||L.e_net,1)})},'image/jpeg',0.82)};img.src=URL.createObjectURL(f)};
$('bRmAv').onclick=function(){api('/w/san/avatar',{body:new Blob([])}).then(function(){setAv('',0)})};
$('bDel').onclick=function(){if(!confirm(L.delacctq))return;api('/w/acct/delete',{json:{confirm:true}}).then(function(j){if(j.deleted){logout();msg('m1',L.deleted)}})};
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
function goApp(w){if(!tok||!me)return;window.open('https://app.karaokeaihome.com/app/#acct='+encodeURIComponent(tok)+'&em='+encodeURIComponent(me.email||'')+'&nm='+encodeURIComponent(me.name||'')+'&go='+w,'_blank')}
$('bGoSan').onclick=function(){goApp('san')};$('bGoStu').onclick=function(){goApp('stu')};
if(tok)load();else if(pending()){email=pending();$('iEmail').value=email;toCode()}else show('stEmail');
})();
"""

def page(l, e):
    t = T[l]
    import json
    return ('<div class="acc"><h1 id="accH">%s</h1><p class="lead">%s</p>'
     '<div id="stEmail" class="card"><label>%s</label><input id="iEmail" type="email" autocomplete="email" inputmode="email"><button id="bSend">%s</button><button class="o" id="bHave" style="margin-left:8px">%s</button><div id="m1" class="msg"></div><p class="mute" style="font-size:.9rem">%s</p></div>'
     '<div id="stCode" class="card hide"><div id="m2" class="msg"></div><label>%s</label><input id="iCode" inputmode="numeric" autocomplete="one-time-code" maxlength="6"><div class="row"><button id="bLogin">%s</button><button class="o" id="bResend">%s</button><button class="o" id="bOther">%s</button></div></div>'
     '<div id="stIn" class="hide"><div class="card"><div class="me"><div class="av" id="uAv">🙂</div><div><div class="mute">%s</div><b id="uName" style="font-size:1.3rem"></b><div class="mute" id="uMail"></div></div></div></div>'
     '<div class="card"><h2 style="margin-top:0">%s</h2><div class="row"><button id="bGoSan">🎪 %s</button><button id="bGoStu">🎙️ %s</button></div><p class="mute" style="font-size:.9rem;margin-bottom:0">%s</p></div>'
     '<div class="card"><h2 style="margin-top:0">%s</h2><div id="player" class="player hide"><b id="pTitle"></b><div class="v"><div id="yt"></div></div><div class="row" style="margin-top:8px"><label class="mute">%s</label><input id="vol" type="range" min="0" max="100" value="90" style="flex:1;margin:0"><button class="o" id="bStop">%s</button></div></div><div id="songs"></div></div>'
     '<div class="card"><h2 style="margin-top:0">%s</h2><label>%s</label><div class="row"><input id="iName" maxlength="30" style="flex:1;margin:0"><button id="bName">%s</button></div>'
     '<p style="margin:14px 0 6px">%s</p><div class="row"><label class="o" style="display:inline-block;padding:11px 16px;border-radius:12px;background:#222;border:1px solid #333;cursor:pointer;font-weight:700">%s<input id="fAv" type="file" accept="image/*" class="hide"></label><button class="o" id="bRmAv">%s</button></div><div id="m3" class="msg"></div>'
     '<p style="margin:14px 0 6px">%s</p><p id="uW" class="mute"></p>'
     '<div class="row" style="margin-top:16px"><button class="o" id="bOut">%s</button><button class="r" id="bDel">%s</button></div></div></div></div>'
     '<script>window.ACC_L=%s;window.ACC_LANG=%s;</script><script src="/account.js"></script>') % (
        e(t['h']), e(t['lead']), e(t['email']), e(t['send']), e(t['have']), e(t['note']), e(t['code']), e(t['login']), e(t['resend']), e(t['other']),
        e(t['hi']), e(t['go_h']), e(t['go_san']), e(t['go_stu']), e(t['go_note']), e(t['songs']), e(t['voice']), e(t['stop']), e(t['acct']), e(t['name']), e(t['save']), e(t['avatar']), e(t['pick']), e(t['rmav']),
        e(t['warranty']), e(t['logout']), e(t['delacct']), json.dumps(t, ensure_ascii=False).replace('</', '<\\/'), json.dumps(l))
