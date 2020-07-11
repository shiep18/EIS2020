#!/usr/bin/python3
import platform
#coding:utf8
#训练及采集图像时的参数配置，谨慎修改！！！
############################
############################
#截取主要跑道区域，作为训练图像
roi_range  = (150, 700, 0, 900)
roi_rangeled = (50,180,0,200)
#保存及训练时图像的大小
image_size = (60, 60)
############################
if(platform.system()=='Windows'):
  print('Windows')
  path_model = '.\\model\\' #模型默认的保存位置
  path_image = '.\\training\\' #采集到的图像默认保存位置
  path_imagedir = '.\\training_dir\\'
  path_imageled = '.\\training_led\\'
elif(platform.system()=='Linux'):
  print('Linux')
  path_model = './model/'#模型默认的保存位置
  #path_image = '/media/pi/BOOT/training1/'#采集到的图像默认保存位置
  path_image = './training/'#采集到的图像默认保存位置
else:
  print('others')
  
#保存模型的名称
model_names = 'track'
model_names2 = 'trafficLed'
############################
#训练的批次
epochs     = 100

#每批次的数据量
batch_size = 100

#学习率
learn_rate = 0.0003
############################
