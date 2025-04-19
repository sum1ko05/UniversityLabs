from printer_base import Printer, Color


common_font_path = "default.json"
Printer.cls_print(color=Color.LightRed, 
                  position=(5, 5), 
                  font_path=common_font_path,
                  string="Simple demo")

script = str("OwO what is this").split(" ")
palette = [Color.LightYellow,
           Color.LightGreen,
           Color.LightBlue,
           Color.DarkPurple]
printer = Printer(color=palette[0], position=(0, 0), font_path=common_font_path)
for i in range(len(script)):
    offset = i * 7
    current_color = palette[i % len(palette)]
    printer.color = current_color
    printer.pos = (offset, 1)
    printer.print(script[i])
with Printer(color=Color.LightCyan, position=(5, 1), font_path=common_font_path) as with_printer:
    with_printer.print("notices")
    with_printer.print("ur code")
