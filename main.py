from src.news_fetch import News
from src.script_generator import ScriptGenerator
from src.text_to_speech import TTS
from src.podcast_generator import PodcastGenerator
from src.uploader import YouTubeUploader
from src.utils import Settings
import re
from pathlib import Path


def main():
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
    news = News(newsapi=settings.NEWS_API_KEY).articles()
    script_generator = ScriptGenerator(
        news=str(news),
        google_api_key=settings.GOOGLE_API_KEY,
    )
    podcast_script = script_generator.result()
    podcast_title = (
        f"{podcast_script.get('podcastTitle')} - {podcast_script.get('episodeTitle')}"
    )
    print(podcast_script)
    file_output_name = re.sub(
        r"[^\w]+",
        "_",
        podcast_title,
    )
    # mp3_files = []
    mp3_files = TTS(prompt=podcast_script).generateAudio()
    # for script in podcast_script.get("script"):
    #     if script.get("host") == "Emma":
    #         audio = TTS(prompt=script.get("line")).female()
    #         if audio[0] is None:
    #             print(f"Failed to generate audio for: {script.get('line')}")
    #             audio = TTS(prompt=script.get("line")).female()
    #         mp3_files.append(audio[0])
    #     else:
    #         audio = TTS(prompt=script.get("line")).male()
    #         if audio[0] is None:
    #             print(f"Failed to generate audio for: {script.get('line')}")
    #             audio = TTS(prompt=script.get("line")).male()
    #         mp3_files.append(audio[0])

    print(mp3_files)
    PodcastGenerator(
        mp3_files=mp3_files,
        output_file=file_output_name,
    ).generate_podcast()
    # VIDEO_METADATA = {
    #     "snippet": {
    #         "title": f"{podcast_title}",
    #         "description": f"{podcast_script}",
    #         "tags": ["podcast", "ai", "python"],
    #         "categoryId": "22",
    #     },
    #     "status": {
    #         "privacyStatus": "private",
    #         "selfDeclaredMadeForKids": False,
    #     },
    # }
    # uploader = YouTubeUploader(
    #     env_path=ENV_PATH,
    #     google_client_id=settings.GOOGLE_CLIENT_ID,
    #     google_client_secret=settings.GOOGLE_CLIENT_SECRET,
    #     google_project_id=settings.GOOGLE_PROJECT_ID,
    # )
    # uploader.upload(
    #     metadata=VIDEO_METADATA,
    #     video_path=Path(__file__) / file_output_name,
    # )


if __name__ == "__main__":
    main()
