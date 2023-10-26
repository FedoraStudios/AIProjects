import pandas as pd
import pickle
from keras.models import model_from_json
from sklearn.neural_network import MLPClassifier

#Reading the CSV
dataset = pd.read_csv('new_radar_distance_data.csv')

#Splitting the data into input (x) and output (y)
x = dataset.iloc[:, [2, 4]].values
y = dataset.iloc[:, 5].values

#Defining MLPClassifier model
model = MLPClassifier(hidden_layer_sizes = (20), random_state = 5, activation = 'relu', batch_size = 200, learning_rate_init = 0.03)

#Testing the model
model.fit(x, y)

#Making predictions on input data
predictions = model.predict(x)

#Saving the classifier
with open('my_dumped_classifier2.pkl', 'wb') as file:
	pickle.dump(model, file)

#Loading file again
with open('my_dumped_classifier2.pkl', 'rb') as saved_model_file:
	saved_model = pickle_load(saved_model_file)

#Testing model
car_data = {'throttle': [0.364332455],
'steer': [0.654],
'distance': [6.674762726]}

data = pd.DataFrame(car_data, columns = ['throttle', 'steer', 'distance'])
predicted_data = saved_model.predict(data)
print('Your Prediction From The Model Is: ', predicted_data)