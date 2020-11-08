
import matplotlib.pyplot as plt
import math
import pandas as pd

map = pd.read_csv('/Users/williamjames/Documents/343 Data/data_ch4/us_outline.csv')
df = pd.read_csv('/Users/williamjames/Documents/343 Data/data_ch4/data.csv')

dist = []
_approx = []
values = []
x_pt = []
y_pt = []
k = 5
for row in range(0, 121):  # Y coord
    for col in range(0, 195):  # X coord
        for i in range(0, len(df)):
            _dist = math.sqrt(math.pow(col - df.x[i], 2) + math.pow(row - df.y[i], 2))
            dist.append(_dist)
            _approx.append(df.move[i])
        neighbors = pd.DataFrame({'Distance': dist, 'Value': _approx})
        neighbors = neighbors.sort_values('Distance')
        new_val = neighbors.Value[0:k].mean()
        values.append(new_val)
        x_pt.append(col)
        y_pt.append(row)
        dist.clear()
        _approx.clear()
        neighbors.drop(neighbors.index, inplace=True)

fig, ax = plt.subplots(figsize=(12, 10))

plt.plot(map.x, map.y)

plt.scatter(x_pt, y_pt, c=values)
