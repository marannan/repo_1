import sys
import os
import csv
from googlesearch import GoogleSearch
from pprint import pprint
import time
import urllib
import mechanize
from bs4 import BeautifulSoup
import re
from pygoogle import pygoogle

def google_search_8(query):
    urls = []
    from google import search
    for url in search(query, tld='es', lang='en', stop=5):
        urls.append(url)    

    return urls[0], urls[1], urls[2]

def google_search_7():
    import urllib
    import json as m_json
    query = raw_input ( 'Query: facebook' )
    query = urllib.urlencode ( { 'q' : query } )
    response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
    json = m_json.loads ( response )
    results = json [ 'responseData' ] [ 'results' ]
    for result in results:
        title = result['title']
        url = result['url']   # was URL in the original and that threw a name error exception
        print ( title + '; ' + url )    


def google_search_6():
    from GoogleScraper import scrape_with_config, GoogleSearchError
    
    # See in the config.cfg file for possible values
    config = {
        'use_own_ip': True,
        'keyword': 'Let\'s go bubbles!',
        'search_engines': ['yandex', 'bing'],
        'num_pages_for_keyword': 1,
        'scrape_method': 'selenium',
        'sel_browser': 'chrome',
        'do_caching': False
    }
    
    try:
        search = scrape_with_config(config)
    except GoogleSearchError as e:
        print(e)
    
    # let's inspect what we got
    
    for serp in search.serps:
        print(serp)
        print(serp.search_engine_name)
        print(serp.scrape_method)
        print(serp.page_number)
        print(serp.requested_at)
        print(serp.num_results)
        # ... more attributes ...
        for link in serp.links:
            print(link)    


def google_search_5(query):
    from xgoogle.search import GoogleSearch, SearchError
    urls = [] 
    try:
        gs = GoogleSearch(query)
        gs.results_per_page = 100
        results = gs.get_results()
        results_len =  min(len(results), 20)
        for res in range(0,results_len):
            #print res.title.encode('utf8')
            #print res.desc.encode('utf8')
            #print results[res].url.encode('utf8')
            urls.append(results[res].url.encode('utf8'))
        if len(results) == 0:
            print "Not found"
            return ["Not found", "Not found", "Not found"]
        if len(urls) < 3:
            for i in range(len(urls),3):
                urls.append("Not found")
            
        return urls
    except SearchError, e:
        print "Search failed: %s" % e   
        return ["Error", "Error", "Error"]


def google_search_4():
    sys.path.append('/home/ashokmarannan/Downloads/google_appengine')
    from google.appengine.api import search
    
    # a query string like this comes from the client
    query = "stories"
    try:
        index = search.Index(name='yourindex', namespace='yournamespace')
        search_results = index.search("stories")
        returned_count = len(search_results.results)
        number_found = search_results.number_found
        for doc in search_results:
            print type(doc)
    except search.Error:
        print "error"     
        
        
def google_search_3(query):
    urls = []
    results = []
    g = pygoogle(query)
    g.pages = 5
    #print '*Found %s results*'%(g.get_result_count())
    results = g.get_urls()  
    if len(results) > 0:
        for result in range(0,3):
            urls.append(results[result])
    
    return urls
    


def google_search_2(query, depth="10"):
    urls = []
    
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent','chrome')]
    term = query.replace(" ", '+')
    g_query = "http://www.google.com/search?q="+term
    html_text = br.open(g_query).read()
    soup = BeautifulSoup(html_text)
    search = soup.findAll('div',attrs={'id':'search'})
    search_text = str(search[0])
    soup_1 = BeautifulSoup(search_text)
    list_items = soup_1.findAll('li')
    regex = "q(?!.*q).*?&amp"
    pattern = re.compile(regex)
    
    result_array = []
    for li in list_items:
        soup_2 = BeautifulSoup(str(li))
        links = soup_2.findAll('a')
        source_link = links[0]
        source_url = re.findall(pattern, str(source_link))
        if len(source_url) > 0:
            result_array.append(str(source_url[0].replace("q=","").replace("&amp","")))
    
    for result in range(0,3):
        urls.append(result_array[result])
        
    return urls


def google_search_1(query):
    urls = [] 
    try:
        gs = GoogleSearch(query)
        #gs.results_per_page = 50
        results = gs.top_results()
        results_len =  min(len(results), 3)
        for res in range(0,results_len):
            urls.append(results[res]['url'])
        if len(results) == 0:
            print "Not found"
            return ["Not found", "Not found", "Not found"]
        if len(urls) < 3:
            for i in range(len(urls),3):
                urls.append("Not found")
            
        return urls
    except:
        print "Search failed" 
        return ["Error", "Error", "Error"]
    


def read_csv_data(data_file):
    row_no = 1
    url_1 = "Not found"
    url_2 = "Not found"
    url_3 = "Not found"
    with open('eo1_with_links.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter='\t',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["Name", "Address", "Zipcode", "URL_1", "URL_2", "URL_3"])                        
        with open(data_file, 'rb') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csv_reader:
                #for item in row:
                    #print item
                if row_no == 230004:
                    return
                if row_no == 1:
                    row_no = row_no + 1
                else:
                    name = str(row[1]) + str(" ") 
                    address = str(row[3]) + str(" ") + str(row[4]) + str(" ") + str(row[5])
                    zipcode = str(row[6])
                    print row_no
                    print str("Name: " + name) 
                    print str("Address: " + address)
                    print str("Zip: " + zipcode)
                    url_1, url_2, url_3 = google_search_8(str(name+address))
                    print url_1
                    print url_2
                    print url_3
                    csv_writer.writerow([name, address, zipcode, url_1, url_2, url_3])                        
                    #time.sleep(2)
                    row_no = row_no + 1
            
    return 


def main():
    #results = []
    #results = google_search_5("psg tech")
    #for result in results:
        #print result
    
    #google_search_8()
    read_csv_data("../Dataset/eo1.csv")
        
    return

if __name__ == "__main__":
    main()