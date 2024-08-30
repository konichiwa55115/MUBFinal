from os import system as cmd
from config import checkdir,bot
import shutil,os

##########

async def splitfunc(splitmessage):
  splittyaudid = splitmessage.from_user.id
  if splitmessage.audio or splitmessage.voice :
    splitpath = await splitmessage.download(file_name="./downloads/")
    filename = os.path.basename(splitpath)
    nom,ex = os.path.splitext(filename)
    if not splitpath.endswith('mp3') :
     mp3file = "./downloads/" + mp3file
     cmd(f'''ffmpeg -i "{splitpath}" -q:a 0 -map a "{mp3file}" -y''')
     os.remove(splitpath)
     splitpath = mp3file
    partdir = './audsplitparts/'
    await checkdir(partdir)
    cmd(f'''ffmpeg -i "{splitpath}" -f segment -segment_time 300 -c copy "{partdir+nom}%09d.wav" -y''')
    listofitems = sorted(os.listdir(partdir))
    for x in listofitems : 
       res = f"{nom+listofitems.index(x).zfill(4)}.mp3"
       x = partdir + x
       cmd(f'''ffmpeg -i "{x}" -q:a 0 -map a "{res}" -y''')
       await bot.send_audio(splittyaudid, res)
       os.remove(res)
    shutil.rmtree(partdir)
    os.remove(splitpath) 
  
  elif splitmessage.video :
      vidsplitdir = './vidsplitparts/'
      vidsplitpath = await splitmessage.download(file_name=vidsplitdir)
      cmd(f"python3 ffmpeg-split.py -f '{vidsplitpath}' -s 130")
      os.remove(vidsplitpath)
      listofparts = os.listdir(vidsplitdir)
      partslist = sorted(listofparts)
      for part in partslist :
        vidpart = f"{vidsplitdir+part}"
        partcaption = vidsplitmsg.caption + ' جـ'+ str(partslist.index(part)+1)
        sentpart = await bot.send_video(splittyaudid,vidpart,caption=partcaption)
      shutil.rmtree(vidsplitdir)