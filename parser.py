import random
import os

'''
indices = random.sample(range(0, 7481), 3000)

vel_indice_strings = ["{0:0=6d}.bin".format(a) for a in indices]
img_indice_strings = ["{0:0=6d}.png".format(a) for a in indices]
label_indice_strings = ["{0:0=6d}.txt".format(a) for a in indices]

for root, dirs, files in os.walk(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\velodyne'):
    for name in files:
        if name not in vel_indice_strings:
            os.remove(os.path.join(root, name))

for root, dirs, files in os.walk(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\image_2'):
    for name in files:
        if name not in img_indice_strings:
            os.remove(os.path.join(root, name))

for root, dirs, files in os.walk(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\image_3'):
    for name in files:
        if name not in img_indice_strings:
            os.remove(os.path.join(root, name))

for root, dirs, files in os.walk(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\label_2'):
    for name in files:
        if name not in label_indice_strings:
            os.remove(os.path.join(root, name))

for root, dirs, files in os.walk(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\calib'):
    for name in files:
        if name not in label_indice_strings:
            os.remove(os.path.join(root, name))
'''

'''
# Another section to split into train, val, and test

indices = []

for root, dirs, files in os.walk(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\training\\calib'):
    for name in files:
        indices.append(name[:-4])

test_indices = random.sample(range(0, 3000), 1500)

# Generate test folder
# 

test_to_delete = []

for test_index in test_indices:
    num = indices[test_index]
    test_to_delete.append(test_index)
    
    os.rename(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\training\\calib\\' + num + '.txt', r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\testing\\calib\\' + num + '.txt')
    os.rename(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\training\\label_2\\' + num + '.txt', r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\testing\\label_2\\' + num + '.txt')
    os.rename(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\training\\image_2\\' + num + '.png', r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\testing\\image_2\\' + num + '.png')
    os.rename(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\training\\image_3\\' + num + '.png', r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\testing\\image_3\\' + num + '.png')
    os.rename(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\training\\velodyne\\' + num + '.bin', r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\testing\\velodyne\\' + num + '.bin')
'''

# Create validation set

'''
indices = []

for root, dirs, files in os.walk(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\training\\calib'):
    for name in files:
        indices.append(name[:-4])

val_indices = random.sample(range(0, 1500), 500)
val_index_strings = []

for val_index in val_indices:
    with open('val.txt', 'a') as the_file:
        the_file.write(indices[val_index] + '\n')
    val_index_strings.append(indices[val_index])

for index in indices:
    if index not in val_index_strings:
        with open('train.txt', 'a') as the_file:
            the_file.write(index + '\n')
'''

'''
indices = []

for root, dirs, files in os.walk(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\testing\\calib'):
    for name in files:
        indices.append(name[:-4])

for index in indices:
    with open('test.txt', 'a') as the_file:
        the_file.write(index + '\n')
'''

import pickle


with open(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\kitti_infos_train.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)

print(" ")

with open(r'C:\\Users\\garvi\\OneDrive\\Desktop\\188 Final\\kitti\\kitti_infos_val.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)
