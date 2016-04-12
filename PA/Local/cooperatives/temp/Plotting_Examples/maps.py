from bokeh.document import Document
from bokeh.embed import file_html
from bokeh.models.glyphs import Circle
from bokeh.models import (
    GMapPlot, Range1d, ColumnDataSource, LinearAxis,
    PanTool, WheelZoomTool, BoxSelectTool, ResetTool,
    GMapOptions, NumeralTickFormatter, PrintfTickFormatter)
from bokeh.resources import INLINE
from bokeh.io import output_file, show

gmap_options = GMapOptions(lat=30.2861, lng=-97.7394, map_type="roadmap", zoom=13)

x_range = Range1d()
y_range = Range1d()

plot = GMapPlot(
        x_range=x_range, y_range=y_range,
        map_options=gmap_options,
        title = "Austin")


source = ColumnDataSource(
    data=dict(
        lat=[30.2861, 30.2855, 30.2869],
        lon=[-97.7394, -97.7390, -97.7405],
        fill=['orange', 'blue', 'green']
    )
)

circle = Circle(x="lon", y="lat", size=15, fill_color="fill", line_color="black")
plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), ResetTool())

xaxis = LinearAxis(axis_label="lat", major_tick_in=0, formatter=NumeralTickFormatter(format="0.000"))
plot.add_layout(xaxis, 'below')

yaxis = LinearAxis(axis_label="lon", major_tick_in=0, formatter=PrintfTickFormatter(format="%.3f"))
plot.add_layout(yaxis, 'left')

show(plot)