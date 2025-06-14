from moviepy import (
    AudioFileClip,
    VideoFileClip,
    concatenate_videoclips,
    concatenate_audioclips,
)
from pathlib import Path

from utils import TEST_AUDIO


class PodcastGenerator:
    def __init__(
        self,
        mp3_files: list,
        output_file: str = "output.mp4",
        bg_video: str = "bg_video.mp4",
        fps: int = 24,
    ):
        self.mp3_files = mp3_files
        self.output_file = output_file
        self.bg_video = bg_video
        self.fps = fps

    def generate_podcast(self) -> None:
        audio_clips = [AudioFileClip(mp3_file) for mp3_file in self.mp3_files]
        combined_audio = concatenate_audioclips(audio_clips)
        video_path = Path(__file__).parent / self.bg_video
        bg_video = VideoFileClip(str(video_path))
        n_loops = int(combined_audio.duration // bg_video.duration) + 1
        looped_bg = concatenate_videoclips([bg_video] * n_loops).subclipped(
            0, combined_audio.duration
        )
        final_video = looped_bg.with_audio(combined_audio)
        final_video.write_videofile("looped_video_with_audio.mp4", fps=24)


if __name__ == "__main__":
    TEST_AUDIO = [
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/c88e3f45084f76f67b2692257d05ac40feff9eb1380503e9efda0818636db082/tmpmbvgwbmb.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/7d43a8718de9a1ace173dc2d2aa839a7639c550a25ff5fa77b1faf41201b26e7/tmpk5aerjt8.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/d0aff4360574af938ddcb7781e9f7f277d005503759759aba98c1d7b9f11b885/tmpsigi_9u6.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/efaf48bb9e22fd227cf9391d2a39a3b466030b450db50ac8597020a87222443f/tmp_0n591u6.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/a6988f803a85d4b3431318b3c240b641e6aca6ebe1dfef58dd4a62f99f18387f/tmpapu03yjy.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/bc362e88eda0505842d94a0a4e938478788ff87a34d55b0346e4120f111d5368/tmpsqeosf9p.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/c3f947f10c170c8a6b95434c403aa49e4cf1475797231ecd41a693b305d9b871/tmpgjfyn_a0.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/593d9fcb8c32135c0a677ec66959cb496baab7a1da9a3a84f61def7640ed02eb/tmpl04ikukv.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/388d443fc3feb96028cf4fd28188b6452908988f61af881c08cef7a21cce5b4d/tmpgnyki66z.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/3cf5263b093f17b11e22c79ffb2ac63710d93860bdd39e053b2a53ae9a2c5872/tmpq60wnlpk.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/ed4223d107b64004965a1acefa3c1a4a7d9719a9bcd5193964a8c3d4fa4c571f/tmpsfae3dwp.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/049e7a55cd1e6f64e16b29cbdc1430842f3ccc2b7ca07c25f77562e0cbeec933/tmp_85fz4ym.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/d292eccf711cd7ea798183ff5631e2c239cbe55a7eafd6bb414e872eb77c9f2b/tmpz3lgdc6k.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/e4932ec83af1404128fa2ccac58d72b3bead9fd6afd8a80cbe9adf6443d86554/tmppo1s6h2b.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/556886cbcf2c30757fd467a1465932b6c3d86d6b043b6b7e9727966f137cf2c3/tmp9giwiaw9.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/d006c92f235bfcd762bd46bffe094a720f926b24fe5b05b12cf3c55fcab4a15a/tmplt0v3gxj.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/6e05a240b8e1062334d51f7652306d8cb8eb38d80b59016eed4b6ef19fe5dd07/tmpvfii_vfn.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/693946ac9de57706210f007bc0e2ac2076baea6e305a288725edf38f7f848b21/tmpkcxyobgy.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/45a6cd9c75f004ce27b7215f949967d47ad75a3fcea55e7a15cbbefd4d3dd9f0/tmp_suhcvr3.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/f17bb34ae19b042f2ab078791316beb616498797fbfc3ab24938e78677f0b486/tmpyzzrclgj.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/4335f6c102a5195fe1a7ab977e29904bc32ef8ce7b24a21d2305b2de7b8a9958/tmpx3stbavo.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/4485924a0a03eb085906e5106613d3b177734e1db59fdc1a0833539ff4b90a2c/tmp0_lr40hj.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/233bb66da88c2e235a5bcd5a16dab987a4d0838a958d727377873fde215f7f4b/tmpd88ibr_p.mp3",
        "/private/var/folders/6g/pgyz9pk12_j3lsmmkwp0n25w0000gn/T/gradio/b71edbe2314b48590fa7ead674b122f9e0c3e02013e642f3fb746884f62ec51d/tmp4af7gxcq.mp3",
    ]
    PodcastGenerator(mp3_files=TEST_AUDIO).generate_podcast()
