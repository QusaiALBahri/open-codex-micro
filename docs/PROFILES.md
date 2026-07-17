# Profiles

Profiles are small agreements between your hands and your software. The
firmware does not need to know which editor or agent client is open; it only
sends the shortcuts you choose.

## Editor-friendly

Use keys for new task, send, pause, approve, reject, retry, stop, next agent,
previous agent, show diff, terminal, focus chat, and help. Start with
[`examples/profile-editor.json`](../examples/profile-editor.json), then map the
labels in [`config.py`](../firmware/circuitpython/config.py).

## Safe defaults

- Prefer reversible actions on a single press.
- Put destructive actions behind a chord or a second layer.
- Keep one key for help and one for returning focus to the terminal.
- Test the layout in a text editor before using it in a real repository.

Share new profiles as JSON plus a short note describing the target software and
operating system. That makes layouts discoverable without making the firmware
client-specific.


