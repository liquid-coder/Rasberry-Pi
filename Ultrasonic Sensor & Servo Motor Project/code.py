from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device, Servo, AngularServo
import time
import RPi.GPIO as GPIO
Device.pin_factory = PiGPIOFactory()


TRIG_PIN = 21
ECHO_PIN = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

s = AngularServo(17,min_angle = 0,max_angle = 180, min_pulse_width = 0.5/1000,max_pulse_width = 25/10000)
def measure_distance():
    GPIO.output(TRIG_PIN, True)
    time.sleep(10**-5)
    GPIO.output(TRIG_PIN, False)
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

while True:
    distance = measure_distance()
    print(distance)
    if distance < 10:
        s.angle = 0
    elif distance < 20:
        s.angle = 45
    elif distance < 30:
        s.angle = 90
    elif distance < 40:
        s.angle = 135
    else:
        s.angle = 180
    time.sleep(0.5)

GPIO.cleanup()
