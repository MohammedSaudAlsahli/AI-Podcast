from gradio_client import Client


class TTS:
    def __init__(
        self,
        prompt: str,
        client: str = "NihalGazi/Text-To-Speech-Unlimited",
        voice: str = "onyx",
        emotion: str = "excited and joyful",
        use_random_seed: bool = True,
        specific_seed: int = 12345,
        api_name: str = "/text_to_speech_app",
    ):
        self.prompt = prompt
        self.client = client
        self.voice = voice
        self.emotion = emotion
        self.use_random_seed = use_random_seed
        self.specific_seed = specific_seed
        self.api_name = api_name

    def __tts_result(self):
        client = Client(self.client)
        client.chat
        result = client.predict(
            prompt=self.prompt,
            voice=self.voice,
            emotion=self.emotion,
            use_random_seed=self.use_random_seed,
            specific_seed=self.specific_seed,
            api_name=self.api_name,
        )
        return result

    def result(self):
        return self.__tts_result()


if __name__ == "__main__":
    script = """
Introduction:
"Welcome to today’s episode of The Productivity Podcast! I’m your host, and let me ask you this—how often do you feel like there’s just never enough time? [cry] It’s overwhelming, isn’t it? But don’t worry—today, we’re diving into the art of time management to help you take control."

Main Discussion:
"Think of time as your most precious resource—once it’s gone, it’s gone. Surely you wouldn’t want to waste it on things that don’t really matter, right? [laughs] Start by prioritizing tasks that align with your goals. And hey, saying 'no' isn’t rude—it’s self-care! [laughs]"

Conclusion:
"That’s it for today! Manage your time wisely, and you’ll create a life that’s both productive and fulfilling. Until next time—take care! [laughs]"  """
    tts = TTS(prompt=script)
    audio = tts.result()
    print(f"Generated audio: {audio}")
    # You can save or play the audio as needed
    # For example, you can use a library like pydub to save it to a file
    # from pydub import AudioSegment
    # audio_segment = AudioSegment.from_file(io.BytesIO(audio), format="mp3")
    # audio_segment.export("output.mp3", format="mp3")
