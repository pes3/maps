# to be finalized
import plotly

import plotly.plotly as py
import plotly.figure_factory as ff
import numpy as np
import pandas as pd
import xlrd
df_sample = pd.read_excel('popdata.xlsx') # Read in your data
values = df_sample['Change'].tolist() # Read in the values contained within your file
fips = df_sample['FIPS'].tolist() # Read in FIPS Codes

colorscale = ["#171c42","#223f78","#1267b2","#4590c4","#8cb5c9","#b6bed5","#dab2be",
              "#d79d8b","#c46852","#a63329","#701b20","#3c0911"]

endpts = list(np.linspace(-75, 75, len(colorscale) - 1)) # Identify a suitable range for your data

fig = ff.create_choropleth(
   fips=fips, values=values, colorscale=colorscale, show_state_data=True, binning_endpoints=endpts, # If your values is a list of numbers, you can bin your values into half-open intervals
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5}, 
    legend_title='% change', title='% Change in disease between 1980-2014'
)
py.plot(fig, filename='diseasechange')
