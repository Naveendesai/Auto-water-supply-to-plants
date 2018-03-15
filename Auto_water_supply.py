import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

while True:
        input_state = GPIO.input(14)
        if input_state == False:
                GPIO.output(18,1)
                GPIO.output(17,0)
                if imput_state == False:
                  time.sleep(120)
                  GPIO.output(27,0)
                print("Moister is there,No water supply")
                time.sleep(1)
        else:
                GPIO.output(17,1)
                GPIO.output(27,1)
                GPIO.output(18,0)              
                print("No Moister,Water supply is started")
