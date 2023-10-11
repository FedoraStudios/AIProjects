import pandas as pd

#Reading from the CSV file
dataset = pd.read_csv(r'country_vaccinations.csv')
print('Shape of the given dataset: ', dataset.shape)
print('Count of columns: ', len(dataset.columns))
print('Name of the used parameters: ', dataset.columns)
print('Display the empty row data: ', dataset.loc[:, dataset.isna().any()])
#Test