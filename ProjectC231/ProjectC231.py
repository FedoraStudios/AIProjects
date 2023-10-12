import pandas as pd
from keras.models import Sequential
from keras.layers import Dense

#Loading datasets
dataset = pd.read_csv(r'books.csv', error_bad_lines = False)

#Splitting input (x) and output (y) variables
x = dataset.iloc[:,[4,11]].values #input
y = dataset.iloc[:,3].values #output

#CNN model
model = Sequential()
model.add(Dense(128, input_dim = 8, activation = 'relu'))
model.add(Dense(128, activation = 'relu'))
model.add(Dense(56, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))
model.summery()