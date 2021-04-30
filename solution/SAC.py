############################################
# reaction game Søren, Anita og Christian
from machine import Pin, Timer, PWM
import urandom
import utime

Led_red = Pin(10, Pin.OUT)
Led_green = Pin(11, Pin.OUT)
Led_yellow = Pin(12, Pin.OUT)
li = [Led_red, Led_green, Led_yellow]

sw1 = Pin(13, Pin.IN)
sw2 = Pin(14, Pin.IN)
sw3 = Pin(15, Pin.IN)
swli = [sw1, sw2, sw3]

buzzer = PWM(Pin(9))

time1 = Timer()
ran = urandom.randint(0,2)
print(ran)

def flash():
    print("flash!")
    li[ran].on()
    
def clear():
    for led in li:
        led.off()

def poll():
    while True:
        if swli[ran].value()==0:
            print("Det var den rigtige!")
            break
        elif swli[0].value()==0 or swli[1].value()==0 or swli[2].value()==0:
            print("buzz")
            # buzz
            #buzzer.freq(494)
            #buzzer.duty_u16(5000)
            utime.sleep(1)
            #buzzer.duty_u16(0)
            print("buzz off")

def start(event):
    clear()
    flash()
    før = utime.ticks_ms()
    poll()
    efter = utime.ticks_ms()
    print(utime.ticks_diff(efter, før))
    clear()

t = urandom.randint(1000,4000)
time1.init(mode=Timer.ONE_SHOT, period=t, callback=start)
############################################

