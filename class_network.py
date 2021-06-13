# -*- coding: utf-8 -*-
"""Class_Network.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r92abiXK5cYrBJk-8vsRB0S0NuxrG3R8
"""

import tensorflow as tf
import tensorflow.keras
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras.utils import to_categorical
import numpy as np

class Network(Model):
  def __init__(self):
    super(Network,self).__init__()
    self.con2d=layers.Conv2D(filters=36,kernel_size=(3,3),activation='relu')
    self.maxpooling2d=layers.MaxPooling2D(pool_size=2,strides=2)
    self.batchnormalization=layers.BatchNormalization()
    self.flatten=layers.Flatten()
    self.layer_1=layers.Dense(units=256,activation='relu')
    self.layer_2=layers.Dense(units=256,activation='relu')
    self.out_layer=layers.Dense(units=10,activation='softmax')

  def call(self,x):
    x=self.con2d(x)
    x=self.maxpooling2d(x)
    x=self.batchnormalization(x)
    x=self.flatten(x)
    x=self.layer_1(x)
    x=self.layer_2(x)
    predict=self.out_layer(x)
    return predict

  def summary(self):
    x=Input(shape=(32,32,3))
    model=Model(inputs=x,outputs=self.call(x))
    return model.summary()

def loss_and_accuracy(model,X_train,y_train,X_test,y_test):
  model.compile(loss='CategoricalCrossentropy',metrics=['accuracy'],optimizer='sgd')
  model.fit(x=X_train,y=y_train,epochs=1,verbose=1)
  model.summary()
  test_loss,test_accuracy= model.evaluate(X_test,y_test)
  return test_loss,test_accuracy

def data_processing(X_train,y_train,X_test,y_test):
    X_train,X_test=X_train/255,X_test/255
    X_mean=np.mean(X_train)
    X_train,X_test=X_train-X_mean,X_test-X_mean
    y_test=to_categorical(y_test)
    y_train=to_categorical(y_train)
    return X_train,y_train,X_test,y_test
    


if __name__ == '__main__':   
    (X_train,y_train),(X_test,y_test)=datasets.cifar10.load_data()
    X_train,y_train,X_test,y_test= data_processing(X_train,y_train,X_test,y_test)
    model=Network()
    Loss,Accuracy =loss_and_accuracy(model,X_train,y_train,X_test,y_test)
  

