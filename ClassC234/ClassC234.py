import pandas as pd
from sklearn.neural_network import MLPClassifier

#Reading the dataset
dataset = pd.read_csv('new_radar_distance_data.csv')

#Defining input (x) and output (y) variables
x = dataset.iloc[:, [2,4]].values
y = dataset.iloc[:, 5].values

#Defining the model
model = MLPClassifier(hidden_layer_sizes = (20), random_state = 5, activation = 'relu', batch_size = 200, learning_rate_init = 0.03) 

#Testing the model
model.fit(x, y)

#Prediction
prediction = model.predict(x)
print("predicted data: ", prediction)