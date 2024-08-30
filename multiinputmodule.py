audmergelist,audmergedel,vidmergedel , vidmergelist,imagedic,imagepdfdic,imagepdfdic1,photomergedel,imgpdflist,photomergedel,pdfqueemerge,pdfmergedel,pdfs,zipfilequee= [],[],[],[],[],[],[],[],[],[],[],[],[],[]

from PIL import Image
from pypdf import PdfMerger
import os,random,shutil
from asyncstdlib.functools import reduce
from config import checkdir,bot
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery , ForceReply,Message

######## دمج الصوتيات #######

async def audmerge(x):
     if len(audmergedel) != 0 :
        for y in audmergedel:
         await y.delete()
     audmergelist.append(x)
     CHOOSE_UR_MERGE = "أرسل الصوتية التالية  \n تنبيه / بعد الانتهاء من إرسال الصوتيات اضغط دمج الآن "
     CHOOSE_UR_MERGE_BUTTONS = [
    [InlineKeyboardButton("دمج الآن ",callback_data="mergenow")] ]
     audnowpull = await x.reply(text = CHOOSE_UR_MERGE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_MERGE_BUTTONS))
     audmergedel.append(audnowpull)
     
async def audmerge1(audmergelist):
    mergedir = "./mergy/"
    await checkdir(mergedir)
    for x in range(0,len(audmergelist)) :
     audmergepath = await audmergelist[x].download(file_name="./downloads/")
     filename = os.path.basename(audmergepath)
     nom,ex = os.path.splitext(filename)
     mp3file = f"{nom}.mp3"
     tempmp3 = f"{random.randint(1,1000)}.mp3"
     if ex == '.mp3' :
       os.replace(audmergepath,mergedir+tempmp3)
     else :
      os.system(f'''ffmpeg -i "{audmergepath}" -q:a 0 -map a "{mergedir+tempmp3}" -y ''')
      os.remove(audmergepath)
     open('list.txt','a').write(f"file '{mergedir+tempmp3}' \n")
    os.system(f'''ffmpeg -f concat -safe 0 -i list.txt "{mp3file}" -y ''')
    await bot.send_audio(audmergelist[-1].from_user.id, mp3file)
    os.remove("list.txt")
    os.remove(mp3file)
    shutil.rmtree(mergedir) 
    audmergelist.clear()
    
     
########## دمج الفيديوهات ######

async def videomerge(x):
     if len(vidmergedel) != 0 :
      for y in vidmergedel:
         await y.delete()
     vidmergelist.append(x)
     CHOOSE_UR_VIDMERGE_MODE = "الآن أرسل الفيديوهات الأخرى و اختر دمج الآن "
     CHOOSE_UR_VIDMERGE_MODE_BUTTONS= [[InlineKeyboardButton("دمج الآن ",callback_data="vidmergenow")]]
     vidnowpull = await x.reply(text = CHOOSE_UR_VIDMERGE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_VIDMERGE_MODE_BUTTONS))
     vidmergedel.append(vidnowpull)
     
async def vidmerge(vidmergelist):
     vidmergdir = "./data/"
     await checkdir(vidmergdir)
     for x in range(0,len(vidmergelist)):
        vidmergepath = await vidmergelist[x].download(file_name=vidmergdir)
        vidmergelist[x] = vidmergepath
     finalvid = await reduce(vidmergefunc,vidmergelist)
     await bot.send_video(CallbackQuery.from_user.id,finalvid)
     shutil.rmtree(vidmergdir)
     os.remove(finalvid)
     vidmergelist.clear()
       
     
async def vidmergefunc(x,y):
  vidres = str(random.randint(1,1000)) + '.mp4'
  os.system(f'''ffmpeg -i "{x}" -i "{y}"  -filter_complex "[0]scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,setsar=1[v0];[1]scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,setsar=1[v1];[v0][0:a:0][v1][1:a:0]concat=n=2:v=1:a=1[v][a]" -map "[v]" -map "[a]" "{vidres}"''') 
  os.remove(x)
  os.remove(y)
  return vidres

################ دمج الصور ######

async def photomerge(x):
      if len(photomergedel) != 0 :
        for y in photomergedel:
         await y.delete()
      imagedic.append(x)
      PRESS_MERGE_IMAGE = "الآن أرسل الصورة الأخرى و اختر دمج الآن "
      PRESS_MERGE_IMAGE_BUTTONS = [[InlineKeyboardButton("دمج الآن ",callback_data="imagemergenow")]]
      imagepullnow = await x.reply(text = PRESS_MERGE_IMAGE,reply_markup = InlineKeyboardMarkup(PRESS_MERGE_IMAGE_BUTTONS))
      photomergedel.append(imagepullnow)
      
async def imgmerge(imagedic,mergemode):
     imgmergid = imagedic[-1].from_user.id
     for x in range(0,len(imagedic)):
      imgpath = await imagedic[x].download(file_name="./downloads/")
      imagedic[x] = imgpath
     finalphoto = await reduce(mergemode,imagedic)
     await bot.send_document(imgmergid,finalphoto)
     await bot.send_photo(imgmergid,finalphoto)
     imagedic.clear()
     os.remove(finalphoto)
     
     
def merge_images1(file1, file2):
    image1 = Image.open(file1)
    image2 = Image.open(file2)
    (width1, height1) = image1.size
    (width2, height2) = image2.size
    result_width = max(width1,width2)
    if width1 > width2 :
      aspectoheight2 = (result_width * height2) / width2
      result_height = height1 + int(aspectoheight2)
      result = Image.new('RGB', (result_width, result_height))
      iso1 = image1.resize((result_width,height1))
      iso2 = image2.resize((result_width,int(aspectoheight2)))
      result.paste(iso1, box=(0, 0))
      result.paste(iso2, box=(0, height1))
    else :
      aspectoheight1 = (result_width * height1) / width1
      result_height = int(aspectoheight1) + height2
      result = Image.new('RGB', (result_width, result_height))
      iso1 = image1.resize((result_width,int(aspectoheight1)))
      iso2 = image2.resize((result_width,height2))
      result.paste(iso1, box=(0, 0))
      result.paste(iso2, box=(0, int(aspectoheight1)))
    outimg = str(random.randint(1,1000)) + '.jpg'
    result.save(outimg) 
    os.remove(file1)
    os.remove(file2)
    return outimg
    
def merge_images2(file1, file2):
    image1 = Image.open(file1)
    image2 = Image.open(file2)
    (width1, height1) = image1.size
    (width2, height2) = image2.size
    result_height = max(height1, height2)
    if height1 > height2 :
      aspectowidth2 = (result_height * width2) / height2
      result_width = width1 + int(aspectowidth2)
      result = Image.new('RGB', (result_width, result_height))
      iso1 = image1.resize((width1,result_height))
      iso2 = image2.resize((int(aspectowidth2),result_height))
      result.paste(iso1, box=(0, 0))
      result.paste(iso2, box=(width1, 0))
    else :
      aspectowidth1 = (result_height * width1) / height1
      result_width = width2 + int(aspectowidth1)
      result = Image.new('RGB', (result_width, result_height))
      iso1 = image1.resize((int(aspectowidth1),result_height))
      iso2 = image2.resize((width2,result_height))
      result.paste(iso1, box=(0, 0))
      result.paste(iso2, box=(int(aspectowidth1), 0))
    outimg = str(random.randint(1,1000)) + '.jpg'
    result.save(outimg) 
    os.remove(file1)
    os.remove(file2)
    return outimg
    
########### دمج الـPDF

async def pdfmerge(x):
       if len(pdfmergedel) != 0 :
        for y in pdfmergedel:
         await y.delete()
       pdfqueemerge.append(x)
       CHOOSE_UR_PDFMERGE_MODE = " بعد الانتهاء من إرسال الملفات اضغط دمج الآن "
       CHOOSE_UR_PDFMERGE_MODE_BUTTONS = [[InlineKeyboardButton("دمج الآن ",callback_data="pdfmergenow")]]

       pdfpullnow = await x.reply(text = CHOOSE_UR_PDFMERGE_MODE,reply_markup = InlineKeyboardMarkup(CHOOSE_UR_PDFMERGE_MODE_BUTTONS))
       pdfmergedel.append(pdfpullnow)
       
async def pdfmerge1(pdfqueemerge) :
      merger = PdfMerger()
      for x in pdfqueemerge:
       pdfmergepath = await x.download(file_name="./downloads/")
       filename = os.path.basename(pdfmergepath)
       merger.append(pdfmergepath)
      merger.write(filename)
      merger.close()
      await  bot.send_document(pdfqueemerge[-1].from_user.id,filename)
      os.remove(filename)
      pdfqueemerge.clear()
      
      

############# تحويل صور لـ pdf ##


async def image2pdf(x):
      if len(photomergedel) != 0 :
        for y in photomergedel:
         await y.delete()
      imgpdflist.append(x)
      THE_LAST_IMAGE = "عند إرسال آخر صورة , اضغط تحويل الآن"
      THE_LAST_IMAGE_BUTTONS = [[InlineKeyboardButton("تحويل الآن ",callback_data="convnow")]]
      imagepullnow = await x.reply(text = THE_LAST_IMAGE,reply_markup = InlineKeyboardMarkup(THE_LAST_IMAGE_BUTTONS))
      photomergedel.append(imagepullnow)
      
async def img2pdf1(imgpdflist,sendid=None):
    for x in imgpdflist :
      if not x.document :
       pdfdir = './img2pdf/'
       imgtopdfpath = await x.download(file_name=pdfdir)
      else :
        imgtopdfpath = x
      imagepdfdic1.append(imgtopdfpath)
      if len(imagepdfdic1) == 1 :
       imagey1 = Image.open(imagepdfdic1[0]).convert('RGB')
      if len(imagepdfdic1) > 1 :
       image2 = Image.open(imgtopdfpath).convert('RGB')
       imagepdfdic.append(image2)
      if x == imgpdflist[-1]:
         filename = os.path.basename(imgtopdfpath)
         nom,ex = os.path.splitext(filename)
         imgpdffile = f"{nom}.pdf"
    imagey1.save(imgpdffile,save_all=True, append_images=imagepdfdic)
    if not imgpdflist[0].document :
     await bot.send_document(imgpdflist[-1].from_user.id,imgpdffile)
    else : 
      await bot.send_document(sendid,imgpdffile)
    os.remove(imgpdffile)
    if os.path.isdir(pdfdir):
     shutil.rmtree(pdfdir)
    imagepdfdic1.clear()
    imagepdfdic.clear()
    imgpdflist.clear()
    
      
######## تحويل الملفات لـZip ####

async def zipfilefunc(x):
    if len(pdfmergedel) != 0 :
        for y in pdfmergedel:
         await y.delete()
    zipfilequee.append(x)
    PRESS_ZIP_FILE = "بعد الانتهاء من إرسال الملفات , اضغط تحويل الآن "
    PRESS_ZIP_FILE_BUTTONS = [
        [InlineKeyboardButton("تحويل الآن",callback_data="zipnow")]]
    pdfpullnow = await x.reply(text =PRESS_ZIP_FILE,reply_markup = InlineKeyboardMarkup(PRESS_ZIP_FILE_BUTTONS))
    pdfmergedel.append(pdfpullnow)


async def zipfunc1(dir,nom,quee=None):
  zipfile = nom + '.zip'
  if not quee == None :
    await checkdir(dir)
    for x in quee:
       zipfilepath = await x.download(file_name=dir)
  shutil.make_archive(nom, 'zip',dir)
  return zipfile
  
  
    
