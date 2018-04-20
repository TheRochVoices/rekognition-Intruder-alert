import boto3
from pprint import pprint
import requests
import cv2
import time

client = boto3.client('rekognition')
cap = cv2.VideoCapture(0)
time.sleep(5)
success, imag = cap.read()
cv2.imwrite('test.jpg', imag)
imagefile = open('test.jpg', 'rb')
img = imagefile.read()

data = client.detect_labels(Image={'Bytes':img}, MinConfidence=60)
#pprint(data['Labels'])

for i in data['Labels']:
	print i
	if i['Name'] == 'Person':
		print('Person spotted')
		break
	'''else:
		print('chhooooooooot spotted')'''

