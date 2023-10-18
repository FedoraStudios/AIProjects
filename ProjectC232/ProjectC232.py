from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

#Loading the datasets
dataset = loadtxt('pokemon.csv', delimiter = ',')

#Splitting Input (X) and Output (Y) Variables
x = dataset[:,1:7]
y = dataset[:,8]

#Defining Keras Model
model = Sequential()
model.add(Dense(12, input_dim=6, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

#Compiling model
model.compile(loss = 'binary_crossentropy', metrics = ['accuracy'])

#Fitting the model
model.fit(x, y, epochs = 250, batch_side = 200)

#Predicting Class model
prediction = model.predict_classes('x')
for i in range(785):
	print(f'{x[i].tolist()} => {prediction[i]} expected {y[i]}')