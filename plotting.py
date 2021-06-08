#Import libraries
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
from datetime import datetime as dt
from motion_detector import df

#Create two new columns to store the start and end times as strings
#This is to display them in the correct format in the hovertool
df['start_str'] = df['Start'].dt.strftime("%Y-%m-%d %H:%M:%S")
df['end_str'] = df['End'].dt.strftime("%Y-%m-%d %H:%M:%S")
#Give the entire dataframe to the CDS Object
cds = ColumnDataSource(df)

#Create a figure object for the graph and give it certain properties
fig = figure(x_axis_type='datetime', height=315, width=1600, title="Motion Graph")
#Remove divisions on y axis and remove grid layout
fig.yaxis.minor_tick_line_color = None
fig.ygrid[0].ticker.desired_num_ticks = 1

#Create hovertool to display start and end time of motion
hover = HoverTool(tooltips=[("Start","@start_str"),("End","@end_str")])

#Add the hovertool to the graph
fig.add_tools(hover)

#Create a quad graph and give it the data to be plotted
#Top and bottom is 1 and 0 because 1 -> movement 0-> no movement
#The other two parameters are the names of the columns in the dataframe
quad_graph = fig.quad(left='Start', right='End', bottom=0, top=1, color="green", source=cds)

#Create the output file
output_file("motion_graph.html")
show(fig)