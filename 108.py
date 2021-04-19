import csv
import plotly.figure_factory as ff
import plotly_express as px
import pandas as pd
df = pd.read_csv("data-108.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Avg.rating of mobiles"])
fig.show()