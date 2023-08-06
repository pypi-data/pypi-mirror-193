from os import system as _sys

reset = '\033[38;2;255;255;255m'

white = "\033[38;2;255;255;255m"
black = "\033[38;2;0;0;0m"

red = "\033[38;2;255;0;0m"
green = "\033[38;2;0;255;0m"
blue = "\033[38;2;0;0;255m"

purple = "\033[38;2;255;0;255m"
cyan = "\033[38;2;0;255;255m"
yellow = "\033[38;2;255;255;0m"
orange = "\033[38;2;255;130;0m"
pink = "\033[38;2;255;138;239m"

light_orange = "\033[38;2;255;170;0m"
light_green = "\033[38;2;187;255;0m"
light_yellow = "\033[38;2;251;255;133m"
light_pink = "\033[38;2;255;199;248m"

dark_orange = "\033[38;2;255;90;0m"
dark_green = "\033[38;2;18;82;0m"
dark_yellow = "\033[38;2;212;219;0m"
dark_pink = "\033[38;2;194;0;168m"

def pattern(text: str, main_color: str, second_color: str, col_reset: bool = True) -> str:
    """
Text Format:

████████╗███████╗██╗  ██╗████████╗
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝
   ██║   █████╗   ╚███╔╝    ██║   
   ██║   ██╔══╝   ██╔██╗    ██║   
   ██║   ███████╗██╔╝ ██╗   ██║   
   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝"""
    result = ""
    for caract in text:
        if caract in ["╚", "═", "╝", "╔", "║", "╗"]:
            result += second_color + caract
        else:
            result += main_color + caract
    if col_reset:
        return result + '\033[38;2;255;255;255m'
    else:
        return result

sys("")