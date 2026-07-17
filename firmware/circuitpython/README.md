# CircuitPython firmware

Copy `code.py` and `config.py` to the root of the board's `CIRCUITPY` drive.
Install `adafruit_hid` and `neopixel` from the matching CircuitPython library
bundle in `lib/`.

The firmware deliberately has no network access and stores no credentials. It
emits ordinary USB keyboard events. Edit `config.py` to match the shortcuts of
your preferred Codex client, editor, terminal, or window manager.

The analogue joystick is treated as a four-way navigation input with a generous
deadzone. If you want pointer movement instead, replace the two `tap` calls in
the joystick section with `adafruit_hid.mouse.Mouse` events.


