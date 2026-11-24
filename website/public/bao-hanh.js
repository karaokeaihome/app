(function(){
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
