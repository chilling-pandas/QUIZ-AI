import requests

class LLMService:
    def __init__(self, model_name="qwen2.5:3b-instruct-q4_K_M"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model_name

    def generate(self, prompt: str):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=payload)
        return response.json()["response"]
