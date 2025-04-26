from typing import Protocol
import re


class LogFilterProtocol(Protocol):
    def match(self, text: str) -> bool:
        ...

class SimpleLogFilter(LogFilterProtocol):
    def __init__(self, pattern: str):
        self.pattern = pattern

    def match(self, text: str) -> bool:
        return self.pattern in text
    
class RegexLogFilter(LogFilterProtocol):
    def __init__(self, pattern: str):
        self.regex = re.compile(pattern)

    def match(self, text: str) -> bool:
        return bool(self.regex.search(text))