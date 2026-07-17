# Hardware guide

The reference build uses a Raspberry Pi Pico or Pico-compatible RP2040 board.
It is intentionally a hand-wired prototype: a builder can move to a custom
PCB later without changing the USB behavior or configuration format.

## Bill of materials

| Part | Quantity | Notes |
| --- | ---: | --- |
| Raspberry Pi Pico / RP2040 board | 1 | USB device support required |
| Momentary keys or low-profile switches | 13 | Normally open, one side to GPIO |
| 5 V-compatible joystick module | 1 | X and Y analog outputs, optional switch |
| EC11 rotary encoder | 1 | A, B, and push switch |
| Capacitive touch breakout | 1 | Optional; a bare foil pad can be used |
| WS2812B or compatible NeoPixel | 1–14 | Use a resistor and bulk capacitor |
| 1N4148 diodes | optional | Recommended for diode-isolated matrix builds |
| USB cable and enclosure | 1 each | Keep ventilation around the board |

## Reference pinout

The stock firmware uses internal pull-ups for active-low buttons. Connect the
other side of each button to GND. Analog joystick outputs must stay within the
board's ADC voltage range; never feed 5 V into an RP2040 GPIO.

| Function | Pico pin |
| --- | --- |
| Key 1–13 | GP0–GP12 |
| Encoder A / B | GP14 / GP15 |
| Encoder push | GP16 |
| Joystick push | GP17 |
| Joystick X / Y | GP26 / GP27 |
| Touch pad | GP28 |
| NeoPixel data | GP13 |
| Common ground | GND |

If your board or breakout uses different pins, edit `config.py`; do not force a
connector into a pin that is not ADC-capable.

## Power and safety

Keep the first build on USB power. A single NeoPixel can draw up to 60 mA at
full white; limit brightness in software and use a 330–470 ohm data resistor
plus a 470–1000 uF capacitor near the LEDs. Test the joystick and touch module
with a multimeter before connecting them to the Pico. Stop if a component gets
hot, smells unusual, or the USB cable disconnects repeatedly.

The enclosure, plate, key spacing, and icon caps are intentionally left to the
builder. This project is a functional alternative, not a product clone.


