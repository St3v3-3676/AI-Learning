from unittest.mock import Mock
from ai_chatbot import AIChatbot

model = Mock()
model.ask.return_value = "This is a test response"  # Replace with your actual AI model implementation
chatbot = AIChatbot(model)

response = chatbot.ask("Hello")
print(response)  # Output: This is a test response q