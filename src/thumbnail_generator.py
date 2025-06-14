from gradio_client import Client

client = Client("Agents-MCP-Hackathon/AI-Marketing-Content-Creator")
result = client.predict(
    current_prompt="Hello!!",
    improvement_request="Hello!!",
    api_name="/improve_ai_prompt",
)
print(result)
