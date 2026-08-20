# Terminator Eyes
Terminator eyes LED fade-in, blink and fade-out animation project with a raspberry pi pico, a 1N4148 diode, a 0.5F 5.5V supercapacitor, 22AWG silicone soldered wiring and powered by a 6V 4xAA battery holder with a SPST rocket switch.

The pico drives two 3mm LED using PWM to create smooth brightness transitions, blinks and fade-outs. The 1N4148 diode feeds power from the switch output into VSYS while preventing reverse current flow and the 0.5F supercapacitor provides short power after switch-off to allow the pico to run the fade-out animation before losing full power.

![Raspberry Pi](https://img.shields.io/badge/-Raspberry_Pi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

## BOM:
| Part                     | Use                                                                 |
|--------------------------|---------------------------------------------------------------------|
| Raspberry Pi Pico        | Microcontroller to run LED program and read switch input            |
| 4x AA Battery Pack       | 6V power for main system                                            |
| KCD11 Rocker Switch      | Toggles power to the system and signals start / stop to the pico    |
| 1N4148 diode             | Allows power to VSYS but blocks reverse flow back to the switch     |
| Supercap (0.5F, 5.5V)    | Keeps the Pico powered after switch-off to run fade-out             |
| 100kΩ Resistor           | Pull-down so GP16 reads LOW when the switch is off                  |
| 2x 3mm RED LEDs          | Eyes inspired by terminator                                         |
| 2x 220Ω Resistors        | Limits current to each LED so they don't burn out                   |
| Jumper / silicon wire    | Connects all components together                                    |

---
## Firmware:

**See code:** [link](https://raw.githubusercontent.com/gethin101/terminator-eyes/refs/heads/main/main.py)

The project is fully programmed in MicroPython via Thonny. The code uses pulse width modulation to create the terminator-style sequence. It handles the fade-in, blink effects, brightness ramps and the final fade-out. 

It constantly monitors the signal going through GP16 from the SPST rocker switch so it knows when to run the fade-out and the 100kΩ pull‑down resistor ensures that the pico always detects the switch-off instantly.

---
<img width="392" height="486" alt="image" src="https://github.com/user-attachments/assets/c6555fb1-d46a-4c7d-bfb2-13a33e845faa" />

---

When the switch is turned off, the supercapacitor keeps the pico powered for a short time so it can run the controlled fade-out instead of just losing power instantly and turning off. The 1N4148 diode makes sure that the power only flows through to the VSYS, allowing the pico to sense the switch state going to GP16 while still receiving power from the supercapacitor.


After running the full animation, if the switch remains on, the LEDs will stay lit. If the switch is turned off at any point, the code immediately runs the fade-out function.


