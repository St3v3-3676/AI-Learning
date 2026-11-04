from typing import Protocol

class AIModel(Protocol):
    def ask(self, prompt: str) -> str:
        ...
