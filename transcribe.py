from os import system as cmd
import requests,pytesseract
from config import checkdir,bot


####### vid & aud transcribtion #####

async def vidaudtransfunc(audmsg,token):
        transpath = await audmsg.download(file_name="./downloads/")
        audtransid = audmsg.from_user.id
        filename = os.path.basename(transpath)
        nom,ex = os.path.splitext(filename)
        mp3file = f"{nom}.mp3"
        result= f"{nom}.txt"
        if not ex == '.mp3':
         cmd(f'''ffmpeg -i "{transpath}" -q:a 0 -map a "{mp3file}" -y ''') 
         os.remove(transpath) 
        else :
          os.replace(transpath,mp3file)
        cmd(f'''python3 speech.py '{token}' "{mp3file}" "{result}" ''')
        os.remove(mp3file) 
        await bot.send_document(audtransid, result)
        os.remove(result)   
        
############ image ocr #####
        
async def ocrfunc(langcode,imgocrmsg):
    data_url = f"https://github.com/tesseract-ocr/tessdata/raw/main/{langcode}.traineddata"
    dirs = r"/usr/share/tesseract-ocr/4.00/tessdata"
    path = os.path.join(dirs, f"{langcode}.traineddata")
    data = requests.get(data_url, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0'})
    open(path, 'wb').write(data.content)
    if imgocrmsg.photo :
    imgocrpath = imgocrmsg.download(file_name="./downloads/")
    else :
      imgocrpath = imgocrmsg
    text = pytesseract.image_to_string(imgocrpath, lang=langcode)
    textspaced = re.sub(r'\r\n|\r|\n', ' ', text)
    os.remove(imgocrpath)
    return textspaced

        
########## Pdf Ocr ######

async def pdfocrfunc(langcode,pdfmessage):
    pdffile = await pdfmessage.download(file_name="./downloads/")
    filename = os.path.basename(pdffile)
    nom,ex = os.path.splitext(filename)
    resultfile = f"{nom}.txt"
    pdfocrdir = "./temp/"
    await checkdir(pdfocrdir)
    pdf = pdfium.PdfDocument(filepath)
    n_pages = len(pdf)
    for page_number in range(n_pages):
     page = pdf.get_page(page_number)
     pil_image = page.render_topil(
        scale=1,
        rotation=0,
        crop=(0, 0, 0, 0),
        colour=(255, 255, 255, 255),
        annotations=True,
        greyscale=False,
        optimise_mode=pdfium.OptimiseMode.NONE,
    )
     pil_image.save(f"./temp/image_{page_number+1}.png")
    os.remove(filepath) 
    for x in range(1,len(os.listdir(pdfocrdir)))
     cmd(f'''sh textcleaner -g "./temp/image_{x}.png" "image_{x}.png" ''')
     textspaced = await ocrfunc(langcode,f"image_{x}.png")
     open(resultfile,'a').write(f'{textspaced} \n')
    await bot.send_document(pdfmessage.from_user.id, resultfile)
    shutil.rmtree(pdfocrdir) 
    os.remove(resultfile)

