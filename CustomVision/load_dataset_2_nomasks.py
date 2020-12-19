"""
Load dataset from https://www.kaggle.com/jessicali9530/lfw-dataset
to Azure Custom Vision
"""

from os import listdir
from os.path import isdir, join
import random

DIR_DATASET = r'PATH\TO\DATASET'
NUMBER_OF_IMAGES = 200

# select diresctories with only one file inside
onlydirs = [f for f in listdir(DIR_DATASET) if isdir(join(DIR_DATASET, f)) and len(listdir(join(DIR_DATASET, f))) == 1]

try:
    photos_for_upload = random.sample(onlydirs, NUMBER_OF_IMAGES)
except ValueError:
    print('Sample size exceeded population size.')


from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import time

ENDPOINT = "<your API endpoint>"
training_key = "<your training key>"
prediction_key = "<your prediction key>"
prediction_resource_id = "<your prediction resource id>"

CUSTOM_VISION_PROJECT_ID = "<your custom vision project id>"

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

print ("Getting project...")
project = trainer.get_project(CUSTOM_VISION_PROJECT_ID)

nomask_tag = None

for tag in trainer.get_tags(project.id):
    if tag.name == "No mask":
        nomask_tag = tag

if not nomask_tag:
    nomask_tag = trainer.create_tag(project.id, "No mask")


print("Adding images to list...")

image_list = []
nomask_list = []
for dir_name in photos_for_upload:
    photo_name = listdir(join(DIR_DATASET, dir_name))[0]
    photo_path = join( DIR_DATASET, dir_name,  photo_name)
    with open(photo_path, 'rb') as img_f:
        nomask_list.append(photo_path)
        image_list.append(ImageFileCreateEntry(name=photo_name, contents=img_f.read(), tag_ids=[nomask_tag.id]))

print("Uploading tagged images...")

# split image list into smaller portions coz batch can have max 64 images
for batch_idx in range(0, len(image_list), 64):
    print(f"\tUploading batch number {int(batch_idx / 64) + 1}...")
    upload_result = trainer.create_images_from_files(project.id, ImageFileCreateBatch(images=image_list[batch_idx : batch_idx + 64]))
    if not upload_result.is_batch_successful:
        print("Image batch upload failed.")
        for image in upload_result.images:
            print("Image status: ", image.status)

print("Upload finished.")