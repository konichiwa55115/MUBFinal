import os,subprocess
from youtube_transcript_api import YouTubeTranscriptApi
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from config import bot,checkdir

############## التحميل المنفرد #####

async def ytdlfunc(x,y,z):
     ytlink = x
     dlmode = y
     yt_id = z
     urldirect = "./urlgrap/"
     await checkdir(urldirect)
     if dlmode == "vid" :  
      try : 
     
       p = subprocess.Popen(["yt-dlp", "-f", "18", "-ciw",ytlink], cwd=urldirect)
       p.wait()
       dlfile = os.listdir(urldirect)[0]
       leechedfile = urldirect + dlfile
       dlfilex = '.' + dlfile.split('.')[-1]
       await bot.send_video(yt_id, leechedfile,caption=dlfile)
       os.remove(leechedfile)
      except DownloadError:
        await bot.send_message(yt_id,'الرابط غير صالح')
       
       
     elif dlmode == "vid720" :
       
       p = subprocess.Popen(["yt-dlp", "-f", "22", "-ciw",ytlink], cwd=urldirect)
       p.wait()
       dlfile = os.listdir(urldirect)[0]
       leechedfile = urldirect + dlfile
       dlfilex = '.' + dlfile.split('.')[-1]
       await bot.send_video(yt_id, leechedfile,caption=dlfile)
       os.remove(leechedfile)
       
     elif dlmode == "aud" : 
      try:
       p = subprocess.Popen(["yt-dlp", "-ciw", "--extract-audio","--audio-format", "mp3",ytlink], cwd=urldirect)
       p.wait()
       dlfile = os.listdir(urldirect)[0]
       leechedfile = urldirect + dlfile
       dlfilex = '.' + dlfile.split('.')[-1]
       await bot.send_audio(yt_id, leechedfile,caption=dlfile)
       os.remove(leechedfile)
      except DownloadError:
        await bot.send_message(yt_id,'الرابط غير صالح')
       
       
     elif dlmode == "direct" : 
      
       p = subprocess.Popen(["wget",ytlink], cwd=urldirect)
       p.wait()
       dlfile = os.listdir(urldirect)[0]
       leechedfile = urldirect + dlfile
       dlfilex = '.' + dlfile.split('.')[-1]
       if dlfilex in audioforms :
         await bot.send_audio(yt_id,leechedfile)
       elif dlfilex in videoforms :
         await bot.send_video(yt_id,leechedfile)
       else : 
         await bot.send_document(yt_id,leechedfile)
       os.remove(leechedfile)
      

     elif dlmode == "svid":
      
      try:
       video = str(random.randint(0,1000)) + ".mp4"
       cap = YoutubeDL().extract_info(ytlink, download=False).get("title", None) 
       p = subprocess.Popen(["yt-dlp","-ciw","-o",video,ytlink], cwd=urldirect)
       p.wait()
       leechedfile = urldirect + video
       await bot.send_video(yt_id,leechedfile,caption=cap)
       os.remove(leechedfile)
      except DownloadError:
        await bot.send_message(yt_id,'الرابط غير صالح')
          
        
       
     elif dlmode=="saud":
      try:
       audio = str(random.randint(0,1000)) + ".mp3"
       cap = YoutubeDL().extract_info(ytlink, download=False).get("title", None)
       p = subprocess.Popen(["yt-dlp", "-ciw", "--extract-audio","--audio-format", "mp3","-o",audio,ytlink], cwd=urldirect)
       p.wait()
       leechedfile = urldirect + audio
       await bot.send_audio(yt_id,leechedfile,caption=cap)
       os.remove(leechedfile)
      except DownloadError:
        await bot.send_message(yt_id,'الرابط غير صالح')
       
########## تحميل القوائم #######

async def ytplstfunc(linky,dlmodey,ytplstidy,numby="0") :
  url = linky
  dlmode = dlmodey
  ytplstid = ytplstidy
  listtext = "yttransy.txt"
  cmd(f'''yt-dlp --flat-playlist -i --print-to-file url {listtext} {url}''')
  urls = open(listtext,'r').readlines()
  for i in range(int(numby),len(urls)) :
    await ytdlfunc(urls[i],dlmode,ytplstid)
  os.remove(listtext)



############# تحميل ملف الترجمة ######

def ytsubfunc(x,y):
  ytlink = x
  yt_id = y
  with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(f'{ytlink}', download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None).replace('＂', '').replace('"', '').replace("'", "").replace("｜", "").replace("|", "")
        subfile = f"{video_title}.txt"
  srt = YouTubeTranscriptApi.get_transcript(video_id,languages=['ar'])
  with open(subfile, "w") as f:
            for i in srt:
             f.write(f" {i['text']} ")
  bot.send_document(yt_id,subfile)
  os.remove(subfile)

############ تحميل ملفات الترجمة بالقوائم ########


def ytsubplstfunc(x,y,n="0") :
  url = x
  ytplstid = y
  playlist = Playlist(url)
  for i in range(int(n),len(playlist)) :
    ytsubfunc(playlist[i],ytplstid)
