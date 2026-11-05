from unittest.mock import Mock


import pytest

from ai_model import AIModel 
from fake_model import FakeModel
from failing_model import FailingModel


class AIChatbot:
    def __init__(self, model: AIModel):
        self.model = model
 
    def ask(self, prompt: str) -> str:
        # Placeholder implementation for generating a response
        prompt = prompt.strip()
        if not prompt:
            raise ValueError("Prompt cannot be empty.")
  
        try:
            response = self.model.ask(prompt)
        except ConnectionError:
            return "Sorry, the AI service is currently unavailable."
        else:
            print(response)
            return response




