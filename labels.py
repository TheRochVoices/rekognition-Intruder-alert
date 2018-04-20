import boto3
from pprint import pprint
import requests

client = boto3.client('rekognition')
imgfile =  open('test1.jpg', 'rb')
img = imgfile.read()
data = client.detect_labels(Image={'Bytes':img}, MinConfidence=60)
pprint(data['Labels'])

for i in data['Labels']:
	print i
	if i['Name'] == 'Person':
		print('Person spotted')
	else:
		print('chhooooooooot spotted')

