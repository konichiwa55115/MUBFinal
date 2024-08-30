from httplib2 import HttpLib2Error
from oauth2client.client import (
    OAuth2WebServerFlow,
    FlowExchangeError,
    OAuth2Credentials,
)
from http.client import (
    NotConnected,
    IncompleteRead,
    ImproperConnectionState,
    CannotSendRequest,
    CannotSendHeader,
    ResponseNotReady,
    BadStatusLine,
)
import urllib3 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from apiclient import http, errors, discovery
from oauth2client.file import Storage
from typing import Optional, Tuple, Union
from config import bot
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery, ForceReply,Message
###################

async def progress(
    cur: Union[int, float],
    tot: Union[int, float],
    start_time: float,
    status: str,
    snt: Message,
    c: bot,
    download_id: str,
):
    if not c.download_controller.get(download_id):
        raise StopTransmission

    try:
        diff = int(time.time() - start_time)

        if (int(time.time()) % 5 == 0) or (cur == tot):
            await asyncio.sleep(1)
            speed, unit = human_bytes(cur / diff, True)
            curr = human_bytes(cur)
            tott = human_bytes(tot)
            eta = datetime.timedelta(seconds=int(((tot - cur) / (1024 * 1024)) / speed))
            elapsed = datetime.timedelta(seconds=diff)
            progress = round((cur * 100) / tot, 2)
            text = f"{status}\n\n{progress}% done.\n{curr} of {tott}\nSpeed: {speed} {unit}PS"
            f"\nETA: {eta}\nElapsed: {elapsed}"
            await snt.edit_text(
                text=text,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Cancel!", f"cncl+{download_id}")]]
                ),
            )

    except Exception as e:
        pass
class MaxRetryExceeded(Exception):
    pass


class UploadFailed(Exception):
    pass


class YouTube:

    MAX_RETRIES = 10

    RETRIABLE_EXCEPTIONS = (
        HttpLib2Error,
        IOError,
        NotConnected,
        IncompleteRead,
        ImproperConnectionState,
        CannotSendRequest,
        CannotSendHeader,
        ResponseNotReady,
        BadStatusLine,
    )

    RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

    def __init__(self, auth: discovery.Resource, chunksize: int = -1):
        self.youtube = auth
        self.request = None
        self.chunksize = chunksize
        self.response = None
        self.error = None
        self.retry = 0

    def upload_video(
        self, video: str, properties: dict, progress: callable = None, *args
    ) -> dict:
        self.progress = progress
        self.progress_args = args
        self.video = video
        self.properties = properties

        body = dict(
            snippet=dict(
                title=self.properties.get("title"),
                description=self.properties.get("description"),
                categoryId=self.properties.get("category"),
            ),
            status=dict(privacyStatus=self.properties.get("privacyStatus")),
        )

        media_body = http.MediaFileUpload(
            self.video,
            chunksize=self.chunksize,
            resumable=True,
        )

        self.request = self.youtube.videos().insert(
            part=",".join(body.keys()), body=body, media_body=media_body
        )
        self._resumable_upload()
        return self.response

    def _resumable_upload(self) -> dict:
        response = None
        while response is None:
            try:
                status, response = self.request.next_chunk()
                if response is not None:
                    if "id" in response:
                        self.response = response
                    else:
                        self.response = None
                        raise UploadFailed(
                            "The file upload failed with an unexpected response:{}".format(
                                response
                            )
                        )
            except errors.HttpError as e:
                if e.resp.status in self.RETRIABLE_STATUS_CODES:
                    self.error = "A retriable HTTP error {} occurred:\n {}".format(
                        e.resp.status, e.content
                    )
                else:
                    raise
            except self.RETRIABLE_EXCEPTIONS as e:
                self.error = "A retriable error occurred: {}".format(e)

            if self.error is not None:
                self.retry += 1

                if self.retry > self.MAX_RETRIES:
                    raise MaxRetryExceeded("No longer attempting to retry.")

                max_sleep = 2 ** self.retry
                sleep_seconds = random.random() * max_sleep
                time.sleep(sleep_seconds)
class Uploader:
    def __init__(self, file: str, title: Optional[str] = None):
        self.file = file
        self.title = title
        self.video_category = {
            1: "Film & Animation",
            2: "Autos & Vehicles",
            10: "Music",
            15: "Pets & Animal",
            17: "Sports",
            19: "Travel & Events",
            20: "Gaming",
            22: "People & Blogs",
            23: "Comedy",
            24: "Entertainment",
            25: "News & Politics",
            26: "Howto & Style",
            27: "Education",
            28: "Science & Technology",
            29: "Nonprofits & Activism",
        }

    async def start(self, progress: callable = None, *args) -> Tuple[bool, str]:
        self.progress = progress
        self.args = args

        await self._upload()

        return self.status, self.message

    async def _upload(self) -> None:
        try:
            loop = asyncio.get_running_loop()

            auth = GoogleAuth(CLIENT_ID, CLIENT_SECRET)

            if not os.path.isfile("auth_token.txt"):
                self.status = False
                self.message = "أنت لم تقم بالمصادقة بعد !."
                return

            auth.LoadCredentialsFile("auth_token.txt")
            google = await loop.run_in_executor(None, auth.authorize)
            categoryId = 27
            categoryName = self.video_category[categoryId]
            title = self.title if self.title else os.path.basename(self.file)
            title = (
                (title)
                .replace("<", "")
                .replace(">", "")[:100]
            )
            description = (""+ "\n")[:5000]
            privacyStatus = "private"
            properties = dict(
                title=title,
                description=description,
                category=categoryId,
                privacyStatus=privacyStatus,
            )
            youtube = YouTube(google)
            r = await loop.run_in_executor(
                None, youtube.upload_video, self.file, properties
            )


            video_id = r["id"]
            self.status = True
            self.message = (
                f"[{title}](https://youtu.be/{video_id}) uploaded to YouTube under category "
                f"{categoryId} ({categoryName})"
            )
        except Exception as e:
            self.status = False
            self.message = f"Error occuered during upload.\nError details: {e}"



class AuthCodeInvalidError(Exception):
    pass


class InvalidCredentials(Exception):
    pass


class NoCredentialFile(Exception):
    pass


class GoogleAuth:
    OAUTH_SCOPE = ["https://www.googleapis.com/auth/youtube.upload"]
    REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"
    API_SERVICE_NAME = "youtube"
    API_VERSION = "v3"

    def __init__(self, CLIENT_ID: str, CLIENT_SECRET: str):
        self.flow = OAuth2WebServerFlow(
            CLIENT_ID, CLIENT_SECRET, self.OAUTH_SCOPE, redirect_uri=self.REDIRECT_URI
        )
        self.credentials: Optional[OAuth2Credentials] = None

    def GetAuthUrl(self) -> str:
        return self.flow.step1_get_authorize_url()

    def Auth(self, code: str) -> None:
        try:
            self.credentials = self.flow.step2_exchange(code)
        except FlowExchangeError as e:
            raise AuthCodeInvalidError(e)
        except Exception:
            raise

    def authorize(self):
        try:
            if self.credentials:
                http = httplib2.Http()
                self.credentials.refresh(http)
                http = self.credentials.authorize(http)
                return discovery.build(
                    self.API_SERVICE_NAME, self.API_VERSION, http=http
                )
            else:
                raise InvalidCredentials("No credentials!")
        except Exception:
            raise

    def LoadCredentialsFile(self, cred_file: str) -> None:
        if not os.path.isfile(cred_file):
            raise NoCredentialFile(
                "No credential file named {} is found.".format(cred_file)
            )
        storage = Storage(cred_file)
        self.credentials = storage.get()

    def SaveCredentialsFile(self, cred_file: str) -> None:
        storage = Storage(cred_file)
        storage.put(self.credentials)

    