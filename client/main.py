import sys
import requests

import camera
import config

def main():
	cam_id = sys.argv[1]
	imgs = camera.get_image(cam_id)
	data = {
		'parking' : imgs[0],
		'background' : imgs[1]
	}
	print requests.post(config.url + '/api/set/' + cam_id, files = data).text

if __name__ == '__main__':
	main()
