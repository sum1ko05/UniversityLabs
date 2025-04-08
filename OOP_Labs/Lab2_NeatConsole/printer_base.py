from enum import Enum
import json

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

    @property
    def pos(self) -> tuple[int, int]:
        return self._pos
    
    @pos.setter
    def pos(self, position: tuple[int, int]):
        if position[0] < 0:
            raise(ValueError)
        if position[1] < 0:
            raise(ValueError)
        self._pos = position

    def __read_font_file(self, font_json_path: str) -> None:
        with open(font_json_path) as json_font:
            items = json.load(json_font)
        if items["metadata"]["version"] == 1.0:
            self._char_size = (items["metadata"]["char_width"], items["metadata"]["char_height"])
        self._chars = items["characters"]

    def __to_font_char(self, char: str) -> list[str]:
        return self._chars[char]
    
    def __prepare_string(self, string: str) -> str: # Preventing key errors
        result = string.upper()
        supported_chars = set(self._chars.keys())
        chars_in_str = set(result)
        removal = chars_in_str - supported_chars
        for char in removal:
            result = result.replace(char, "")
        return result

    def __render_text(self, string: str) -> list[str]:
        result = []
        for i in range(self.pos[1]): # Making vertical offset
            result.append("")
        for i in range(self._char_size[1]): # Constructing strings from top to bottom
            rendered_str = ""
            rendered_str += self.color.value # Applying color to string
            rendered_str += " " * self.pos[0] # Applying horizontal offset
            for char in string:
                rendered_str += self._chars[char][i] + " " # After preparing text it's safe to check by index trust me
            rendered_str += Color.Reset.value # Clean color after finishing writing
            result.append(rendered_str)
        return result
    
    def __out_to_console(self, render: list[str]) -> None:
        for string in render:
            print(string)

    @classmethod
    def cls_print(cls, color: Color, position: tuple[int, int], font_path: str, string: str):
        cls(color, position, font_path).print(string)

    def print(self, string: str):
        adapted_str = self.__prepare_string(string)
        rendered_str = self.__render_text(adapted_str)
        self.__out_to_console(rendered_str)

# p = Printer(color=Color.LightPurple, position=(5, 2), font_path="default.json")
# p.print("You are boykisser")
# print("\033[31mHello\033[0m")
# print(p.chars)