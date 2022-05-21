from typing import Literal, Mapping, Tuple
from micropython import machine
from wasp import draw565

class Accelerometer:
    def reset(self): pass
    def steps(self): pass

class Backlight: pass
class Battery: pass
class CST816S: pass
class HRS:
    DATA: Tuple[int, ...]
    def __init__(self): pass
    def disable(self): pass
    def enable(self): pass
    def read_hrs(self): pass
I2C = machine.I2C
class Pin:
    IN = "IN"
    IRQ_FALLING = "IRQ_FALLING"
    OUT = "OUT"
    pins: Mapping[str, machine.Pin]
    def __call__(self, v=None): pass
    def __init__(self, id, diirection, value: Literal[0,1], quiet: bool): pass
    def init(self, d, value): pass
    def irq(self, trigger, handler): pass
    def off(self): pass
    def on(self): pass
    def raise_irq(self): pass
    def value(self, v=None): pass

class RTC:
    def get_localtime(self): pass
    def get_time(self): pass
    def get_uptime_ms(self): pass
    def set_localtime(self, t): pass
    def time(self, t) -> float: pass
    def update(self): pass
    @property
    def uptime(self): pass

class SPIST789_SPI: pass
class Vibrator: pass

backlight: Backlight
battery: Battery
button: machine.Pin
def connected() -> bool: pass
display: SPIST789_SPI
drawable: draw565.Draw565
free: int
hrs: HRS
# os
# print_exception
# rtc
# sleep_ms
# spi
# sys
# time
# touch
# traceback
# vibrator
# warnings
accel: Accelerometer
