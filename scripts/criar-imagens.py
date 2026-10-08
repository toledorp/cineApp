from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math, random
out=Path('assets/images')
font=Path('C:/Windows/Fonts/arialbd.ttf')
def poster(key,bg,accent,title,kind):
 im=Image.new('RGB',(600,900),bg); d=ImageDraw.Draw(im)
 for y in range(900):
  ratio=y/900
  c=tuple(int(a*(1-ratio*.55)) for a in bg)
  d.line((0,y,600,y),fill=c)
 random.seed(7)
 if kind=='space':
  for _ in range(110):
   x,y=random.randrange(600),random.randrange(670); r=random.choice([1,1,2]); d.ellipse((x-r,y-r,x+r,y+r),fill='#D5D7E9')
  for r in [200,240,280]: d.ellipse((300-r,360-r*.5,300+r,360+r*.5),outline=accent,width=3)
  d.ellipse((150,195,450,495),fill=accent)
  d.ellipse((170,210,440,470),fill='#C1A5E3')
  d.ellipse((225,230,440,445),fill='#8D73B7')
  d.polygon([(230,555),(370,555),(315,425),(285,425)],fill='#ECE7E0')
 elif kind=='city':
  d.ellipse((370,120,490,240),fill=accent)
  for i in range(9):
   x=i*75-30; top=random.randrange(270,490)
   d.rectangle((x,top,x+65,690),fill='#171524')
   for yy in range(top+20,670,34):
    for xx in range(x+12,x+55,22): d.rectangle((xx,yy,xx+8,yy+13),fill=accent if (i==5 and yy<top+60) else '#343044')
  d.polygon([(200,690),(400,690),(320,575),(280,575)],fill='#55414F')
 elif kind=='sea':
  d.ellipse((195,150,405,360),fill=accent)
  for i in range(11):
   y=360+i*32
   d.polygon([(0,y),(150,y-18),(340,y+12),(600,y-20),(600,900),(0,900)],fill=(25+i*3,95+i*4,114+i*4))
  d.polygon([(205,440),(395,440),(350,490),(250,490)],fill='#142C38')
  d.line((300,320,300,440),fill='#FFF0D4',width=5)
  d.polygon([(305,325),(305,420),(370,420)],fill='#FFF0D4')
 elif kind=='forest':
  d.ellipse((220,115,380,275),fill=accent)
  d.polygon([(0,520),(160,250),(300,520),(450,300),(600,500),(600,900),(0,900)],fill='#365C55')
  d.polygon([(0,660),(220,420),(330,650),(500,390),(600,600),(600,900),(0,900)],fill='#183F38')
  d.polygon([(240,690),(360,690),(325,560),(275,560)],fill='#CEBFA0')
  for x in [50,120,480,550]:
   d.polygon([(x-65,590),(x,330),(x+65,590)],fill='#102F2D')
 elif kind=='cafe':
  d.ellipse((370,130,500,260),fill=accent)
  d.polygon([(245,470),(300,140),(355,470)],fill='#55334E')
  d.line((225,470,375,470),fill='#55334E',width=12)
  d.line((240,360,360,360),fill=bg,width=10)
  d.line((260,290,340,290),fill=bg,width=8)
  d.rounded_rectangle((140,500,400,660),radius=25,fill='#F5D3B2')
  d.ellipse((155,485,385,535),fill='#64403C')
  d.arc((350,525,460,625),-90,90,fill='#F5D3B2',width=18)
  for x in [210,270,330]: d.arc((x-15,410,x+30,490),90,270,fill='#F7E9DD',width=4)
 else:
  d.ellipse((350,125,495,270),fill=accent)
  d.polygon([(0,540),(160,330),(340,570),(490,350),(600,520),(600,900),(0,900)],fill='#788569')
  d.polygon([(130,900),(470,900),(320,410),(280,410)],fill='#3D4650')
  d.line((300,445,300,850),fill='#F8D684',width=6)
  d.rounded_rectangle((175,410,425,640),radius=28,fill=accent)
  d.rounded_rectangle((195,438,405,520),radius=12,fill='#334553')
  d.rectangle((185,575,415,593),fill='#FFEBC3')
  for x in [200,375]: d.ellipse((x-17,615,x+17,656),fill='#252732')
 d.rectangle((0,705,600,900),fill='#101017')
 small=ImageFont.truetype(str(font),15); big=ImageFont.truetype(str(font),43)
 d.text((40,735),'C I N E A P P   /   ORIGINAL',font=small,fill=accent)
 y=778
 for line in title:
  d.text((40,y),line,font=big,fill='#FAF8F5'); y+=50
 im.save(out/'filmes'/f'{key}.png')
poster('orbita',(36,28,69),'#E4B986',['ALÉM DA','ÓRBITA'],'space')
poster('cidade',(54,34,63),'#FF9070',['ÚLTIMA LUZ'],'city')
poster('mar',(40,100,117),'#FFD8A0',['MAR DE','MEMÓRIAS'],'sea')
poster('floresta',(30,67,57),'#F3D899',['O VALE','SECRETO'],'forest')
poster('encontro',(122,64,86),'#F8BA92',['UM CAFÉ','EM PARIS'],'cafe')
poster('viagem',(78,121,138),'#EDBB67',['PRÓXIMA','PARADA'],'bus')
im=Image.new('RGBA',(256,256),(0,0,0,0)); d=ImageDraw.Draw(im)
d.rounded_rectangle((15,15,241,241),radius=55,fill='#FF795E')
d.rounded_rectangle((57,100,199,185),radius=10,fill='#101017')
d.polygon([(53,71),(184,48),(194,84),(60,107)],fill='#101017')
for x in [65,105,145]: d.polygon([(x,69-(x-65)*.17),(x+19,65-(x-65)*.17),(x+38,92-(x-65)*.17),(x+18,95-(x-65)*.17)],fill='#FFF4E1')
d.polygon([(113,119),(113,166),(154,142)],fill='#FFF4E1')
im.save(out/'cineapp-logo.png')
icon=Image.new('RGBA',(1024,1024),'#101017'); icon.alpha_composite(im.resize((640,640)),(192,192)); icon.convert('RGB').save(out/'cineapp-icon.png')
print('6 cartazes, logotipo e ícone criados.')
