import os,shutil,cv2
from pyrogram import Client
premiumids = [6234365091,2003751632,6762468805,6440064616,683965784]
msrmvprmids = [937922509]
imageforms = [".jpg",".png"]
audioforms = [".mp3",".ogg",".m4a",".aac",".flac",".wav",".wma",".opus"]
videoforms = [".mp4",".mkv",".mov",".avi",".wmv",".avchd",".webm",".flv"]
subtitleforms = ['.ass','.srt']
temptxt = "res.txt"

async def checkdir(dir):
  if os.path.isdir(dir):
      shutil.rmtree(pdfocrdir)
  os.mkdir(dir)
 
async def getdur(twittervidpath)
     cap = cv2.VideoCapture(twittervidpath)
     fps = cap.get(cv2.CAP_PROP_FPS)
     totalNoFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
     durationInSeconds = totalNoFrames // fps
     videodur = int(durationInSeconds)
     return videodur
    
bot = Client(
    "MultiUsageBotFinal",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5782497998:AAFdx2dX3yeiyDIcoJwPa_ghY2h_dozEh_E"
)
#6032076608:AAGhqffAlibHd7pipzA3HR2-0Ca3sDFlmdI 
#5782497998:AAFdx2dX3yeiyDIcoJwPa_ghY2h_dozEh_E
#6306753444:AAFnoiusUbny-fpy4xxZWYqGNh_c7yOioW8
#6709809460:AAGWWXJBNMF_4ohBNRS22Tg0Q3-vkm376Eo
#6466415254:AAE_m_mYGHFuu3MT4T0qzqVCm0WvR4biYvM
#6812722455:AAEjCb1ZwgBa8DZ4_wVNNjDZbe6EtQZOUxo
