from ai_model import AIModel 
from fake_model import FakeModel
from failing_model import FailingModel

class AIChatbot:
    def __init__(self, model: AIModel):
        self.model = model
        self.model_call_count = 0  # Track the number of times the model's ask method is called

    def ask(self, prompt: str) -> str:
        # Placeholder implementation for generating a response
        if prompt.strip() == "":
            raise ValueError("Prompt cannot be empty.")
        
        try:
            response = self.model.ask(prompt)
            self.model_call_count += 1
        except ConnectionError:
            return "Sorry, the AI service is currently unavailable."
        else:
            return response





