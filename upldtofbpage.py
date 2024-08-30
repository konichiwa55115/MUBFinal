import os,requests

######### الرفع لفيسبوك #######

async def upldtofbpage(pageid,accesstoken,x,replo):
    fbpageid = pageid
    fbpath = await x.download(file_name="./downloads/")
    files = {'source': open(fbpath, 'rb')}
    payload = {
              'access_token': accesstoken, 
              'title': x.caption,
              'description': x.caption }
    url1 = f'''https://graph-video.facebook.com/v19.0/{fbpageid}/videos'''
    x2 = requests.post(url1,files=files,data=payload,verify=False)
    videoidlst = x2.text.replace('"','').replace('{','').replace('}','').split(':')
    videoid = videoidlst[1]
    videolink = f"https://www.facebook.com/{pageid}/videos/{videoid}/"
    await replo.edit_text(videolink)
    os.remove(fbpath)
    