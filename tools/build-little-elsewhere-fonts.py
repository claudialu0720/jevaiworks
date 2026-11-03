"""Rebuild self-hosted marketing webfonts after copy changes.
Requires fonttools and brotli; source TTFs/OFLs are downloaded from Google Fonts.
Run the landing generator first. Cached sources stay in ignored .preview/.
"""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import quote
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.preview/font-tools'))
from fontTools.ttLib import TTFont
from fontTools import subset
from fontTools.varLib.instancer import instantiateVariableFont
CACHE=ROOT/'.preview/font-sources'; CACHE.mkdir(parents=True,exist_ok=True)
OUT=ROOT/'assets/little-elsewhere/fonts'; OUT.mkdir(parents=True,exist_ok=True)
text=''.join((ROOT/p).read_text(encoding='utf-8') for p in ['little-elsewhere/index.html','little-elsewhere/en/index.html'])
chars=set(map(ord,text)) | set(range(32,127))
def source(family,name):
 p=CACHE/(family+'-'+name)
 if not p.exists():p.write_bytes(urlopen('https://raw.githubusercontent.com/google/fonts/main/ofl/'+family+'/'+quote(name),timeout=45).read())
 return p
for family,weights in [('lxgwwenkaitc',[(400,'Regular'),(700,'Bold')]),('fredoka',[(400,'Regular'),(500,'Medium')])]:
 for weight,label in weights:
  name='LXGWWenKaiTC-'+label+'.ttf' if family=='lxgwwenkaitc' else 'Fredoka[wdth,wght].ttf'
  font=TTFont(source(family,name))
  if family=='fredoka':font=instantiateVariableFont(font,{'wdth':100,'wght':weight},inplace=True)
  options=subset.Options();options.flavor='woff2';options.name_IDs=['*'];options.name_legacy=True
  builder=subset.Subsetter(options=options)
  # Include all Latin/extended Latin in Fredoka, including future English copy.
  builder.populate(unicodes=(chars if family=='lxgwwenkaitc' else set(range(32,592)) | set(range(8192,8304))))
  builder.subset(font);font.flavor='woff2'
  target=OUT/(('lxgw-wenkai-tc' if family=='lxgwwenkaitc' else 'fredoka')+'-'+label.lower()+'.woff2')
  font.save(target);print(target.name,target.stat().st_size,flush=True)
 (OUT/(family+'-OFL.txt')).write_bytes(source(family,'OFL.txt').read_bytes())
