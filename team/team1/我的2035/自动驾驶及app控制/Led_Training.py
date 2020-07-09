#!/usr/bin/env python3  
# encoding: utf-8 
import time
time1 = time.time()
import os
import sys
import CarConf
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
####训练图片,保存模型####
if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)

time_end = time.time()
t = time_end - time1
print("loading tensorflow cost:{:.0f}m{:.0f}s ".format(t//60, t % 60))

time2 = time.time()

np.random.seed(7)
img_h, img_w = CarConf.image_size[1], CarConf.image_size[0] 
nbatch_size = CarConf.batch_size
nepochs = CarConf.epochs 
p = os.path.split(os.path.abspath(sys.argv[0]))[0]

#加载图片
def load_data():
    global img_w, img_h
    path = CarConf.path_imageled
    files = os.listdir(path)
    images = []
    labels = []
    for f in files:
        img_path = path + f
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=(img_w, img_h))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        images.append(img_array)

        if 's_' in f:
            labels.append(0)
        # elif 's_' in f:
        #     labels.append(1)
        # elif 'r_' in f:
        #     labels.append(2)
        # elif 'l_' in f:
        #     labels.append(3)
        elif 'o_' in f:
            labels.append(1)
    data = np.array(images)
    labels = np.array(labels)

    labels = tf.keras.utils.to_categorical(labels, 2)
    return data, labels

#构建网络
def main():
    #############model for track#########################
    model = tf.keras.models.Sequential()

    model.add(tf.keras.layers.Conv2D(32, kernel_size=(3, 3), input_shape=(img_h, img_w, 3), activation='relu', strides=(2, 2)))
    model.add(tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu', strides=(2, 2)))
    model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(256, activation='relu'))
    model.add(tf.keras.layers.Dense(2, activation='softmax'))
    model.summary()

    print("compile.......")
    sgd = tf.keras.optimizers.Adam(lr=CarConf.learn_rate)  
    model.compile(loss='mean_squared_error', optimizer=sgd, metrics=['accuracy'])

    print("load_data......")
    images, lables = load_data()
    images /= 255
    
    time_end = time.time()
    t = time_end - time2
    print("loading date cost:{:.0f}m{:.0f}s ".format(t//60, t % 60))
    
    x_train, x_test, y_train, y_test = train_test_split(images, lables, test_size=0.2)
    print(x_train.shape, y_train.shape)

    print("train.......")
    model.fit(x_train, y_train, batch_size=nbatch_size, epochs=nepochs, verbose=1, validation_data=(x_test, y_test))

    print("evaluate......")
    scroe, accuracy = model.evaluate(x_test, y_test, batch_size=nbatch_size)
    print('scroe:', scroe, 'accuracy:', accuracy)

    yaml_string = model.to_yaml()
    path = p + CarConf.path_model
    if not os.path.exists(path):
        os.makedirs(path)
        print('Create Path \'' + path + '\' success!')
    with open(path + CarConf.model_names2 + '.yaml', 'w') as outfile:
         outfile.write(yaml_string)
    model.save_weights(path + CarConf.model_names2 + '.h5', save_format='h5')
    print('Save model at: ' + path)

if __name__ == '__main__':
    main()
    time_end = time.time()
    t = time_end - time1
    print("training time:{:.0f}m{:.0f}s ".format(t//60, t % 60))
