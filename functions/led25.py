import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def triple_blink():
    
    i = 0
    
    while i < 3:
        led.value = True
        time.sleep(0.5)
        led.value = False
        time.sleep(0.5)
        i += 1
