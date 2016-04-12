#plotting year wise trends based input data
#input data must a dict with key = year and val is value (all are int)
def plot_trend_plotly(data):
    #plotly signin
    tls.set_credentials_file(marannan, 'qj21u6pmzw')
        
    try:
        x_axis = []
        y_axis = []
        
        for key in data:
            x_axis.append(datetime(year=int(key),month=12,day=31))
            y_axis.append(int(data[key]))
            
        
        data_plotly = [
            go.Scatter(
                x = x_axis,
                y = y_axis
            )
        ]               

    except:
        print "error : input data must a dict with key = year and val is value (all are int)"
        print traceback.print_exc(file=sys.stdout)
        return traceback.print_exc(file=sys.stdout)  
        
    try:
        file_name = "trends/" +"trend_" + str(time.strftime("%H:%M:%S")) + "_plotly.png"
        fig = dict( data=data_plotly)
        py.image.save_as(fig, filename = file_name)
        plot_url = py.plot(data_plotly, filename = file_name, auto_open = False, fileopt = 'new')
    
        return plot_url, file_name

    except:
        print "error : plotting"
        print traceback.print_exc(file=sys.stdout)
        return traceback.print_exc(file=sys.stdout)
                                  


#plotting on google maps based on lat and long values from zip codes
#data_file = file with "LATITUDE" and "LONGITUDE" columns
#column_name = colring the data points
#sample_size = sample no of rows from data_file for plotting
#marker_size = size of point (1-500)
import pandas as pd
data_read = False
data_df = pd.DataFrame

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
    from bokeh.resources import CDN
    from bokeh.embed import file_html    
    from bokeh.models import (
        GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool,
        GMapPlot, Range1d, ColumnDataSource, LinearAxis, HoverTool, PanTool, WheelZoomTool, BoxSelectTool, 
        ResetTool, PreviewSaveTool, GMapOptions,ResizeTool, NumeralTickFormatter, PrintfTickFormatter, BoxZoomTool
    ) 
    
    global data_read, data_df
    
    #args validation
    if os.path.isfile(data_file) == False:
        print "error : file not found"
        print traceback.print_exc(file=sys.stdout)
        return traceback.print_exc(file=sys.stdout)  
    
    years = range(1900,2100)
    year = 'all'
    for yr in years:
        if str(yr) in data_file:
            year = str(yr)
        
    try:
        #read data from file
        if data_read == False:
            
            #plot for full data set
            if sample_size == None or sample_size == 'all':
                sample_size = "all"
                df = pd.read_csv(data_file, low_memory = False)
             
            #plot for sample size   
            else:
                n = sum(1 for line in open(data_file)) - 1 #number of records in file (excludes header)
                s = sample_size #desired sample size
                skip = sorted(random.sample(xrange(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
                df = pd.read_csv(data_file, skiprows=skip, low_memory = False)  
            
            data_df = df
            data_read = True
                
        else:
            df = data_df
    
        
        #selecting rows with column_value more than 0
        #print "total no of rows : " + str(len(df))
        #df = df[df[column_name] != 0]
        #df = df[df[column_name] != 0.0]
        #df = df[df[column_name].astype(str) != '0']
        #df = df[df[column_name].astype(str) != '0.0']
        #df = df[df[column_name].astype(str) != '.']
        #df = df[df[column_name].astype(str) != 'nan']
        #df = df[df[column_name].astype(str) != '']
        #print "total no of rows after cleaning: " + str(len(df))
        
        #taking lat and log values from the data from plotting on map
        df_lat = df["LATITUDE"]
        df_lon = df["LONGITUDE"]
        
        #creating description for each points when mouse pointer is hovered over
        #check year column is available
        try:
            df_year = df['YEAR']
        except:
            df['YEAR'] = str(year)
            
        df_desc = df["EIN"].astype(str) + ' : ' + df['NAME'] + ' : ' + df['CITY'] + ', ' + df['STATE'] + ' : ' + df['YEAR'].astype(str) + ' : ' + column_name + ' : ' + df[column_name].astype(str)
    
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
        data_list = df[column_name].astype(str).tolist()
        
        #cleaned up data for coloring the points on map
        plot_val = []    
                
        #cleaning data. convert all values to int if possible
        for data in data_list:
            #check if data is an int val
            try:
                val = int(data)            
            except:
                #check if data is float val
                try:
                    val = float(data)
                    val = int(val)
                except:
                    #data is not int or float, thats okay add to the list.
                    val = data
            
            plot_val.append(val)
            

   
        #creating color_list for corresponding data list
        colors = []       
        colors_list = ['aquamarine', 'aqua', 'blue', 'blueviolet', 'brown', 'chartreuse', 'deeppink',
                       'magenta', 'forestgreen', 'yellow', 'red', 'gold', 'orange', 'black', 'wheat']
    
        for val in plot_val:
            try:
                val = int(val)
                if val == 0:
                    colors.append(colors_list[0])
                elif val < 5000:
                    colors.append(colors_list[1])
                elif val < 10000:
                    colors.append(colors_list[2])
                elif val < 100000:
                    colors.append(colors_list[3])
                elif val < 500000:
                    colors.append(colors_list[4])
                elif val < 1000000:
                    colors.append(colors_list[5])
                elif val < 10000000:
                    colors.append(colors_list[6])
                elif val < 25000000:
                    colors.append(colors_list[7])
                elif val < 50000000:
                    colors.append(colors_list[8])
                elif val < 100000000:
                    colors.append(colors_list[9])
                elif val < 250000000:
                    colors.append(colors_list[10])
                elif val < 500000000:
                    colors.append(colors_list[11])
                elif val < 1000000000:
                    colors.append(colors_list[12])
                else:
                    colors.append(colors_list[13])
            
            except:
                colors.append(colors_list[14])

    except:
        print "error : creating data for plotting"
        print traceback.print_exc(file=sys.stdout)
        return traceback.print_exc(file=sys.stdout)  
    

    #print column_name
    #for color in colors_list:
        #print color + " : " + str(colors.count(color))
 
    #if 1:
        #return

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
        title = "Core_501(c)_other_" + str(year) + " : " +" Organisations based on " + column_name
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
        
        circle = Circle(x="lon", y="lat", size = marker_size, fill_color = 'fill', fill_alpha=0.8, line_color=None)
        plot.add_glyph(source, circle)
        hover = HoverTool()    
        #hover.tooltips = [('NAME :','@desc')]
        hover.tooltips = '@desc'   
        plot.add_tools(hover, PanTool(), WheelZoomTool(), PreviewSaveTool(), ResetTool(), ResizeTool())
        
        time_stamp = str(time.strftime("%H:%M:%S")).replace(':',"_")
        
        if year == None:
            year = 'no_year'
            
        plot_file_name = "maps/core_501c_others_" + year + "_" + column_name.lower() + "_" + "sample_size_" + str(sample_size) + "_time_" + time_stamp + ".html"
        #output_file(plot_file_name,title=title)
        #show(plot)
        plot_html = file_html(plot, CDN, title)
        plot_file = open(plot_file_name, mode='w')
        plot_file.write(plot_html)
        
    except:
        print "error : plotting"
        print traceback.print_exc(file=sys.stdout)
        return traceback.print_exc(file=sys.stdout)            
    

    return plot_file_name

#tesing program
if __name__ == "__main__":
    import sys
    import time
    import os
    
    cols = ['OTHSAL', 'COMPENS', 'ASS_EOY', 'TOTREV']
    data_path = '/media/ashok/My_Drive/Downloads/NCCS/Core_501(c)_others_with_geo_loc/'
    
    
    data_files = os.listdir(data_path)

    try:
        year = str(sys.argv[1])
        for file in data_files:
            if year in file:
                data_file = data_path + file
                break
    except:
        for file in data_files:
            if "all" in file:
                data_file = data_path + file
                break
    
    try:
        
        sample_size = sys.argv[2]
        if sample_size == 'all':
            pass
        else:
            sample_size = int(sample_size)
        
    except:
        sample_size = 'all'
        
    try:
        marker_size = int(sys.argv[3])
        
    except:
        marker_size = 5
    
    #print "plotting : " + 'TOTREV'
    #print plot_map_bokeh(data_file, 'TOTREV', sample_size, marker_size)
    #print "done"    
    
    for col in cols:
        print "plotting : " + col
        print plot_map_bokeh(data_file, col, sample_size, marker_size)
        print "done"
        time.sleep(5)
    
  
    print "all done"