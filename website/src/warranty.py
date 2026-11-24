# -*- coding: utf-8 -*-
# Trang TRA CỨU BẢO HÀNH công khai /<lang>/bao-hanh/ : khách nhập mã bảo hành KAH (hoặc serial) để xem ngày kích hoạt, hạn, tình trạng.
# Gọi máy chủ GET https://api.karaokeaihome.com/bh?q=... (repo karaokeaihome/sever, worker.js + acct.js warrantyPublic). Máy chủ chỉ trả tình trạng bảo hành, không trả thông tin chủ loa.
T = {
 'vi': dict(nav="Bảo hành", h="Tra cứu bảo hành", lead="Nhập mã bảo hành của loa để xem ngày kích hoạt, ngày hết hạn và tình trạng bảo hành.",
  label="Mã bảo hành (KAH-xxxx-xxxx-xxxx) hoặc số serial", ph="KAH-0000-0000-0000", btn="Tra cứu",
  where_h="Mã bảo hành ở đâu?", where=["Trên TV của loa: <b>Cài đặt</b> → <b>Bảo hành</b>.","Trong app Karaoke AI Home: mục <b>Tài khoản</b> (khi điện thoại đã kết nối với loa).","Trong email xác nhận gửi tới tài khoản đã kết nối với loa."],
  rule="Bảo hành chính hãng 12 tháng, tự kích hoạt khi loa kết nối Wi‑Fi về máy chủ lần đầu. Ngày kích hoạt lưu trên máy chủ, không thay đổi được.",
  code="Mã bảo hành", model="Loại máy", start="Ngày kích hoạt", end="Hết hạn", left="Còn lại", days="{n} ngày",
  ok="Còn bảo hành", exp="Đã hết bảo hành", inactive="Chưa kích hoạt", inactive_p="Bảo hành sẽ tự kích hoạt khi loa kết nối Wi‑Fi lần đầu.",
  nf="Không tìm thấy loa với mã này. Kiểm tra lại mã trên màn hình Cài đặt → Bảo hành của loa.", short="Mã quá ngắn, hãy nhập đủ mã bảo hành.",
  limit="Bạn đã tra cứu quá nhiều lần hôm nay, mai thử lại nhé.", net="Không kết nối được máy chủ, thử lại sau nhé.",
  help="Cần hỗ trợ bảo hành? Gửi email kèm mã bảo hành tới info@karaokeaihome.com"),
 'en': dict(nav="Warranty", h="Warranty check", lead="Enter your speaker’s warranty code to see its activation date, expiry date and warranty status.",
  label="Warranty code (KAH-xxxx-xxxx-xxxx) or serial number", ph="KAH-0000-0000-0000", btn="Check",
  where_h="Where is the warranty code?", where=["On the speaker’s TV screen: <b>Settings</b> → <b>Warranty</b>.","In the Karaoke AI Home app: <b>Account</b> (once your phone is connected to the speaker).","In the confirmation email sent to the account connected to the speaker."],
  rule="12‑month official warranty, activated automatically the first time the speaker connects to our server over Wi‑Fi. The activation date is stored on our server and cannot be changed.",
  code="Warranty code", model="Model", start="Activated on", end="Expires on", left="Remaining", days="{n} days",
  ok="Under warranty", exp="Warranty expired", inactive="Not activated yet", inactive_p="The warranty activates automatically when the speaker first connects to Wi‑Fi.",
  nf="No speaker found with this code. Please check the code under Settings → Warranty on the speaker.", short="The code is too short. Please enter the full warranty code.",
  limit="Too many checks today. Please try again tomorrow.", net="Can’t reach the server. Please try again later.",
  help="Need warranty service? Email us your warranty code at info@karaokeaihome.com"),
 'ja': dict(nav="保証", h="保証の確認", lead="スピーカーの保証コードを入力すると、保証開始日・終了日・保証状況を確認できます。",
  label="保証コード（KAH-xxxx-xxxx-xxxx）またはシリアル番号", ph="KAH-0000-0000-0000", btn="確認する",
  where_h="保証コードはどこにありますか？", where=["スピーカーのテレビ画面：<b>設定</b> → <b>保証</b>。","Karaoke AI Home アプリ：<b>アカウント</b>（スマホをスピーカーに接続済みの場合）。","スピーカーに接続したアカウントに届く確認メール。"],
  rule="12か月の正規保証。スピーカーが初めて Wi‑Fi でサーバーに接続したときに自動で開始します。開始日はサーバーに記録され、変更できません。",
  code="保証コード", model="機種", start="保証開始日", end="保証終了日", left="残り", days="{n}日",
  ok="保証期間内", exp="保証期間終了", inactive="未開始", inactive_p="スピーカーが初めて Wi‑Fi に接続すると自動で保証が始まります。",
  nf="このコードのスピーカーは見つかりません。スピーカーの 設定 → 保証 でコードをご確認ください。", short="コードが短すぎます。保証コードをすべて入力してください。",
  limit="本日の確認回数の上限に達しました。明日お試しください。", net="サーバーに接続できません。しばらくしてからお試しください。",
  help="保証サービスのご依頼は、保証コードを添えて info@karaokeaihome.com までメールしてください"),
 'ko': dict(nav="보증", h="보증 조회", lead="스피커의 보증 코드를 입력하면 활성화일, 만료일, 보증 상태를 확인할 수 있습니다.",
  label="보증 코드(KAH-xxxx-xxxx-xxxx) 또는 시리얼 번호", ph="KAH-0000-0000-0000", btn="조회",
  where_h="보증 코드는 어디에 있나요?", where=["스피커의 TV 화면: <b>설정</b> → <b>보증</b>.","Karaoke AI Home 앱: <b>계정</b>(휴대폰을 스피커에 연결한 경우).","스피커에 연결된 계정으로 보낸 확인 이메일."],
  rule="12개월 정품 보증으로, 스피커가 처음 Wi‑Fi로 서버에 연결될 때 자동으로 시작됩니다. 활성화 날짜는 서버에 저장되며 변경할 수 없습니다.",
  code="보증 코드", model="모델", start="활성화일", end="만료일", left="남은 기간", days="{n}일",
  ok="보증 기간 내", exp="보증 만료", inactive="아직 활성화되지 않음", inactive_p="스피커가 처음 Wi‑Fi에 연결되면 보증이 자동으로 시작됩니다.",
  nf="이 코드의 스피커를 찾을 수 없습니다. 스피커의 설정 → 보증에서 코드를 확인해 주세요.", short="코드가 너무 짧습니다. 보증 코드를 모두 입력해 주세요.",
  limit="오늘 조회 횟수를 초과했습니다. 내일 다시 시도해 주세요.", net="서버에 연결할 수 없습니다. 잠시 후 다시 시도해 주세요.",
  help="보증 서비스가 필요하신가요? 보증 코드와 함께 info@karaokeaihome.com 으로 이메일을 보내 주세요"),
 'fr': dict(nav="Garantie", h="Vérifier la garantie", lead="Saisissez le code de garantie de votre enceinte pour voir sa date d’activation, sa date de fin et l’état de la garantie.",
  label="Code de garantie (KAH-xxxx-xxxx-xxxx) ou numéro de série", ph="KAH-0000-0000-0000", btn="Vérifier",
  where_h="Où trouver le code de garantie ?", where=["Sur l’écran TV de l’enceinte : <b>Paramètres</b> → <b>Garantie</b>.","Dans l’application Karaoke AI Home : <b>Compte</b> (une fois le téléphone connecté à l’enceinte).","Dans l’e‑mail de confirmation envoyé au compte connecté à l’enceinte."],
  rule="Garantie officielle de 12 mois, activée automatiquement lors de la première connexion Wi‑Fi de l’enceinte à notre serveur. La date d’activation est enregistrée sur notre serveur et ne peut pas être modifiée.",
  code="Code de garantie", model="Modèle", start="Activée le", end="Fin le", left="Restant", days="{n} jours",
  ok="Sous garantie", exp="Garantie expirée", inactive="Pas encore activée", inactive_p="La garantie s’active automatiquement à la première connexion Wi‑Fi de l’enceinte.",
  nf="Aucune enceinte trouvée avec ce code. Vérifiez le code dans Paramètres → Garantie sur l’enceinte.", short="Code trop court. Saisissez le code de garantie complet.",
  limit="Trop de vérifications aujourd’hui. Réessayez demain.", net="Serveur injoignable. Réessayez plus tard.",
  help="Besoin d’une intervention sous garantie ? Écrivez‑nous avec votre code de garantie à info@karaokeaihome.com"),
 'zh': dict(nav="保修", h="保修查询", lead="输入音箱的保修码，即可查看激活日期、到期日期和保修状态。",
  label="保修码（KAH-xxxx-xxxx-xxxx）或序列号", ph="KAH-0000-0000-0000", btn="查询",
  where_h="保修码在哪里？", where=["在音箱的电视画面：<b>设置</b> → <b>保修</b>。","在 Karaoke AI Home 应用：<b>账户</b>（手机已连接音箱时）。","在发送到已连接音箱账户的确认邮件中。"],
  rule="12 个月官方保修，音箱首次通过 Wi‑Fi 连接服务器时自动激活。激活日期保存在服务器上，无法更改。",
  code="保修码", model="型号", start="激活日期", end="到期日期", left="剩余", days="{n} 天",
  ok="在保修期内", exp="已过保修期", inactive="尚未激活", inactive_p="音箱首次连接 Wi‑Fi 时将自动激活保修。",
  nf="未找到此保修码对应的音箱。请在音箱的 设置 → 保修 中核对保修码。", short="保修码太短，请输入完整的保修码。",
  limit="今天查询次数过多，请明天再试。", net="无法连接服务器，请稍后再试。",
  help="需要保修服务？请将保修码发送邮件至 info@karaokeaihome.com"),
}
LOCALE = {'vi': 'vi-VN', 'en': 'en-GB', 'ja': 'ja-JP', 'ko': 'ko-KR', 'fr': 'fr-FR', 'zh': 'zh-CN'}
# biểu tượng nét mảnh một màu (khiên có dấu tích) — chỉ dùng cho trang này
ICON = '<svg viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.8 4.5 5.6v5.6c0 4.6 3.1 8.6 7.5 10 4.4-1.4 7.5-5.4 7.5-10V5.6z"/><path d="m8.6 12.2 2.4 2.4 4.6-4.8"/></svg>'
CSS = """
.wty{max-width:640px;margin:0 auto;padding:16px}.wty .wi{color:var(--acc);display:flex;justify-content:center;margin-top:8px}.wty h1{text-align:center;margin:10px 0 6px}.wty .lead{text-align:center}
.wty form{margin:18px 0}.wty label{display:block;color:var(--mute);font-size:.95rem;margin-bottom:6px}
.wty .rw{display:flex;gap:8px}.wty input{flex:1;min-width:0;box-sizing:border-box;padding:13px 14px;border-radius:12px;border:1px solid #333;background:#111;color:var(--fg);font-size:1.1rem;letter-spacing:.04em;text-transform:uppercase}
.wty button{cursor:pointer;border:0;border-radius:12px;padding:12px 18px;font-weight:700;font-size:1rem;background:var(--acc);color:#111;white-space:nowrap}.wty button:disabled{opacity:.6}
.wty .res{margin:16px 0;padding:18px;border-radius:16px;background:#141417;border:1px solid #2a2a30}.wty .res.hide{display:none}
.wty .st{display:flex;align-items:center;gap:10px;font-size:1.3rem;font-weight:800}.wty .st svg{flex:none}.wty .st.g{color:#6fcf8f}.wty .st.r{color:#e06666}.wty .st.y{color:#e8b84a}
.wty dl{display:grid;grid-template-columns:auto 1fr;gap:8px 16px;margin:14px 0 0}.wty dt{color:var(--mute)}.wty dd{margin:0;font-weight:700;overflow-wrap:anywhere}.wty dd.c{white-space:nowrap;font-variant-numeric:tabular-nums;letter-spacing:.02em}
.wty .bar{height:8px;border-radius:99px;background:#2a2a30;margin-top:14px;overflow:hidden}.wty .bar i{display:block;height:100%;background:var(--acc)}
.wty .err{color:#e06666}.wty .rule{font-size:.92rem}
@media(max-width:480px){.wty .rw{flex-direction:column}.wty button{width:100%}}
"""
JS = r"""(function(){
var A='https://api.karaokeaihome.com',L=window.WTY_L,LC=window.WTY_LC,$=function(i){return document.getElementById(i)};
var esc=function(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})};
var ok='<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="m8 12.3 2.7 2.7L16 9.6"/></svg>';
var no='<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M9 9l6 6M15 9l-6 6"/></svg>';
var wait='<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>';
function fmt(t){try{return new Date(t).toLocaleDateString(LC,{day:'2-digit',month:'2-digit',year:'numeric',timeZone:'Asia/Ho_Chi_Minh'})}catch(e){return new Date(t).toISOString().slice(0,10)}}
function out(h){var r=$('wRes');r.innerHTML=h;r.classList.remove('hide')}
function row(k,v,c){return '<dt>'+esc(k)+'</dt><dd'+(c?' class="c"':'')+'>'+esc(v)+'</dd>'}
function go(q){q=(q||'').trim();if(!q)return;var b=$('wBtn');b.disabled=true;out('<p class="mute">…</p>');
  try{history.replaceState(null,'','?q='+encodeURIComponent(q))}catch(e){}
  fetch(A+'/bh?q='+encodeURIComponent(q)).then(function(r){return r.json().catch(function(){return {ok:false,error:'server'}})}).then(function(j){b.disabled=false;
    if(!j.ok)return out('<p class="err">'+esc(j.error==='limit'?L.limit:j.error==='short'?L.short:L.net)+'</p>');
    if(!j.found)return out('<p class="err">'+esc(L.nf)+'</p>');
    var d=row(L.code,j.code,1)+(j.model?row(L.model,j.model):'');
    if(!j.active)return out('<div class="st y">'+wait+esc(L.inactive)+'</div><p class="mute" style="margin:8px 0 0">'+esc(L.inactive_p)+'</p><dl>'+d+'</dl>');
    d+=row(L.start,fmt(j.start))+row(L.end,fmt(j.end-1));if(j.valid)d+=row(L.left,L.days.replace('{n}',j.daysLeft));
    var p=Math.max(0,Math.min(100,100*(j.now-j.start)/(j.end-j.start)));
    out('<div class="st '+(j.valid?'g':'r')+'">'+(j.valid?ok:no)+esc(j.valid?L.ok:L.exp)+'</div><dl>'+d+'</dl><div class="bar"><i style="width:'+p.toFixed(1)+'%"></i></div>')
  }).catch(function(){b.disabled=false;out('<p class="err">'+esc(L.net)+'</p>')})}
$('wForm').onsubmit=function(e){e.preventDefault();go($('wQ').value)};
var q0=new URLSearchParams(location.search).get('q');if(q0){$('wQ').value=q0;go(q0)}
})();
"""

def page(l, e):
    import json
    t = T[l]
    return ('<div class="wty"><div class="wi">%s</div><h1>%s</h1><p class="lead">%s</p>'
            '<form id="wForm" class="card" autocomplete="off"><label for="wQ">%s</label><div class="rw"><input id="wQ" name="q" placeholder="%s" maxlength="40" autocapitalize="characters" spellcheck="false" required><button id="wBtn" type="submit">%s</button></div></form>'
            '<div id="wRes" class="res hide" aria-live="polite"></div>'
            '<h2>%s</h2><ul>%s</ul><p class="mute rule">%s</p><p class="note">%s</p></div>'
            '<script>window.WTY_L=%s;window.WTY_LC=%s;</script><script src="/bao-hanh.js"></script>') % (
        ICON, e(t['h']), e(t['lead']), e(t['label']), e(t['ph']), e(t['btn']),
        e(t['where_h']), ''.join('<li>%s</li>' % x for x in t['where']), e(t['rule']), e(t['help']),
        json.dumps(t, ensure_ascii=False).replace('</', '<\\/'), json.dumps(LOCALE[l]))
