import usb_hid
from time import sleep
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_es import KeyboardLayout
from keycode_win_es import Keycode
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

def pulse_keys(combo, w_time):
    print(f"going to write {combo}")
    sleep(w_time)
    layout.write(combo)

def open_shell():
    print("opening shell...")
    kbd.send(Keycode.LEFT_ALT, Keycode.T)
    kbd.release_all()
    kbd.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.T)
    kbd.release_all()
def enter():
    kbd.send(Keycode.ENTER)
    kbd.release_all()