"""User-editable profile for Open Codex Micro.

Shortcut values use CircuitPython's adafruit_hid Keycode names. A key action is
one key or a tuple representing a chord. Keep this file simple so profiles can
be shared without changing firmware logic.
"""

import board
from adafruit_hid.keycode import Keycode

KEY_PINS = tuple(getattr(board, f"GP{i}") for i in range(13))
ENCODER_A = board.GP14
ENCODER_B = board.GP15
ENCODER_SWITCH = board.GP16
JOYSTICK_SWITCH = board.GP17
JOYSTICK_X = board.GP26
JOYSTICK_Y = board.GP27
TOUCH_PIN = board.GP28
PIXEL_PIN = board.GP13
PIXEL_COUNT = 1

# Replace these with the shortcuts used by your terminal or editor.
KEYMAP = (
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.C),
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.ENTER),
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.P),
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.A),
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.R),
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.T),
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.W),
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.L),
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.S),
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.B),
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.F),
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.G),
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.H),
)

ENCODER_STEP = (Keycode.CONTROL, Keycode.ALT, Keycode.RIGHT)
ENCODER_BACK = (Keycode.CONTROL, Keycode.ALT, Keycode.LEFT)
ENCODER_PRESS = (Keycode.CONTROL, Keycode.ALT, Keycode.ENTER)
JOYSTICK_PRESS = (Keycode.CONTROL, Keycode.ALT, Keycode.SPACE)

PIXEL_IDLE = (16, 8, 24)
PIXEL_ACTIVE = (50, 180, 120)
PIXEL_ERROR = (180, 32, 24)
BRIGHTNESS = 0.18


