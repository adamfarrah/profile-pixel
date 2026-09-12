import base64,os
s=open('index.html').read()
imgs={'BG':'assets/bg_s.jpg','PFP':'assets/pfp_s.png','CLOVER':'assets/clover_s.png','KOI':'assets/koi_s.jpg'}
mime={'.jpg':'image/jpeg','.png':'image/png'}
uri={k:'data:%s;base64,%s'%(mime[os.path.splitext(f)[1]],base64.b64encode(open(f,'rb').read()).decode()) for k,f in imgs.items()}
s=s.replace('<link rel="preload" as="image" href="assets/pfp.png">\n','')
s=s.replace('<link rel="icon" id="favi" href="assets/pfp.png">','<link rel="icon" id="favi" href="data:,">')
s=s.replace('<meta property="og:image" content="assets/koi.jpg">','')
s=s.replace('background:#253248 url(assets/bg.jpg) center/cover no-repeat}','background:var(--bgimg)}')
s=s.replace('background:url(assets/bg.jpg) center/cover no-repeat;','background:var(--bgimg) center/cover no-repeat;')
s=s.replace('src="assets/pfp.png"','src="data:," data-img="PFP"')
s=s.replace('src="assets/clover.png"','src="data:," data-img="CLOVER"')
s=s.replace('src="assets/koi.jpg"','src="data:," data-img="KOI"')
s=s.replace('  --max:1080px;','  --bgimg:url("%s");\n  --max:1080px;'%uri['BG'],1)
s=s.replace('  --clv:url(assets/clover.png);','',1)
js="var IMG={PFP:'%s',CLOVER:'%s',KOI:'%s'};\n"%(uri['PFP'],uri['CLOVER'],uri['KOI'])
js+="document.querySelectorAll('[data-img]').forEach(function(n){n.src=IMG[n.getAttribute('data-img')]});\n"
js+="document.documentElement.style.setProperty('--clv','url(\"'+IMG.CLOVER+'\")');\n"
s=s.replace('/* ---------- ICONS ---------- */', js+'\n/* ---------- ICONS ---------- */',1)
assert s.count('assets/')==0, s.count('assets/')
open('index_standalone.html','w').write(s)
import pathlib
here=pathlib.Path(__file__).resolve().parent
(here/'Onyx-website.html').write_text(s,encoding='utf-8')
open('/home/user/Onyx-website.html','w').write(s)
print('MB',round(len(s)/1048576,2),'| refs',s.count('assets/'))
