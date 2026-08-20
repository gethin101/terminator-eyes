import machine
import utime
import urandom

sw = machine.Pin(16, machine.Pin.IN)

left = machine.PWM(machine.Pin(20))  
right = machine.PWM(machine.Pin(4)) 

left.freq(1000)
right.freq(1000)

def set_both(level):
    left.duty_u16(level)
    right.duty_u16(level)

def fade_out(duration_ms):
    steps = 2000
    delay = duration_ms / steps

    for i in range(steps):
        remaining = (steps - i) / steps
        lvl = int((remaining ** 2.5) * 65535)
        set_both(lvl)
        utime.sleep_ms(int(delay))


def terminator_eye_full(duration_ms):

    program_start = utime.ticks_ms()
    base = 65535

    steps = 5000
    delay = duration_ms / steps

    for i in range(steps):
        if sw.value() == 0:
            fade_out(5000)
            return

        progress = i / (steps - 1)
        level = int((progress**2.2) * 65535)


        if i == int(3500 / delay):
            set_both(0); utime.sleep_ms(40)
            set_both(level); utime.sleep_ms(40)
            set_both(0); utime.sleep_ms(40)
            set_both(level); utime.sleep_ms(40)

        set_both(level)
        utime.sleep_ms(int(delay))

    set_both(base)
    utime.sleep_ms(5000)

    for _ in range(2):
        if sw.value() == 0:
            fade_out(5000)
            return
        set_both(0); utime.sleep_ms(40)
        set_both(base); utime.sleep_ms(40)
        set_both(0); utime.sleep_ms(40)
        set_both(base); utime.sleep_ms(40)
        utime.sleep_ms(500)

    set_both(base)
    utime.sleep_ms(6000)

    for _ in range(5):
        if sw.value() == 0:
            fade_out(5000)
            return
        drop = int(base * 0.4)
        set_both(base - drop)
        utime.sleep_ms(25)
        set_both(base)
        utime.sleep_ms(20)

    set_both(base)
    utime.sleep_ms(4000)

    for _ in range(2):
        if sw.value() == 0:
            fade_out(5000)
            return
        set_both(0); utime.sleep_ms(40)
        set_both(base); utime.sleep_ms(40)
        utime.sleep_ms(500)

    set_both(base)
    utime.sleep_ms(5000)

    for i in range(200):
        if sw.value() == 0:
            fade_out(5000)
            return
        lvl = int(base - (i / 199) * base)
        set_both(lvl)
        utime.sleep_ms(2)

    set_both(0); utime.sleep_ms(40)
    set_both(base)

    utime.sleep_ms(70)

    set_both(0)
    utime.sleep_ms(600)

    set_both(base)
    utime.sleep_ms(120)
    set_both(0); utime.sleep_ms(40)
    set_both(base)

    set_both(base)
    utime.sleep_ms(8000)

    while utime.ticks_diff(utime.ticks_ms(), program_start) < 61000:
        if sw.value() == 0:
            fade_out(5000)
            return

        r = urandom.getrandbits(8)

        if r < 3:
            set_both(0); utime.sleep_ms(60)
            set_both(base)
            utime.sleep_ms(200)

        elif r == 4:
            set_both(0); utime.sleep_ms(40)
            set_both(base); utime.sleep_ms(40)
            set_both(0); utime.sleep_ms(40)
            set_both(base)
            utime.sleep_ms(300)

        else:
            utime.sleep_ms(150)

    set_both(base)
    utime.sleep_ms(8000)

    set_both(base)
    while True:
        if sw.value() == 0:
            fade_out(5000)
            return
        utime.sleep_ms(200)

while True:
    if sw.value() == 1:
        terminator_eye_full(6000)
    else:
        set_both(0)
        utime.sleep_ms(50)

#gethin101 - 8/26
