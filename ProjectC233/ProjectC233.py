import pandas as pd

#Reading the CSV file
df = pd.read_csv('projectC233_studentData.csv')

#Obtaining the total mass of all subjects by using sum functions
df['Total_marks_obtained'] = df.iloc[:, [2, 3, 4]].sum(axis = 1)
df.loc[df['Total_marks_obtained'] > 250, 'Grade'] = 'A'
df.loc[df['Total_marks_obtained'] < 250, 'Grade'] = 'B'

#Calculating ovrall mass of marks obtained
df['Percentage'] = (df['Total_marks_obtained'] / df['Overall_Total']) * 100

#Printing output
print('Overall Student Results: \n', df)