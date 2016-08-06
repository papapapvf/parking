import sys
import requests
import threading

import camera
import config


def set_interval(func, sec):
	def func_wrapper():
		set_interval(func, sec)
		func()
	t = threading.Timer(sec, func_wrapper)
	t.start()
	return t


def loop():
	try:
		camera.loop()
		cam_id = sys.argv[1]
		imgs = camera.get_image()
		data = {
			'parking' : imgs[0],
			'background' : imgs[1]
		}
		print requests.post(config.url + '/api/set/' + cam_id, files = data).text
	except:
		print 'error'


def main():
	camera.setup()
	set_interval(loop, 1)
	# loop()


if __name__ == '__main__':
	main()
