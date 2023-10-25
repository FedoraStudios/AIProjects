import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

#Reading the Comma Seperated Value (CSV)
dataset = pd.read_csv('projectC234_EPL.csv')

#Sorting the dataset
goals_column = dataset['Goals']
sorted_club_data_by_ascending_order = goals_column.groupby(dataset['Club'])
sum_of_goal_by_each_club = sorted_club_data_by_ascending_order.sum()
sorted_goal_values = sum_of_goal_by_each_club.sort_values(ascending = False)
print('Premier league goals of each clubs: ', sorted_goal_values)

#Finding the premier league top goal scorers
epl_top_goals = dataset.sort_values(by = ['Goals'], ascending = False)[:10]
print('Top goal scorer in premier league: ', epl_top_goals)

#Displaying data on a bar graph
fig = px.bar(epl_top_goals, x = 'Name', y = 'Goals', color = 'Goals', hover_data = ['Club', 'Age'], text = 'Goals')
fig.show