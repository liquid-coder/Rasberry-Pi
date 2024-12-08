from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device, Servo, AngularServo
from time import sleep
Device.pin_factory = PiGPIOFactory()
s = AngularServo(17,min_angle = 0, max_angle = 180,min_pulse_width=0.5/1000,max_pulse_width = 25/10000)
while True:
s.angle=120
sleep(1)
s.angle=60 
sleep(1)
