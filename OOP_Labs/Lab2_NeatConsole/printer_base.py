from enum import Enum
import json
import os


class Color(Enum):
    DarkBlack = "\033[0;30m"
    DarkRed = "\033[0;31m"
    DarkGreen = "\033[0;32m"
    DarkYellow = "\033[0;33m"
    DarkBlue = "\033[0;34m"
    DarkPurple = "\033[0;35m"
    DarkCyan = "\033[0;36m"
    DarkWhite = "\033[0;37m"

    LightBlack = "\033[0;90m"
    LightRed = "\033[0;91m"
    LightGreen = "\033[0;92m"
    LightYellow = "\033[0;93m"
    LightBlue = "\033[0;94m"
    LightPurple = "\033[0;95m"
    LightCyan = "\033[0;96m"
    LightWhite = "\033[0;97m"

    Reset = "\033[0m"


class Printer:
    def __init__(self, color: Color, position: tuple[int, int], font_path: str):
        self.color = color
        self.pos = position
        self.__read_font_file(font_path)

    # region properties
    @property
    def color(self) -> Color:
        return self._color
    
    @color.setter
    def color(self, color: Color):
        self._color = color
    
    @property
    def pos(self) -> tuple[int, int]:
        return self._pos
    
    @pos.setter
    def pos(self, position: tuple[int, int]):
        if position[0] < 0:
            raise ValueError("Position is out of valid range")
        if position[1] < 0:
            raise ValueError("Position is out of valid range")
        self._pos = position
    # endregion

    # region context_managing
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        pass
    # endregion

    # region low_level
    def __read_font_file(self, font_json_path: str) -> None:  # It's possible to make it public to change font in middle of object lifetime
        try:
            with open(font_json_path) as json_font:
                items = json.load(json_font)
        except FileNotFoundError:
            raise FileNotFoundError(f"File \"{font_json_path}\" not found in \"{os.getcwd()}\"")
        if items["metadata"]["version"] == 1.0:
            self._char_size = (items["metadata"]["char_width"], items["metadata"]["char_height"])
        self._chars = items["characters"]
 
    def __prepare_string(self, string: str) -> str:  # Preventing key errors
        result = string.upper()
        supported_chars = set(self._chars.keys())
        chars_in_str = set(result)
        removal = chars_in_str - supported_chars
        for char in removal:
            result = result.replace(char, "")
        return result

    def __render_text(self, string: str) -> list[str]:
        result = []
        for i in range(self.pos[1]):  # Making vertical offset
            result.append("")
        for i in range(self._char_size[1]):  # Constructing strings from top to bottom
            rendered_str = ""
            rendered_str += self.color.value  # Applying color to string
            rendered_str += " " * self.pos[0]  # Applying horizontal offset
            for char in string:
                rendered_str += self._chars[char][i] + " "  # After preparing text it's safe to check by index trust me
            rendered_str += Color.Reset.value  # Clean color after finishing writing
            result.append(rendered_str)
        return result

    @staticmethod
    def __out_to_console(render: list[str]) -> None:
        for string in render:
            print(string)
    # endregion

    @classmethod
    def cls_print(cls, color: Color, position: tuple[int, int], font_path: str, string: str):
        cls(color, position, font_path).print(string)

    def print(self, string: str):
        adapted_str = self.__prepare_string(string)
        rendered_str = self.__render_text(adapted_str)
        self.__out_to_console(rendered_str)
