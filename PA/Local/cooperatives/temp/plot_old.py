import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from datetime import datetime
import time
import pandas as pd
import traceback
import sys
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np  
import colorobject
import json

plotly_logged = False


def plotly_login(username,api_key):
    tls.set_credentials_file(username, api_key)
    plotly_logged = True
    

def create_data(data):
    
    x_axis = []
    y_axis = []
    
    for key in data:
        x_axis.append(datetime(year=int(key),month=12,day=31))
        y_axis.append(int(data[key]))
        
    
    data = [
        go.Scatter(
            x = x_axis,
            y = y_axis
        )
    ]   
    
    return data
    

def plot_trend(data=None):
    global plotly_logged
    
    
    if plotly_logged == False:
        plotly_login('marannan', 'qj21u6pmzw')
        
    try:
        try:
            x_y = create_data(data)
        except:
            print "error : input data. input data is a dict with key = year and val is value (all are int)"
            return "error : input data. input data is a dict with key = year and val is value (all are int)"
        
        file_name = "trends/" +"trend_" + str(time.strftime("%H:%M:%S")) + "_plotly.png"
        fig = dict( data=x_y)
        py.image.save_as(fig, filename = file_name)
        plot_url = py.plot(x_y, filename = file_name, auto_open = False, fileopt = 'new')
    
        return plot_url, file_name

    except:
        print "error : exiting..."
        print traceback.print_exc(file=sys.stdout)     


def plot_map_plotly(data_file, column_name, sample_size = None):
    global plotly_logged
    
    
    if plotly_logged == False:
        plotly_login('marannan', 'qj21u6pmzw')


    #plot for full data set
    if sample_size == None:
        df = pd.read_csv(data_file, low_memory = False)
     
    #plot for sample size   
    else:
        n = sum(1 for line in open(data_file)) - 1 #number of records in file (excludes header)
        s = sample_size #desired sample size
        skip = sorted(random.sample(xrange(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
        df = pd.read_csv(data_file, skiprows=skip)            

    
    #selecting columns with val more than 0
    df = df[df[column_name] > 0]
    
    df['DESC'] = df['NAME'] + ' ' + df['CITY'] + ', ' + df['STATE'] + ' ' + column_name +' : ' + df[column_name].astype(str)
    
    scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
        [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]
    
    data = [ dict(
            type = 'scattergeo',
            locationmode = 'USA-states',
            lon = df['LONGITUDE'],
            lat = df['LATITUDE'],
            text = df['DESC'],
            mode = 'markers',
            marker = dict( 
                size = 5, 
                opacity = 0.8,
                reversescale = True,
                autocolorscale = False,
                symbol = 'circle',
                line = dict(
                    width=1,
                    color='rgba(102, 102, 102)'
                ),
                colorscale = scl,
                cmin = 0,
                color = df[column_name],
                cmax = df[column_name].max(),
                colorbar=dict(
                    title=column_name
                )
            ))]
    
    layout = dict(
            title = 'Organisations based on ' + column_name,
            #width = 1000,
            #height = 2000,            
            colorbar = True, 
            geo = dict(
                scope='usa',
                projection=dict( type='albers usa' ),
                showland = True,
                landcolor = "rgb(250, 250, 250)",
                subunitcolor = "rgb(217, 217, 217)",
                countrycolor = "rgb(217, 217, 217)",
                countrywidth = 1,
                subunitwidth = 1
            ),
        )
    file_name = "maps/" + column_name + "_map_" + str(time.strftime("%H:%M:%S")) + "_plotly.png"
    fig = dict( data=data, layout = layout)
    py.image.save_as(fig, filename = file_name)
    plot_url = py.plot( fig, validate=False, filename = file_name, auto_open = False, fileopt = 'new', low_memory=False)
    
    
    return plot_url, file_name


def plot_map_matplotlib(data_file, column_name, sample_size = None, marker_size = None):
    
    #plot for full data set
    if sample_size == None:
        df = pd.read_csv(data_file, low_memory = False)
     
    #plot for sample size   
    else:
        n = sum(1 for line in open(data_file)) - 1 #number of records in file (excludes header)
        s = sample_size #desired sample size
        skip = sorted(random.sample(xrange(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
        df = pd.read_csv(data_file, skiprows=skip)            

    
    #selecting columns with val more than 0
    df = df[df[column_name] > 0]
    
    
    #taking lat and log values
    df_lat = df["LATITUDE"]
    df_lon = df["LONGITUDE"]
    df_desc = df['NAME'] + ' ' + df['CITY'] + ', ' + df['STATE'] + ' ' + column_name +' : ' + df[column_name].astype(str)
    
    
    
    lat = df_lat.tolist()
    lon = df_lon.tolist()  
    desc = df_desc.tolist()

    
    data_list = df[column_name].tolist()

    plot_val = []
    
            
    #clean data
    for data in data_list:
        try:
            data = str(data)
            if data == '.' or data == '..' or data == '' or data == ' ' or data == 'nan' or data == 'na':
                #print "warning : not a num " + str(rev)
                plot_val.append(0)
            
            elif '.' in data:
                #print "warning : not a num " + str(rev)
                val = int(data.split('.')[0])
                plot_val.append(val)
                
            else:
                val = int(data)
                
                if val < 0:
                    val = 0
                    
                #if val > 1000000000:
                    #val = 0
                            
                plot_val.append(val)

        except:
            plot_val.append(0)
            
    #plotting       
    try:   
        m = Basemap(projection='merc',llcrnrlat=20,urcrnrlat=50, llcrnrlon=-130,urcrnrlon=-60,lat_ts=20,resolution='c')
        m.drawcoastlines()
        m.drawcountries()
        m.drawstates()
        m.drawmapboundary(fill_color='white') 
        
        title = "Organisations based on " + column_name
        plt.title(title)
        x,y = m(lon, lat)
        cmap = plt.cm.get_cmap('hsv')
        
        try:
            if marker_size == None:
                marker_size = 2
        except:
            marker_size = 2
            
        sc = plt.scatter(x,y, c=plot_val, vmin=0, vmax=None, marker='.', cmap=cmap, s=marker_size, edgecolors='none')
        cbar = plt.colorbar(sc, shrink = .5)
        cbar.ax.set_yticklabels(['>5000','>10000','>50000','>100000','>250000','>500000','>1000000','>10000000','>100000000','>1000000000'])
        cbar.set_label(column_name)
        file_name = "maps/" + column_name + "_map_" + str(time.strftime("%H:%M:%S")) + "_matplotlib.png"
        plt.savefig(file_name,format='eps', dpi=1000)
        plt.show()        
        return file_name

    except:
        print "error : exiting..."
        print traceback.print_exc(file=sys.stdout)
        

    return

def plot_map_bokeh(data_file, column_name, sample_size = None, marker_size = None):
    
    from bokeh.io import output_file, show
    from bokeh.plotting import figure, vplot
    from bokeh.models import (
        GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool,
        GMapPlot, Range1d, ColumnDataSource, LinearAxis, HoverTool, PanTool, WheelZoomTool, BoxSelectTool, 
        ResetTool, PreviewSaveTool, GMapOptions,ResizeTool, NumeralTickFormatter, PrintfTickFormatter, BoxZoomTool
    )  

    style_1 = """
    [{"featureType":"water","elementType":"all","stylers":[{"visibility":"on"},{"lightness":33}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#f2e5d4"}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#c5dac6"}]},{"featureType":"poi.park","elementType":"labels","stylers":[{"visibility":"on"},{"lightness":20}]},{"featureType":"road","elementType":"all","stylers":[{"lightness":20}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"color":"#c5c6c6"}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#e4d7c6"}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#fbfaf7"}]},{"featureType":"water","elementType":"all","stylers":[{"visibility":"on"},{"color":"#acbcc9"}]}]
    """

    style_2 = """
    [{"featureType":"road","elementType":"geometry","stylers":[{"visibility":"off"}]},{"featureType":"poi","elementType":"geometry","stylers":[{"visibility":"off"}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#fffffa"}]},{"featureType":"water","stylers":[{"lightness":50}]},{"featureType":"road","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"transit","stylers":[{"visibility":"off"}]},{"featureType":"administrative","elementType":"geometry","stylers":[{"lightness":40}]}]
    """    
    
    
    map_options = GMapOptions(lat=39.5, lng=-98.35, map_type="satellite", zoom=4, styles = style_2)
    
    plot = GMapPlot(x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options, title="Organisations based on " + column_name, plot_width=1200, plot_height=720)
    
    
    #plot for full data set
    if sample_size == None:
        df = pd.read_csv(data_file, low_memory = False)
     
    #plot for sample size   
    else:
        n = sum(1 for line in open(data_file)) - 1 #number of records in file (excludes header)
        s = sample_size #desired sample size
        skip = sorted(random.sample(xrange(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
        df = pd.read_csv(data_file, skiprows=skip)            

    
    #selecting columns with val more than 0
    df = df[df[column_name] > 0]
    
    
    #taking lat and log values
    df_lat = df["LATITUDE"]
    df_lon = df["LONGITUDE"]
    df_desc = df["EIN"].astype(str) + ' : ' + df['NAME'] + ' : ' + df['CITY'] + ', ' + df['STATE'] + ' : ' + column_name + ' : ' + df[column_name].astype(str)
    
    lat = df_lat.tolist()
    lon = df_lon.tolist() 
    desc = df_desc.tolist()
    
    data_list = df[column_name].tolist()
    
    plot_val = []
    
            
    #clean data
    for data in data_list:
        try:
            data = str(data)
            if data == '.' or data == '..' or data == '' or data == ' ' or data == 'nan' or data == 'na':
                #print "warning : not a num " + str(rev)
                plot_val.append(0)
            
            elif '.' in data:
                #print "warning : not a num " + str(rev)
                val = int(data.split('.')[0])
                plot_val.append(val)
                
            else:
                val = int(data)
                
                if val < 0:
                    val = 0
                    
                #if val > 1000000000:
                    #val = 0
                            
                plot_val.append(val)

        except:
            plot_val.append(0)    

    
    colors = []  
            
    colors_list = ['aqua', 'blue', 'green', 'brown', 'red', 'gold', 'orange', 'black']
    
    for val in plot_val:
        if val < 10000:
            colors.append(colors_list[0])
        elif val < 50000:
            colors.append(colors_list[1])
        elif val < 100000:
            colors.append(colors_list[2])
        elif val < 500000:
            colors.append(colors_list[3])
        elif val < 1000000:
            colors.append(colors_list[4])
        elif val < 100000000:
            colors.append(colors_list[5])
        elif val < 500000000:
            colors.append(colors_list[6])
        elif val < 1000000000:
            colors.append(colors_list[6])
        else:
            colors.append(colors_list[7])
    
    
    source = ColumnDataSource(
        data=dict(
            lat = lat,
            lon = lon,
            desc = desc,
            colors=colors,
            fill=colors,
        )
    )
    
        
    
    circle = Circle(x="lon", y="lat", size=5, fill_color = 'fill', fill_alpha=0.8, line_color='black')
    plot.add_glyph(source, circle)
    

    hover = HoverTool()    
    #hover.tooltips = [('NAME :','@desc')]
    hover.tooltips = '@desc'   
    
    time_stamp = str(time.strftime("%H:%M:%S")).replace(':',"_")
              
    plot.add_tools(hover, PanTool(), WheelZoomTool(), PreviewSaveTool(), ResetTool(), ResizeTool())
    file_name = "maps/core_501c_others_" + column_name.lower() + "_" + time_stamp + ".html"
    output_file(file_name)
    #show(plot)    
    


if __name__ == "__main__":
    #tesing program
    cols = ['OTHSAL', 'COMPENS', 'ASS_EOY', 'TOTREV']

    try:
        col = int(sys.argv[1])

    except:
        col = 0
    
    try:
        sample_size = int(sys.argv[2])
        
    except:
        sample_size = None
        
    try:
        marker_size = int(sys.argv[3])
        
    except:
        marker_size = None
    
    #for col in cols:
    print plot_map_bokeh('/media/ashok/My_Drive/Downloads/NCCS/Core_501(c)_others_with_geo_loc/Core_501(c)_others_all_in_one.csv', cols[col], sample_size, marker_size)
    #print plot_map_plotly('/media/ashok/My_Drive/Downloads/NCCS/Core_501(c)_others_with_geo_loc/Core_501(c)_others_all_in_one.csv', cols[col], sample_size)
    
    
    print "done"