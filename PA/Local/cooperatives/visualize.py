#plotting on google maps based on lat and long values from zip codes
#data_file = file with "LATITUDE" and "LONGITUDE" columns
#column_name = colring the data points
#sample_size = sample no of rows from data_file for plotting
#marker_size = size of point (1-500)
def plot_map_bokeh(data_file, column_name, sample_size = None, marker_size = 2):
    
    #imports
    from datetime import datetime
    import time
    import pandas as pd
    import traceback
    import sys 
    import os
    import random
    from bokeh.io import output_file, show
    from bokeh.plotting import figure, vplot
    from bokeh.models import (
        GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool,
        GMapPlot, Range1d, ColumnDataSource, LinearAxis, HoverTool, PanTool, WheelZoomTool, BoxSelectTool, 
        ResetTool, PreviewSaveTool, GMapOptions,ResizeTool, NumeralTickFormatter, PrintfTickFormatter, BoxZoomTool
    ) 

    #args validation
    if os.path.isfile(data_file) == False:
        print "error : file not found"
        print traceback.print_exc(file=sys.stdout)
        return traceback.print_exc(file=sys.stdout)  

    if sample_size < -1:
        sample_size = None
    
    try:
        int(sample_size)
    
    except:
        sample_size = None

    if marker_size < -1:
        marker_size = 2
            
    try:
        int(marker_size)
    
    except:
        marker_size = 2


    
    try:
        #read data from file
        #plot for full data set
        if sample_size == None:
            sample_size == "all"
            df = pd.read_csv(data_file, low_memory = False)
         
        #plot for sample size   
        else:
            n = sum(1 for line in open(data_file)) - 1 #number of records in file (excludes header)
            s = sample_size #desired sample size
            skip = sorted(random.sample(xrange(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
            df = pd.read_csv(data_file, skiprows=skip)            
    
        
        #selecting rows with column_value more than 0
        #df = df[df[column_name] > 0]
        
        
        #taking lat and log values from the data from plotting on map
        df_lat = df["LATITUDE"]
        df_lon = df["LONGITUDE"]
        
        #creating description for each points when mouse pointer is hovered over
        df_desc = df["EIN"].astype(str) + ' : ' + df['NAME'] + ' : ' + df['CITY'] + ', ' + df['STATE'] + ' : ' + column_name + ' : ' + df[column_name].astype(str)
    
    except:
        print "error : reading data file"
        print traceback.print_exc(file=sys.stdout)
        return traceback.print_exc(file=sys.stdout)
    
    
    try:
        #creating plot data lists
        lat = df_lat.tolist()
        lon = df_lon.tolist() 
        desc = df_desc.tolist()
        
        #creating data for coloring the points on map
        data_list = df[column_name].tolist()
        
        #cleaned up data for coloring the points on map
        plot_val = []    
                
        #cleaning data
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
                        
                    plot_val.append(val)
    
            except:
                plot_val.append(0)    

   
            #creating color_list for corresponding data list
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

    except:
        print "error : creating data for plotting"
        print traceback.print_exc(file=sys.stdout)
        return traceback.print_exc(file=sys.stdout)            
    
    
    try:
        #plotting starts
        #google map layout styles for rendering #more styles can be found at https://snazzymaps.com/ just copy the JavaScript Style Array from a style page
        style_1 = """
        [{"featureType":"water","elementType":"all","stylers":[{"visibility":"on"},{"lightness":33}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#f2e5d4"}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#c5dac6"}]},{"featureType":"poi.park","elementType":"labels","stylers":[{"visibility":"on"},{"lightness":20}]},{"featureType":"road","elementType":"all","stylers":[{"lightness":20}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"color":"#c5c6c6"}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#e4d7c6"}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#fbfaf7"}]},{"featureType":"water","elementType":"all","stylers":[{"visibility":"on"},{"color":"#acbcc9"}]}]
        """
    
        style_2 = """
        [{"featureType":"road","elementType":"geometry","stylers":[{"visibility":"off"}]},{"featureType":"poi","elementType":"geometry","stylers":[{"visibility":"off"}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#fffffa"}]},{"featureType":"water","stylers":[{"lightness":50}]},{"featureType":"road","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"transit","stylers":[{"visibility":"off"}]},{"featureType":"administrative","elementType":"geometry","stylers":[{"lightness":40}]}]
        """    
        
        #defining map positing, zoom and layout style
        map_options = GMapOptions(lat=39.5, lng=-98.35, map_type="satellite", zoom=4, styles = style_2)
    
        #creating a plot over google maps
        title = "Core_501(c)_other : Organisations based on " + column_name
        width = 1400
        height = 900
        plot = GMapPlot(x_range = DataRange1d(), y_range = DataRange1d(), map_options = map_options, title = title, plot_width = width, plot_height = height)        
        
        
        #creating data soruce for plotting
        source = ColumnDataSource(
            data=dict(
                lat = lat,
                lon = lon,
                desc = desc,
                colors=colors,
                fill=colors,
            )
        )
        
            
        
        circle = Circle(x="lon", y="lat", size = marker_size, fill_color = 'fill', fill_alpha=0.8, line_color='black')
        plot.add_glyph(source, circle)
        hover = HoverTool()    
        #hover.tooltips = [('NAME :','@desc')]
        hover.tooltips = '@desc'   
        plot.add_tools(hover, PanTool(), WheelZoomTool(), PreviewSaveTool(), ResetTool(), ResizeTool())
        
        print type(plot)
        
        time_stamp = str(time.strftime("%H:%M:%S")).replace(':',"_")                  
        file_name = "maps/core_501c_others_" + column_name.lower() + "_" + "sample_size_" + str(sample_size) + "_time_" + time_stamp + ".html"
        
        output_file(file_name,title=title)
        show(plot)
        
    except:
        print "error : plotting"
        print traceback.print_exc(file=sys.stdout)
        return traceback.print_exc(file=sys.stdout)            
    

    return file_name

#tesing program
if __name__ == "__main__":
    import sys
    cols = ['OTHSAL', 'COMPENS', 'ASS_EOY', 'TOTREV']
    
    try:
        sample_size = int(sys.argv[1])
        
    except:
        sample_size = None
        
    try:
        marker_size = int(sys.argv[2])
        
    except:
        marker_size = None
    
    
    for col in cols:
        print plot_map_bokeh('/media/ashok/My_Drive/Downloads/NCCS/Core_501(c)_others_with_geo_loc/Core_501(c)_others_all_in_one.csv', col, sample_size, marker_size)
    
  
    print "done"