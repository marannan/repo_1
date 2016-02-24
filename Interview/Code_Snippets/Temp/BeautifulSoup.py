from bs4 import BeautifulSoup
import urllib2

resp = urllib2.urlopen("http://www.saintgeorgecathedral.com/")
soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))

for link in soup.find_all('a', href=True):
    #if "www." in link['href']:
    print link['href']
        
        

import urllib
import lxml.html
connection = urllib.urlopen('http://www.saintgeorgecathedral.com/')

dom =  lxml.html.fromstring(connection.read())

for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
    print link