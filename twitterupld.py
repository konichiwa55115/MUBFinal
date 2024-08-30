from threading import Lock 
from typing import Union
from tgbot_ping import get_runtime
import logging,re,traceback,tweepy,tempfile,requests
from pyrogram import Client, enums, filters, types
from config import getdur,bot

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(filename)s [%(levelname)s]: %(message)s")
tweet_format = "https://twitter.com/{screen_name}/status/{id}"

async def twitterupload(u,w,x,y,z):
    global TwitterClient,TwitterApi
    TwitterClient, TwitterApi = await __connect_twitter(u,w,x,y)
    videodur = z.video.duration
    twittervidpath = await z.download(file_name="./upldtotwitter/")
    if videodur == 0 : 
      videodur = await getdur(twittervidpath)
    if videodur <= 140 :
      await tweet_single_photo_handler(TwitterClient, z)
      os.remove(twittervidpath)
    else : 
      cmd(f"python3 ffmpeg-split.py -f '{twittervidpath}' -s 130")
      os.remove(twittervidpath)
      listofparts = os.listdir('./upldtotwitter')
      groups = []
      files = []
      partslist = sorted(listofparts)
      for part in partslist :
        vidpart = f"./upldtotwitter/{part}"
        partcaption = z.caption + ' جـ'+ str(partslist.index(part)+1)
        sentpart = await bot.send_video(z.from_user.id,vidpart,caption=partcaption)
        groups.append(sentpart)
      for group in groups:
         img_data = await group.download(in_memory=True)
         setattr(img_data, "mode", "rb")
         caption = z.caption
         if caption:
            setattr(z, "text", caption)
         files.append(img_data)
      result = await send_tweet(z, files)
      await notify_result(result, z)
      os.remove(vidpart)
      


async def upload_media(api, pic) -> Union[list, None]:
     if pic is None:
        return None
     ids = []
     for item in pic:
        item.seek(0)
        mid = api.media_upload(item.name, file=item)
        ids.append(mid)
     return [i.media_id for i in ids]

async def __get_tweet_id_from_reply(message) -> int:
     reply_to = twittermessage.reply_to_message
     if reply_to:
        tweet_id = await __get_tweet_id_from_url(reply_to.entities[0].url or "")
     else:
        tweet_id = None
     logging.info("Replying to %s", tweet_id)
     return tweet_id

async def __get_tweet_id_from_url(url) -> int:
     try:
        # https://twitter.com/williamwoo7/status/1326147700425809921?s=20
        tweet_id = re.findall(r"https?://twitter\.com/.+/status/(\d+)", url)[0]
     except IndexError:
        tweet_id = None
     return tweet_id

async def __connect_twitter(u,w,x,y):
     CONSUMER_KEY = u
     CONSUMER_SECRET = w
     ACCESS_KEY = x
     ACCESS_SECRET = y
     client = tweepy.Client(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_KEY,
        access_token_secret=ACCESS_SECRET,
     )
     api = tweepy.API(
        tweepy.OAuth1UserHandler(
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token=ACCESS_KEY,
            access_token_secret=ACCESS_SECRET,
        )
     )
     return client,api

async def tweet_single_photo_handler(client, message: types.Message):
     await twittermessage.reply_chat_action(enums.ChatAction.UPLOAD_PHOTO)
     img_data = await message.download(in_memory=True)
     setattr(img_data,"mode","rb")
     result = await send_tweet(message,[img_data])
     await notify_result(result,twittermessage)

async def send_tweet(message, pics: Union[list, None] = None) -> dict:
    logging.info("Preparing tweet for...")
    chat_id = twittermessage.chat.id
    text = message.text or message.caption
    if not text:
        text = ""
    tweet_id = await __get_tweet_id_from_reply(message)
    logging.info("Tweeting...")
    ids = await upload_media(TwitterApi, pics)
    try:
        status = TwitterClient.create_tweet(text=text, media_ids=ids, in_reply_to_tweet_id=tweet_id)
        logging.info("Tweeted")
        response = status.data
    except Exception as e:
        if "Your Tweet text is too long." in str(e):
            logging.warning("Tweet too long, trying to make it shorter...")
            # try to post by making it shorter
            status = TwitterClient.create_tweet(text=text[:110] + "...", media_ids=ids, in_reply_to_tweet_id=tweet_id)
            response = status.data
        else:
            logging.error(traceback.format_exc())
            response = {"error": str(e)}

    return response
    
async def notify_result(result, message: types.Message):
     if result.get("error"):
        resp = f"❌ Error: `{result['error']}`"
     else:
        url = tweet_format.format(screen_name="x", id=result["id"])
        resp = f"✅ Your [tweet]({url}) has been sent.\n"
     await twittermessage.reply_text(resp, quote=True, parse_mode=enums.ParseMode.MARKDOWN)
