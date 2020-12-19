"""
Load dataset from https://www.kaggle.com/andrewmvd/face-mask-detection
to Azure Custom Vision
"""

from os import listdir
from os.path import isfile, join

DIR_DATASET = r'PATH\TO\DATASET'
DIR_ANNOTATIONS = DIR_DATASET + "\\" + "annotations"
DIR_IMAGES = DIR_DATASET + "\\" + "images"

onlyfiles = [f for f in listdir(DIR_ANNOTATIONS) if isfile(join(DIR_ANNOTATIONS, f))]

print("Selecting photos with only one face...")
photos_wiht_one_face = []
for filename in onlyfiles:
    with open(DIR_ANNOTATIONS + '\\' + filename, 'r') as f:
        objects_count = 0 
        for line in f.readlines():
            if 'object' in line:
                objects_count += 1
            if objects_count > 2:
                break
        if objects_count <= 2:
            photos_wiht_one_face.append(filename.split('.')[0])

print(f"\tFound {len(photos_wiht_one_face)} photos with one face.")

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

mask_tag = None
nomask_tag = None

for tag in trainer.get_tags(project.id):
    if tag.name == "Mask":
        mask_tag = tag
    elif tag.name == "No mask":
        nomask_tag = tag

if not mask_tag:
    mask_tag = trainer.create_tag(project.id, "Mask")
if not nomask_tag:
    nomask_tag = trainer.create_tag(project.id, "No mask")


print("Adding images to list...")

image_list = []

mask_list = []
no_mask_list = []
for name in photos_wiht_one_face:
    with open(DIR_ANNOTATIONS + '\\' + name + '.xml', 'r') as f:
        classification = f.read().split('<name>')[1].split('</name>')[0]
    with open(DIR_IMAGES + '\\' + name + '.png', 'rb') as img_f:
        if classification == 'with_mask':
            mask_list.append(name)
            image_list.append(ImageFileCreateEntry(name=name + '.png', contents=img_f.read(), tag_ids=[mask_tag.id]))
        elif classification == 'without_mask':
            no_mask_list.append(name)
            image_list.append(ImageFileCreateEntry(name=name + '.png', contents=img_f.read(), tag_ids=[nomask_tag.id]))

print(f"\t{len(mask_list)} photos with mask")
print(f"\t{len(no_mask_list)} photos without mask")

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
