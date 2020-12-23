import os
import random
dir = './bottle-dataset'
data_dir = os.path.join(dir,'images')

images_list = os.listdir(data_dir)
test_size=int(0.1*len(images_list))
val_size = int(0.1*len(images_list))
random.shuffle(images_list)
test_data = images_list[:test_size]
val_data = images_list[test_size:test_size+val_size]
train_data = images_list[test_size+val_size:]
print(len(test_data))
print(len(val_data))
print(len(train_data))
with open('../data/train.txt','w') as f:
    for data in train_data:
        f.write('../bottle-dataset/images/'+data)
        f.write('\n')

with open('../data/test.txt','w') as f:
    for data in test_data:
        f.write('../bottle-dataset/images/'+data)
        f.write('\n')
with open('../data/val.txt','w') as f:
    for data in test_data:
        f.write('../bottle-dataset/images/'+data)
        f.write('\n')
# label_dir = os.path.join(dir,'label')
#
# types = ['waterdrop','circle','eclipse']
# data_list = {}
#
# for type in types:
#     print(type)
#     data_list = os.listdir(os.path.join(data_dir,type))
#
#     label_list = os.listdir(os.path.join(label_dir,type))
#     data_list = set([f.split('.')[0] for f in data_list])
#     label_list  = set ([f.split('.')[0] for f in label_list])
#
#     print(data_list.difference(label_list))

