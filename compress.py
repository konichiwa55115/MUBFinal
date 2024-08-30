from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet
from os import system as cmd
import os
from config import bot


async def compressaud(rate,audcompmessage):
    comppath = await audcompmessage.download(file_name="./downloads/")
    filename = os.path.basename(comppath)
    nom,ex = os.path.splitext(filename)
    mp3file = f"{nom}.mp3"
    audcompid = audcompmessage.from_user.id
    cmd(f''' ffmpeg -i "{comppath}" -b:a "{rate}" "{mp3file}" -y ''' )
    await bot.send_audio(audcompid, mp3file)
    os.remove(comppath) 
    os.remove(mp3file) 
    
    
async def pdfcompress(pdfcompmessage):
          pdfpath = await pdfcompmessage.download(file_name="./downloads/")
          filename = os.path.basename(pdfpath)
          pdfcompid = pdfcompmessage.from_user.id
          PDFNet.Initialize("demo:1676040759361:7d2a298a03000000006027df7c81c9e05abce088e7286e8312e5e06886"); doc = PDFDoc(f"{pdfpath}")
          doc.InitSecurityHandler()
          Optimizer.Optimize(doc)
          doc.Save(filename, SDFDoc.e_linearized)
          doc.Close()
          await bot.send_document(pdfcompid, filename)
          os.remove(pdfpath) 
          os.remove(filename)
          
          
async def vidcompress(vidcompmessage):
        videopath = await vidcompmessage.download(file_name="./downloads/")
        filename = os.path.basename(videopath)
        nom,ex = os.path.splitext(filename)
        mp4file = f"{nom}.mp4"
        vidcompid = vidcompmessage.from_user.id
        cmd(f'''ffmpeg -y -i "{videopath}" -vf "setpts=1*PTS" -r 10 "{mp4file}"''')
        await bot.send_video(vidcompid,mp4file)
        os.remove(mp4file)
        os.remove(videopath)
        