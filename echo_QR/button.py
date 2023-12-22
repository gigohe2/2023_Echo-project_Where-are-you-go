import time
import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

BUTTON1_PIN = 33
BUTTON2_PIN = 31
BUTTON3_PIN = 29
BUTTON4_PIN = 23


GPIO.setup(BUTTON1_PIN, GPIO.IN)
GPIO.setup(BUTTON2_PIN, GPIO.IN)
GPIO.setup(BUTTON3_PIN, GPIO.IN)
GPIO.setup(BUTTON4_PIN, GPIO.IN)

# 0 : pushed / 1 : default

while True:
  

    print(GPIO.input(BUTTON1_PIN), GPIO.input(BUTTON2_PIN), GPIO.input(BUTTON3_PIN), GPIO.input(BUTTON4_PIN))
    if GPIO.input(BUTTON1_PIN) == 0:
        print("set")
        break
print('hello world out of while')