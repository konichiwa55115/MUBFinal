from os import system as cmd
from config import checkdir,bot
import pypdfium2 as pdfium
from zipfile import ZipFile 
import tika
tika.initVM()
from tika import parser

######### استخراج pdf #####

async def pdfextract(filemessage,greyscale) :
        pdffilepath = await filemessage.download(file_name="./downloads/")
        filename = os.path.basename(pdffilepath)
        nom,ex = os.path.splitext(filename)
        zipnom = nom + '.zip'
        unzippath = "./unzipprocess/"
        await checkdir(unzippath)
        pdf = pdfium.PdfDocument(pdffilepath)
        global n_pages
        n_pages = len(pdf)
        for page_number in range(n_pages):
         page = pdf.get_page(page_number)
         pil_image = page.render_topil(
            scale=1,
            rotation=0,
            crop=(0, 0, 0, 0),
            colour=(255, 255, 255, 255),
            annotations=True,
            greyscale=greyscale,
            optimise_mode=pdfium.OptimiseMode.NONE,)
         pil_image.save(f"./{extractpath}/image_{str(page_number+1).zfill(5)}.png")
        os.remove(pdffilepath)
        return unzippath
         
############ استخراج zip #####


async def unzipfunc(unzipmessage)
         unzipfilepath = await unzipmessage.download(file_name="./downloads/")
         unzipzipid = unzipmessage.from_user.id
         unzippath = "./unzipprocess/"
         await checkdir(unzippath)
         with ZipFile(unzipfilepath, 'r') as zObject: 
          zObject.extractall(path=unzippath) 
         files = os.listdir(unzippath)
         for x in sorted(files):
          sentfile = f"{unzippath}{x}"
          tempnom,tempex = os.path.splitext(x)
          itsextension = tempex
          if itsextension == ".mp3" or itsextension == ".m4a" or itsextension == ".ogg":
            await bot.send_audio(unzipzipid,sentfile)
          elif itsextension == ".mp4" or itsextension == ".mkv" :
            await bot.send_video(unzipzipid,sentfile)
          elif itsextension == ".jpg" or itsextension == ".png" :
            await bot.send_photo(unzipzipid,sentfile)
          else :
              await bot.send_document(unzipzipid,sentfile)
         shutil.rmtree(unzippath)  
         
############ استخراج epub #####

async def ebupextract(epubmsg):
           epubpath = await epubmsg.download(file_name="./downloads/")
           filename = os.path.basename(epubpath)
           nom,ex = os.path.splitext(filename)
           epubid = epubpath.from_user.id
           unzippath = "./unzipprocess/"
           await checkdir(unzippath)
           parsed = parser.from_file(epubpath)
           textfile1 = f"mod{nom}.txt"
           textfile = f"{nom}.txt"
           finaltext = parsed['content']
           open(textfile1, "a").write(f" {finaltext} ")
           infile = open(textfile1,encoding='utf-8').readlines()
           res = open(textfile, 'w')
           word = "¦"
           for line in infile :
            if line.strip() and word not in line : 
             res.write(line)
           res.close()
           await bot.send_document(epubid,textfile)
           os.remove(textfile)
           os.remove(textfile1)
           os.remove(epubpath)
           
  

