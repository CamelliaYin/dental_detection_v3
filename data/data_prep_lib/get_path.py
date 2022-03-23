import os


# transfer yolov5 data to yolov3 format, for both train and val
# directory: outside images, and within images there two DATASETS: train and val
# NOTE: two DATASETS with images, not annotations

prefix0 = 'data'
prefix1 = 's-iid' #TODO: customise dataset name here
prefix = os.path.join(prefix0, prefix1)

with open('train.txt', 'w') as f0:
    for filename in os.listdir('images/train'):
        file_dir = os.path.join(prefix, filename)
        print(file_dir, file=f0)
f0.close()

with open('valid.txt', 'w') as f1:
    for filename in os.listdir('images/val'):
        file_dir = os.path.join(prefix, filename)
        print(file_dir, file=f1)
f1.close()