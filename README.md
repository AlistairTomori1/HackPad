# My HackPad

My HackPad is a 6-key (2x3) macropad built around the Seeed XIAO RP2040. It includes 2 EC11 rotary encoders (one for volume, one for timeline scrubbing) and a 0.91 inch 128x32 I2C OLED display (SSD1306) for status and layer info.

## Features
- 6x MX-style keys (2 columns x 3 rows matrix)
- 2x EC11 rotary encoder 1 for Volume, the other is for moving through video timeline
- 0.91 inch 128x32 I2C OLED (pin order: GND-VCC-SCL-SDA)
- KMK (CircuitPython) firmware with layers
- 3D-printed case designed to fit the PCB, OLED, and encoder cleanly

## Photos

## Schematic
<img src="assets/schematic.png" alt="Schematic" width="600"/>

Notes:
- Keys are wired as a 2x3 matrix with 1N4148 diodes to prevent ghosting.
- OLED uses I2C (SDA/SCL) and is powered from VBUS (5V).
- There are two encoders; each uses two GPIO pins plus a shared GND common (4 GPIO total).

## PCB
<img src="assets/pcb.png" alt="PCB" width="600"/>

Notes:
- Switches are laid out on standard MX spacing.
- Diodes are placed close to their switches for clean routing.
- XIAO is positioned so the USB port is accessible at the board edge.
- Silkscreen includes the project name plus a "XIAO HERE" orientation label.

## Case and CAD
<img src="assets/case.png" alt="Case CAD" width="600"/>
<img src="assets/case_empty.png" alt="Case Empty CAD" width="600"/>

How it fits together:
- Top plate holds switches and keycaps.
- Middle cavity supports the PCB and provides clearance for solder joints.
- OLED sits above the key cluster.
- Encoder is mounted at the top-right with knob clearance.
- Bottom closes the case and provides mounting points.

(Designed for 3D printing.)

## Firmware Overview (KMK / CircuitPython)
This project uses KMK firmware (Python) for fast iteration.

Default behavior:
- Layer 0:
  - Keys: common editing macros (copy/paste/undo/redo, etc.)
  - Encoder 1: volume up/down
  - Encoder 2: timeline scrub (left/right)
- Layer 1:
  - Keys: media controls
  - Encoder 1: previous/next track
  - Encoder 2: fine scrub (Shift + left/right)

Firmware file:
- `firmware/main.py`

## BOM (Bill of Materials)
Everything needed to build this hackpad:

Electronics:
- 1x Seeed XIAO RP2040
- 6x MX-style switches
- 6x 1N4148 diodes (DO-35, through-hole)
- 2x EC11 rotary encoders
- 1x 0.91 inch 128x32 I2C OLED display (SSD1306, pin order: GND-VCC-SCL-SDA)
- 1x 1x4 2.54mm pin header (for the OLED)
- 1x PCB board

Hardware and Case:
- 6x Blank DSA keycaps (White)
- 3D-printed case (top and bottom, or top/middle/bottom depending on your design)
- 4x M3x16mm screws
- 4x M3 heatset inserts (5x4mm)

