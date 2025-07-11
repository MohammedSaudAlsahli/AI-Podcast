from src.news_fetch import News
from src.script_generator import ScriptGenerator
from src.text_to_speech import TTS
from src.podcast_generator import PodcastGenerator
from src.uploader import YouTubeUploader
from src.utils import Settings, ROOT_PATH
import re
import os
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
logging.getLogger("urllib3").setLevel(logging.WARNING)


def main():
    settings = Settings()

    ENV_PATH = settings.Config.env_file

    news = News(newsapi_key=settings.NEWS_API_KEY).articles()

    script_generator = ScriptGenerator(
        news=str(news),
        google_api_key=settings.GOOGLE_API_KEY,
    )

    podcast_script = script_generator.result()

    podcast_title = (
        f"{podcast_script.get('podcastTitle')} - {podcast_script.get('episodeTitle')}"
    )

    formatted_description = "\n".join(
        [f'[{line["host"]}]: "{line["line"]}"' for line in podcast_script["script"]]
    )

    file_output_name = re.sub(
        r"[^\w]+",
        "_",
        podcast_title,
    )
    mp3_files = TTS(prompt=podcast_script).generateAudio()
    for file in mp3_files:
        if file is None:
            mp3_files = TTS(prompt=podcast_script).generateAudio()

    PodcastGenerator(
        mp3_files=mp3_files,
        output_file=file_output_name,
    ).generate_podcast()

    VIDEO_METADATA = {
        "snippet": {
            "title": f"{podcast_title}",
            "description": f"{formatted_description}",
            "tags": ["podcast", "ai", "python"],
            "categoryId": "22",
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False,
        },
    }

    uploader = YouTubeUploader(
        env_path=ENV_PATH,
        google_client_id=settings.GOOGLE_CLIENT_ID,
        google_client_secret=settings.GOOGLE_CLIENT_SECRET,
        google_project_id=settings.GOOGLE_PROJECT_ID,
        token_uri=settings.TOKEN_URI,
        access_token=settings.ACCESS_TOKEN,
        refresh_token=settings.REFRESH_TOKEN,
    )

    video_path = ROOT_PATH / "assets" / f"{file_output_name}.mp4"

    uploader.upload(
        metadata=VIDEO_METADATA,
        video_path=video_path,
    )

    if video_path.exists():
        os.remove(video_path)
        logger.info(f"Deleted video file: {video_path}")


if __name__ == "__main__":
    main()
