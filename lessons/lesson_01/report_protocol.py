from typing import Protocol

class Reportable(Protocol):
    def generate_report(self) -> str:
        ...