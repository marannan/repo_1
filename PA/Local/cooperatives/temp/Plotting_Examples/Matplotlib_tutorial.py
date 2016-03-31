
# coding: utf-8

# # Welcome to the PyLadies Workshop on IPython Notebook and Matplotlib!
# ## Presenters:  Mark Blunk and Gina Schmalzle
# 
# This is part 2 of the workshop -- getting started with Matplotlib presented by Gina Schmalzle.
# In this part of the workshop we will learn how to make:
# 1. Scatter Plots -- we will also learn how to change the attributes of the scatterplot.
# 2. Histograms -- we will play around with how these look too.
# 3. Maps!  We will also learn how to put data on maps too.
# 
# At the end will be time to experiment with plotting yourself, play around with the code, ask questions or whatever!
# 
# # The Data 
# I thought it would be fun to work with real data instead of some randomly generated data.  The data we will use are modeled weather forecasts at weather stations across the United States.  This information is presented on the [OpenWeatherMap project](http://openweathermap.org/) who provides an API service to download this information, but unfortunately, does not keep a historical record of the forecasts.  Gina and her friend David Branner created a [database](https://github.com/WeatherStudy/weather_study) that collects the weather forecasts for these stations.  The file target_day_20140422.dat that came in this repo was extracted from this database collecting the forecasts.  It is a flat file of weather forecasts for each station in the United States for the 'target day' of April 22, 2014. The stations themselves are defined by their latitude and longitude and the file contains forecasts that were done 0 to 7 days out, where day zero is the forecast made on April 22.  Hence a forecast made one day out was made on April 21, two days out April 20th, etc. 
# 
# # Getting to the Basics -- Data Structures
# A basic understanding of data structures is useful when playing with an visualizing data, so we will go over some data structures that will be used in this notebook.  In computer science, a data structure is a way to organize data in a computer that makes it computationally efficient.  Here we will be using two basic data structures:  *lists* and *dictionaries*.  
# 
# ### Lists 
# Lists represent a sequence of values.  In python a list is designated with square brackets [].  The following are examples of lists.

# In[20]:

a = []
b = ['a', 'b', 'c']
c = [4,1,6,9,2,10]
d = [[1,2,3],['a','n','q']]


# The items in these lists are called elements.  You can figure out how many elements are in these lists by asking for its length:

# In[21]:

print (len(d))


# How many elements does d have? Make a guess, then change the cell above to find out. 
# 
# The example d above has a list as an element.  This is called a list of lists.  
# 
# So how do you retrieve an element of a list? Each element is assigned a number, starting at 0, that represents where it sits in the list.  For example, element 0 of b is 'a'.  It can be retrieved like this:

# In[22]:

b[0]


# What is c[4]?  How about d[2]?  
# 
# Great things about lists are that they are very simple to understand, and they take up relatively little amounts of memory. However they do have some limitations.  Say if you have a long list of values, but you wanted to see if a certain value is in the list.  You potentially would have to read through all the items in the list in order to see if it is in there.  Hence, it can be computationally slow.  
# 
# ### Dictionaries
# 
# Also known as associative arrays, maps, symbol tables, or hash tables, this data structure is really computationally fast, but uses lots of memory.  A dictionary consists of key-value pairs, where the keys are all unique and refer to a specific value.  Values among the keys can be identical, however.  Dictionaries are designated with curly brackets {}.  Here are examples of dictionaries:

# In[23]:

dict_a = {}
dict_b = {'Hello beautiful': 'Ew, Gross', 'Goodbye Gorgeous':'Finally'}
dict_c = {'Bad Pickup Lines': {'example 1': 'Did it hurt when you fell from heaven?',
                               'example 2': 'Do you alway wear your shoes over your socks?'
                              }}


# Each of these listed above are dictionaries.  The items to the left of the colon are the 'keys', and the items to the right are values.  If you want to list the keys you can type:

# In[24]:

dict_b.keys()


# And you can retrieve their values by typing:

# In[25]:

dict_b['Goodbye Gorgeous']


# dict_c is a dictionary of dictionaries.  How would you get the value for 'example 2'? Try in the next cell. 

# In[ ]:




# The great thing about dictionaries is that we can have a lot of data, but if we know the key, we can very quickly get the associated values.
# 
# OK - now let's put what we've learned to good use and start our Matplotlib adventure!
# 
# # Retrieving the data 

# Let's Read in the data.  These 'data' are actually weather forecasts (modeled) for individual weather stations across the United States. The file that will be read contains the forecast for one day (April 22, 2014) for 0 to 7 days out, where the 0th day is the forecast on April 22nd.    

# In[26]:

# Read file
filename='target_day_20140422.dat'
f = open(filename, 'r')
contents = f.readlines()


# In[27]:

contents


# Let's make a dictionary of values, where lat, long are the keys.  The values are also dictionaries, where the number of days out are the keys, and MaxT and MinT are the values.

# In[28]:

forecast_dict = {}
for line in range(1, len(contents)):
    line_split = contents[line].split(' ')
    try:
        forecast_dict[line_split[0], line_split[1]][line_split[2]] = {'MaxT':float(line_split[3]),
                                                                      'MinT':float(line_split[4][:-1])}
    except:
        forecast_dict[line_split[0], line_split[1]] = {}
        forecast_dict[line_split[0], line_split[1]][line_split[2]] = {'MaxT':float(line_split[3]),
                                                                      'MinT':float(line_split[4][:-1])}


# In[29]:

forecast_dict


# ### Why did we need to put these values into a somewhat complicated data structure?
# It will make it easier to retrieve the value for a specific forecasted day out. 
# 
# Also note that you could use other data structures with this -- your could use lists, or maybe use a dataframe (from the pandas module), the point is to try computationally to make different aspects of the data easily accessible.
# 
# Let's take a look at some things here.  Keys are all for an individual weather stations, defined by their location:

# In[30]:

forecast_dict.keys()


# Let's pick a random station, and see what its values are:

# In[31]:

forecast_dict[('40.51218', '-111.47435')]


# The output above shows the forecasted Max T and Min T values for 0-7 days out for a specific station at Latitude 40.51218N, Longitude -111.47435E.

# # Prepare our data for Plotting  
# The plot will be Max T vs. day out for this one station.  It will be a simple plot, but first, we need to make some lists that matplotlib can use to do the plotting.  We will need a list of days, and a list of corresponding Max T values.

# In[32]:

# First retrieve the days 
day_keys  = forecast_dict[('40.51218', '-111.47435')].keys()
print (day_keys)


# Dictionaries don't necessarily sort alphabetically or numerically.  
# For fun, now that we have a list of keys, let's sort them.

# In[33]:

day_keys.sort()


# Matplotlib plots lists of one thing against another.  So, let's make our lists.
# First define our lists

# In[34]:

# First define the variables as lists
day_list = []; maxt_list = []

# Then populate the lists
for day_key in day_keys:
    day_list.append(float(day_key))
    maxt_list.append(float(forecast_dict[('40.51218', '-111.47435')][day_key]['MaxT']))

# Now the element in one list corresponds with an element in the other list, for a given 
# element number.  For example day_list[0] corresponds to maxt_list[0]
print (day_list)
print (maxt_list)


# # Time to Plot!  General Scatter Plots
# First let's import everything we will need.

# In[35]:

get_ipython().magic('matplotlib inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np


# We also want to modify some of the default values for plotting.  The default parameters are found in Matplotlib's RC file.  The values are collected into a dictionary that you can access by typing:

# In[ ]:

mpl.rcParams.keys()


# And you can see the value using the keys.  For example, if you want the resolution of your figure you would type:

# In[ ]:

mpl.rcParams[u'figure.dpi']


# So let's ensure that our plots have good resolution and are fairly sizeable:

# In[ ]:

mpl.rcParams[u'figure.figsize'] = [12, 8]
mpl.rcParams[u'figure.dpi'] = 300


# Now let's make our first scatter plot!

# In[ ]:

plt.scatter(day_list, maxt_list)
# Add a line:
# plt.plot(day_list, maxt_list)


# Now let's jazz is up a bit -- 
# Let's Make the lines red and dashed and change the size of the circles, change them to stars and make them green

# In[ ]:

plt.plot(day_list, maxt_list, '.r--')
plt.scatter(day_list, maxt_list, s = 400, color='green', marker='*')
plt.show()


# Labels, labels, labels!  How is one to know what you just plotted?  Let's add the axes labels and the title

# In[ ]:

plt.plot(day_list, maxt_list, '.r--')
plt.scatter(day_list, maxt_list, s = 400, color='green', marker='*')
plt.ylabel ('Forecasted Max Temperature, Deg F')
plt.xlabel ('Days from Target day April 22, 2014')
plt.title ('Forecasted Max Temperature')
plt.show()


# More marker fun can be found [here](http://matplotlib.org/api/markers_api.html).  More line fun can be found [here](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot).

# Getting the idea?
# 
# Let's do another plot.  Let's look at all of the Max Temperature forecasts 2 days out, and plot them with respect to Latitude.  We will need to pick out from forecast_dict all the Max T values for all of the weather stations made 2 days before April 22, 2014.  First, we will need to get all the Latitudes and Longitudes for each site, then we will need to pick out all the Max T values for each of the stations for that day.  
# 
# We will keep in mind that maybe in the future you might want to look at Min T, or a different day.

# In[ ]:

# Get keys of forecast_dict (lats and longs):
keys = forecast_dict.keys()
# Circle through all the keys to get the values for the 2nd day maximum temperature and the
# corresponding Lat and Longs
day_out = '2'       # 0-7
temp = 'MaxT'  # MaxT or MinT
temperature = []; lat = []; lon = []
for key in keys:
    temperature.append(float(forecast_dict[key][day_out][temp]))
    lat.append(float(key[0]))
    lon.append(float(key[1]))
# Now that those are collected, let's see what the Temperature as a function of Latitude is:
plt.scatter(temperature,lat)


# # Coloring Points in a Scatter Plot
# Let's try again, but this time, color according to Longitude.  Again, let's keep in mind we may want to color by something else.  You can try playing with these later.

# In[ ]:

color_by = lon
label = 'Long'  # Need to rename if 'color_by' is changed
max_color_by = max(color_by)
min_color_by = min(color_by)

fig, ax = plt.subplots()
s = ax.scatter(temperature, lat,   
               c=color_by, 
               s=200, 
               marker='o',                   # Plot circles
              # alpha = 0.2,
               cmap = plt.cm.coolwarm,       # Color pallete
               vmin = min_color_by,          # Min value  
               vmax = max_color_by)          # Max value

cbar = plt.colorbar(mappable = s, ax = ax)   # Mappable 'maps' the values of s to an array of RGB colors defined by a color palette
cbar.set_label(label)
plt.xlabel('{0} in Deg F, forecasted {1} days out'.format(temp,day_out))
plt.ylabel('Latitude, Deg N')
plt.title('{0} forecasted {1} Days out from target day April 22, 2014'.format(temp,day_out))
plt.show()


# Color map stuff can be found here: http://matplotlib.org/users/colormaps.html
# 
# # Histograms!
# Let's take a step back and work on a histogram.
# What we are going to plot is the distribution of forecasted temperatures.
# Let's start with a very simple histogram of the temperature we left off with -- 

# In[ ]:

plt.hist(temperature)
plt.ylabel ('Counts')
plt.xlabel(temp)
plt.show()


# Now let's try again and jazz it up..
# Let's increase the number of bins (bin size calculated by the difference Min and Max values, divided by the number of bins). Let's also change the color of the bars and make them a little translucent.

# In[ ]:

plt.hist(temperature, 100, color='green', alpha=0.2)
plt.ylabel ('Counts')
plt.xlabel(temp)
plt.title('Histogram of {0}'.format(temp))
plt.show()


# Python histograms give you some information about them.  Let's explore.

# In[ ]:

n, bins, patches = plt.hist(temperature, 10, color='green', alpha=0.2)


# In[ ]:

# n are the number of counts
n


# In[ ]:

# bins are the x-centered location of the bins
bins


# In[ ]:

# And patches are a list of the matplotlib rectangle shapes that make 
# the bins.
patches


# In[ ]:

patches[0]


# # Mapping
# Now that we have the basics down, let's start with the mapping!
# We will be using Matplotlib's basemap:  http://matplotlib.org/basemap/.  Basemap was imported in the second cell of this notebook.
# 
# Let's make a simple Mercator Projection Map.  The code in the next cell is straight from the Basemap example section -- http://matplotlib.org/basemap/users/merc.html
# 
# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon are the lat/lon values of the lower left and upper right corners of the map.
# lat_ts is the latitude of true scale.
# resolution = 'c' means use crude resolution coastlines.

# In[ ]:

# Define the projection, scale, the corners of the map, and the resolution.
m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,            llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
# Draw the coastlines
m.drawcoastlines()
# Color the continents
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))
# fill in the oceans 
m.drawmapboundary(fill_color='aqua')
plt.title("Mercator Projection")
plt.show()


# Now let's change this map to do what we need.  Let's
# 1. Change the area to the continental United States
# 2. Increase the resolution to intermediate ('i')
# 3. Remove the horrific ocean/land colors provided above

# In[ ]:

m = Basemap(projection='merc',llcrnrlat=20,urcrnrlat=50,            llcrnrlon=-130,urcrnrlon=-60,lat_ts=20,resolution='i')
m.drawcoastlines()
m.drawcountries()
#m.drawstates()
# draw parallels and meridians.
parallels = np.arange(-90.,91.,5.)
# Label the meridians and parallels
m.drawparallels(parallels,labels=[False,True,True,False])
# Draw Meridians and Labels
meridians = np.arange(-180.,181.,10.)
m.drawmeridians(meridians,labels=[True,False,False,True])
m.drawmapboundary(fill_color='white')
plt.title("Forecast {0} days out".format(day_out))
plt.show()


# Now let's try adding our data!  Let's just plot their locations first...

# In[ ]:

m = Basemap(projection='merc',llcrnrlat=20,urcrnrlat=50,            llcrnrlon=-130,urcrnrlon=-60,lat_ts=20,resolution='i')
m.drawcoastlines()
m.drawcountries()
# draw parallels and meridians.
parallels = np.arange(-90.,91.,5.)
# Label the meridians and parallels
m.drawparallels(parallels,labels=[False,True,True,False])
# Draw Meridians and Labels
meridians = np.arange(-180.,181.,10.)
m.drawmeridians(meridians,labels=[True,False,False,True])
m.drawmapboundary(fill_color='white')
plt.title("Forecast {0} days out".format(day_out))
x,y = m(lon, lat)
m.plot(x,y, 'bo', markersize=5)
plt.show()


# Now let's color the stations by their forecasted temperature (Max T) and add a colorbar
# 

# In[ ]:

m = Basemap(projection='merc',llcrnrlat=20,urcrnrlat=50,            llcrnrlon=-130,urcrnrlon=-60,lat_ts=20,resolution='i')
m.drawcoastlines()
m.drawcountries()
# draw parallels and meridians.
parallels = np.arange(-90.,91.,5.)
# Label the meridians and parallels
m.drawparallels(parallels,labels=[True,False,False,False])
# Draw Meridians and Labels
meridians = np.arange(-180.,181.,10.)
m.drawmeridians(meridians,labels=[True,False,False,True])
m.drawmapboundary(fill_color='white')
plt.title("Forecast {0} days out".format(day_out))
x,y = m(lon, lat)
jet = plt.cm.get_cmap('jet')
sc = plt.scatter(x,y, c=temperature, vmin=0, vmax =35, cmap=jet, s=20, edgecolors='none')
cbar = plt.colorbar(sc, shrink = .5)
cbar.set_label(temp)
plt.show()


# Well, that concludes what we are going over today.  Here are a few exercises you can try:
# 
# 1. In the first graph -- include the weather forecast through time for multiple stations.  Color each set of lines differently for each weather station.  Also color the points differently for each
#  
# 2. In the second graph -- Try creating a figure with subplots and show the forecasted Max Temperature and forecasted Mon Temperature as a function of Latitude side by side.
# 
# 3. In the histogram -- Try overlaying a histogram with of the distribution of Max T values for day 2 with the distribution of Min T values for the same day.
# 
# 4. For the map -- Create a figure with multiple maps, where each map shows the forecasted distribution of temperature for each day out.  Change the resolution.  Change the location of labels.
# 
# 5. What is the difference of the temperature forecast made April 22, 2014 with the previous forecast days? Can you map the differences?  
# 
# Thanks for joining us today!  Hope you had fun :-).
