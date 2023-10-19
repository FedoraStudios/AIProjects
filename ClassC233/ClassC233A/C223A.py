import pandas as pd

data = pd.read_csv('student_promoted.csv')
data.loc[data['Attendance'] > 75, 'student_promoted'] = 'Promoted'
data.loc[data['Attendance'] < 75, 'student_promoted'] = "Not Promoted"
print(data)