import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
pwm=GPIO.PWM(17,50)
pwm.start(7) 

while True:
  pwm.ChangeDutyCycle(5.3) 
  sleep(1)
  pwm.ChangeDutyCycle(8.7) 
  sleep(1)
