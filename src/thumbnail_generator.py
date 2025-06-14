from gradio_client import Client


class ThumbnailGenerator:
    def __init__(
        self,
        current_prompt: str,
        client: str = "Agents-MCP-Hackathon/AI-Marketing-Content-Creator",
    ):
        self.current_prompt = current_prompt
        self.client = client
        self.theclient = Client(self.client)

    def __inhance_prompt(self) -> str:
        # client = Client(self.client)
        prompt_inh = self.theclient.predict(
            current_prompt=self.current_prompt,
            improvement_request=self.current_prompt,
            api_name="/improve_ai_prompt",
        )
        return prompt_inh[0]

    def generate_thumbnail(self) -> str:
        # client = Client(self.client)
        improved_prompt = self.__inhance_prompt()
        thumbnail = self.theclient.predict(
            prompt=improved_prompt,
            num_steps=50,
            style="none",
            api_name="/single_image_generation",
        )
        return thumbnail[0]


if __name__ == "__main__":
    thumbnail_generator = ThumbnailGenerator(
        current_prompt="Cricket Shenanigans, Cosmic Mapping, and College Paydays!!",
    )
    thumbnail = thumbnail_generator.generate_thumbnail()
    print(thumbnail)
