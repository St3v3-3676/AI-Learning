from ai_model import AIModel 
from fake_model import FakeModel

class AIChatbot:
    def __init__(self, model: AIModel):
        self.model = model 

    def ask(self, prompt: str) -> str:
        # Placeholder implementation for generating a response
        return self.model.ask(prompt)

model = FakeModel()  # Replace with your actual AI model implementation
chatbot = AIChatbot(model)

response = chatbot.ask("What is the capital of France?")
print(response)  # Output: This a test response


