from utils import TEST_NEWS, SYSTEM_PROMPT
from httpx import post
from json import loads, JSONDecodeError
import re


class ScriptGenerator:
    def __init__(
        self,
        news: str,
        openrouter_api_key: str,
        system_prompt: str = SYSTEM_PROMPT,
        model: str = "deepseek/deepseek-r1-0528-qwen3-8b:free",
        site_url: str = "https://openrouter.ai/api/v1/chat/completions",
    ):
        self.news = news
        self.model = model
        self.site_url = site_url
        self.system_prompt = system_prompt
        self.openrouter_api_key = openrouter_api_key

    @staticmethod
    def __sanitize_script(raw_script: str) -> str:
        if raw_script.startswith("```json") and raw_script.endswith("```"):
            raw_script = raw_script[7:-3].strip()

        standardized_script = raw_script.replace("\r\n", "\n")
        standardized_script = re.sub(
            r"\n[\s\t]*\n", "\n", standardized_script, flags=re.MULTILINE
        )
        standardized_script = "\n".join(
            line.strip() for line in standardized_script.split("\n")
        )
        standardized_script = re.sub(r",\s*([}\]])", r"\1", standardized_script)

        return standardized_script.strip()

    def __raw_podcast_script(self) -> str:
        response = post(
            url=self.site_url,
            headers={
                "Authorization": f"Bearer {self.openrouter_api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "<YOUR_SITE_URL>",
                "X-Title": "<YOUR_SITE_NAME>",
            },
            data=dumps(
                {
                    "model": self.model,
                    "messages": [
                        {
                            "role": "system",
                            "content": self.system_prompt,
                        },
                        {
                            "role": "user",
                            "content": self.news,
                        },
                    ],
                }
            ),
        )
        cleaned_script = self.__sanitize_script(
            response.json()
            .get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
        )

        try:
            return loads(cleaned_script)
        except JSONDecodeError as e:
            return {
                "Error parsing JSON": {e},
                "cleaned_script": cleaned_script,
            }

    def result(self):
        return self.__raw_podcast_script()


if __name__ == "__main__":
    from json import dumps, dump
    from utils import Settings

    settings = Settings()

    script_generator = ScriptGenerator(
        news=TEST_NEWS,
        openrouter_api_key=settings.OPENROUTER_API_KEY,
    )
    podcast_script = script_generator.result()
    print((podcast_script))

    print(type(podcast_script))
    with open("podcast-script-output.json", "w", encoding="utf-8") as f:
        dump(podcast_script, f, indent=4, ensure_ascii=False)
