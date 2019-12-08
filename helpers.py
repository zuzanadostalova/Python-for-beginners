# New module
from pip._vendor.colorama import init, Fore

def display(message, is_warning=False):
    if is_warning:
        print(Fore.MAGENTA + message)
    else:
        print(Fore.LIGHTBLUE_EX + message)