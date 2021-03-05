from machine import Pin, PWM
import time

Led_onboard = Pin(25, Pin.OUT)
Led_red = Pin(10, Pin.OUT)
Led_green = Pin(11, Pin.OUT)
Led_yellow = Pin(12, Pin.OUT)
sw1 = Pin(13, Pin.IN)
sw2 = Pin(14, Pin.IN)
sw3 = Pin(15, Pin.IN)
buzzer = PWM(Pin(9))

buzzer.freq(440)
buzzer.duty_u16(5000)
time.sleep(1)
buzzer.freq(494)
buzzer.duty_u16(5000)
time.sleep(1)
buzzer.freq(523)
buzzer.duty_u16(5000)
time.sleep(1)
buzzer.duty_u16(0)
i = 0
while True:
    if sw1.value()==0:
        Led_red.on()
    else:
        Led_red.off()
    if sw2.value()==0:
        Led_green.on()
    else:
        Led_green.off()
    if sw3.value()==0:
        Led_yellow.on()
    else:
        Led_yellow.off()
    time.sleep(0.1)
    i+=1
    if i>=10:
        if Led_onboard.value()==1:
            Led_onboard.value(0)
        else:
            Led_onboard.value(1)
        i=0
        
