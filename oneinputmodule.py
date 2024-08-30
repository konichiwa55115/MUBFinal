from config import audioforms,videoforms,bot
from os import system as cmd
from pydub import AudioSegment
import noisereduce as nr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
from telegraph import upload_file



########## إزالة الضوضاء ####

async def noisermvfunc(path,mp3file):
    audio = AudioSegment.from_file(path)
    samples = np.array(audio.get_array_of_samples())
    reduced_noise = nr.reduce_noise(samples, sr=audio.frame_rate,stationary=True,prop_decrease=0.75)
    fig, ax = plt.subplots(2, 1, figsize=(15,8))
    ax[0].set_title("Original signal")
    ax[0].plot(samples)
    ax[1].set_title("Reduced noise signal")
    ax[1].plot(reduced_noise)
    plt.show()
    reduced_audio = AudioSegment(
    reduced_noise.tobytes(), 
    frame_rate=audio.frame_rate, 
    sample_width=audio.sample_width, 
    channels=audio.channels)
    reduced_audio.export(mp3file, format="mp3")

######### التضخيم #####

async def amplify(amplemode):
 amplepath = await amplemessage.download(file_name="./downloads/")
 filename = os.path.basename(amplepath)
 nom,ex = os.path.splitext(filename)
 mp4file = f"{nom}.mp4"
 mp3file = f"{nom}.mp3"
 if ex in audioforms :
        amplaudid = amplemessage.from_user.id
        cmd(f'''ffmpeg -i "{amplepath}" -filter:a volume={amplemode}dB "{mp3file}"''')
        await bot.send_audio(amplaudid, mp3file)
        os.remove(mp3file) 
 elif ex in videoforms :
        amplvidid = amplemessage.from_user.id
        cmd(f'''ffmpeg -i "{amplepath}" -filter:a volume={amplemode}dB "{mp3file}"''')
        cmd(f'''ffmpeg -i "{amplepath}" -i "{mp3file}" -c:v copy -map 0:v:0 -map 1:a:0 "{mp4file}"''')
        await bot.send_video(amplvidid, mp4file) 
        os.remove(mp4file) 
 os.remove(amplepath) 
        
        
################## التحويل 

async def convy(k):
   convpath = await convmessage.download(file_name="./downloads/")
   filename = os.path.basename(convpath)
   nom,ex = os.path.splitext(filename)
   m4afile = f"{nom}.m4a"
   mp4file = f"{nom}.mp4"
   mp3file = f"{nom}.mp3"
   if k == "m4afile" :
       convaudid = convmessage.from_user.id
       cmd(f'''ffmpeg -i "{convpath}" -c:a aac -b:a 192k "{m4afile}" -y ''')
       await bot.send_audio(convaudid, m4afile)
       os.remove(m4afile) 
   elif k == "mp3file" :
      convaudmp3id = convmessage.from_user.id
      cmd(f'''ffmpeg -i "{convpath}" -q:a 0 -map a "{mp3file}" -y ''')
      await  bot.send_audio(convaudmp3id, mp3file)
      os.remove(mp3file)
   elif k == "mp4file" :
      convvidid = convmessage.from_user.id
      cmd(f'''ffmpeg -i "{convpath}" -codec copy "{mp4file}" -y ''')
      await bot.send_video(convvidid, mp4file)
      os.remove(mp4file) 
   os.remove(convpath) 
      
########### التسريع

async def spoody(speedmessage,spdrateaud,spdratevid):
    speedpath = await speedmessage.download(file_name="./downloads/")
    filename = os.path.basename(speedpath)
    nom,ex = os.path.splitext(filename)
    mp4file = f"{nom}.mp4"
    mp3file = f"{nom}.mp3"
    if ex in audioforms :
      spdaudid = speedmessage.from_user.id
      cmd(f'''ffmpeg -i "{speedpath}" -filter:a "atempo={spdrateaud}" -vn "{mp3file}" -y ''')
      await bot.send_audio(spdaudid, mp3file) 
      os.remove(mp3file) 
    elif ex in videoforms :
       spdvidid = speedmessage.from_user.id
       cmd(f'''ffmpeg -i "{speedpath}" -filter_complex "[0:v]setpts={spdratevid}*PTS[v];[0:a]atempo={spdrateaud}[a]" -map "[v]" -map "[a]" "{mp4file}" -y ''')
       await  bot.send_video(spdvidid,mp4file)
       os.remove(mp4file)
    os.remove(speedpath) 
       
       
############ التبطيء

async def slowfunc(spdratevid,spdrateaud):
    slowpath = await slowmessage.download(file_name="./downloads/")
    filename = os.path.basename(slowpath)
    nom,ex = os.path.splitext(filename)
    mp4file = f"{nom}.mp4"
    mp3file = f"{nom}.mp3"
    if ex in audioforms :
      slowaudid = slowmessage.from_user.id
      cmd(f'''ffmpeg -i "{slowpath}" -filter:a "atempo={spdrateaud}" -vn "{mp3file}" -y ''')
      await bot.send_audio(slowaudid, mp3file) 
      os.remove(mp3file) 
    elif ex in videoforms :
       slowvidid = slowmessage.from_user.id
       cmd(f'''ffmpeg -i "{slowpath}" -filter_complex "[0:v]setpts={spdratevid}*PTS[v];[0:a]atempo={spdrateaud}[a]" -map "[v]" -map "[a]" "{mp4file}" -y ''')
       await  bot.send_video(slowvidid,mp4file)
       os.remove(mp4file) 
    os.remove(slowpath) 
    
##### وضع العامود الواحد ###

async def pdfonepagefunc(filepath):
    img = Image.open(filepath)
    (width, height) = img.size
    width = int(width)
    height = int(height)
    img1width = int(int(width) / 2)
    result1 = Image.new('RGB', (img1width, height))
    result2 = Image.new('RGB', (img1width, height))
    image1 = img.crop(box=(0,0,img1width,height))
    image2 = img.crop(box=(img1width,0,width,height))
    result1.paste(image1, box=(0, 0))
    result2.paste(image2, box=(0, 0))
    return result1,result2
   
####### الرفع لتلغراف ######

async def upld2telegraph(upldtotelegraphmessage):
        upldtelegraphpath = await upldtotelegraphmessage.download(file_name="./downloads/")
        try:
            response = upload_file(upldtelegraphpath)
        except:
            await upldtotelegraphmessage.reply("يجب أن يكون حجم الملف أقل من 5 ميغا ") 
        else:
            await upldtotelegraphmessage.reply(f'**تم رفع الملف إلى تلغراف \n\n📚https://telegra.ph{response[0]}**',disable_web_page_preview=False,)
        os.remove(upldtelegraphpath)
        
