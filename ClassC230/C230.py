from numpy import loadtxt
from keras.model import Sequential
from keras.layers import Dense

#Loading dataset
dataset = loadtxt('diabetes_dataset.csv', delimiter = ',')

x = dataset[:,0:8]
y = dataset[:,8]

print('Value of X is: ', x)
print('Value of Y is: ', y)