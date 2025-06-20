from moviepy import (
    AudioFileClip,
    VideoFileClip,
    concatenate_videoclips,
    concatenate_audioclips,
)
from src.utils import BG_VIDEO, ROOT_PATH


class PodcastGenerator:
    def __init__(
        self,
        mp3_files: list,
        output_file: str,
        bg_video: str = BG_VIDEO,
        fps: int = 24,
    ):
        self.mp3_files = mp3_files
        self.output_file = ROOT_PATH / "assets" / output_file
        self.bg_video = bg_video
        self.fps = fps

    def generate_podcast(self):
        audio_clips = [AudioFileClip(mp3_file) for mp3_file in self.mp3_files]
        combined_audio = concatenate_audioclips(audio_clips)
        video_path = self.bg_video
        bg_video = VideoFileClip(str(video_path))
        n_loops = int(combined_audio.duration // bg_video.duration) + 1
        looped_bg = concatenate_videoclips([bg_video] * n_loops).subclipped(
            0, combined_audio.duration
        )
        final_video = looped_bg.with_audio(combined_audio)
        final_video.write_videofile(f"{self.output_file}.mp4", fps=24)
