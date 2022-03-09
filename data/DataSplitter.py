import os
import shutil
import glob

image_files = glob.glob('train/*.jpg')
total_images = len(image_files)
split_size = total_images//3

os.mkdir('train/Akib')
os.mkdir('train/Alif')
os.mkdir('train/FSK')

akib_images = image_files[ : split_size]
alif_images = image_files[split_size : 2*split_size]
fsk_images = image_files[2*split_size : ]

unique_images = set.union(set(akib_images), set(alif_images), set(fsk_images))

print(f'Unique images before moving: {len(unique_images)}')

for image in akib_images:
    shutil.move(image, 'train/akib/')

for image in alif_images:
    shutil.move(image, 'train/alif/')

for image in fsk_images:
    shutil.move(image, 'train/fsk/')

new_files = set.union(set(glob.glob('train/akib/*')), set(glob.glob('train/alif/*')), set(glob.glob('train/fsk/*')))
print(f'Unique files after moving: {len(new_files)}')