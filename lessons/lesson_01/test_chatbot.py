from ai_chatbot import AIChatbot
from fake_model import FakeModel
from failing_model import FailingModel

def test_chatbot_response():
    model = FakeModel()
    chatbot = AIChatbot(model)

    response = chatbot.ask("Hello, how are you?")
    assert response == "This is a test response"

def test_chatbot_passes_correct_prompt():
    model = FakeModel()
    chatbot = AIChatbot(model)

    chatbot.ask("Explain Python inheritance.")
    assert model.last_prompt == "Explain Python inheritance."

def test_chatbot_handles_connection_error():
    model = FailingModel()
    chatbot = AIChatbot(model)

    response =chatbot.ask("Explain Python inheritance.")
    assert response == "Sorry, the AI service is currently unavailable."

def test_chatbot_calls_model_once():
    model = FakeModel()
    chatbot = AIChatbot(model)

    chatbot.ask("What is the capital of France?")
    assert model.call_count == 1




