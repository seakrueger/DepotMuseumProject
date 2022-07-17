from buildhat import Motor
from time import sleep

motor_a = Motor('A')
motor_a.set_default_speed(100)
#motor_a.run_for_seconds(5)

motor_a.start()
print("Waiting...")
sleep(5)
motor_a.stop()