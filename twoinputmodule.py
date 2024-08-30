import os,cv2,shutil
from config import bot
montaglist,vidsubslist,vidsrt = [],[],[]

###### منتجة فيديو ### 

async def imagetovidfunc(x,replo):
     imgid = x.from_user.id
     if x.photo and len(montaglist) == 0 :
      await replo.edit_text("معالجة ⏱️")
      montaglist.append(x)
      await replo.edit_text("الآن أرسل الصوتية") 
      
     elif x.photo and len(montaglist) == 1 and not montaglist[0].photo   :
      await replo.delete()
      replo2 = await x.reply_text("جار المنتجة") 
      imgfile = await x.download(file_name="./downloads/")
      filename = os.path.basename(imgfile)
      nom,ex = os.path.splitext(filename)
      mp4file = f"{nom}.mp4"
      mp3file = f"{nom}.mp3"
      audfilemon = await montaglist[0].download(file_name="./downloads/")
      os.system(f'''ffmpeg -i "{audfilemon}" -q:a 0 -map a "{mp3file}" -y ''')
      os.system(f'''ffmpeg -r 1 -loop 1 -y -i  "{imgfile}" -i "{mp3file}" -c:v libx264 -tune stillimage -c:a copy -shortest -vf scale=1920:1080 "{mp4file}"''')
      await bot.send_video(imgid, mp4file)
      await replo2.edit_text("تمت المنتجة  ✅  ")
      os.remove(imgfile) 
      os.remove(mp4file)
      os.remove(mp3file) 
      os.remove(audfilemon) 
      montaglist.clear()
      
     elif x.audio or x.voice and len(montaglist) == 0 :
      await replo.edit_text("معالجة ⏱️")
      montaglist.append(x)
      await replo.edit_text("الآن أرسل الصورة") 
      
     elif x.audio or x.voice and len(montaglist) == 1 and montaglist[0].photo  :
      await replo.delete()
      replo2 = await x.reply_text("جار المنتجة") 
      audfilemon = await x.download(file_name="./downloads/")
      filename = os.path.basename(audfilemon)
      nom,ex = os.path.splitext(filename)
      mp4file = f"{nom}.mp4"
      mp3file = f"{nom}.mp3"
      imgfile = await montaglist[0].download(file_name="./downloads/")
      os.system(f'''ffmpeg -i "{audfilemon}" -q:a 0 -map a "{mp3file}" -y ''')
      os.system(f'''ffmpeg -r 1 -loop 1 -y -i  "{imgfile}" -i "{mp3file}" -c:v libx264 -tune stillimage -c:a copy -shortest -vf scale=1920:1080 "{mp4file}"''')
      await bot.send_video(imgid, mp4file)
      await replo2.edit_text("تمت المنتجة  ✅  ")
      os.remove(audfilemon) 
      os.remove(mp4file)
      os.remove(mp3file) 
      os.remove(imgfile)
      montaglist.clear()
     else :
       montaglist.clear()
       return imagetovidfunc(x)

################ إبدال صوت فيديو ###

async def vidaudsub(x,replo):
      resid = x.from_user.id 
      if x.video and len(vidsubslist) == 0 :
         await replo.edit_text("معالجة ⏱️")
         vidsubslist.append(x)
         await replo.edit_text("الآن أرسل الصوتية")
         vidaudsubid = x.from_user.id
      elif x.video and len(vidsubslist) == 1 and not vidsubslist[0].video :
       await replo.delete()
       replo2 = await x.reply_text("جار الإبدال ") 
       vidfile = await x.download(file_name="./downloads/")
       filename = os.path.basename(vidfile)
       nom,ex = os.path.splitext(filename)
       mp4file = f"{nom}.mp4"
       audfile = await vidsubslist[0].download(file_name="./downloads/")
       os.system(f'''ffmpeg -i "{vidfile}" -i "{audfile}" -c:v copy -map 0:v:0 -map 1:a:0 "{mp4file}"''')
       await bot.send_video(resid, mp4file)
       await replo2.edit_text("تم الإبدال ✅  ") 
       os.remove(vidfile) 
       os.remove(mp4file) 
       os.remove(audfile) 
       vidsubslist.clear()
       
      elif x.audio or x.voice and len(vidsubslist) == 0 :
        await replo.edit_text("معالجة ⏱️")
        vidsubslist.append(x)
        await replo.edit_text("الآن أرسل الفيديو")
        
      elif x.audio or x.voice and len(vidsubslist) == 1 and vidsubslist[0].video  :
       await replo.delete()
       replo2 = await x.reply_text("جار الإبدال ") 
       audfile = await x.download(file_name="./downloads/")
       filename = os.path.basename(audfile)
       nom,ex = os.path.splitext(filename)
       mp4file = f"{nom}.mp4"
       vidfile = await vidsubslist[0].download(file_name="./downloads/")
       os.system(f'''ffmpeg -i "{vidfile}" -i "{audfile}" -c:v copy -map 0:v:0 -map 1:a:0 "{mp4file}"''')
       await bot.send_video(resid, mp4file)
       await replo2.edit_text("تم الإبدال ✅  ")
       os.remove(audfile) 
       os.remove(mp4file) 
       os.remove(vidfile) 
       vidsubslist.clear()
       
      else :
        vidsubslist.clear()
        return vidaudsub(x)
        
################## ترجمة + فيديو #######
        
async def vidsrtfunc(x,replo):
     vrtid = x.from_user.id
     if (len(vidsrt) == 0 or len(vidsrt) > 2 ) and x.document :
        await replo.edit_text("معالجة ⏱️")
        vidsrt.clear()
        vidsrt.append(x)
        await replo.edit_text("الآن أرسل الفيديو")
        
     elif (len(vidsrt) == 0 or len(vidsrt) > 2 ) and (x.video) :
        await replo.edit_text("معالجة ⏱️")
        vidsrt.clear()
        vidsrt.append(x)
        await replo.edit_text("الآن أرسل ملف الترجمة")
        
     elif (len(vidsrt) == 1) and (x.video ) and not vidsrt[0].video   : 
        await replo.delete()
        replo2 = await x.reply_text("جار الدمج ⏱️") 
        vidfile = await x.download(file_name="./downloads/")
        filename = os.path.basename(srtpath)
        nom,ex = os.path.splitext(filename)
        mp4file = f"{nom}.mp4"
        subfile = await vidsrt[0].download(file_name="./downloads/")
        os.system(f'''ffmpeg -i "{vidfile}" -filter_complex subtitles='{subfile}' -c:a copy "{mp4file}"''')
        await bot.send_video(vrtid,mp4file)
        await replo2.edit_text("تم الدمج  ✅  ")
        os.remove(subfile)
        os.remove(vidfile)
        os.remove(mp4file)
        vidsrt.clear()
        
     elif (len(vidsrt) == 1) and x.document and vidsrt[0].video  : 
        await replo.delete()
        replo2 = await x.reply_text("جار الدمج ⏱️")
        subfile = await x.download(file_name="./downloads/")
        vidfile = await vidsrt[0].download(file_name="./downloads/")
        filename = os.path.basename(vidfile)
        nom,ex = os.path.splitext(filename)
        mp4file = f"{nom}.mp4"
        os.system(f'''ffmpeg -i "{vidfile}" -filter_complex subtitles='{subfile}' -c:a copy "{mp4file}"''')
        await bot.send_video(vrtid,mp4file)
        await replo2.edit_text("تم الدمج  ✅  ")
        os.remove(subfile)
        os.remove(vidfile)
        os.remove(mp4file)
        vidsrt.clear()
        
     else :
        vidsrt.clear()
        await x.reply_text("حدث خطأ ما")
