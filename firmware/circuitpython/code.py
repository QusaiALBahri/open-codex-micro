"""Open Codex Micro reference firmware for CircuitPython on RP2040."""

import analogio
import digitalio
import keypad
import neopixel
import rotaryio
import time
import usb_hid

from adafruit_hid.keyboard import Keyboard

import config

try:
    import touchio
except ImportError:
    touchio = None


keyboard = Keyboard(usb_hid.devices)
keys = keypad.Keys(config.KEY_PINS, value_when_pressed=False, pull=True)
encoder = rotaryio.IncrementalEncoder(config.ENCODER_A, config.ENCODER_B)
encoder_switch = digitalio.DigitalInOut(config.ENCODER_SWITCH)
encoder_switch.direction = digitalio.Direction.INPUT
encoder_switch.pull = digitalio.Pull.UP
joystick_switch = digitalio.DigitalInOut(config.JOYSTICK_SWITCH)
joystick_switch.direction = digitalio.Direction.INPUT
joystick_switch.pull = digitalio.Pull.UP
joystick_x = analogio.AnalogIn(config.JOYSTICK_X)
joystick_y = analogio.AnalogIn(config.JOYSTICK_Y)
try:
    touch = touchio.TouchIn(config.TOUCH_PIN) if touchio else None
except (RuntimeError, ValueError):
    # Some boards expose touchio but do not support capacitive touch on GP28.
    touch = None
pixels = neopixel.NeoPixel(config.PIXEL_PIN, config.PIXEL_COUNT, brightness=config.BRIGHTNESS, auto_write=True)
pixels.fill(config.PIXEL_IDLE)


def tap(action):
    """Press a key or chord and release it reliably."""
    if isinstance(action, tuple):
        keyboard.press(*action)
        keyboard.release_all()
    else:
        keyboard.press(action)
        keyboard.release(action)


def edge(previous, current):
    return previous and not current


last_encoder = encoder.position
last_encoder_switch = True
last_joystick_switch = True
last_touch = False
last_report = time.monotonic()
last_joystick_action = 0.0
joystick_center_x = joystick_x.value
joystick_center_y = joystick_y.value

while True:
    event = keys.events.get()
    if event and event.pressed and event.key_number < len(config.KEYMAP):
        tap(config.KEYMAP[event.key_number])
        pixels.fill(config.PIXEL_ACTIVE)

    position = encoder.position
    while position > last_encoder:
        tap(config.ENCODER_STEP)
        last_encoder += 1
    while position < last_encoder:
        tap(config.ENCODER_BACK)
        last_encoder -= 1

    encoder_state = encoder_switch.value
    if edge(last_encoder_switch, encoder_state):
        tap(config.ENCODER_PRESS)
    last_encoder_switch = encoder_state

    joystick_state = joystick_switch.value
    if edge(last_joystick_switch, joystick_state):
        tap(config.JOYSTICK_PRESS)
    last_joystick_switch = joystick_state

    # Joystick movement becomes cursor-like arrows only after leaving the
    # deadzone. This keeps a resting analogue stick quiet.
    now = time.monotonic()
    x = joystick_x.value
    y = joystick_y.value
    if now - last_joystick_action >= config.JOYSTICK_REPEAT_SECONDS:
        if abs(x - joystick_center_x) > config.JOYSTICK_DEADZONE:
            tap(config.JOYSTICK_RIGHT if x > joystick_center_x else config.JOYSTICK_LEFT)
            last_joystick_action = now
        elif abs(y - joystick_center_y) > config.JOYSTICK_DEADZONE:
            tap(config.JOYSTICK_DOWN if y > joystick_center_y else config.JOYSTICK_UP)
            last_joystick_action = now
    touch_state = touch.value if touch else False
    if touch_state and not last_touch:
        pixels.fill(config.PIXEL_ACTIVE)
    last_touch = touch_state

    if time.monotonic() - last_report > 0.6:
        pixels.fill(config.PIXEL_IDLE if not touch_state else config.PIXEL_ACTIVE)
        last_report = time.monotonic()

    time.sleep(0.004)

