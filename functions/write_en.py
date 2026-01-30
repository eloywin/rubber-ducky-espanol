from time import sleep
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

def pulse_keys(combo, w_time):
    print(f"going to write {combo}")
    sleep(w_time)
    layout.write(combo)

def open_shell():
    kbd.press(Keycode.LEFT_ALT, Keycode.T)
    kbd.release_all()
    kbd.press(Keycode.LEFT_CTRL, Keycode.LEFT_ALT, Keycode.T)
    kbd.release_all()