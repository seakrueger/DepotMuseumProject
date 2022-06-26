import RPi.GPIO as GPIO
import time

BUTTON1 = 19
BUTTON2 = 23
BUTTON3 = 36

LED1 = 33
LED2 = 35
LED3 = 37

GPIO.setmode(GPIO.BOARD)

GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

while True:
	print(GPIO.input(BUTTON1), GPIO.input(BUTTON2), GPIO.input(BUTTON3))

	time.sleep(0.5)