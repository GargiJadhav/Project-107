import pandas as pd
import plotly.express as pe

data = pd.read_csv("Data.csv")

mean = data.groupby(["student_id", "level"], as_index = False)["attempt"].mean()

fig = pe.scatter(mean, x="student_id", y = "level", size="attempt", color="attempt")

fig.show()