import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

#Reading the CSV
dataset = pd.read_csv('projectC234_EPL.csv')

football_club = dataset['Club'].value_counts().head(20)
print('Top 20 clubs with maximum penalty accuracy premium league: \n', football_club)

club_fig = go.Figure(data = [go.Pie(labels = football_club.index, values = football_club.values, hole = 0.5)])
club_fig.show()
