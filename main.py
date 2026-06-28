import machine
import utime

left = machine.PWM(machine.Pin(15))
right = machine.PWM(machine.Pin(14))

left.freq(1000)
right.freq(1000)

def set_both(level):
    left.duty_u16(level)
    right.duty_u16(level)

def fade_in(duration_ms):
    steps = 800 
    delay = duration_ms / steps

    for i in range(steps):
        level = int((i / (steps - 1)) * 65535) 
        set_both(level)
        utime.sleep_ms(int(delay))

fade_in(7000)
set_both(65535)

while True:
    set_both(65535)
    utime.sleep_ms(50)

