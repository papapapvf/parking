import cv


capture = cv.CaptureFromCAM(0)


def get_image():
	return (open('img/parkng.jpg', 'rb'), open('img/background.jpg', 'rb'))


def setup():
	img = cv.QueryFrame(capture)
	cv.SaveImage("img/background.jpg", img)


def loop():
	img = cv.QueryFrame(capture)
	cv.SaveImage("img/parkng.jpg", img)


def main():
	setup()
	loop()

if __name__ == '__main__':
	main()
