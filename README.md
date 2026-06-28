# BOM
| Qty | Item | Cost (£) | Link | Notes |
|-----|------|----------|------|-------|
| 1  | Raspberry Pi Pico | **OWN** | N/A | Headers |
| 2 | Red LEDs | **OWN** | N/A | 5mm |
| 2 | 330Ω resistors | **OWN** | N/A | 1/LED |
| 2m | 22AWG silicone wire | £2.55 | [AE](https://www.aliexpress.com/item/1005006403191349.html?spm=a2g0o.order_list.order_list_main.9.4ae71802DOKMSO) | Black 22AWG |
| 5 | SPST rocker switch | £2.88 | [AE](https://www.aliexpress.com/item/1005009143297950.html?spm=a2g0o.order_list.order_list_main.4.4ae71802DOKMSO) | KCD11 10X15mm |
| 1 | 6V battery holder | **OWN** | N/A | 4x AA |
| 4 | AA batteries | **OWN** | N/A | 1.5V each, KODAK |
| 1 | 1N4148 diode | **OWN** | N/A | For power down |
| 40 | Electrolytic capacitor | £ | [AE](https://www.aliexpress.com/item/1005011811368397.html?spm=a2g0o.productlist.main.1.1ccfAwSPAwSPhH&algo_pvid=ef5df676-e53e-4d44-a2fb-860b16e3ebae&algo_exp_id=ef5df676-e53e-4d44-a2fb-860b16e3ebae-0&pdp_ext_f=%7B%22order%22%3A%223246%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21GBP%211.42%211.42%21%21%2112.34%2112.34%21%402103985c17826554210472484ef7a7%2112000056639843385%21sea%21GB%217850874718%21X%211%210%21n_tag%3A-29919%3Bd%3Ac7b67d0a%3Bm03_new_user%3A-29895&curPageLogUid=u1bxgRaDw9Wa&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005011811368397%7C_p_origin_prod%3A) | 10V 470uF 40PCS or 1000uF |

**£** running total

**£** fee

No breadboard, PCB or perfboard. Wiring done loose with AWG and soldering. Code in Thonny Micropython.

Fade on when powered, capacitor constantly being filled -> power switch flipped, capacitor discharges power into pico VSYS, fade-out animation on LEDs.

**Fade out animation based on capacitor microfarads**

470uF is about 0.5s

**1000uF is about 1s**

2200uF is about 2s

# Wiring
# Wiring Table (Soft-Off Fade-Out Circuit)

| From                     | To                          | Notes |
|--------------------------|------------------------------|-------|
| Battery + (red)          | Switch INPUT                 | Main power feed into switch |
| Switch OUTPUT            | 1N4148 diode (non‑stripe end) | Diode oriented toward Pico |
| 1N4148 diode (stripe end)| Pico VSYS                    | Stripe end ALWAYS points to VSYS |
| Battery – (black)        | Pico GND                     | Common ground |
| Capacitor + (long leg)   | Pico VSYS                    | Charges when Pico is powered |
| Capacitor – (short leg)  | Pico GND                     | Provides discharge path |
| LED 1 anode (long leg)   | Pico GPIO (e.g., GP15)       | PWM pin for fade control |
| LED 1 cathode (short leg)| 330Ω resistor → Pico GND     | Current limiting resistor |
| LED 2 anode (long leg)   | Pico GPIO (e.g., GP14)       | Second PWM pin |
| LED 2 cathode (short leg)| 330Ω resistor → Pico GND     | Current limiting resistor |










