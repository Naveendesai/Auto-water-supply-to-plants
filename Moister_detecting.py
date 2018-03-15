import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

while True:
  input_state = GPIO.input(14)
    if input_state == False:
      GPIO.output(18,1)
      GPIO.output(17,0)
      print("Moister is there")
      time.sleep(1)
    else:
      GPIO.output(17,1)
      GPIO.output(18,0)
      print("No Moister")
