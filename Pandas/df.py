# Create a simple Pandas DataFrame:

import pandas as pd

data = {
  "calories" : [200, 400, 230],
  "duration" : [23, 45, 30]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)
print(df.loc[["day1", "day2"]])