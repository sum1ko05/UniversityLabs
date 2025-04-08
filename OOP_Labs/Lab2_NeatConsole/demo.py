from printer_base import Printer, Color

common_font_path = "default.json"
Printer.cls_print(color=Color.LightRed, 
                  position=(5, 5), 
                  font_path=common_font_path,
                  string="Simple demo")

script = str("Hi my name is Reggie").split(" ")
pallete = [Color.DarkYellow, 
           Color.LightYellow,
           Color.LightGreen,
           Color.LightBlue,
           Color.DarkPurple]
printer = Printer(color=pallete[0], position=(0, 0), font_path=common_font_path)
for i in range(len(script)):
    offset = i * 7
    current_color = pallete[i % len(pallete)]
    printer.color = current_color
    printer.pos = (offset, 1)
    printer.print(script[i])