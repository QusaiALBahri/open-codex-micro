# Open Codex Micro

An open, repairable control surface for agentic coding workflows.

Open Codex Micro is a compact macro pad that turns the actions you repeat while
working with coding agents into physical controls: launch a task, pause it,
approve a change, move between sessions, or return focus to the terminal. It is
designed to be built from readily available parts rather than purchased as a
closed accessory.

This is an independent open-source project. It is not made by, endorsed by, or
affiliated with OpenAI or Work Louder. “Codex” is used here to describe a
workflow and the project does not reproduce proprietary firmware, software, or
industrial design.

## What you build

- 13 hot-swappable or soldered macro keys
- A two-axis joystick for navigation and a press action
- A rotary encoder with push switch
- A capacitive touch input for a second layer
- Per-key or strip RGB status lighting
- USB HID output, so it works without a special driver
- A plain-text configuration that can be edited without recompiling
- Optional serial events for a desktop companion or your own integration

The reference firmware targets a Raspberry Pi Pico or another RP2040 board
running CircuitPython. The design is deliberately simple enough to adapt to an
Arduino-compatible board, a Pi Zero running Linux, or a custom PCB.

## Quick start

1. Gather the parts listed in [`hardware/README.md`](hardware/README.md).
2. Install CircuitPython on a Raspberry Pi Pico and copy the libraries in the
   CircuitPython bundle: `adafruit_hid`, `neopixel`, and the built-in modules
   used by the firmware.
3. Copy `firmware/circuitpython/code.py` and `config.py` to the board's `CIRCUITPY`
   drive.
4. Wire the controls according to the pin table in the hardware guide.
5. Edit `config.py` to change shortcuts and LED colors.
6. Plug the board into USB. It appears as a normal keyboard and works with your
   terminal, editor, browser, or Codex client.

The default layout intentionally uses familiar keyboard shortcuts instead of
depending on a private API. This makes the device useful with any agent
interface that supports configurable shortcuts.

## Repository map

| Path | Purpose |
| --- | --- |
| `firmware/circuitpython/` | Ready-to-copy RP2040 firmware |
| `hardware/` | Wiring, bill of materials, and enclosure notes |
| `host/` | Optional serial companion utilities |
| `docs/` | Design decisions and extension points |
| `examples/` | Starter profiles for different workflows |

## Responsible project notes

This repository is authored by **Qusai Al Bahri** with help from AI tools for
brainstorming, drafting, and review. Human testing, hardware safety checks, and
the final choice of shortcuts remain the builder's responsibility.

Project home and author: [albahri.org](https://albahri.org)

The aim is practical openness: readable code, ordinary components, no account,
no telemetry, and no claim that a DIY build is an exact copy of a commercial
device. Build one, improve it, and share your layout.

## License

Code and documentation are released under the MIT License. Hardware files are
released under CERN-OHL-S-2.0 where applicable; see `LICENSE` and
`hardware/README.md` for the boundary between software and hardware material.

## Search terms

open-source macro pad, Raspberry Pi Pico macro pad, RP2040 keyboard, CircuitPython
HID, agent workflow controller, coding assistant keyboard, programmable keypad,
open Codex Micro alternative, DIY developer tool, Qusai Al Bahri, albahri.org


