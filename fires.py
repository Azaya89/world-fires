import csv
from plotly.graph_objects import Layout
from plotly import offline
from datetime import datetime


filename = "global_fires_7d.csv"

# Open file in python csv-readable format
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    ## Print header rows
    # for i,r in enumerate(header_row):
    #     print(i,r)

    # Get details for the plot
    lats, lons, brights, dates = [], [], [], []
    for row in reader:
        date = datetime.strptime(row[5], "%Y-%m-%d")
        lats.append(row[0])
        lons.append(row[1])
        brights.append(float(row[2]))
        dates.append(date)

# Design and plot data
data = [
    {
        "type": "scattergeo",
        "lat": lats,
        "lon": lons,
        "text": dates,
        "marker": {
            "size": [bright / 20 for bright in brights],
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Intensity"},
        },
    }
]

my_layout = Layout(title=f"Fires around the world from {dates[0]} to {dates[-1]}")

fig = {"data": data, "layout": my_layout}
offline.plot(fig)
