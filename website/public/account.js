
(function(){var A='https://api.karaokeaihome.com',L=window.ACC_L,LG=window.ACC_LANG,$=function(i){return document.getElementById(i)};
var tok=null;try{tok=localStorage.getItem('kah_acct')}catch(e){}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return'&#'+c.charCodeAt(0)+';'})}
function msg(id,t,bad){var m=$(id);m.textContent=t||'';m.className='msg'+(bad?' err':'')}
function api(p,o){o=o||{};var h={};if(tok)h['X-Acct']=tok;if(o.json!==undefined){h['Content-Type']='application/json';o.body=JSON.stringify(o.json)}
  return fetch(A+p,{method:o.method||(o.body?'POST':'GET'),headers:h,body:o.body}).then(function(r){return r.json().catch(function(){return{}}).then(function(j){j._s=r.status;return j})})}
function errText(j){var c=j.code;if(j.noacct)return L.noacct;if(c==='email')return L.e_email;if(c==='wait')return L.e_wait;if(c==='limit')return L.e_limit;
  if(c==='expired')return L.e_expired;if(c==='tries')return L.e_tries;if(c==='wrong')return L.e_wrong.replace('{n}',j.left);return L.e_net}
var email='';
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
function logout(){tok=null;try{localStorage.removeItem('kah_acct')}catch(e){}stopPlay();show('stEmail')}
$('bOut').onclick=logout;
function fmt(t){var d=new Date(t);return d.toLocaleDateString(LG==='vi'?'vi-VN':LG)}
var me=null;
function load(){api('/w/acct/me').then(function(a){if(a._s===401){logout();return}me=a;show('stIn');$('uName').textContent=a.name||a.email;$('uMail').textContent=a.email;$('iName').value=a.name||'';
  if(a.warranty&&a.warranty.start){$('uW').innerHTML=esc(L.wcode)+': <b>'+esc(a.warranty.code)+'</b><br>'+esc(L.wend)+': <b>'+fmt(a.warranty.start+365*864e5)+'</b>'}else $('uW').textContent=L.nowarranty;
  api('/w/san/me').then(function(s){setAv(s.uid,s.av);if(!a.name&&s.name)$('iName').value=s.name});songs()}).catch(function(){msg('m1',L.e_net,1)})}
function setAv(uid,av){var e=$('uAv');if(av){e.style.backgroundImage='url('+A+'/w/san/av?u='+encodeURIComponent(uid)+'&v='+av+')';e.textContent=''}else{e.style.backgroundImage='';e.textContent='🙂'}}
$('bName').onclick=function(){var n=$('iName').value;api('/w/acct/name',{json:{name:n}}).then(function(j){if(!j.ok)return msg('m3',L.e_name,1);
  api('/w/san/me',{json:{name:n}}).then(function(){msg('m3',L.saved);$('uName').textContent=j.name})})};
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
