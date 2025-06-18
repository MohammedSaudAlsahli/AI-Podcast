from gradio_client import Client
import time


class TTS:
    def __init__(
        self,
        prompt: str,
        client: str = "NihalGazi/Text-To-Speech-Unlimited",
        emotion: str = "excited and joyful",
        use_random_seed: bool = True,
        specific_seed: int = 12345,
        api_name: str = "/text_to_speech_app",
    ):
        self.prompt = prompt
        self.client = client
        self.emotion = emotion
        self.use_random_seed = use_random_seed
        self.specific_seed = specific_seed
        self.api_name = api_name

    def __tts_result(self, voice: str):
        client = Client(self.client)
        result = client.predict(
            prompt=self.prompt,
            voice=voice,
            emotion=self.emotion,
            use_random_seed=self.use_random_seed,
            specific_seed=self.specific_seed,
            api_name=self.api_name,
        )
        return result

    def __female(self):
        return self.__tts_result(voice="alloy")

    def __male(self):
        return self.__tts_result(voice="dan")

    def generateAudio(self):
        mp3_files = []

        for script in self.prompt.get("script", []):
            prompt = script.get("line", "")
            if script.get("host") == "Emma":
                audio = TTS(prompt=prompt).__female()
                if audio[0] is None:
                    print(f"Retrying female voice for: {prompt}")
                    time.sleep(1)
                    audio = TTS(prompt=prompt).__female()
            else:
                audio = TTS(prompt=prompt).__male()
                if audio[0] is None:
                    print(f"Retrying male voice for: {prompt}")
                    time.sleep(1)
                    audio = TTS(prompt=prompt).__male()

            mp3_files.append(audio[0])
            time.sleep(1)

        return mp3_files
