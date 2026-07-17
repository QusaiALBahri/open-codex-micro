# Open Codex Micro

### Your coding workflow, within reach.

<p align="center">
  <img src="docs/assets/open-codex-micro.svg" alt="Illustrated Open Codex Micro macro pad with keys, encoder, joystick, and status light" width="900">
</p>

<p align="center"><strong>13 keys · joystick · encoder · touch · USB HID · no cloud</strong></p>

<p align="center">
  <a href="#quick-start-six-steps">Build it</a> ·
  <a href="hardware/README.md">See the wiring</a> ·
  <a href="firmware/circuitpython/code.py">Read the firmware</a> ·
  <a href="https://github.com/QusaiALBahri/open-codex-micro/issues/new/choose">Share an idea</a>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-7c3aed.svg)](LICENSE)
[![Hardware: RP2040](https://img.shields.io/badge/Hardware-RP2040-2563eb.svg)](hardware/README.md)
[![Firmware: CircuitPython](https://img.shields.io/badge/Firmware-CircuitPython-059669.svg)](firmware/circuitpython/README.md)
[![Status: prototype](https://img.shields.io/badge/Status-prototype-f59e0b.svg)](docs/BUILD-CHECKLIST.md)

Open Codex Micro is a compact, repairable macro pad for agentic coding
workflows. Give repeated actions a physical place: start a task, pause it,
approve a change, move between sessions, show a diff, or return focus to the
terminal.

It is a weekend-buildable alternative for people who want the feeling of a
dedicated coding control surface without a closed device, vendor daemon, or
subscription.

This is an independent open-source project. It is not made by, endorsed by, or
affiliated with OpenAI or Work Louder. “Codex” is used here to describe a
workflow and the project does not reproduce proprietary firmware, software, or
industrial design.

## Choose your path

| I want to… | Start here |
| --- | --- |
| Build one this weekend | [`hardware/README.md`](hardware/README.md) |
| Flash the reference firmware | [`firmware/circuitpython/README.md`](firmware/circuitpython/README.md) |
| Change the shortcuts | [`firmware/circuitpython/config.py`](firmware/circuitpython/config.py) |
| Pick a layout | [`docs/PROFILES.md`](docs/PROFILES.md) |
| Understand the design | [`docs/design.md`](docs/design.md) |
| Report a problem | [Open an issue](https://github.com/QusaiALBahri/open-codex-micro/issues/new/choose) |

## What you build

- 13 hot-swappable or soldered macro keys
- A two-axis joystick for navigation and a press action
- A rotary encoder with push switch
- A capacitive touch input for a second layer
- Per-key or strip RGB status lighting
- USB HID output, so it works without a special driver
- A plain-text configuration that can be edited without recompiling
- Optional serial events for a desktop companion or your own integration

## At a glance

| Small enough for a corner of your desk | Open enough to repair | Flexible enough to keep |
| --- | --- | --- |
| RP2040 + USB-C power | Through-hole or hand-wired prototype | Shortcuts live in one editable file |
| 13 direct GPIO buttons | No account or telemetry | Works with terminals, editors, and browsers |
| One bright status pixel | Common, replaceable parts | Add your own layout profiles |

The reference firmware targets a Raspberry Pi Pico or another RP2040 board
running CircuitPython. The design is deliberately simple enough to adapt to an
Arduino-compatible board, a Pi Zero running Linux, or a custom PCB.

## Quick start: six steps

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

The default layout uses ordinary keyboard shortcuts rather than a private API.
That keeps the pad useful with a terminal, editor, browser, or Codex client.
The complete first-build checklist is in [`docs/BUILD-CHECKLIST.md`](docs/BUILD-CHECKLIST.md).

## A useful first layout

The reference profile gives each key a job without pretending that every
software client has the same commands:

```text
[ new task ] [ send ] [ pause ] [ approve ] [ reject ]
[ retry    ] [ stop ] [ next ] [ previous ] [ show diff ]
[ terminal ] [ focus ] [ help ]   ◉ encoder   ◎ joystick
```

Treat these as labels, not fixed product behavior. Map them to shortcuts that
already exist in your own tools.

## Repository map

| Path | Purpose |
| --- | --- |
| `firmware/circuitpython/` | Ready-to-copy RP2040 firmware |
| `hardware/` | Wiring, bill of materials, and enclosure notes |
| `host/` | Optional serial companion utilities |
| `docs/` | Design decisions and extension points |
| `examples/` | Starter profiles for different workflows |
| `.github/` | Issue forms that make bug reports easier to reproduce |

## Responsible project notes

This repository is authored by **Qusai Al Bahri** with help from AI tools for
brainstorming, drafting, and review. Human testing, hardware safety checks, and
the final choice of shortcuts remain the builder's responsibility.

Project home and author: [albahri.org](https://albahri.org)

The aim is practical openness: readable code, ordinary components, no account,
no telemetry, and no claim that a DIY build is an exact copy of a commercial
device. Build one, improve it, and share your layout.

## Current limits

This is a reference prototype, not a finished consumer product. The firmware
has been syntax-checked but needs physical testing on the builder's exact board,
switches, joystick, encoder, and CircuitPython version. The default shortcuts
are intentionally generic and should be reviewed before mapping any destructive
action.

## Roadmap

- [x] RP2040/CircuitPython reference firmware
- [x] Hardware pinout and first-build checklist
- [x] Safer joystick calibration and repeat handling
- [ ] Printable case and switch plate
- [ ] Per-key RGB expansion
- [ ] Community layout gallery

## License

Code and documentation are released under the MIT License. Hardware files are
released under CERN-OHL-S-2.0 where applicable; see `LICENSE` and
`hardware/README.md` for the boundary between software and hardware material.

## Search terms

open-source macro pad, Raspberry Pi Pico macro pad, RP2040 keyboard, CircuitPython
HID, agent workflow controller, coding assistant keyboard, programmable keypad,
open Codex Micro alternative, DIY developer tool, Qusai Al Bahri, albahri.org

