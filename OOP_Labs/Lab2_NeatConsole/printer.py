from typing import Protocol, Optional
from enum import Enum
import json

class Color(Enum):
    DarkBlack = "\e[0;30m"
    DarkRed = "\e[0;31m"
    DarkGreen = "\e[0;32m"
    DarkYellow = "\e[0;33m"
    DarkBlue = "\e[0;34m"
    DarkPurple = "\e[0;35m"
    DarkCyan = "\e[0;36m"
    DarkWhite = "\e[0;37m"

    LightBlack = "\e[0;90m"
    LightRed = "\e[0;91m"
    LightGreen = "\e[0;92m"
    LightYellow = "\e[0;93m"
    LightBlue = "\e[0;94m"
    LightPurple = "\e[0;95m"
    LightCyan = "\e[0;96m"
    LightWhite = "\e[0;97m"

    Reset = "\e[0m"

# Python specific, implemented through protocols
class FontReaderProtocol(Protocol):
    pass