import subprocess
from asyncstdlib.functools import reduce
from pyrogram import Client, filters,enums,StopTransmission,types
import os ,re , random ,shutil,asyncio ,requests,logging,time,string,datetime,httplib2,tempfile,traceback

from os import system as cmd
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery , ForceReply,Message
from PyPDF2 import PdfWriter, PdfReader
from pathlib import Path
from urllib.parse import urlparse, unquote

from checkparticipant import *
from musicrmv import *
from config import *
from oneinputmodule import *
from twoinputmodule import *
from multiinputmodule import *
from transcribe import *
from twitterupld import *
from ytdlpfunc import *
from ytupld import *
from upldtofbpage import *
from extract import *
from splitfunc import *
from color import *
from compress import *

fsub  = "sunnaybots"

ytregex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"


### Developed By @AbuMarthad


@bot.on_message(filters.command('apiswitch1') & filters.private)
async def command2(bot,message):
   if not (await pyro_fsub(bot, message,fsub) == True):
            return
   global CLIENT_ID,CLIENT_SECRET
   CLIENT_ID = "389708947332-oienmum8v600cegsnhb6puk4prsv3pf6.apps.googleusercontent.com"
   CLIENT_SECRET = "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"
   auth = GoogleAuth(CLIENT_ID,CLIENT_SECRET)
   url = auth.GetAuthUrl()
   button = [[InlineKeyboardButton(text="Authentication URL", url=url)],]
   await message.reply_text(text="الآن قم بتفعيل الـapi",reply_markup=InlineKeyboardMarkup(button),)
   help_callback_filter = filters.create(lambda _, __, query: query.data.startswith("help+") )
@bot.on_message(filters.command('apiswitch2') & filters.private)
async def command2(bot,message):
   if not (await pyro_fsub(bot, message,fsub) == True):
            return
   global CLIENT_ID,CLIENT_SECRET
   CLIENT_ID = "664256487809-21lnbeqr7cau7fng78oeli1bnqcjthvp.apps.googleusercontent.com"
   CLIENT_SECRET = "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"
   auth = GoogleAuth(CLIENT_ID,CLIENT_SECRET)
   url = auth.GetAuthUrl()
   button = [[InlineKeyboardButton(text="Authentication URL", url=url)],]
   await message.reply_text(text="الآن قم بتفعيل الـapi",reply_markup=InlineKeyboardMarkup(button),)
   help_callback_filter = filters.create(lambda _, __, query: query.data.startswith("help+") )


@bot.on_message(filters.command('setbucket') & filters.text & filters.private)
async def command9(bot,message):
  if not (await pyro_fsub(bot, message,fsub) == True):
            return
  global bucketname
  bucketname = message.text.split("setbucket", maxsplit=1)[1]
  bucketname = bucketname.replace(" ", "")
  await message.reply_text("تم ضبط المعرف ")
  

@bot.on_message(filters.command('ytsub') & filters.text & filters.private)
async def command20(bot,message):
     if not (await pyro_fsub(bot, message,fsub) == True):
            return
     ytlink = message.text.split("ytsub", maxsplit=1)[1].replace(" ", "")
     yt_id = message.from_user.id
     await ytsubfunc(ytlink,yt_id)

@bot.on_message(filters.command('ytsubplst') & filters.text & filters.private)
async def command20(bot,message):
     if not (await pyro_fsub(bot, message,fsub) == True):
            return
     ytlink = message.text.split(" ")[1]
     yt_id = message.from_user.id
     if len(message.text.split(" ")) == 2 :
      await ytsubplstfunc(ytlink,yt_id)
     elif len(message.text.split(" ")) == 3 :
      numpy = message.text.split(" ")[-1] 
      await ytsubplstfunc(ytlink,yt_id,numpy)
     

@bot.on_message(filters.command('clear') & filters.private)
async def command2(bot,message):
    if not (await pyro_fsub(bot, message,fsub) == True):
            return
    audmergelist.clear()
    vidmergelist.clear()
    montaglist.clear()
    vidsubslist.clear()
    imagedic.clear()
    imagepdfdic.clear()
    imagepdfdic1.clear()
    vidsrt.clear()
    audmergelist.clear()
    pdfqueemerge.clear()
    
    listofdirectories = ["ytplst.txt","yttransy.txt","./mergy/","./vidmerge/","./vidmerge2/","./downloads/","./unzipprocess/","./pdfmerge/","./data/","./parts/","./rvtemp/","./grtemp/","./temp/","./zipdir/"]
    for x in listofdirectories:
        if os.path.exists(x):
            if os.path.isdir(x):
               shutil.rmtree(x)
            else :
                os.remove(x)
    cmd("find  -type f -name '*mp4' -print    -delete")
    cmd("find  -type f -name '*mp3' -print    -delete")
    cmd("find  -type f -name '*jpg' -print    -delete")
    cmd("find  -type f -name '*png' -print    -delete")
    cmd("find  -type f -name '*pdf' -print    -delete")
    await bot.send_message(message.from_user.id,'تم المحو ☑️')
    
   

@bot.on_message(filters.private & filters.incoming & filters.text & filters.regex('4/1A') | filters.regex('EAAFyBZAo9GtgBO') )
async def _api_code(client, message):
    if not (await pyro_fsub(bot, message, fsub) == True):
            return
    apimessage = message.text
    if '4/1A' in apimessage :
        code = apimessage.replace(" ", "")
        try:
            auth = GoogleAuth(CLIENT_ID, CLIENT_SECRET)

            auth.Auth(code)

            auth.SaveCredentialsFile("auth_token.txt")

            msg = await message.reply_text("تمت المصادقة بنجاح ", True)
            with open("auth_token.txt", "r") as f:
                cred_data = f.read()
        except Exception as e:
            await message.reply_text("فشلت المصادقة للأسف", True)
    elif 'EAAFyBZAo9GtgBO' in apimessage :
        global FBAPI
        FBAPI = apimessage.replace(" ", "")
        await message.reply_text("تم ضبط API ")


   
   

    ########### الوظائف الرئيسية ###########
@bot.on_message(filters.command('start') & filters.private)
async def command1(bot,message):
    if not (await pyro_fsub(bot, message,fsub) == True):
            return
    await bot.send_message(message.chat.id, " السلام عليكم أنا بوت متعدد الاستعمالات , فقط أرسل الفيديو أو الصوتية أو الملف هنا\n\n [طريقة استعمال البوت](https://telegra.ph/%D8%B7%D8%B1%D9%8A%D9%82%D8%A9-%D8%A7%D8%B3%D8%AA%D8%B9%D9%85%D8%A7%D9%84-%D8%A7%D9%84%D8%A8%D9%88%D8%AA-01-20) \n\n [لبقية البوتات](https://t.me/sunnaybots/2) ",disable_web_page_preview=True)

@bot.on_message(filters.private & filters.incoming & filters.voice | filters.audio | filters.video | filters.document | filters.photo | filters.animation )
async def _telegram_file(client, message):
 if not (await pyro_fsub(bot, message,fsub) == True):
            return
 global  replo,nepho,temponame,nomo,exo
 nepho = message  
 if nepho.video :
      fileesize = round(int(nepho.video.file_size)/(1024*1024),2)
 elif nepho.audio :
        fileesize = round(int(nepho.audio.file_size)/(1024*1024),2)
 elif nepho.document :
        fileesize = round(int(nepho.document.file_size)/(1024*1024),2)
 elif nepho.photo or nepho.voice :
    fileesize = 1
 if int(fileesize) <= 200 :
       pass
 elif int(nepho.from_user.id) in premiumids :
    pass
 else :
       await nepho.reply("🛑 مسموح بملفات حجمها أقل من 200 ميغا \n \n 🟥 لإزالة القيد يمكنك الاشتراك في الباقة المميزة \n\n https://t.me/sunnaybots/9 ",disable_web_page_preview=True) 
       return
 if nepho.photo :
  nomo = nepho.photo.file_unique_id
  exo = ".jpg"
 elif nepho.voice :
  nomo = nepho.voice.file_unique_id
  exo = ".ogg"
 elif nepho.audio : 
  temponame = nepho.audio.file_name.lower()
  nomo,exo = os.path.splitext(temponame)
 elif nepho.video : 
  nomo = nepho.video.file_unique_id
  exo = ".mp4"
 elif nepho.document  : 
  temponame = nepho.document.file_name.lower()
  nomo,exo = os.path.splitext(temponame)
 if 'mergeid' in globals() and mergeid== nepho.from_user.id and exo in audioforms :
    await audmerge(nepho)
    return 
 if 'vidsrtid' in globals() and vidsrtid == nepho.from_user.id and (exo in subtitleforms or exo in videoforms) :
   if (exo in videoforms and len(vidsrt) == 1 and  vidsrt[0].video ) or (exo in subtitleforms and len(vidsrt) == 1 and not vidsrt[0].video) :
    pass
   else :
    await vidsrtfunc(nepho,replo)
    del globals()['vidsrtid']
    return
 if 'imagetovidid' in globals() and imagetovidid == nepho.from_user.id and ( exo in audioforms or exo in imageforms) :
      if (exo in audioforms and len(montaglist) == 1 and not montaglist[0].photo ) or (exo in imageforms and len(montaglist) == 1 and (montaglist[0].photo)) :
        pass 
      else :
         await imagetovidfunc(nepho,replo)
         del globals()['imagetovidid']
         return 
 if 'vidaudsubid' in globals() and vidaudsubid == nepho.from_user.id and ( exo in audioforms or exo in videoforms) :
    if (exo in audioforms and len(vidsubslist) == 1 and not vidsubslist[0].video ) or (exo in videoforms and len(vidsubslist) == 1 and (vidsubslist[0].video)) :
        pass 
    else :
         await vidaudsub(nepho,replo)
         del globals()['vidaudsubid']
         return 
 if 'zipfileid' in globals() and zipfileid == nepho.from_user.id :
         await zipfilefunc(nepho)
         return 
 if 'vidmergeid' in globals() and vidmergeid == nepho.from_user.id and exo in videoforms :
         await videomerge(nepho)
         return 
 if 'pdfmergeid' in globals() and pdfmergeid == nepho.from_user.id and exo == ".pdf" :
         await pdfmerge(nepho)
         return         
 if 'photomergeid' in globals() and photomergeid == nepho.from_user.id and exo in imageforms :
         await photomerge(nepho)
         return  
 if 'imageconvid' in globals() and imageconvid == nepho.from_user.id and exo in imageforms :
         await image2pdf(nepho)
         return
 
 if exo in audioforms :
  
  CHOOSE_UR_AUDIOUSER_MODE = "اختر العملية  التي تريد "
  CHOOSE_UR_AUDIOUSER_MODE_BUTTONS = [
    [InlineKeyboardButton("تضخيم  ",callback_data="amplifyaud"),InlineKeyboardButton("قص ",callback_data="trim"),InlineKeyboardButton("ضغط ",callback_data="comp")],
    [InlineKeyboardButton("تسريع ",callback_data="speedy"),InlineKeyboardButton("تبطيئ",callback_data="slowly"),InlineKeyboardButton("تحويل ",callback_data="conv")], 
    [InlineKeyboardButton("دمج  ",callback_data="audmerge"),InlineKeyboardButton("إعادة التسمية ",callback_data="renm"),InlineKeyboardButton("تفريغ ",callback_data="transcribe")],
    [InlineKeyboardButton("تغيير الصوت",callback_data="voicy"),InlineKeyboardButton("ضغط الملفات ",callback_data="zipfile"),InlineKeyboardButton("تقسيم الصوتية ",callback_data="splitty")],
    [InlineKeyboardButton("الرفع لأرشيف",callback_data="upldarch"),InlineKeyboardButton("منتجة فيديو ",callback_data="imagetovid"),InlineKeyboardButton(" التفاصيل  ",callback_data="detailsoffile")],
    [InlineKeyboardButton("إبدال صوت الفيديو ",callback_data="subs"),InlineKeyboardButton("إزالة الصمت",callback_data="rmvsilence"),InlineKeyboardButton("إزالة ضوضاء",callback_data="noisermv")],
    [ InlineKeyboardButton(" إزالة الموسيقا ",callback_data="mscrmv")]]
  replo = await nepho.reply(text = CHOOSE_UR_AUDIOUSER_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_AUDIOUSER_MODE_BUTTONS))
 elif exo in videoforms :
  CHOOSE_UR_VIDEO_MODE = "اختر العملية  التي تريد "
  CHOOSE_UR_VIDEO_MODE_BUTTONS = [
    
    [InlineKeyboardButton("تضخيم  ",callback_data="amplifyaud"),InlineKeyboardButton("قص ",callback_data="trim"),InlineKeyboardButton("ضغط ",callback_data="comp")],
    [InlineKeyboardButton("تسريع ",callback_data="speedy"),InlineKeyboardButton("تبطيئ",callback_data="slowly"),InlineKeyboardButton("تحويل ",callback_data="conv")], 
    [InlineKeyboardButton("دمج  ",callback_data="audmerge"),InlineKeyboardButton("إعادة التسمية ",callback_data="renm"),InlineKeyboardButton("تفريغ ",callback_data="transcribe")],
    [InlineKeyboardButton("تغيير الصوت",callback_data="voicy"),InlineKeyboardButton("ضغط الملفات ",callback_data="zipfile"),InlineKeyboardButton("الرفع لتويتر",callback_data="upldtotwitter")],
    [InlineKeyboardButton("الرفع لأرشيف",callback_data="upldarch"),InlineKeyboardButton("الرفع ليوتيوب",callback_data="upldtout"),InlineKeyboardButton("الرفع لفيسبوك",callback_data="manuscript")],
    [InlineKeyboardButton(" ترجمة + فيديو",callback_data="vidsrt"),InlineKeyboardButton("تغيير الأبعاد  ",callback_data="vidasp"),InlineKeyboardButton("الرفع لتلغراف",callback_data="upldtotelegraph")],
    [InlineKeyboardButton("إبدال صوت الفيديو ",callback_data="subs"),InlineKeyboardButton("كتم الصوت ",callback_data="mute"),InlineKeyboardButton("إزالة الصمت",callback_data="rmvsilence")],
    [InlineKeyboardButton(" تقسيم  ",callback_data="vidsplit"),InlineKeyboardButton(" التفاصيل  ",callback_data="detailsoffile"),InlineKeyboardButton(" إزالة الموسيقا ",callback_data="mscrmv")]]
  replo = await nepho.reply(text = CHOOSE_UR_VIDEO_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_VIDEO_MODE_BUTTONS))
 elif exo == ".pdf":
    CHOOSE_UR_PDF_MODE = "اختر العملية  التي تريد "
    CHOOSE_UR_PDF_MODE_BUTTONS = [
    
    [InlineKeyboardButton("قص ",callback_data="trim"),InlineKeyboardButton("ضغط ",callback_data="comp"),InlineKeyboardButton("إعادة التسمية ",callback_data="renm")],
    [InlineKeyboardButton("دمج  ",callback_data="audmerge"),InlineKeyboardButton("تفريغ ",callback_data="transcribe"),InlineKeyboardButton(" التفاصيل  ",callback_data="detailsoffile")],
    [InlineKeyboardButton("ضغط الملفات ",callback_data="zipfile"),InlineKeyboardButton("استخراج",callback_data="unzip"),InlineKeyboardButton("الرفع لأرشيف",callback_data="upldarch")],
    [InlineKeyboardButton("عكس pdf",callback_data="reversepdf"),InlineKeyboardButton(" وضع العامود الواحد",callback_data="pdfonepagemode")]]
    replo = await nepho.reply(text = CHOOSE_UR_PDF_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_PDF_MODE_BUTTONS))
    
 elif exo in imageforms :
    CHOOSE_UR_IMAGE_MODE = "اختر العملية  التي تريد "
    CHOOSE_UR_IMAGE_MODE_BUTTONS = [[InlineKeyboardButton("تحويل ",callback_data="conv"),InlineKeyboardButton("الرفع لتلغراف",callback_data="upldtotelegraph")],
      [InlineKeyboardButton("دمج  ",callback_data="audmerge"),InlineKeyboardButton("إعادة التسمية ",callback_data="renm")],
      [InlineKeyboardButton("تلوين",callback_data="coloring"),InlineKeyboardButton("تفريغ ",callback_data="transcribe")],
      [InlineKeyboardButton("الرفع لأرشيف",callback_data="upldarch"),InlineKeyboardButton("ضغط الملفات ",callback_data="zipfile")],
      [InlineKeyboardButton("منتجة فيديو ",callback_data="imagetovid"),InlineKeyboardButton("صورة إلى gif",callback_data="imagetogif")]]

    replo = await nepho.reply(text = CHOOSE_UR_IMAGE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_IMAGE_MODE_BUTTONS))
 elif exo == ".epub" or exo == ".zip":
    CHOOSE_UR_EPUB_MODE = "اختر العملية  التي تريد "
    CHOOSE_UR_EPUB_MODE_BUTTONS = [
    
    [InlineKeyboardButton("استخراج",callback_data="unzip"),InlineKeyboardButton("إعادة التسمية ",callback_data="renm")],
    [InlineKeyboardButton(" التفاصيل  ",callback_data="detailsoffile"),InlineKeyboardButton("الرفع لأرشيف",callback_data="upldarch")]]
    replo = await nepho.reply(text = CHOOSE_UR_EPUB_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_EPUB_MODE_BUTTONS))
 elif exo in subtitleforms :
    CHOOSE_UR_SUBTITLE_MODE = "اختر العملية  التي تريد "
    CHOOSE_UR_SUBTITLE_MODE_BUTTONS = [
    
    [InlineKeyboardButton("ترجمة + فيديو",callback_data="vidsrt"),InlineKeyboardButton("إعادة التسمية ",callback_data="renm")],
    [InlineKeyboardButton(" التفاصيل  ",callback_data="detailsoffile"),InlineKeyboardButton("الرفع لأرشيف",callback_data="upldarch")]
]

    replo = await nepho.reply(text = CHOOSE_UR_SUBTITLE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_SUBTITLE_MODE_BUTTONS))
 else:
    CHOOSE_UR_TEXT_MODE = "اختر العملية  التي تريد "
    CHOOSE_UR_TEXT_MODE_BUTTONS = [
    
    [InlineKeyboardButton("إعادة التسمية ",callback_data="renm")],
    [InlineKeyboardButton(" التفاصيل  ",callback_data="detailsoffile"),InlineKeyboardButton("الرفع لأرشيف",callback_data="upldarch")]]

    replo = await nepho.reply(text = CHOOSE_UR_TEXT_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_TEXT_MODE_BUTTONS))
  


 @bot.on_callback_query()
 async def callback_query(CLIENT,CallbackQuery): 

########## خواص التضخيم ###########
  if CallbackQuery.data == "amplifyaud" and CallbackQuery.from_user.id == nepho.from_user.id:
     if exo in audioforms or exo in videoforms :
      global amplemessage
      amplemessage = nepho
      CHOOSE_UR_AMPLE_MODE = "اختر نمط التضخيم "
      CHOOSE_UR_AMPLE_MODE_BUTTONS = [
    [InlineKeyboardButton("5db",callback_data="mod1")],
     [InlineKeyboardButton("10db",callback_data="mod2")],
     [InlineKeyboardButton("15db",callback_data="mod3")],
     [InlineKeyboardButton("20db",callback_data="mod4")],
     [InlineKeyboardButton("25db",callback_data="mod5")]]
      await CallbackQuery.edit_message_text(text = CHOOSE_UR_AMPLE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_AMPLE_MODE_BUTTONS))
          
  elif CallbackQuery.data == "mod1":
      await CallbackQuery.edit_message_text("جار التضخيم ")
      await amplify(5,amplemessage)
      await CallbackQuery.edit_message_text("تم التضخيم ✅  ")

  elif CallbackQuery.data == "mod2":
      await CallbackQuery.edit_message_text("جار التضخيم ")
      await amplify(10,amplemessage)
      await CallbackQuery.edit_message_text("تم التضخيم ✅  ")
         
      
  elif CallbackQuery.data == "mod3":
      await CallbackQuery.edit_message_text("جار التضخيم ")
      await amplify(15,amplemessage)
      await CallbackQuery.edit_message_text("تم التضخيم ✅  ") 
        

  elif CallbackQuery.data == "mod4" :
      await CallbackQuery.edit_message_text("جار التضخيم ")
      await amplify(20,amplemessage)
      await CallbackQuery.edit_message_text("تم التضخيم ✅  ")
         

  elif CallbackQuery.data == "mod5":
      await CallbackQuery.edit_message_text("جار التضخيم ")
      await amplify(25,amplemessage)
      await CallbackQuery.edit_message_text("تم التضخيم ✅  ") 
        


 ########## خواص الضغط ###########

  
  elif CallbackQuery.data == "comp" and CallbackQuery.from_user.id == nepho.from_user.id:
   if exo in audioforms or exo in videoforms or exo == ".pdf" :
       
       if exo == ".pdf":
          await CallbackQuery.edit_message_text("جار الضغط")
          pdfcompmessage = nepho
          await pdfcompress(pdfcompmessage)
          await CallbackQuery.edit_message_text("تم الضغط ✅  ")   
          
           
       elif exo in videoforms:
        await CallbackQuery.edit_message_text("جار الضغط ")
        vidcompmessage = nepho
        await vidcompress(vidcompmessage)

        await CallbackQuery.edit_message_text("تم الضغط ✅  ")   
        
        
       elif exo in audioforms:
        global audcompmessage
        audcompmessage = nepho
        CHOOSE_UR_COMP_MODE = " اختر نمط الضغط \n كلما قل الرقم زاد الضغط و قل حجم الصوتية "
        CHOOSE_UR_COMP_MODE_BUTTONS = [
    [InlineKeyboardButton("10k",callback_data="compmod1")],
     [InlineKeyboardButton("20k",callback_data="compmod2")],
     [InlineKeyboardButton("30k",callback_data="compmod3")],
     [InlineKeyboardButton("40k",callback_data="compmod4")],
     [InlineKeyboardButton("50k",callback_data="compmod5")]]

        await CallbackQuery.edit_message_text(text = CHOOSE_UR_COMP_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_COMP_MODE_BUTTONS) )
      

  elif  CallbackQuery.data == "compmod1":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    await compressaud("10k",audcompmessage)
    await CallbackQuery.edit_message_text("تم الضغط ✅  ") 
      

  elif  CallbackQuery.data == "compmod2":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    await compressaud("20k",audcompmessage)
    await CallbackQuery.edit_message_text("تم الضغط ✅  ") 
      

  elif  CallbackQuery.data == "compmod3":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    await compressaud("30k",audcompmessage) 
    await CallbackQuery.edit_message_text("تم الضغط ✅  ") 
      

  elif  CallbackQuery.data == "compmod4":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    await compressaud("40k",audcompmessage)
    await CallbackQuery.edit_message_text("تم الضغط ✅  ")
    

  elif  CallbackQuery.data == "compmod5":
    await CallbackQuery.edit_message_text("جار الضغط ") 
    await compressaud("50k",audcompmessage)
    await CallbackQuery.edit_message_text("تم الضغط ✅  ")   
    

 ########## خاصية التسريع  ###########
       
  elif CallbackQuery.data == "speedy" and CallbackQuery.from_user.id == nepho.from_user.id:
   if exo in audioforms or exo in videoforms :
    global speedmessage 
    speedmessage = nepho
    CHOOSE_UR_SPEED_MODE = "اختر نمط التسريع "
    CHOOSE_UR_SPEED_MODE_BUTTONS = [
    [InlineKeyboardButton("x1.25",callback_data="spd1")],
    [InlineKeyboardButton("x1.3",callback_data="spd1.2")],
     [InlineKeyboardButton("x1.5 ",callback_data="spd2")],
     [InlineKeyboardButton("x1.75",callback_data="spd3")],
      [InlineKeyboardButton("x2",callback_data="spd4")]]

    await CallbackQuery.edit_message_text(text = CHOOSE_UR_SPEED_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_SPEED_MODE_BUTTONS))
      

  elif CallbackQuery.data == "spd1":
   await CallbackQuery.edit_message_text("جار التسريع")
   await spoody(speedmessage,1.25,0.8)
   await CallbackQuery.edit_message_text("تم التسريع ✅  ") 
     
  elif CallbackQuery.data == "spd1.2":
   await CallbackQuery.edit_message_text("جار التسريع")
   await spoody(speedmessage,1.3,0.7692307692307)
   await CallbackQuery.edit_message_text("تم التسريع ✅  ") 
     
  elif CallbackQuery.data == "spd2":
    await CallbackQuery.edit_message_text("جار التسريع")
    await spoody(speedmessage,1.5,0.66666666666)
    await CallbackQuery.edit_message_text("تم التسريع ✅  ") 
    
  elif CallbackQuery.data == "spd3":
    await CallbackQuery.edit_message_text("جار التسريع")
    await spoody(speedmessage,1.75,0.57142857142)
    await CallbackQuery.edit_message_text("تم التسريع ✅  ") 
    
  elif CallbackQuery.data == "spd4":
    await CallbackQuery.edit_message_text("جار التسريع")
    await spoody(speedmessage,2,0.5) 
    await CallbackQuery.edit_message_text("تم التسريع ✅  ") 
    

  
  elif CallbackQuery.data == "slowly" and CallbackQuery.from_user.id == nepho.from_user.id:
   if exo in audioforms or exo in videoforms :
    global slowmessage
    slowmessage = nepho
    CHOOSE_UR_SLOW_MODE = "اختر نمط التبطيء "
    CHOOSE_UR_SLOW_MODE_BUTTONS = [[InlineKeyboardButton("x0.75",callback_data="slow1")],[InlineKeyboardButton("x0.5",callback_data="slow2")]]
    await CallbackQuery.edit_message_text(text = CHOOSE_UR_SLOW_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_SLOW_MODE_BUTTONS))
      
  elif CallbackQuery.data == "slow1":
   await CallbackQuery.edit_message_text("جار التبطيئ")
   await slowfunc(slowmessage,1.25,0.8)
   await CallbackQuery.edit_message_text("تم التبطيء ✅  ") 
     
  elif CallbackQuery.data == "slow2":
   await CallbackQuery.edit_message_text("جار التبطيئ")
   await slowfunc(slowmessage,1.5,0.66666666666)
   await CallbackQuery.edit_message_text("تم التبطيء ✅  ") 
     

 ########## خواص التحويل ###########

  elif CallbackQuery.data == "conv" and CallbackQuery.from_user.id == nepho.from_user.id:
    if exo in audioforms or exo in imageforms or exo in videoforms :
        if exo in imageforms :
         await replo.delete()
         imagepdfdic1.clear()
         imagepdfdic.clear()
         imgpdflist.clear()
         await checkdir('./img2pdf/')
         imgconvmessage = nepho
         await image2pdf(imgconvmessage)
         global imageconvid 
         imageconvid = imgconvmessage.from_user.id
         
        elif exo in audioforms or exo in videoforms :
         global convmessage
         convmessage = nepho
         CHOOSE_UR_CONV_MODE = "اختر نمط التحويل"
         CHOOSE_UR_CONV_MODE_BUTTONS = [[InlineKeyboardButton("تحويل صوتية/ فيديو إلى mp3",callback_data="audconv")],[InlineKeyboardButton("تحويل صوتية/ فيديو إلى m4a",callback_data="audconvm4a")],[InlineKeyboardButton("تحويل فيديو إلى mp4 ",callback_data="vidconv")]]

         await CallbackQuery.edit_message_text(text = CHOOSE_UR_CONV_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_CONV_MODE_BUTTONS))
      

  elif CallbackQuery.data == "audconv" :
   await CallbackQuery.edit_message_text("جار التحويل ") 
   await convy("mp3file",convmessage)
   await CallbackQuery.edit_message_text("تم التحويل ✅  ") 
   

  elif CallbackQuery.data == "audconvm4a" :
   await CallbackQuery.edit_message_text("جار التحويل ") 
   await convy("m4afile",convmessage)
   await CallbackQuery.edit_message_text("تم التحويل ✅  ") 
   
   
  elif CallbackQuery.data == "vidconv" :
   await CallbackQuery.edit_message_text("جار التحويل ") 
   await convy("mp4file",convmessage)
   await CallbackQuery.edit_message_text("تم التحويل ✅  ") 
   


  elif CallbackQuery.data == "convnow" :
    await CallbackQuery.edit_message_text("جار التحويل   ") 
    del globals()['imageconvid']
    await img2pdf1(imgpdflist)
    await CallbackQuery.edit_message_text("تم التحويل ✅  ") 
    


 ########## خاصية تغيير الصوت ###########

  elif  CallbackQuery.data == "voicy" and CallbackQuery.from_user.id == nepho.from_user.id:  
    if exo in audioforms or videoforms :
        global voicechangemessage
        voicechangemessage = nepho
        voicpath = await voicechangemessage.download(file_name="./downloads/")
        filename = os.path.basename(voicpath)
        nom,ex = os.path.splitext(filename)
        mp4file = f"{nom}.mp4"
        mp3file = f"{nom}.mp3"
        if exo in audioforms :
         await CallbackQuery.edit_message_text("جار تغيير الصوت ") 
         voicechangeaudid = voicechangemessage.from_user.id
         cmd(f'''ffmpeg -i "{voicpath}" -af asetrate=44100*0.75,aresample=44100,atempo=4/3 "{mp3file}"''')
         await bot.send_audio(voicechangeaudid, mp3file)
         await CallbackQuery.edit_message_text("تم تحويل الصوت ✅  ") 
         os.remove(mp3file) 
        elif exo in videoforms :
           await CallbackQuery.edit_message_text("جار تغيير الصوت ") 
           voicechangevidid = voicechangemessage.from_user.id
           cmd(f'''ffmpeg -i "{voicpath}" -af asetrate=44100*0.75,aresample=44100,atempo=4/3 "{mp3file}"''')
           cmd(f'''ffmpeg -i "{voicpath}" -i "{mp3file}" -c:v copy -map 0:v:0 -map 1:a:0 "{mp4file}"''')
           await bot.send_video(voicechangevidid,mp4file)
           os.remove(mp4file)
           await CallbackQuery.edit_message_text("تم تحويل الصوت ✅  ") 
           os.remove(mp3file) 
        os.remove(voicpath) 
    


 ########## إبدال صوت الفيديو ###########

  elif  CallbackQuery.data == "subs" and CallbackQuery.from_user.id == nepho.from_user.id:
    if exo in audioforms or exo in videoforms :
     global subsmessage,vidaudsubid
     subsmessage = nepho
     vidaudsubid = subsmessage.from_user.id
     await vidaudsub(subsmessage,replo)
    


  ########## خاصية المنتجة  ###########

  elif  CallbackQuery.data == "imagetovid" and CallbackQuery.from_user.id == nepho.from_user.id:
     if exo in audioforms or exo in imageforms :
        global imagetovidid,imagetovidmessage
        imagetovidmessage = nepho
        imagetovidid = imagetovidmessage.from_user.id
        await imagetovidfunc(imagetovidmessage,replo)

     



 ########## خواص القص ###########

  elif CallbackQuery.data == "trim" and CallbackQuery.from_user.id == nepho.from_user.id:
    if exo in audioforms or exo in videoforms or exo == ".pdf":
        if exo == ".pdf":
          global pdftrimmessage
          pdftrimmessage = nepho
          await CallbackQuery.edit_message_text("معالجة ⏱️")
          await replo.delete()
          replo2= await pdftrimmessage.reply_text(" الآن أرسل نقطة البداية والنهاية بهذه الصورة \n start-end ",reply_markup=ForceReply(True))
         
           
        elif exo in audioforms or exo in videoforms :
          global audvidtrimmessage
          audvidtrimmessage = nepho
          await CallbackQuery.edit_message_text("معالجة ⏱️")
          await replo.delete()
          replo2 = await audvidtrimmessage.reply_text("الآن أرسل نقطة البداية والنهاية بهذه الصورة \n\n hh:mm:ss-hh:mm:ss",reply_markup=ForceReply(True))
          

  elif CallbackQuery.data == "normaltrim" :
    await CallbackQuery.edit_message_text("جار المعالجة ⌛ ")  
    trimpath = await audvidtrimmessage.download(file_name="./downloads/")
    filename = os.path.basename(trimpath)
    nom,ex = os.path.splitext(filename)
    mp4file = f"{nom}.mp4"
    mp3file = f"{nom}.mp3"
    if exo in audioforms :
       await CallbackQuery.edit_message_text("جار القص")  
       trimaudid = audvidtrimmessage.from_user.id
       cmd(f'''ffmpeg -i "{trimpath}" -q:a 0 -map a "trim{mp3file}" -y ''')
       cmd(f'''ffmpeg -i "trim{mp3file}" -ss {strt_point} -to {end_point} -c copy "{mp3file}" -y ''')
       await  bot.send_audio(trimaudid, mp3file)
       await CallbackQuery.edit_message_text("تم القص  ✅  ")
       os.remove(mp3file) 
       os.remove(f"trim{mp3file}")
    elif exo in videoforms :
      await CallbackQuery.edit_message_text("جار القص")  
      
      trimvidid = audvidtrimmessage.from_user.id
      cmd(f'''ffmpeg -i "{trimpath}" -ss {strt_point} -strict -2 -to {end_point} -c:a aac -codec:v h264 -b:v 1000k "{mp4file}" -y ''')
      await bot.send_video(trimvidid, mp4file)  
      await CallbackQuery.edit_message_text("تم القص  ✅  ") 
      os.remove(mp4file) 
    os.remove(trimpath) 
    del audvidtrimmessage
    
  elif CallbackQuery.data == "reversetrim" :
    if exo in audioforms :
     await CallbackQuery.edit_message_text("جار القص  ")
     trimpath = await audvidtrimmessage.download(file_name="./downloads/")
     filename = os.path.basename(trimpath)
     nom,ex = os.path.splitext(filename)
     mp4file = f"{nom}.mp4"
     mp3file = f"{nom}.mp3"
     trimaudrevid = audvidtrimmessage.from_user.id
     starsec = re.split(':',strt_point)
     if len(starsec) == 3 :
        strtseconds = int(starsec[0])*60*60 + int(starsec[1])*60 + int(starsec[2])
     elif len(starsec) == 2 : 
         strtseconds = int(starsec[0])*60 + int(starsec[1])
     elif len(starsec) == 1 : 
        strtseconds =  int(starsec[0])
     endsec = re.split(':',end_point)
     if len(endsec) == 3 :
        endseconds = int(endsec[0])*60*60 + int(endsec[1])*60 + int(endsec[2])
     elif len(endsec) == 2 : 
         endseconds = int(endsec[0])*60 + int(endsec[1])
     elif len(endsec) == 1 : 
        endseconds =  int(endsec[0])
     cmd(f'''ffmpeg -i "{trimpath}" -af "aselect='not(between(t,{strtseconds},{endseconds}))'" "{mp3file}"''')
     await bot.send_audio(trimaudrevid,mp3file)
     await CallbackQuery.edit_message_text("تم القص  ✅  ")
     os.remove(mp3file)
     os.remove(trimpath)
     del audvidtrimmessage
    
  
  
 ########## خاصية إعادة التسمية ###########

  elif CallbackQuery.data == "renm" and CallbackQuery.from_user.id == nepho.from_user.id:
    global renmmessage
    renmmessage = nepho
    await replo.delete()
    replo2= await renmmessage.reply_text("الآن أدخل الاسم الجديد ",reply_markup=ForceReply(True))

 ########## خاصية التفريغ  ###########

  elif CallbackQuery.data == "transcribe" and CallbackQuery.from_user.id == nepho.from_user.id:
   if exo in audioforms or exo in videoforms or exo in imageforms or exo == ".pdf":
       if exo in audioforms or exo in videoforms :
        global audvidtranscribemessage
        audvidtranscribemessage = nepho
        await CallbackQuery.edit_message_text("معالجة ⏱️")
        CHOOSE_UR_TRANSCRIBE_LANG = "اختر اللغة التي تريد "
        CHOOSE_UR_TRANSCRIBE_LANG_BUTTONS = [
    
    [InlineKeyboardButton("العربية",callback_data="transar")],
    [InlineKeyboardButton("الانجليزية",callback_data="transen")],
    [InlineKeyboardButton("الفرنسية",callback_data="transfr")],
    [InlineKeyboardButton("الروسية",callback_data="transru")],
    [InlineKeyboardButton("الألمانية",callback_data="transge")],
    [InlineKeyboardButton("التركية",callback_data="transturk")],]
        await CallbackQuery.edit_message_text(text = CHOOSE_UR_TRANSCRIBE_LANG,reply_markup = InlineKeyboardMarkup( CHOOSE_UR_TRANSCRIBE_LANG_BUTTONS))
       elif  exo == ".pdf":
        global pdftranscribemessage
        pdftranscribemessage = nepho
        await CallbackQuery.edit_message_text("معالجة ⏱️")
        CHOOSE_UR_PDFOCRLANG = "اختر لغة النص"
        CHOOSE_UR_PDFOCRLANG_BUTTONS = [
        [InlineKeyboardButton("العربية ",callback_data="pdfara")],
       [InlineKeyboardButton("الانجليزية ",callback_data="pdfeng")]]
        await CallbackQuery.edit_message_text(text = CHOOSE_UR_PDFOCRLANG,reply_markup = InlineKeyboardMarkup( CHOOSE_UR_PDFOCRLANG_BUTTONS))
       elif  exo in imageforms :
        global pictranscribemessage
        pictranscribemessage = nepho
        CHOOSE_UR_OCRLANG = "اختر لغة النص"
        CHOOSE_UR_OCRLANG_BUTTONS = [
        [InlineKeyboardButton("العربية ",callback_data="ara")],[InlineKeyboardButton("الانجليزية ",callback_data="eng")]]
        await CallbackQuery.edit_message_text(text = CHOOSE_UR_OCRLANG,reply_markup = InlineKeyboardMarkup( CHOOSE_UR_OCRLANG_BUTTONS))
     
     
   
  elif CallbackQuery.data == "ara":
    await CallbackQuery.edit_message_text("جار التفريغ ⏳")
    textspaced = await ocrfunc('ara',pictranscribemessage)
    await pictranscribemessage.reply(textspaced[:-1], quote=True, disable_web_page_preview=True)
    await CallbackQuery.edit_message_text("تم التفريغ  ✅  ")
    
  elif CallbackQuery.data == "eng":
    await CallbackQuery.edit_message_text("جار التفريغ ⏳")
    textspaced = await ocrfunc('eng',pictranscribemessage)
    await pictranscribemessage.reply(textspaced[:-1], quote=True, disable_web_page_preview=True)
    await CallbackQuery.edit_message_text("تم التفريغ  ✅  ")
    
  elif CallbackQuery.data == "pdfara":
        await CallbackQuery.edit_message_text("جار التفريغ ⏳")
        await pdfocrfunc('ara',pdftranscribemessage)
        await CallbackQuery.edit_message_text("تم التفريغ  ✅  ")
        
     
  elif CallbackQuery.data == "pdfeng":
        await CallbackQuery.edit_message_text("جار التفريغ ⏳ ")
        await pdfocrfunc('eng',pdftranscribemessage)
        await CallbackQuery.edit_message_text("تم التفريغ  ✅  ")

        
  elif CallbackQuery.data == "transar":
    await CallbackQuery.edit_message_text("جار التفريغ")
    langtoken = "RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH"
    await vidaudtransfunc(audvidtranscribemessage,langtoken)
    await CallbackQuery.edit_message_text("تم التفريغ ✅  ") 
    

  elif CallbackQuery.data == "transen":
    await CallbackQuery.edit_message_text("جار التفريغ")
    langtoken = "2OVHUDKLF33Z44DOOX7GBAWEL5GOXI3Z"
    await vidaudtransfunc(audvidtranscribemessage,langtoken)
    await CallbackQuery.edit_message_text("تم التفريغ ✅  ") 


  

 ########## خاصية كتم الفيديو ###########

  elif CallbackQuery.data == "mute" and CallbackQuery.from_user.id == nepho.from_user.id:
   if exo in videoforms :
    videomutemessage = nepho
    await CallbackQuery.edit_message_text("معالجة ⏱️")
    mutepath = await videomutemessage.download(file_name="./downloads/")
    filename = os.path.basename(mutepath)
    nom,ex = os.path.splitext(filename)
    mp4file = f"{nom}.mp4"
    vidmuteid = videomutemessage.from_user.id
    await CallbackQuery.edit_message_text("جار الكتم")
    cmd(f'''ffmpeg -i "{mutepath}" -f lavfi -i anullsrc -map 0:v -map 1:a -c:v copy -shortest "{mp4file}"''')
    await bot.send_document(vidmuteid, mp4file)
    await CallbackQuery.edit_message_text("تم الكتم  ✅  ")
    os.remove(mutepath) 
    os.remove(mp4file) 
   

 ##########  خواص الدمج ###########

  elif CallbackQuery.data == "audmerge" and CallbackQuery.from_user.id == nepho.from_user.id:
    if exo in audioforms or exo in videoforms or exo in imageforms or exo == ".pdf":
        if exo in audioforms:
         global mergeid
         audmergemessage = nepho
         mergeid = audmergemessage.from_user.id
         await replo.delete()
         if 'audmergelist' in globals():
            globals()['audmergelist'].clear()
         if 'audmergedel' in globals():
            globals()['audmergedel'].clear()
         await audmerge(audmergemessage)
         
        elif exo in videoforms : 
          if nepho.from_user.id ==6234365091 :
            vidmergemessage = nepho
            global vidmergeid
            vidmergeid = vidmergemessage.from_user.id
            await replo.delete()
            if globals()['vidmergelist'] :
             vidmergelist.clear()
            if globals()['vidmergedel'] :
             vidmergedel.clear()
            await videomerge(vidmergemessage)
          else : 
           await CallbackQuery.edit_message_text("هذه الميزة متوفرة لمالك البوت فقط")
            
        elif exo in imageforms:
          
          imgmergemessage = nepho
          global photomergeid
          photomergeid = imgmergemessage.from_user.id
          await replo.delete()
          if 'imagedic' in globals():
            globals()['imagedic'].clear()
          if 'photomergedel' in globals():
            globals()['photomergedel'].clear()
            
          await photomerge(imgmergemessage)
          
        elif exo == ".pdf":
          pdfmergemessage = nepho
          global pdfmergeid,pdfmergeid2
          pdfmergeid = pdfmergemessage.from_user.id
          pdfmergeid2 = pdfmergemessage.from_user.id
          await replo.delete()
          if 'pdfmergedel' in globals():
            globals()['pdfmergedel'].clear()
          if 'pdfqueemerge' in globals():
            globals()['pdfqueemerge'].clear()
          await pdfmerge(pdfmergemessage)
          
      

  elif CallbackQuery.data == "mergenow":
    if len(audmergelist) < 2 :
        await CallbackQuery.edit_message_text("لقد أرسلت صوتية واحدة فقط !")
        return
    else :
         pass
    del globals()['mergeid']
    await CallbackQuery.edit_message_text("جار الدمج ⏳ ") 
    await audmerge1(audmergelist)
    await CallbackQuery.edit_message_text("تم الدمج  ✅  ")
    
    
  
  elif CallbackQuery.data == "pdfmergenow":
      if len(pdfqueemerge) < 2 :
        await CallbackQuery.edit_message_text("لقد أرسلت ملفاً واحداً فقط !")
        return
      else :
         pass
      del globals()['pdfmergeid']
      await CallbackQuery.edit_message_text("جار الدمج ⏳ ")
      await pdfmerge1(pdfqueemerge)
      await CallbackQuery.edit_message_text("تم الدمج  ✅  ")
   


  elif CallbackQuery.data == "imagemergenow" :
     if len(imagedic) < 2 :
        await CallbackQuery.edit_message_text("لقد أرسلت صورة واحدة فقط !")
        return
     else :
         pass
     global photoreplo
     PRESS_MERGEMODE_IMAGE = "اختر نمط الدمج "
     PRESS_MERGEMODE_IMAGE_BUTTONS = [
    [InlineKeyboardButton("متجاورتين بالجانب",callback_data="sidebyside")],
    [InlineKeyboardButton("الأولى فوق والثانية تحت ",callback_data="updown")]]
     photoreplo = await CallbackQuery.edit_message_text(text = PRESS_MERGEMODE_IMAGE,reply_markup = InlineKeyboardMarkup(PRESS_MERGEMODE_IMAGE_BUTTONS))
     
  elif CallbackQuery.data == "sidebyside" :
     del globals()['photomergeid']
     await CallbackQuery.edit_message_text("جار الدمج ⏳")
     await imgmerge(imagedic,merge_images2)
     await CallbackQuery.edit_message_text("تم الدمج  ✅  ")
     
     

  elif CallbackQuery.data == "updown" :
     del globals()['photomergeid']
     await CallbackQuery.edit_message_text("جار الدمج")
     await imgmerge(imagedic,merge_images1)
     await CallbackQuery.edit_message_text("تم الدمج  ✅  ")
     
  elif  CallbackQuery.data == "vidmergenow" :
     if len(vidmergelist) < 2 :
        await CallbackQuery.edit_message_text("لقد أرسلت فيديو واحد فقط !")
        return
     else :
         pass
     del globals()['vidmergeid']
     await CallbackQuery.edit_message_text("جار  الدمج ⏳")
     await vidmerge(vidmergelist)
     await CallbackQuery.edit_message_text("تم الدمج  ✅  ")
     

      ###### خاصية التقسيم #######

  elif CallbackQuery.data == "splitty" and CallbackQuery.from_user.id == nepho.from_user.id:
   if exo in audioforms :
    splitmessage = nepho
    await CallbackQuery.edit_message_text("جار التقسيم ⏳")
    await splitfunc(splitmessage)
    await CallbackQuery.edit_message_text("تم التقسيم  ✅  ")
    
   


    ########## خاصية الرفع لأرشيف
  
  elif CallbackQuery.data == "upldarch" and CallbackQuery.from_user.id == nepho.from_user.id:
      if nepho.from_user.id==6234365091 :
         archmessage = nepho
         await CallbackQuery.edit_message_text("معالجة ⏱️")
         upldarchpath = await archmessage.download(file_name="./downloads/")
         filename = os.path.basename(upldarchpath)
         await CallbackQuery.edit_message_text("جار الرفع")
         cmd(f'''rclone copy "{upldarchpath}" 'myarchive':"{bucketname}"''')
         os.remove(upldarchpath)
         resurl = f"https://archive.org/download/{bucketname}/{filename}"
         await CallbackQuery.edit_message_text(resurl)
      else :
         await CallbackQuery.edit_message_text("هذه الميزة متوفرة لمالك البوت فقط")
      

##### تغيير أبعاد الفيديو ######
  
  elif CallbackQuery.data == "vidasp" and CallbackQuery.from_user.id == nepho.from_user.id:
    if exo in videoforms:
     global vidaspmessage
     vidaspmessage = nepho
     await CallbackQuery.edit_message_text("معالجة ⏱️")
     CHOOSE_UR_VIDRES_MODE = "الآن اختر أبعادالناتج"
     CHOOSE_UR_VIDRES_MODE_BUTTONS = [
    [InlineKeyboardButton("9:16",callback_data="vidresnow11")],
    [InlineKeyboardButton("16:9",callback_data="vidresnow169")]]
     await CallbackQuery.edit_message_text(text = CHOOSE_UR_VIDRES_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_VIDRES_MODE_BUTTONS))

  elif CallbackQuery.data == "vidresnow11":
    await  CallbackQuery.edit_message_text("جار التحويل")
    vidaspmessage11 = vidaspmessage
    vidrespath11 = await vidaspmessage11.download(file_name="./downloads/")
    filename = os.path.basename(vidrespath11)
    nom,ex = os.path.splitext(filename)
    mp4file = f"{nom}.mp4"
    vidres11id = vidaspmessage11.from_user.id
    cmd(f'''ffmpeg -i "{vidrespath11}" -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1:color=black" "{mp4file}"''')
    await bot.send_document(vidres11id,mp4file) 
    await CallbackQuery.edit_message_text("تم التحويل   ✅  ")
    os.remove(mp4file)
    os.remove(vidrespath11)
    

  elif CallbackQuery.data == "vidresnow169":
    await  CallbackQuery.edit_message_text("جار التحويل")
    vidaspmessage69 = vidaspmessage
    vidrespath69 = await vidaspmessage.download(file_name="./downloads/")
    filename = os.path.basename(vidrespath69)
    nom,ex = os.path.splitext(filename)
    mp4file = f"{nom}.mp4"
    vidres169id = vidaspmessage69.from_user.id
    cmd(f'''ffmpeg -i "{vidrespath69}" -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:-1:-1:color=black" "{mp4file}"''')
    await bot.send_video(vidres169id,mp4file) 
    await CallbackQuery.edit_message_text("تم التحويل  ✅  ")
    os.remove(mp4file)
    os.remove(vidrespath69)
    

########### خاصية إزالة الصمت ##########

  elif CallbackQuery.data == "rmvsilence" :
   await CallbackQuery.edit_message_text(" هذه الميزة لا تعمل حالياً 😴")
   return 
   if exo in audioforms:
    global rmvslmessage
    rmvslmessage = nepho
    await  CallbackQuery.edit_message_text("جار إزالة الصمت")
    rmvsilencepath = await rmvslmessage.download(file_name="./downloads/")
    filename = os.path.basename(rmvsilencepath)
    nom,ex = os.path.splitext(filename)
    mp3file = f"{nom}.mp3"
    await noisermvfunc(rmvsilencepath,mp3file)
    os.rename(mp3file,rmvsilencepath)
    
    rmvsilenceid = rmvslmessage.from_user.id
    cmd(f'''ffmpeg -i "{rmvsilencepath}" -af "silenceremove=start_periods=1:stop_periods=-1:start_threshold=-30dB:stop_threshold=-50dB:start_silence=2:stop_silence=2" "{mp3file}"''')
    await bot.send_audio(rmvsilenceid,mp3file)
    await CallbackQuery.edit_message_text("تمت إزالة الصمت  ✅  ")
    os.remove(rmvsilencepath)
    os.remove(mp3file)
   

   ######## تحويل الصورة إلى gif##########
 
  elif CallbackQuery.data == "imagetogif" and CallbackQuery.from_user.id == nepho.from_user.id:
    if exo in imageforms :
      global imagetogifmessage
      imagetogifmessage = nepho
      await replo.delete()
      replo2 = await imagetogifmessage.reply_text("الآن أرسل مدة الفيديو بالثانية",reply_markup=ForceReply(True))
      await asyncio.sleep(20)
      if 'gifpath' not in locals() :
           await replo2.delete()
           del imagetogifmessage
    

      ######### ترجمة + فيديو ############
  
  elif CallbackQuery.data == "vidsrt" and CallbackQuery.from_user.id == nepho.from_user.id:
    global vidsrtmessage,vidsrtid
    vidsrtmessage = nepho
    vidsrtid = vidsrtmessage.from_user.id
    await vidsrtfunc(vidsrtmessage,replo)

  
  ######### خاصية عكس الـpdf  #########

  
  elif  CallbackQuery.data == "reversepdf" and CallbackQuery.from_user.id == nepho.from_user.id :
   if exo == ".pdf":
    reversepdfmessage = nepho
    await CallbackQuery.edit_message_text("جار العكس")
    await pdfextract(reversepdfmessage,'rvtemp')
    pdfrevid = reversepdfmessage.from_user.id
    rpdfpage = [] 
    for x in range(1,n_pages+1):
      page=f"./rvtemp/image_{str(x).zfill(5)}.png"
      rpdfpage.append(page)
    rpdfpage.reverse()
    imagey = Image.open(rpdfpage[0]).convert('RGB')
    for x in range(1,len(rpdfpage)):
     image2 = Image.open(rpdfpage[x]).convert('RGB')
     imagepdfdic.append(image2)
    pdffile = f"{nom}.pdf"
    imagey.save(pdffile,save_all=True, append_images=imagepdfdic)
    await bot.send_document(pdfrevid,pdffile)
    await CallbackQuery.edit_message_text("تم العكس  ✅  ")
    os.remove(pdffile)
    shutil.rmtree("./rvtemp/")
    imagepdfdic.clear()
    rpdfpage.clear()
   
  elif  CallbackQuery.data == "coloring" and CallbackQuery.from_user.id == nepho.from_user.id:
   if exo in imageforms or exo == ".pdf":
    global colormessage 
    colormessage = nepho
    YOUR_COLOR_MODE = "اختر نمط التلوين"
    YOUR_COLOR_MODE_BUTTONS = [
    [InlineKeyboardButton("رمادي",callback_data="Grayscale")],
    [InlineKeyboardButton("أحمر",callback_data="red")],
    [InlineKeyboardButton("أصفر",callback_data="yellow")],
    [InlineKeyboardButton("أزرق فاتح",callback_data="whiteblue")],
    [InlineKeyboardButton("أرجواني",callback_data="purple")]]
    await CallbackQuery.edit_message_text(text = YOUR_COLOR_MODE,reply_markup = InlineKeyboardMarkup(YOUR_COLOR_MODE_BUTTONS))
  
    

  elif  CallbackQuery.data == "Grayscale" :
   await CallbackQuery.edit_message_text("جار التلوين")
   await Coloringfunc("g",colormessage)
   await CallbackQuery.edit_message_text("تم التلوين ✅  ") 
   
  elif  CallbackQuery.data == "red" :
   await CallbackQuery.edit_message_text("جار التلوين")
   await Coloringfunc("r",colormessage)
   await CallbackQuery.edit_message_text("تم التلوين ✅  ") 
   
  elif  CallbackQuery.data == "yellow" :
   await CallbackQuery.edit_message_text("جار التلوين")
   await Coloringfunc("y",colormessage)
   await CallbackQuery.edit_message_text("تم التلوين ✅  ") 
   
  elif  CallbackQuery.data == "purple" :
   await CallbackQuery.edit_message_text("جار التلوين")
   await Coloringfunc("p",colormessage)
   await CallbackQuery.edit_message_text("تم التلوين ✅  ") 
   
  elif  CallbackQuery.data == "whiteblue" :
   await CallbackQuery.edit_message_text("جار التلوين")
   await Coloringfunc("b",colormessage)
   await CallbackQuery.edit_message_text("تم التلوين ✅  ") 
   




    ############  خاصية الأرشفة ######## 

  elif  CallbackQuery.data == "zipfile" and CallbackQuery.from_user.id == nepho.from_user.id:
    await replo.delete()
    global zipfileid,zipfilemessage
    zipfilemessage = nepho
    zipfileid = nepho.from_user.id
    await zipfilefunc(zipfilemessage)

  elif  CallbackQuery.data == "zipnow" :
    await CallbackQuery.edit_message_text("جار الأرشفة  ⏱️  ")
    del globals()['zipfileid']
    zipdir = './zipdir/'
    zipnom = str(random.randint(0,1000))
    zipfile = await zipfunc1(zipdir,zipnom,zipfilequee)
    await bot.send_document(zipfilequee[-1].from_user.id,zipfile)
    os.remove(zipfile)
    shutil.rmtree(zipdir)
    await CallbackQuery.edit_message_text("تمت الأرشفة  ✅  ")
    

    ############خواص الاستخراج ###########

  elif  CallbackQuery.data == "unzip" and CallbackQuery.from_user.id == nepho.from_user.id:
    if exo == ".zip" or exo == ".pdf" or exo == ".epub":
        unzipmessage = nepho
        if exo == ".zip":
         await CallbackQuery.edit_message_text("جار الاستخراج ⏱️")
         await unzipfunc(unzipmessage)
         await CallbackQuery.edit_message_text("تم الاستخراج  ✅  ")
        elif exo == ".pdf":
         await CallbackQuery.edit_message_text("جار الاستخراج ⏱️")
         extractdir = await pdfextract(unzipmessage,False)
         zipfile = await zipfunc1(extractdir,unzipmessage.document.file_name.split('.')[0])
         await bot.send_document(unzipmessage.from_user.id,zipfile)
         os.remove(zipfile)
         images = os.listdir(extractdir)
         for x in sorted(images):
          await bot.send_photo(unzipmessage.from_user.id,extractdir+x)
         shutil.rmtree(extractdir)
         await CallbackQuery.edit_message_text("تم الاستخراج  ✅  ")
         
        elif exo == ".epub":
           await CallbackQuery.edit_message_text("جار الاستخراج ⏱️")
           await ebupextract(unzipmessage)
           await CallbackQuery.edit_message_text("تم الاستخراج  ✅  ") 


    ########## إزالة الضوضاء #############

  elif  CallbackQuery.data == "noisermv" and CallbackQuery.from_user.id == nepho.from_user.id :
    if exo in audioforms or exo in videoforms :
        await CallbackQuery.edit_message_text(" هذه الميزة لا تعمل حالياً 😴")
        return 
        #await CallbackQuery.edit_message_text("جار المعالجة ⌛ ")
          
        noisermvmessage = nepho
        noisermvpath = await noisermvmessage.download(file_name="./downloads/")
        filename = os.path.basename(noisermvpath)
        nom,ex = os.path.splitext(filename)
        mp3file = f"{nom}.mp3"
        mp4file = f"{nom}.mp4"
        if exo in audioforms :
            await CallbackQuery.edit_message_text("جار الإزالة ")
            noisermvaudid = noisermvmessage.from_user.id
            await noisermvfunc(noisermvpath,mp3file)
            await bot.send_audio(noisermvaudid,mp3file)
            await CallbackQuery.edit_message_text("تمت الإزالة  ✅  ")
            
        elif exo in videoforms:
            await CallbackQuery.edit_message_text("جار الإزالة ")
            noisermvvidid = noisermvmessage.from_user.id
            await noisermvfunc(noisermvpath,mp3file)
            cmd(f'''ffmpeg -i "{noisepath}" -i "{mp3file}" -c:v copy -map 0:v:0 -map 1:a:0 "{mp4file}"''')
            await bot.send_video(noisermvvidid,mp4file)
            os.remove(mp4file)
            await CallbackQuery.edit_message_text("تمت الإزالة  ✅  ")
        os.remove(noisermvpath)
        os.remove(mp3file)
        



    ############ خاصية الرفع ليوتيوب ###########

  elif  CallbackQuery.data == "upldtout" and CallbackQuery.from_user.id == nepho.from_user.id:
    if nepho.from_user.id ==6234365091 :
        if exo in videoforms:
         upldutubmessage = nepho
         await CallbackQuery.edit_message_text("معالجة ⏱️")
         upldtubepath = await upldutubmessage.download(file_name="./downloads/")
         videoupldtitle = upldutubmessage.caption
         upload = Uploader(upldtubepath,videoupldtitle )
         snt = await CallbackQuery.edit_message_text("جار الرفع")
         link = await upload.start(progress,snt)
         await snt.edit_text(text=link, parse_mode=enums.ParseMode.MARKDOWN)
         os.remove(upldtubepath)
    else :
         await CallbackQuery.edit_message_text("🟥 لتفعيل الميزة يمكنك الاشتراك في الباقة المميزة \n\n https://t.me/sunnaybots/9 ",disable_web_page_preview=True)
         
    

  elif  CallbackQuery.data == "manuscript" and CallbackQuery.from_user.id == nepho.from_user.id :
       if nepho.from_user.id ==6234365091 :
        if exo in videoforms:
         global fbapimessage 
         fbapimessage = nepho
         CHOOSE_UR_FBPAGE = "اختر اسم الصفحة"
         CHOOSE_UR_FBPAGE_BUTTONS = [
    [InlineKeyboardButton("أسئلة البوت",callback_data="kqa")],
    [InlineKeyboardButton("فقه القرون",callback_data="fqo")],
    [InlineKeyboardButton("الأنصاري بن ابراهيم ",callback_data="ansary")],
    [InlineKeyboardButton("السنة الواضحة ",callback_data="sunnah")],
    [InlineKeyboardButton("قطوف الخليفي ",callback_data="kotof")],
    [InlineKeyboardButton("المواد الصوتية الخليفي",callback_data="kpod")],
    [InlineKeyboardButton("المواد الصوتية التميمي",callback_data="tmemepod")],
    [InlineKeyboardButton("المواد الصوتية نواف الشمري",callback_data="shamrypod")]]
         await CallbackQuery.edit_message_text(text = CHOOSE_UR_FBPAGE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FBPAGE_BUTTONS))
       else :
         await CallbackQuery.edit_message_text("🟥 لتفعيل الميزة يمكنك الاشتراك في الباقة المميزة \n\n https://t.me/sunnaybots/9 ",disable_web_page_preview=True)
         

  elif CallbackQuery.data == "kqa":
         await CallbackQuery.edit_message_text("معالجة ⏱️")
         await upldtofbpage(227535600451310,FBAPI,fbapimessage,replo)
         #await CallbackQuery.edit_message_text("تم الرفع ✅")
         

  elif CallbackQuery.data == "fqo":
         await CallbackQuery.edit_message_text("معالجة ⏱️")
         await upldtofbpage(137037322817687,FBAPI,fbapimessage,replo)
        # await CallbackQuery.edit_message_text("تم الرفع ✅")
         
  elif CallbackQuery.data == "ansary":
         await CallbackQuery.edit_message_text("معالجة ⏱️")
         await upldtofbpage(112807441778266,FBAPI,fbapimessage,replo)
        # await CallbackQuery.edit_message_text("تم الرفع ✅")
         
  elif CallbackQuery.data == "sunnah":
         await CallbackQuery.edit_message_text("معالجة ⏱️")
         await upldtofbpage(104480982720950,FBAPI,fbapimessage,replo)
         #await CallbackQuery.edit_message_text("تم الرفع ✅")
         
  elif CallbackQuery.data == "kotof":
         await CallbackQuery.edit_message_text("معالجة ⏱️")
         await upldtofbpage(258676494004533,FBAPI,fbapimessage,replo)
         #await CallbackQuery.edit_message_text("تم الرفع ✅")
         
  elif CallbackQuery.data == "kpod":
         await CallbackQuery.edit_message_text("معالجة ⏱️")
         await upldtofbpage(104273582327264,FBAPI,fbapimessage,replo)
         #await CallbackQuery.edit_message_text("تم الرفع ✅")
         
  elif CallbackQuery.data == "tmemepod":
         await CallbackQuery.edit_message_text("معالجة ⏱️")
         await upldtofbpage(311739208683441,FBAPI,fbapimessage,replo)
         #await CallbackQuery.edit_message_text("تم الرفع ✅")
         
  elif CallbackQuery.data == "shamrypod":
         await CallbackQuery.edit_message_text("معالجة ⏱️")
         await upldtofbpage(296575040202407,FBAPI,fbapimessage,replo)
         #await CallbackQuery.edit_message_text("تم الرفع ✅")
         

  elif  CallbackQuery.data == "upldtotwitter" and CallbackQuery.from_user.id == nepho.from_user.id:
    if nepho.from_user.id ==6234365091 :
     if exo in videoforms:
      global twittermessage
      twittermessage = nepho
      await CallbackQuery.edit_message_text("معالجة ⏱️")
      CHOOSE_UR_TWPAGE = "اختر اسم الصفحة"
      CHOOSE_UR_TWPAGE_BUTTONS = [
    [InlineKeyboardButton("أسئلة البوت",callback_data="kqatwitter")],
    [InlineKeyboardButton("فقه القرون",callback_data="fqotwitter")]]
      await CallbackQuery.edit_message_text(text = CHOOSE_UR_TWPAGE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_TWPAGE_BUTTONS))
    else :
         await CallbackQuery.edit_message_text("🟥لتفعيل الميزة يمكنك الاشتراك في الباقة المميزة \n\n https://t.me/sunnaybots/9 ",disable_web_page_preview=True)
         
  elif  CallbackQuery.data == "kqatwitter" :
    await CallbackQuery.edit_message_text("معالجة ⏱ ")
    CONSUMER_KEY = "i72lBPnd7xZlKYOl1ELaeUgt4"
    CONSUMER_SECRET = "TE6STQVwjok9caTV1g8jjyPmxlbNnN4TbIdJ8GNmkiTFfqEoC4"
    ACCESS_KEY = "1741622894411579392-tdooWDUon86TTunB4JtgvPll2rDwUw"
    ACCESS_SECRET = "cS30r9Ff2nlWmX0Pb2Nuigfrip8Htvv5JlZgyJPWizTtk"
    await twitterupload(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET,twittermessage)
    await CallbackQuery.edit_message_text("تم الرفع  ✅  ")
    
  elif  CallbackQuery.data == "fqotwitter" :
    await CallbackQuery.edit_message_text("معالجة ⏱ ")
    CONSUMER_KEY = "vI7bd1TjXv5jfzvKzOKAb90yo"
    CONSUMER_SECRET = "r1pkkhWP8IRBewkbZO9nXcDoNfwIUm8773qZ42QNBUxtyvBNnS"
    ACCESS_KEY = "1764030842744020992-wqkXkqexkGsG1p1YtMBBT4WiZeTvGm"
    ACCESS_SECRET = "dHE7bSnAUQKhutMjhNuMtrFU0fLJ2Yb4WEFYilipavz6H"
    await twitterupload(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET,twittermessage)
    await CallbackQuery.edit_message_text("تم الرفع  ✅  ")
  elif  CallbackQuery.data == "upldtotelegraph" and CallbackQuery.from_user.id == nepho.from_user.id :
    if exo in imageforms or exo in videoforms :
        await CallbackQuery.edit_message_text("معالجة ⏱ ")
        upldtotelegraphmessage = nepho
        await replo.delete()
        await upld2telegraph(upldtotelegraphmessage)
        
  elif  CallbackQuery.data == "detailsoffile" and CallbackQuery.from_user.id == nepho.from_user.id:
    if nepho.video :
      filename1 ,ex1 = os.path.splitext(nepho.video.file_name)
      filesize = round(int(nepho.video.file_size)/(1024*1024),2)
      await CallbackQuery.edit_message_text(f"اسم الملف : \n {filename1} \n حجم الملف : \n {filesize} ميغا بايت  ")
    elif nepho.audio :
        filename1,ex1 = os.path.splitext(nepho.audio.file_name)
        filesize = round(int(nepho.audio.file_size)/(1024*1024),2)
        await CallbackQuery.edit_message_text(f"اسم الملف : \n {filename1} \n حجم الملف : \n {filesize} ميغا بايت  ")
    elif nepho.document :
        filename1,ex1 = os.path.splitext(nepho.document.file_name)
        filesize = round(int(nepho.document.file_size)/(1024*1024),2)
        await CallbackQuery.edit_message_text(f"اسم الملف : \n {filename1} \n حجم الملف : \n {filesize} ميغا بايت  ")
    else :
        await CallbackQuery.edit_message_text("الخاصية تدعم الوسائط والمستندات فقط ")

  
  elif  CallbackQuery.data == "pdfonepagemode" and CallbackQuery.from_user.id == nepho.from_user.id :
    if exo == ".pdf" :
        await CallbackQuery.edit_message_text("جار العمل")
        pdfonepagemessage = nepho
        pdfonepagemessageid = nepho.from_user.id
        await pdfextract(pdfonepagemessage,'onepagetemp')
        pdfonepage = [] 
        for x in range(1,n_pages+1):
          page=f"./onepagetemp/image_{str(x).zfill(5)}.png"
          img1,img2 = await pdfonepagefunc(page)
          image11 = f"./onepagetemp/image_{str(x).zfill(5)}1.png"
          image12 = f"./onepagetemp/image_{str(x).zfill(5)}2.png"
          img1.save(image11)
          img2.save(image12)
          os.remove(page)
          pdfonepage.append(image12)
          pdfonepage.append(image11)
        imagey = Image.open(pdfonepage[0]).convert('RGB')
        for x in range(1,len(pdfonepage)):
         image2 = Image.open(pdfonepage[x]).convert('RGB')
         imagepdfdic.append(image2)
        pdffile = f"{nom}.pdf"
        imagey.save(pdffile,save_all=True, append_images=imagepdfdic)
        await bot.send_document(pdfonepagemessageid,pdffile)
        await CallbackQuery.edit_message_text("تم الضبط  ✅  ")
        os.remove(pdffile)
        shutil.rmtree("./onepagetemp/")
        imagepdfdic.clear()
        pdfonepage.clear()

  elif CallbackQuery.data == "videocallyback" :
    await CallbackQuery.edit_message_text("جار التحميل ")
    if 'youtube' in ytlink or 'youtu.be' in ytlink:
     dlmode = 'vid' 
     await ytdlfunc(ytlink,dlmode,yt_id)
    elif 'story.php' in ytlink :
       dlmode = "svid"
       ytlink1 =f"https://www.facebook.com/{ytlink.split('=')[1].split('&')[0]}/posts/{ytlink.split('fbid=')[1]}"
       await ytdlfunc(ytlink1,dlmode,yt_id)
    elif 'permalink.php' in ytlink :
        storyid = ytlink.split('=')[1].split('&')[0]
        profileid = ytlink.split('&id=')[1].split('&')[0]
        dlmode = "svid"
        ytlink1 =f"https://www.facebook.com/{profileid}/posts/{storyid}"
        await ytdlfunc(ytlink1,dlmode,yt_id)
    else :
      dlmode = 'svid'
      await ytdlfunc(ytlink,dlmode,yt_id)
    
    await CallbackQuery.edit_message_text("تم التحميل  ✅ ")

  elif CallbackQuery.data == "audiocallback" :
    await CallbackQuery.edit_message_text("جار التحميل ")
    
    if 'youtube' in ytlink or 'youtu.be' in ytlink:
     dlmode = 'aud'
     await ytdlfunc(ytlink,dlmode,yt_id)
    elif 'story.php' in ytlink :
       dlmode = 'saud'
       ytlink1 =f"https://www.facebook.com/{ytlink.split('=')[1].split('&')[0]}/posts/{ytlink.split('fbid=')[1]}"
       await ytdlfunc(ytlink1,dlmode,yt_id)
    elif 'permalink.php' in ytlink :
        dlmode = 'saud'
        storyid = ytlink.split('=')[1].split('&')[0]
        profileid = ytlink.split('&id=')[1].split('&')[0]
        ytlink1 =f"https://www.facebook.com/{profileid}/posts/{storyid}"
        await ytdlfunc(ytlink1,dlmode,yt_id)
    else :
      dlmode = 'saud'
      await ytdlfunc(ytlink,dlmode,yt_id)
    await CallbackQuery.edit_message_text("تم التحميل  ✅ ")
  elif CallbackQuery.data == "directurl" :
    await CallbackQuery.edit_message_text("جار التحميل ")
    dlmode = "direct"
    await ytdlfunc(ytlink,dlmode,yt_id)
    await CallbackQuery.edit_message_text("تم التحميل  ✅ ")

  
  elif CallbackQuery.data == "videocallback1" :
    dlmode = "vid"
    await CallbackQuery.edit_message_text("جار التحميل ")
    await ytplstfunc(ytplsturl,dlmode,ytplstid)
    await CallbackQuery.edit_message_text("تم التحميل  ✅ ")

  elif CallbackQuery.data == "audiocallback1" :
    dlmode = "aud"
    await CallbackQuery.edit_message_text("جار التحميل ")
    await ytplstfunc(ytplsturl,dlmode,ytplstid)
    await CallbackQuery.edit_message_text("تم التحميل  ✅ ")
    
  elif CallbackQuery.data == "mscrmv" and CallbackQuery.from_user.id == nepho.from_user.id:
   if nepho.audio or nepho.voice or nepho.video : 
    mscrmvmessage = nepho
    mscrmvid = mscrmvmessage.from_user.id
    tempnom = 54388953228
    tempmp3 = f"{tempnom}.mp3"
    if mscrmvmessage.video : 
      streamdur = mscrmvmessage.video.duration
    elif mscrmvmessage.audio : 
      streamdur = mscrmvmessage.audio.duration
    elif mscrmvmessage.voice : 
      streamdur = mscrmvmessage.voice.duration
    if mscrmvid in premiumids or mscrmvid in msrmvprmids  :
        await CallbackQuery.edit_message_text("جار إزالة المعازف⌛ ")
        await musicrmv(mscrmvmessage,streamdur)
         
        await CallbackQuery.edit_message_text("تمت إزالة المعازف ☑️")
    else : 
        
        if int(streamdur) <= 120: 
          await CallbackQuery.edit_message_text("جار إزالة المعازف⌛ ")
          await musicrmv(mscrmvmessage,streamdur)
          await CallbackQuery.edit_message_text("تمت إزالة المعازف ☑️")
          
        else : 
          await CallbackQuery.edit_message_text("الحد الأقصى فيديو دقيقتين \n\n لإزالة القيد يمكنك الاشتراك بالباقة المميزة \n\n https://t.me/sunnaybots/9 ",disable_web_page_preview=True)
          
  elif CallbackQuery.data == "vidsplit" and CallbackQuery.from_user.id == nepho.from_user.id:
      vidsplitmsg = nepho
      await CallbackQuery.edit_message_text("جار التقسيم ⏳ ")
      await splitfunc(vidsplitmsg)
      await CallbackQuery.edit_message_text("تم التقسيم☑️")
    
      
  else : 
    await CallbackQuery.edit_message_text("عفواً ، لقد انتهت مدة الاختيار ، أرسل الملف مجدداً ")
          
 

 
 @bot.on_message(filters.private & filters.reply)
 async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
     
        if 'audvidtrimmessage' in globals() and globals()["audvidtrimmessage"].from_user.id == message.from_user.id : 
          endstart = message.text 
          tempid = message.from_user.id
          msgid = message.reply_to_message_id
          await bot.delete_messages(tempid,msgid)
          await message.delete()
          global strt_point,end_point
          if '/' in endstart :
           strt, end = os.path.split(endstart)
           strt_point=strt 
           end_point = end 
          elif '-' in endstart : 
           startend = re.split('-',endstart)
           strt_point=startend[0] 
           end_point = startend[1]
           CHOOSE_UR_TRIMMODE = "اختر نمط القص" ;CHOOSE_UR_TRIMMODE_BUTTONS = [[InlineKeyboardButton("قص عادي",callback_data="normaltrim")],[InlineKeyboardButton("قص معكوس",callback_data="reversetrim")]]
          await message.reply(text = CHOOSE_UR_TRIMMODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_TRIMMODE_BUTTONS))
          
          
        elif 'pdftrimmessage' in globals() and globals()["pdftrimmessage"].from_user.id == message.from_user.id : 
          pdftrimpath = await globals()["pdftrimmessage"].download(file_name="./downloads/")
          pdfcutid = globals()["pdftrimmessage"].from_user.id
          filename = os.path.basename(pdftrimpath)
          pstartpend = message.text 
          msgid = message.reply_to_message_id
          await bot.delete_messages(pdfcutid,msgid)
          await message.delete()
          global pdfstrt_point,pdfend_point 
          
          if '/' in pstartpend :
           strt, end = os.path.split(pstartpend)
           pdfstrt_point=strt 
           pdfend_point = end 
           
          elif '-' in pstartpend : 
           startend = re.split('-',pstartpend)
           pdfstrt_point= startend[0]
           pdfend_point = startend[1]
          pages = (int(pdfstrt_point), int(pdfend_point))
          reader = PdfReader(pdftrimpath)
          writer = PdfWriter()
          page_range = range(pages[0], pages[1] + 1)
          for page_num, page in enumerate(reader.pages, 1):
           if page_num in page_range:
            writer.add_page(page)
           with open(filename, 'wb') as out:
            writer.write(out)
          with open(filename,'rb') as f : 
            await bot.send_document(pdfcutid,f)
          os.remove(pdftrimpath) 
          os.remove(filename)
          del globals()["pdftrimmessage"]
          
        elif 'imagetogifmessage' in globals() and globals()["imagetogifmessage"].from_user.id == message.from_user.id : 
          timeofvidstoned = message.text
          gifpath = await globals()["imagetogifmessage"].download(file_name="./downloads/")
          imagegifid = globals()["imagetogifmessage"].from_user.id
          filename = os.path.basename(gifpath)
          nom,ex = os.path.splitext(filename)
          mp4file = f"{nom}.mp4"
          msgid = message.reply_to_message_id
          await bot.delete_messages(imagegifid,msgid)
          await message.delete()
          cmd(f'''ffmpeg -loop 1 -i "{gifpath}" -c:v libx264 -t {timeofvidstoned} -pix_fmt yuv420p -vf scale=1920:1080 "mod{mp4file}"''') 
          cmd(f'''ffmpeg -i "mod{mp4file}" -f lavfi -i anullsrc -map 0:v -map 1:a -c:v copy -shortest "{mp4file}"''')
          await bot.send_video(imagegifid,mp4file) 
          os.remove(mp4file)
          os.remove(f"mod{mp4file}")
          os.remove(gifpath)   
          del globals()["imagetogifmessage"]
          
   
        elif 'renmmessage' in globals() and globals()["renmmessage"].from_user.id == message.from_user.id : 
          newname = message.text
          renmpath = await globals()["renmmessage"].download(file_name="./downloads/")
          filename = os.path.basename(renmpath)
          nom,ex = os.path.splitext(filename)
          renmid = globals()["renmmessage"].from_user.id
          msgid = message.reply_to_message_id
          await bot.delete_messages(renmid,msgid)
          await message.delete()
          newfile = f"{newname}{ex}"
          os.rename(renmpath,newfile)
          if ex in audioforms :
            await bot.send_audio(renmid,newfile)
          elif ex in videoforms  :
            await bot.send_video(renmid,newfile)
          elif ex in imageforms :
            await bot.send_photo(renmid,newfile)
          else : 
             await bot.send_document(renmid,newfile)
          os.remove(newfile)
          del globals()["renmmessage"]
@bot.on_message(filters.private & filters.incoming & filters.text & filters.regex(ytregex) | filters.regex('permalink.php') |filters.regex('story.php') | filters.regex('facebook') | filters.regex('https') | filters.regex('http') )
async def _telegram_file(client, message):
 if not (await pyro_fsub(bot, message,fsub) == True):
            return
 if message.from_user.id not in premiumids : 
   pass
 else : 
   if 'playlist' in message.text:
     global ytplsturl,ytplstid
     ytplsturl = message.text
     ytplstid = message.from_user.id
     CHOOSE_UR_SCRAPPLST_MODE = " اختر صيغة التحميل "
     CHOOSE_UR_SCRAPPLST_MODE_BUTTONS = [
       [InlineKeyboardButton("فيديو",callback_data="videocallback1")],
       [InlineKeyboardButton("صوتية",callback_data="audiocallback1")]
          ]
     await message.reply(text = CHOOSE_UR_SCRAPPLST_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_SCRAPPLST_MODE_BUTTONS))
   elif 'drive.google.com/file' in message.text :
    gdowndir = "./gdowndir/"
    if os.path.isdir(gdowndir) == False : 
      os.mkdir(gdowndir)
    p = subprocess.Popen(["gdown", "--fuzzy",message.text],cwd=gdowndir)
    p.wait()
    dlfile = os.listdir(gdowndir)[0]
    leechedfile = gdowndir + dlfile
    dlfilex = '.' + dlfile.split('.')[-1]
    if dlfilex in audioforms :
         await bot.send_audio(message.from_user.id,leechedfile)
    elif dlfilex in videoforms :
         await bot.send_video(message.from_user.id,leechedfile)
    else : 
         await bot.send_document(message.from_user.id,leechedfile)
    os.remove(leechedfile)
     
     
   else : 
     global yt_id , ytlink
     ytlink = message.text
     yt_id = message.from_user.id
     CHOOSE_UR_SCRAP_MODE = " اختر صيغة التحميل "
     CHOOSE_UR_SCRAP_MODE_BUTTONS = [
       [InlineKeyboardButton("فيديو",callback_data="videocallyback")],
       [InlineKeyboardButton("صوتية",callback_data="audiocallback")],
        [InlineKeyboardButton("رابط مباشر",callback_data="directurl")]
          ]
     await message.reply(text = CHOOSE_UR_SCRAP_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_SCRAP_MODE_BUTTONS))
      
 
bot.run()