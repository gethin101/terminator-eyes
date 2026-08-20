# Terminator Eyes
Terminator eyes LED fade-in and fade-out animation project with a raspberry pi pico, a 1N4148 diode, an 1000uF electrolytic capacitor, 22AWG silicone soldered wiring and powered by a 6V battery holder with a SPST rocket switch.

![Raspberry Pi](https://img.shields.io/badge/-Raspberry_Pi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

| Part                     | Use                                                                 |
|--------------------------|---------------------------------------------------------------------|
| Raspberry Pi Pico        | Runs the LED animation program and reads the switch input.          |
| 4× AA Battery Pack       | Provides main power for the system.                                 |
| On/Off Switch            | Turns the system on/off and signals the Pico to start/stop.         |
| Diode (1N4148)           | Allows power to VSYS but blocks reverse flow back to the switch.    |
| Supercapacitor (5.5V)    | Keeps the Pico powered briefly after switch-off for fade-out.       |
| 100kΩ Resistor           | Pull-down so GP16 reads LOW when the switch is off.                 |
| 2× LEDs                  | Creates the Terminator eye visual effect.                           |
| 2× 220Ω Resistors        | Limits current to each LED.                                         |
| Jumper Wires             | Connects all components together.                                   |


---


---
No breadboard, PCB or perfboard. Wiring done loose with AWG and soldering. Code in Thonny Micropython.

Fade on when powered, capacitor constantly being filled -> power switch flipped, capacitor discharges power into pico VSYS, fade-out animation on LEDs.

**Fade out animation based on capacitor microfarads**

470uF is about 0.5s

**1000uF is about 1s**

2200uF is about 2s

---

# Wiring

| From                     | To                          | Notes |
|--------------------------|------------------------------|-------|
| Battery + (red)          | Switch INPUT                 | Main power feed into switch |
| Switch OUTPUT            | 1N4148 diode (non‑stripe end) | Diode oriented toward Pico |
| 1N4148 diode (stripe end)| Pico VSYS                    | Stripe end ALWAYS points to VSYS (black) |
| Battery – (black)        | Pico GND                     | Common ground |
| Capacitor + (long leg)   | Pico VSYS                    | Charges when Pico is powered |
| Capacitor – (short leg)  | Pico GND                     | Provides discharge path |
| LED 1 anode (long leg)   | Pico GPIO (e.g., GP15)       | PWM pin for fade control |
| LED 1 cathode (short leg)| 330Ω resistor → Pico GND     | Current limiting resistor |
| LED 2 anode (long leg)   | Pico GPIO (e.g., GP14)       | Second PWM pin |
| LED 2 cathode (short leg)| 330Ω resistor → Pico GND     | Current limiting resistor |

<img width="1536" height="1024" alt="wiring image - AI" src="https://github.com/user-attachments/assets/db7eebaa-b6c0-4b2d-ab5b-d688e3ed3260" />
**AI image**










