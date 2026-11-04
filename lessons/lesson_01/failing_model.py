class FailingModel:
    def __init__(self):
        # Initialize any necessary attributes for the failing model
        self.last_prompt = None

    def ask(self, prompt: str) -> str:
        # Simulate a failure in generating a response
        self.last_prompt = prompt
        raise ConnectionError("AI service unavailable. Please try again later.")