<<<<<<< HEAD
import cv
capture = cv.CaptureFromCAM(0)
img = cv.QueryFrame(capture)
cv.SaveImage("img/parking.jpg", img)

def get_image(cam_id):
	return (open('img/parkng.jpg', 'rb'), open('img/background.jpg', 'rb'))
=======
def get_image(cam_id):
	return (open('img/parking.jpg', 'rb'), open('img/background.jpg', 'rb'))
>>>>>>> 35284c370f7c53f80b2696afa4634a30b0f8585b
