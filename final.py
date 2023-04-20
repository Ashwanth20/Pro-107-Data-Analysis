import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
student_df = df.loc[df['student_id'] == "TRL_987"]
print(df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Scatter(
    x = df.groupby("level")["attempt"].mean(),
    y = ['Level 1', 'Level 2', 'Level 3', ' Level 4'],
    orientation = 'h'))
fig.show()