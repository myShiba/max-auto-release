import time
from ocr import getTXT
import pydirectinput
from pynput import keyboard
import time
import pygetwindow as gw

win = gw.getWindowsWithTitle('Roblox')[0]

pydirectinput.moveTo(1241, 995, duration=.1)

break_program = False
def on_press(key):
    global break_program
    if key == keyboard.Key.end:
        break_program = True
    if key == keyboard.Key.home:
        win.activate()
        break_program = False

def main():
    global break_program
    print("Press END to pause program  ||  Press HOME to resume program")
    input("Press Enter to continue...")
    win.activate()
    pydirectinput.moveTo(1241, 995, duration=.1)
    pydirectinput.click(button='left', clicks=1, interval=.1)
    time.sleep(1)
    with keyboard.Listener(on_press=on_press) as listener:
        while True:
            time.sleep(.005)
            if(break_program==False):
                if(getTXT()):
                    pydirectinput.moveTo(1241, 995, duration=.1)
                    pydirectinput.click(button='left', clicks=1, interval=.1)
                else:
                    break_program=True

if __name__ == "__main__":
    main()