from gradio_client import Client
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class ThumbnailGenerator:
    def __init__(
        self,
        current_prompt: str,
        client: str = "Agents-MCP-Hackathon/AI-Marketing-Content-Creator",
    ):
        self.current_prompt = current_prompt
        self.client = client
        self.theclient = Client(self.client)

    def __inhance_prompt(self):
        prompt_inh = self.theclient.predict(
            current_prompt=self.current_prompt,
            improvement_request=self.current_prompt,
            api_name="/improve_ai_prompt",
        )
        return prompt_inh[0]

    def generate_thumbnail(self):
        improved_prompt = self.__inhance_prompt()
        thumbnail = self.theclient.predict(
            prompt=improved_prompt,
            num_steps=50,
            style="none",
            api_name="/single_image_generation",
        )
        return thumbnail[0]
