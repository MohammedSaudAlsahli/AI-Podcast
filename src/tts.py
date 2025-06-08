from gradio_client import Client


class TTS:
    def __init__(
        self,
        text: str,
        model_name: str = "k2-fsa/text-to-speech",
        language: str = "English",
        repo_id: str = "csukuangfj/vits-piper-en_GB-southern_english_male-medium|8 speakers",
        sid: str = "4",
        speed: float = 1,
        api_name: str = "/process",
    ):
        self.model_name = model_name
        self.text = text
        self.language = language
        self.repo_id = repo_id
        self.sid = sid
        self.speed = speed
        self.api_name = api_name

    def tts_result(self):
        client = Client(self.model_name)
        result = client.predict(
            language=self.language,
            repo_id=self.repo_id,
            text=self.text,
            sid=self.sid,
            speed=self.speed,
            api_name=self.api_name,
        )
        return result

    def result(self):
        return self.tts_result()
