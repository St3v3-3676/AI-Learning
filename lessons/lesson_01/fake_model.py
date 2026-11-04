class FakeModel:
    def __init__(self):
        # Initialize any necessary attributes for the fake model
        self.last_prompt = None
        self.call_count = 0
    def ask(self, prompt: str) -> str:
        # Placeholder implementation for generating a response
        self.last_prompt = prompt
        self.call_count += 1
        return "This is a test response"
    