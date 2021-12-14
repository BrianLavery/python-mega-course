# Only works with actual webcam
# Can't have a filename begin with a number

from motion_detector_162 import df

from bokeh.plotting import figure, show, output_file

p = figure(x_axis_type = 'datetime', height = 100, width = 500, title = "Motion Graph", sizing_mode = "scale_both")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

q = p.quad(left = df["Start"], right = df["End"], bottom = 0, top = 1, color = "green")

output_file('./charts/motion_detector_time_plot.html')
show(p)