import os
import shutil
from MislabeledSamples import badLabels

print(f"Bad Images: {len(badLabels)}")

source = 'train'
destination = 'train_cleaned'

all_images = os.listdir(source)
print(f"All Images: {len(all_images)}")

cleaned_images = []

for image in all_images:
    if image not in badLabels:
        cleaned_images.append(image)

print(f"Cleaned Images: {len(cleaned_images)}")

counter = 0
for image in cleaned_images:
    shutil.move(os.path.join(source, image), os.path.join(destination, image))
    counter += 1

print(f"{counter} files moved successfully!")