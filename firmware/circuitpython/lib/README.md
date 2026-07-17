# CircuitPython libraries

Download the library bundle matching the CircuitPython version on your board
from the official CircuitPython downloads page, then copy these folders into
the board's `CIRCUITPY/lib/` directory:

- `adafruit_hid`
- `neopixel.mpy` (or the matching `neopixel.py` module)

`analogio`, `digitalio`, `keypad`, `rotaryio`, `time`, and `usb_hid` are
provided by CircuitPython itself on supported boards. The touch input is
optional; the firmware continues to run if the board lacks `touchio` support.


