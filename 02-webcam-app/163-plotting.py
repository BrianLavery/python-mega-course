from motion_detector_163 import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

p = figure(x_axis_type = 'datetime', height = 100, width = 500, title = "Motion Graph", sizing_mode = "scale_both")
p.yaxis.minor_tick_line_color = None
# p.ygrid[0].ticker.desired_num_ticks = 1

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds = ColumnDataSource(df)

hover = HoverTool(tooltips = [("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

q = p.quad(left = df["Start"], right = df["End"], bottom = 0, top = 1, color = "green", source = cds)

output_file('./charts/motion_detector_time_plot_hover_datetime.html')
show(p)