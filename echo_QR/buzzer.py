import time
import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

BUZZER_PIN = 35

GPIO.setup(BUZZER_PIN, GPIO.OUT, initial=GPIO.LOW)

while True:
  
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    time.sleep(0.2)
    break
