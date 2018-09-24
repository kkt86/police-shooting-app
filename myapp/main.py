from os.path import dirname, join
import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import layout, widgetbox
from bokeh.models import ColumnDataSource, Div
from bokeh.models.widgets import RangeSlider, MultiSelect, Select
from bokeh.plotting import figure
from bokeh.transform import factor_cmap


def load_data():
    data = pd.read_csv("data/PoliceKillingsUS.csv", encoding="ISO-8859-1")
    data["year"] = data.date.apply(lambda x: int("20{}".format(x.split("/")[-1])))
    return data


def prepare_data(data):
    aggregated_data = data.groupby("state").agg("size")
    states = aggregated_data.index.tolist()
    counts = [x for x in aggregated_data]
    return states, counts


data = load_data()

states, counts = prepare_data(data)
source = ColumnDataSource(data=dict(states=states, counts=counts))

# input controls
year = RangeSlider(title="Year", start=data.year.min(), end=data.year.max(), value=(data.year.min(), data.year.max()))
age = RangeSlider(title="Age", start=data.age.min(), end=data.age.max(), value=(data.age.min(), data.age.max()))
manner_of_death = Select(title="Manner of death", value="All", options=["All"] + data.manner_of_death.unique().tolist())
armed = Select(title="Armed", value="All", options=["All"] + data.armed.dropna().unique().tolist())
gender = Select(title="Gender", value="All", options=["All"] + data.gender.dropna().unique().tolist())
race = Select(title="Race", value="All", options=["All"] + data.race.dropna().unique().tolist())
threat_level = Select(title="Threat level", value="All", options=["All"] + data.threat_level.dropna().unique().tolist())
flee = Select(title="Flee", value="All", options=["All"] + data.flee.dropna().unique().tolist())

controls = [year, age, manner_of_death, armed, gender, race, threat_level, flee]
sizing_mode = 'fixed'  # 'scale_width' also looks nice with this example
inputs = widgetbox(*controls, sizing_mode=sizing_mode)

p = figure(x_range=states, plot_height=350, plot_width=1000, toolbar_location=None, title="States counts")
p.vbar(x='states', top='counts', width=0.9, source=source)

# p = figure(plot_height=600, plot_width=700, title="", toolbar_location=None)
l = layout([
    [inputs, p],
], sizing_mode=sizing_mode)

curdoc().add_root(l)
