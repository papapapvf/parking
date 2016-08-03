import camera
import requests
import config

def main():
	imgs = camera.get_image()
	data = {
		'parking' : imgs[0],
		'background' : imgs[1]
	}
	print requests.post('http://127.0.0.1:5000/api/set/1', files = data).text

if __name__ == '__main__':
	main()
