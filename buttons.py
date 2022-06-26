import RPi.GPIO as GPIO
import time
import subprocess

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

def light_led(led):
	GPIO.output(led, GPIO.HIGH)
	try:
		proc = subprocess.run(["cvlc", "https://www.youtube.com/watch?v=TLwhqmf4Td4"])
		print("The exit code was: %d" % proc.returncode)
	finally:
		GPIO.output(led, GPIO.LOW)

while True:
	if GPIO.input(BUTTON1):
		light_led(LED1)

	if GPIO.input(BUTTON2):
		light_led(LED2)

	if GPIO.input(BUTTON3):
		light_led(LED3)

	time.sleep(0.5)
	print("whatever")