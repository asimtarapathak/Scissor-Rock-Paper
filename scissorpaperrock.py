import random,time
from colorama import Fore, Back, Style
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

hand = {0: "\U0000270C  Scissor ",1: "\U0000270A  Rock ",2: "\U0001F590  Paper "}

emoji_lst = {0: "\U0000270C  Scissor...  ",1: "\U0000270A Rock...   ",2: "\U0001F590 Paper...  "}

sound = {0: "Scissor",1: "Rock",2: "Paper"}

def ready():
    for key in range(0,3):
        print(Back.BLUE+Fore.WHITE+"\r Ready : "+Style.RESET_ALL+" "+Back.GREEN+emoji_lst[key]+Style.RESET_ALL, end="")
        speak.Speak(sound[key])
        time.sleep(1)

def show_hand():
    showing = random.randint(0,2)
    print("\n\n"+Back.RED+hand[showing]+Style.RESET_ALL)



ready()
show_hand()