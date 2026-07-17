# Contributing

Small, testable improvements are welcome. Before opening an issue or pull
request, please describe the board, operating system, CircuitPython version,
and wiring used. A photograph or serial log is often more useful than a long
description.

Good first contributions include new layout profiles, enclosure adaptations,
documentation fixes, and tests for the host utilities. Do not include secrets,
machine-specific paths, or copied proprietary firmware.

For firmware changes, run a Python syntax check on the host-side modules and
manually verify that a disconnected or unpopulated optional control does not
make the whole pad unusable. Hardware changes should include an updated pin
table and a note about current draw.


