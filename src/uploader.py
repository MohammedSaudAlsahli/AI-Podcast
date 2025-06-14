from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from dotenv import set_key
# from utils import Settings
# from pathlib import Path


# settings = Settings()
# ENV_PATH = settings.Config.env_file


class YouTubeUploader:
    def __init__(
        self,
        env_path,
        google_client_id: str,
        google_client_secret: str,
        google_project_id: str,
    ):
        self.env_path = env_path
        self.google_client_id = google_client_id
        self.google_client_secret = google_client_secret
        self.google_project_id = google_project_id
        self.CLIENT_CONFIG = {
            "installed": {
                "client_id": google_client_id,
                "client_secret": google_client_secret,
                "project_id": google_project_id,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "redirect_uris": ["http://localhost"],
            }
        }
        self.SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

    def __save_token_to_env(self, token):
        set_key(str(self.env_path), "ACCESS_TOKEN", token.token)
        set_key(str(self.env_path), "REFRESH_TOKEN", token.refresh_token)

    def get_authenticated_service(self):
        creds = None

        if settings.ACCESS_TOKEN and settings.REFRESH_TOKEN:
            creds = Credentials(
                token=settings.ACCESS_TOKEN,
                refresh_token=settings.REFRESH_TOKEN,
                token_uri=settings.TOKEN_URI,
                client_id=settings.GOOGLE_CLIENT_ID,
                client_secret=settings.GOOGLE_CLIENT_SECRET,
                scopes=self.SCOPES,
            )
            if creds.expired and creds.refresh_token:
                creds.refresh(Request())
                self.__save_token_to_env(creds)
        else:
            flow = InstalledAppFlow.from_client_config(
                self.CLIENT_CONFIG,
                self.SCOPES,
            )
            creds = flow.run_local_server(port=0)
            self.__save_token_to_env(creds)

        return build("youtube", "v3", credentials=creds)

    def upload_video(self, youtube, file_path, metadata):
        media = MediaFileUpload(file_path, chunksize=-1, resumable=True)
        request = youtube.videos().insert(
            part="snippet,status", body=metadata, media_body=media
        )

        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"📤 Upload progress: {int(status.progress() * 100)}%")

        print("✅ Upload complete!")
        print(f"🎬 Title: {response['snippet']['title']}")
        print(f"🔗 URL: https://youtu.be/{response['id']}")
        return response


if __name__ == "__main__":
    from utils import Settings, BG_VIDEO

    settings = Settings()
    ENV_PATH = settings.Config.env_file

    VIDEO_METADATA = {
        "snippet": {
            "title": "My AI-Podcast Episode",
            "description": "Uploaded via Python with .env token caching.",
            "tags": ["podcast", "ai", "python"],
            "categoryId": "22",
        },
        "status": {
            "privacyStatus": "private",
            "selfDeclaredMadeForKids": False,
        },
    }

    try:
        print("🚀 Starting YouTube upload...")
        uploader = YouTubeUploader(
            env_path=ENV_PATH,
            google_client_id=settings.GOOGLE_CLIENT_ID,
            google_client_secret=settings.GOOGLE_CLIENT_SECRET,
            google_project_id=settings.GOOGLE_PROJECT_ID,
        )
        youtube = uploader.get_authenticated_service()
        print("🔐 Authenticated!")
        uploader.upload_video(youtube, BG_VIDEO, VIDEO_METADATA)
    except Exception as e:
        print(f"❌ Error: {e}")
