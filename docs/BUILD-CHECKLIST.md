# Build checklist

Use this page as a short path from parts to a working USB controller.

## Before wiring

- [ ] Raspberry Pi Pico or RP2040-compatible board
- [ ] 13 momentary switches and wire
- [ ] Joystick module with 3.3 V-safe outputs
- [ ] EC11 rotary encoder
- [ ] Optional touch breakout and NeoPixel
- [ ] USB cable, multimeter, and a non-conductive test surface

## First power-on

1. Install CircuitPython for your exact board.
2. Copy the libraries named in `firmware/circuitpython/lib/README.md`.
3. Wire only the keys, then copy `code.py` and `config.py`.
4. Confirm the board appears as a USB keyboard before adding optional controls.
5. Add the encoder, joystick, touch input, and LED one at a time.
6. Edit the keymap only after the basic inputs are stable.

## If something goes wrong

- No USB device: press BOOTSEL while reconnecting and reinstall CircuitPython.
- Keys fire by themselves: check the common ground and active-low wiring.
- Joystick drifts: increase the deadzone in `code.py`.
- LED resets the board: lower `BRIGHTNESS` and check the power capacitor.
- Touch is unavailable: leave it disconnected; the firmware treats it as optional.

Never feed 5 V into an RP2040 GPIO. Stop testing if a part becomes hot or the
USB connection repeatedly resets.


