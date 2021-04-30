# Karsten og Co
import utime
import urandom
import machine

while True:
    utime.sleep(5)
    target = urandom.randint(10, 12)
    startTime=utime.time_ns()
    machine.Pin(target,machine.Pin.OUT).on()
    print("selected ", target)
    x=machine.Pin(target+3,machine.Pin.IN)
    while x.value() == True:
            x=machine.Pin(target+3,machine.Pin.IN)
    itTook = utime.time_ns()-startTime
    machine.Pin(target,machine.Pin.OUT).off()
    print ("Took: " , itTook)
 