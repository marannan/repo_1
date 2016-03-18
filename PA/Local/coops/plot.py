import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from datetime import datetime
import time
import pandas as pd


def create_data(x=None,y=None):
    
    
    if x == None:
        x_axis = [
            datetime(year=2013, month=10, day=04),
            datetime(year=2013, month=11, day=05),
            datetime(year=2013, month=12, day=06)
        ]
        
    else:
        x_axis = []
        for yr in x:
            x_axis.append(datetime(year = yr))
        
    
    if y == None:
        y_axis = [1,2,3,4,5]
        
    
    else:
        y_axis = y
    
    
    data = [
        go.Scatter(
            x = x_axis,
            y = y_axis
        )
    ]    
    
    return data

def create_data_1(data):
    
    x_axis = []
    y_axis = []
    
    for key in data:
        x_axis.append(datetime(year=key,month=12,day=31))
        y_axis.append(data[key])
        
    
    data = [
        go.Scatter(
            x = x_axis,
            y = y_axis
        )
    ]   
    
    return data
    

def plot_graph(data=None):
    sigin_in()
    
    x_y = create_data_1(data)
    
    file_name = "plot_" + str(time.strftime("%H:%M:%S"))
    
    plot_url = py.plot(x_y, filename = file_name, auto_open = False, fileopt = 'new')
    
    return plot_url

#needs to be completed
def plot_map():
    sigin_in()
    df = pd.read_csv('sample.csv')
    df.head()
    
    #df['text'] = df['NAME'] #+ ' ' + df['CITY'] + ', ' + df['STATE'] + ' ' + 'ASSETS: ' + df['ASSETS'].astype(str)
    
    df['text'] = df['NAME'] + ' ' + df['CITY'] + ', ' + df['STATE'] + ' ' + 'ASSETS: ' + df['ASSETS'].astype(str)    
    
    
    scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
        [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]
    
    data = [ dict(
            type = 'scattergeo',
            locationmode = 'USA-states',
            lon = df['LAT'],
            lat = df['LONG'],
            text = df['text'],
            mode = 'markers',
            marker = dict( 
                size = 8, 
                opacity = 0.8,
                reversescale = True,
                autocolorscale = False,
                symbol = 'square',
                line = dict(
                    width=1,
                    color='rgba(102, 102, 102)'
                ),
                colorscale = scl,
                cmin = 0,
                color = df['ASSETS'],
                cmax = df['ASSETS'].max(),
                colorbar=dict(
                    title="Assets in 2013"
                )
            ))]
    
    layout = dict(
            title = 'Assets in 2013',
            colorbar = True,   
            geo = dict(
                scope='usa',
                projection=dict( type='USA' ),
                showland = True,
                landcolor = "rgb(250, 250, 250)",
                subunitcolor = "rgb(217, 217, 217)",
                countrycolor = "rgb(217, 217, 217)",
                countrywidth = 0.5,
                subunitwidth = 0.5        
            ),
        )   
    
    file_name = "plot_" + str(time.strftime("%H:%M:%S"))
    fig = dict( data=data, layout=layout )
    url = py.plot( fig, validate=False, filename = file_name, auto_open = False, fileopt = 'new')
    
    return url


#sample maps plotting
def plot_maps_sample():
    sigin_in()
    
    import plotly.plotly as py
    import pandas as pd
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
    df.head()
    
    df['text'] = df['airport'] + ' ' + df['city'] + ', ' + df['state'] + ' ' + 'Arrivals: ' + df['cnt'].astype(str)
    
    scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
        [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]
    
    data = [ dict(
            type = 'scattergeo',
            locationmode = 'USA-states',
            lon = df['long'],
            lat = df['lat'],
            text = df['text'],
            mode = 'markers',
            marker = dict( 
                size = 8, 
                opacity = 0.8,
                reversescale = True,
                autocolorscale = False,
                symbol = 'square',
                line = dict(
                    width=1,
                    color='rgba(102, 102, 102)'
                ),
                colorscale = scl,
                cmin = 0,
                color = df['cnt'],
                cmax = df['cnt'].max(),
                colorbar=dict(
                    title="Incoming flights February 2011"
                )
            ))]
    
    layout = dict(
            title = 'Most trafficked US airports<br>(Hover for airport names)',
            colorbar = True,   
            geo = dict(
                scope='usa',
                projection=dict( type='albers usa' ),
                showland = True,
                landcolor = "rgb(250, 250, 250)",
                subunitcolor = "rgb(217, 217, 217)",
                countrycolor = "rgb(217, 217, 217)",
                countrywidth = 0.5,
                subunitwidth = 0.5        
            ),
        )
    
    file_name = "plot_" + str(time.strftime("%H:%M:%S"))
    fig = dict( data=data, layout=layout )
    url = py.plot( fig, validate=False, filename = file_name, auto_open = False, fileopt = 'new')
    
    return url 
    
    

def sigin_in():
    tls.set_credentials_file(username='marannan', api_key='qj21u6pmzw')

if __name__ == "__main__":
    sigin_in()
    #print plot_graph(data=None)
    print plot_maps_sample()