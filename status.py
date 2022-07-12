import time

def log_input(queue):
	while True:
		data = queue.get()
		print(data)

		time.sleep(0.1)