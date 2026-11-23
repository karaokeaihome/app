
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
  $('vipState').textContent=t==='adv'?L.vip_on:L.vip_free;$('bVip').classList.toggle('hide',t==='adv')}
$('bVip').onclick=function(){$('vipBox').classList.toggle('hide')};$('bVipBuy').onclick=function(){msg('m6',L.vip_soon)};
function goApp(w){if(!tok||!me)return;window.open('https://app.karaokeaihome.com/app/#acct='+encodeURIComponent(tok)+'&em='+encodeURIComponent(me.email||'')+'&nm='+encodeURIComponent(me.name||'')+'&go='+w+'&lang='+LG,'_blank')}
$('bGoSan').onclick=function(){goApp('san')};$('bGoStu').onclick=function(){goApp('stu')};$('bGoGuide').onclick=function(e){e.preventDefault();goApp('guide')};
function notifs(n){n=n||{};$('notifs').innerHTML=['san','top','upd','promo'].map(function(k){return '<label class="sw"><span>'+esc(L['k_'+k])+'</span><input type="checkbox" data-k="'+k+'"'+(n[k]?' checked':'')+'></label>'}).join('')}
$('notifs').onchange=function(){var n={};[].forEach.call($('notifs').querySelectorAll('input'),function(i){n[i.dataset.k]=i.checked?1:0});api('/w/acct/notif',{json:{notif:n}}).then(function(j){msg('m4',j.ok?L.saved:L.e_net,!j.ok)})};
if(tok)load();else if(pending()){email=pending();$('iEmail').value=email;toCode()}else show('stEmail');
})();
