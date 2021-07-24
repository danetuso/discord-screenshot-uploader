#!/usr/bin/python
"""
Save image from clipboard to file, upload to s3, then overwrite clipboard with url
"""
from PIL import ImageGrab
import boto3
import pyperclip

import os
from datetime import datetime

# Define API Credentials
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''

# Define Bucket Details
S3_BUCKET_NAME='bucketname'
S3_REGION='us-west-1'
S3_URL='https://bucketname.s3.us-west-1.amazonaws.com/'

# Define Temporary Local File Location
data_path=os.getenv('LOCALAPPDATA')
SAVE_PATH_DIR=data_path + "\\Temp\\"
#SAVE_PATH_DIR='C:/ctrlv/'


# Define Image File Name (Default: datetime 2021-07-23T16.25.08.png)
now = datetime.now()
IMAGE_NAME = now.strftime("%Y-%m-%dT%H.%M.%S")


image_path = SAVE_PATH_DIR + IMAGE_NAME + ".png"
image = ImageGrab.grabclipboard()

if image is not None:
	image.save(image_path)
	s3_client = boto3.client('s3',
		aws_access_key_id=AWS_ACCESS_KEY_ID,
		aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
		region_name=S3_REGION)
	try:
		response = s3_client.upload_file(image_path, S3_BUCKET_NAME, IMAGE_NAME + ".png")
		pyperclip.copy(S3_URL + IMAGE_NAME + '.png')
		os.remove(image_path)
	except Exception as e:
		print(e)
else:
	print("Clipboard empty or not containing image")