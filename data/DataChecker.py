import glob
import os

train_images = set(glob.glob('train/*'))
print(f"Training Images: {len(train_images)}")
valid_images = set(glob.glob('valid/*'))
print(f"Validation Images: {len(valid_images)}")
test_images = set(glob.glob('test/*'))
print(f"Testing Images: {len(test_images)}")

valid_test = set.union(valid_images, test_images)

union = set.union(valid_test, train_images)
print(len(union))