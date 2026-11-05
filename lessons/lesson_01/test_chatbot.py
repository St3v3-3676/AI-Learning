import pytest

from ai_chatbot import AIChatbot
from fake_model import FakeModel
from failing_model import FailingModel
from mock_model import Mock

@pytest.fixture
def chatbot():
    model = FakeModel()
    return AIChatbot(model)

def test_chatbot_response(chatbot):
    response = chatbot.ask("Hello, how are you?")
    assert response == "This is a test response"

def test_chatbot_passes_correct_prompt(chatbot):
    chatbot.ask("Explain Python inheritance.")
    assert chatbot.model.last_prompt == "Explain Python inheritance."

def test_chatbot_handles_connection_error(chatbot):
    response = chatbot.ask("Explain Python inheritance.")
    assert response == "Sorry, the AI service is currently unavailable."

def test_chatbot_calls_model_once(chatbot):
    chatbot.ask("What is the capital of France?")
    assert chatbot.model.call_count == 1

def test_chatbot_rejects_empty_prompt(chatbot):
    with pytest.raises(ValueError):
        chatbot.ask("")

    assert chatbot.model.call_count == 0  # Ensure the model's ask method was not called

def test_chatbot_strips_whitespace(chatbot):
    chatbot.ask("   Explain Python   ")
    assert chatbot.model.last_prompt == "Explain Python"


def test_unexpected_error():
    model = Mock()
    model.ask.side_effect = ValueError("Invalid Model")

    chatbot = AIChatbot(model)

    with pytest.raises(ValueError):
        chatbot.ask("Hello")

    model.ask.assert_called_once_with("Hello") 
    
    
def test_connection_error():
    model = Mock()

    model.ask.side_effect = ConnectionError(
        "Service unavailable"
    )

    chatbot = AIChatbot(model)

    response = chatbot.ask("Hello")

    assert response == (
        "Sorry, the AI service is currently unavailable."
    )

    model.ask.assert_called_once_with("Hello")




