import os,cv2,shutil
from config import videoforms, audioforms,checkdir,getdur,bot

async def musicrmv(x,z):
  tempnom = '54388953228'
  tempmp3 = f"{tempnom}.mp3"
  rmvmessage = x
  mscrmvid = rmvmessage.from_user.id
    
  rmvpath = await rmvmessage.download(file_name="./downloads/")
  filename = os.path.basename(rmvpath)
  nom,ex = os.path.splitext(filename)
  mp4file = f"msrmvd{nom}.mp4"
  mp3file = f"msrmvd{nom}.mp3"
  finalsound = f"{nom}.wav"
  workdir = './workdir/'
  await checkdir(workdir)
  os.system(f'''ffmpeg -i "{rmvpath}" -q:a 0 -map a "{tempmp3}" -y''')
  streamdur = int(z)
  if streamdur == 0 : 
    streamdur = await getdur(rmvpath)
  if streamdur <= 120 :
         os.system(f'''spleeter separate -p spleeter:2stems -o workdir "{tempmp3}"''')
         if ex in audioforms :
            os.system(f'''ffmpeg -i "{workdir+tempnom}/vocals.wav" -q:a 0 -map a "{mp3file}" -y''')
            await bot.send_audio(mscrmvid,mp3file,caption=nom)
         elif ex in videoforms :
          os.system(f'''ffmpeg -i "{rmvpath}" -i "./{workdir+tempnom}/vocals.wav" -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 "{mp4file}" -y''')
          await bot.send_video(mscrmvid, mp4file,caption=nom)
          os.remove(mp4file)
  else :
        partsdir = './parts/'
        musicrmvlist = 'musicrmvlist.txt'
        await checkdir(partsdir)
        os.system(f'''ffmpeg -i "{tempmp3}" -f segment -segment_time 120 -c copy "{partsdir}rmvd%09d.wav" -y''')
        numbofitems = len(os.listdir(partsdir))
        for x in range(0,numbofitems):
             myzfillvar = str(x).zfill(9)
             pathy=f"{partsdir}rmvd{myzfillvar}.wav"
             os.system(f'''spleeter separate -p spleeter:2stems -o workdir "{pathy}"''')
             rmvdvoice = f"{workdir}rmvd{myzfillvar}/vocals.wav"
             open(musicrmvlist,'a').write(f'''file {rmvdvoice} \n''')
        os.system(f'''ffmpeg -f concat -safe 0 -i {musicrmvlist} "{finalsound}" -y''')
        if ex in audioforms : 
           os.system(f'''ffmpeg -i "{finalsound}" -q:a 0 -map a "{mp3file}" -y''')
           await bot.send_audio(mscrmvid, mp3file,caption=nom)
        elif ex in videoforms : 
             os.system(f'''ffmpeg -i "{rmvpath}" -i "{finalsound}" -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 "{mp4file}" -y''')
             await bot.send_video(mscrmvid, mp4file,caption=nom)
             os.remove(mp4file)
        shutil.rmtree(partsdir) 
        os.remove(musicrmvlist)
        os.remove(finalsound)
  shutil.rmtree(workdir)
  if os.path.isfile(rmvpath):
   os.remove(rmvpath)
  if os.path.isfile(mp3file):
   os.remove(mp3file)
  if os.path.isfile(tempmp3):
   os.remove(tempmp3)
