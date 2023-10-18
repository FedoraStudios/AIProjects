from numpy import loadtxt
from keras.model import Sequential
from keras.layers import Dense

#Loading dataset
dataset = loadtxt('diabetes_dataset.csv', delimiter = ',')

#Input and Output variables
x = dataset[:,0:8]
y = dataset[:,8]

print('Value of X is: ', x)
print('Value of Y is: ', y)

#Defining Keras Model

model = Sequential()
model.add(Dense(12, input_dim = 8, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))
model.summery()

