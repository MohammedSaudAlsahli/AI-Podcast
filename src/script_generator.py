from src.utils import SYSTEM_PROMPT
import json
import google.generativeai as genai


class ScriptGenerator:
    def __init__(
        self,
        news: str,
        google_api_key: str,
        system_prompt: str = SYSTEM_PROMPT,
        model: str = "models/gemini-1.5-flash",
    ):
        self.news = news
        self.model = model
        self.system_prompt = system_prompt
        genai.configure(api_key=google_api_key)
        self.client = genai

    def __extract_json(self, text: str) -> dict:
        """Extracts JSON from markdown or plain text response."""
        try:
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            return json.loads(text)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON format", "raw_response": text}

    def __generate_response(self) -> dict:
        """Generates and validates the JSON response."""
        try:
            model = self.client.GenerativeModel(
                model_name=self.model, system_instruction=self.system_prompt
            )

            response = model.generate_content(
                contents=[
                    {
                        "role": "user",
                        "parts": [
                            {
                                "text": f"Convert this news into podcast script JSON:\n{self.news}"
                            }
                        ],
                    }
                ],
                generation_config={
                    "temperature": 0.3,
                    "response_mime_type": "application/json",
                    "max_output_tokens": 2000,
                },
            )

            if not response.candidates:
                return {"error": "No response generated", "metadata": {}}

            json_response = self.__extract_json(response.text)

            return {
                "data": json_response,
                "metadata": {
                    "model": self.model,
                    "tokens": response.usage_metadata.total_token_count,
                    "finish_reason": response.candidates[0].finish_reason.name,
                },
            }

        except Exception as e:
            return {
                "error": str(e),
                "metadata": {"model": self.model, "exception_type": type(e).__name__},
            }

    def result(self) -> dict:
        """Returns the final JSON-formatted result."""
        response = self.__generate_response()

        if "error" in response:
            return {
                "status": "error",
                "message": response["error"],
                "metadata": response.get("metadata", {}),
            }
        else:
            return response.get("data")


if __name__ == "__main__":
    news_article = "NASA announces discovery of water on Mars..."
    generator = ScriptGenerator(
        news=news_article,
        google_api_key="YOUR_API_KEY",
    )

    result = generator.result()
    print(
        json.dumps(
            result,
            indent=2,
        )
    )
