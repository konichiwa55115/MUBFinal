from os import system as cmd
import shutil
from multiinputmodule import img2pdf1
from config import bot

async def Coloringfunc(y,colormessage):
   color = y
   imgid = colormessage.from_user.id
   if colormessage.photo :
     colorpath = await colormessage.download(file_name="./downloads/")
     filename = os.path.basename(colorpath)
     nom,ex = os.path.splitext(filename)
     imgfile = f"{nom}.jpg"
     await colorpic(color,colorpath,imgfile) 
     await bot.send_photo(imgid,imgfile)
     os.remove(colorpath)
     os.remove(imgfile)
   elif exo == ".pdf":
    if color == "g":
     extractdir = await pdfextract(colormessage,True)
     imglist = sorted(os.listdir(extractdir))
     await img2pdf1(imglist,imgid)
    else : 
      extractdir = await pdfextract(colormessage,False)
      imglist = sorted(os.listdir(extractdir))
      coloredimglist = []
      coloredimgdir = './colordir/'
      await checkdir(coloredimgdir)
      for x in imglist : 
        await colorpic(color,extractdir+x,coloredimgdir+x) 
        coloredimglist.append(coloredimgdir+x)
        await img2pdf1(coloredimglist,imgid)
        shutil.rmtree(coloredimgdir)
      imglist.clear()


async def colorpic(color,colorpath,imgfile):
      if color == "g" : 
       cmd(f'''sh color2gray -f rms "{colorpath}" "{imgfile}" ''')
      elif color == "y" :
         cmd (f'''sh coloration -h 60 -s 50 -l 0 "{colorpath}" "{imgfile}" '''  )
      elif color == "b":
          cmd (f'''sh coloration -h 180 -s 50 -l 0 "{colorpath}" "{imgfile}" '''  )
      elif color == "r":
          cmd (f'''sh coloration -h 0 -s 50 -l 0 "{colorpath}" "{imgfile}" '''  )
      elif color == "p":
         cmd (f'''sh coloration -h 330 -s 50 -l 0 "{colorpath}" "{imgfile}" '''  )