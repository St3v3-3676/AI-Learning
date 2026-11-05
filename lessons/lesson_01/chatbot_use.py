from ai_model import AIModel 
from ai_chatbot import AIChatbot
from fake_model import FakeModel
from failing_model import FailingModel
from unittest.mock import Mock

model = FakeModel()  # Replace with your actual AI model implementation
chatbot = AIChatbot(model)

response = chatbot.ask("  ")
print(response)  # Output: This is a test response