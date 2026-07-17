# Open Codex Micro — Español

[English](README.md) · [العربية](README.ar.md) · [简体中文](README.zh-CN.md) · **Español**

### Tu flujo de programación, al alcance de la mano.

Open Codex Micro es un macropad pequeño, reparable y de código abierto para
flujos de trabajo con agentes de programación. Convierte acciones repetitivas
en controles físicos: iniciar una tarea, pausarla, aprobar cambios, cambiar de
sesión, ver diferencias o volver rápidamente al terminal.

![Ilustración de Open Codex Micro](docs/assets/open-codex-micro.svg)

## Qué incluye

- 13 teclas programables
- Joystick de dos ejes con pulsación
- Encoder rotatorio con pulsación
- Entrada táctil opcional
- Luz de estado RGB
- Salida USB HID, sin controlador especial
- Firmware CircuitPython para Raspberry Pi Pico / RP2040

## Primeros pasos

1. Consulta la [lista de materiales y el cableado](hardware/README.md).
2. Sigue la [lista de construcción](docs/BUILD-CHECKLIST.md).
3. Copia el [firmware](firmware/circuitpython/README.md) a `CIRCUITPY`.
4. Personaliza los atajos en [`config.py`](firmware/circuitpython/config.py).

> Empieza conectando solo las teclas. Añade el joystick, el encoder, el tacto y
> la luz uno por uno. No conectes 5 V a ningún GPIO del RP2040.

Este es un proyecto independiente y no está afiliado a OpenAI ni Work Louder.
Creado por **Qusai Al Bahri**, con ayuda de herramientas de IA para ideación y
revisión.

Sitio del autor: [albahri.org](https://albahri.org)


