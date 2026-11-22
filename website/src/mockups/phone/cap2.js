const {chromium}=require('playwright');const fs=require('fs');
// node cap2.js <lang|vi> : chup cac man hinh; neu co dict-<lang>.json thi thay chu truoc khi chup
const lang=process.argv[2]||'vi';
const D=lang=='vi'?JSON.parse(fs.readFileSync('dict-vi.json')):JSON.parse(fs.readFileSync('dict-'+lang+'.json'));
const SCREENS=[['home',"go('home')"],['remote',"go('remote')"],['songs',"go('songs')"],['ai',"go('ai')"],['more',"go('more')"],['dich',"go('dich')"],
 ['fit1',"go('more');fitOpen()"],['fit2',"fitCat('gym')"],['fit3',"fitPlay('gy1')"]];
(async()=>{
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:2});
 await p.route(/\/fitness\/img\/.*\.jpg/,r=>{const f='/mnt/project-files/karaoke-app/fitness/assets/fitness/img/'+r.request().url().split('/img/')[1].split('?')[0];try{r.fulfill({path:f})}catch(e){r.abort()}});
 p.on('pageerror',e=>console.log('ERR',e.message));
 await p.goto('file://'+__dirname+'/app/index.html?demo=1&platform=android');
 await p.waitForTimeout(1500);
 const texts={};
 for(const [name,js] of SCREENS){
  await p.evaluate(js);
  if(name=='dich'&&D.PAIR){await p.evaluate(pr=>{$('tFrom').value=pr[0];$('tTo').value=pr[1];tSave()},D.PAIR)}await p.waitForTimeout(name=='fit3'?2500:900);
  texts[name]=await p.evaluate((D)=>{const out=[];const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;const nodes=[];
   while(n=w.nextNode())nodes.push(n);
   for(const n of nodes){const t=n.nodeValue.trim();if(!t)continue;const el=n.parentElement;if(!el||el.offsetParent===null&&getComputedStyle(el).position!='fixed')continue;
    const r=el.getBoundingClientRect();if(!(r.width&&r.height&&r.bottom>0&&r.top<844))continue;
    if(D[t]!==undefined){n.nodeValue=n.nodeValue.replace(t,D[t])}else out.push(t)}
   document.querySelectorAll('select option').forEach(o=>{if(D['OPT:'+o.text]!==undefined)o.text=D['OPT:'+o.text]});
   document.querySelectorAll('input[placeholder],textarea[placeholder]').forEach(i=>{const t=i.placeholder;if(D['PH:'+t]!==undefined)i.placeholder=D['PH:'+t];else if(i.offsetParent)out.push('PH:'+t)});
   return [...new Set(out)]},D);
  await p.waitForTimeout(400);
  const t2=await p.evaluate((D)=>{const out=[];const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;const nodes=[];
   while(n=w.nextNode())nodes.push(n);
   for(const n of nodes){const t=n.nodeValue.trim();if(!t)continue;const el=n.parentElement;if(!el||el.offsetParent===null&&getComputedStyle(el).position!='fixed')continue;
    const r=el.getBoundingClientRect();if(!(r.width&&r.height&&r.bottom>0&&r.top<844))continue;
    if(D[t]!==undefined){n.nodeValue=n.nodeValue.replace(t,D[t])}else out.push(t)}
   document.querySelectorAll('select option').forEach(o=>{if(D['OPT:'+o.text]!==undefined)o.text=D['OPT:'+o.text]});
   document.querySelectorAll('input[placeholder],textarea[placeholder]').forEach(i=>{const t=i.placeholder;if(D['PH:'+t]!==undefined)i.placeholder=D['PH:'+t];else if(i.offsetParent)out.push('PH:'+t)});
   return [...new Set(out)]},D);
  await p.waitForTimeout(100);
  await p.screenshot({path:'shots/'+lang+'-'+name+'.png'});
 }
 fs.writeFileSync('missing-'+lang+'.json',JSON.stringify(texts,null,1));await b.close();
})();
