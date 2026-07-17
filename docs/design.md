# Design notes

## Why USB HID first

USB HID gives the project a useful baseline: the board works with a locked-down
computer, a terminal, a browser, or an editor without a vendor daemon. A local
serial channel remains available for builders who want richer status or a
window-manager integration.

## Why profiles live in one small file

Agent products change quickly, but a physical layout should not need to change
with every software release. The firmware owns input scanning and safety; the
profile owns the vocabulary. This also makes it easy to publish a layout for a
different editor without forking the firmware.

## Future hardware directions

- a diode-isolated switch matrix for a smaller pin count
- a detachable USB-C daughterboard
- a per-key RGB PCB with current limiting
- an optional e-paper status strip
- a 3D-printable low-profile case and a laser-cut plate

The project should remain usable when every optional feature is removed.


