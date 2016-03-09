import sys
import os
import csv
from googlesearch import GoogleSearch
from pprint import pprint
import time
import urllib
import httplib2
from bs4 import BeautifulSoup
import urllib2
import re

#import mechanize
#from bs4 import BeautifulSoup
#from pygoogle import pygoogle

us_states_dict = {
'AL':'Alabama',
'AK':'Alaska',
'AZ':'Arizona',
'AR':'Arkansas',
'CA':'California',
'CO':'Colorado',
'CT':'Connecticut',
'DE':'Delaware',
'FL':'Florida',
'GA':'Georgia',
'HI':'Hawaii',
'ID':'Idaho',
'IL':'Illinois',
'IN':'Indiana',
'IA':'Iowa',
'KS':'Kansas',
'KY':'Kentucky',
'LA':'Louisiana',
'ME':'Maine',
'MD':'Maryland',
'MA':'Massachusetts',
'MI':'Michigan',
'MN':'Minnesota',
'MS':'Mississippi',
'MO':'Missouri',
'MT':'Montana',
'NE':'Nebraska',
'NV':'Nevada',
'NH':'New Hampshire',
'NJ':'New Jersey',
'NM':'New Mexico',
'NY':'New York',
'NC':'North Carolina',
'ND':'North Dakota',
'OH':'Ohio',
'OK':'Oklahoma',
'OR':'Oregon',
'PA':'Pennsylvania',
'RI':'Rhode Island',
'SC':'South Carolina',
'SD':'South Dakota',
'TN':'Tennessee',
'TX':'Texas',
'UT':'Utah',
'VT':'Vermont',
'VA':'Virginia',
'WA':'Washington',
'WV':'West Virginia',
'WI':'Wisconsin',
'WY':'Wyoming'}

common_sites = [
"facebook", 
"yahoo", 
"faithstreet", 
"guidestar", 
"manta", 
"donationplanet",
"fundraise", 
"taxexemptworld", 
"orgcouncil", 
"razoo", 
"charitynavigator",
"faqs.org",
"yellowpages",
"maprequest",
"citizenaudit",
"charityblossom",
"nonprofitlocator",
"wikipedia",
"tripadvisor",
"yelp",
"nonprofitfacts",
"propublica",
"nonprofitlookup",
"infofree",
"foursquare",
"christianvolunteering",
"greatnonprofits",
"unityworldwideministries",
"parishesonline",
"causeiq",
"findthecompany",
"charity-charities.org",
"linkedin",
"mapquest",
"501c3lookup",
"dailymail",
"whitepages",
"churchfinder",
"punchbowl",
"usachurches",
"nccsweb"]

def format_urls(urls_list):
    urls = ""
    
    for url in urls_list:
        if urls == "":
            urls = url
        else:
            urls = urls + " , " + str(url)

    #print urls
    return urls

def exract_links(url):
     
    try:
        
        resp = urllib2.urlopen(url)
        soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
        
        urls_list = []
        for link in soup.find_all('a', href=True):
            #if "www." in link['href']:
            urls_list.append(link['href'])

    except:
        return []
    
    return urls_list


def is_common_site(url):
    for site in common_sites:
        if site in url:
            return True
    
    return False

def google_search(query):
    urls = []
    from google import search
    for url in search(query, tld='es', lang='en', stop=5):
        if is_common_site(url) == True: 
            None
        else:
            urls.append(url)  
        
    if len(urls) == 0:
        #print "Not found"
        return ["Not found", "Not found", "Not found"]
    if len(urls) < 3:
        for i in range(len(urls),3):
            urls.append("Not found")    
            
    
    return urls[0], urls[1], urls[2]


def read_csv_data(data_file):
    row_no = 1
    url_1 = "Not found"
    url_2 = "Not found"
    url_3 = "Not found"
    with open('eo1_100.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter='\t',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["ORGNAME", "STREET", "CITY", "STATE", "ZIP", "URL", "SECOND_LEVEL_LINKS"])                        
        with open(data_file, 'rb') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csv_reader:
                #for item in row:
                    #print item
                if row_no == 102:
                    return
                if row_no == 1:
                    row_no = row_no + 1
                else:
                    org_name = str(row[1]) + str(" ") 
                    street = str(row[3]) 
                    city = str(row[4]) 
                    state = str(row[5])
                    state_full = us_states_dict[str(row[5])]
                    zipcode = str(row[6])
                    address = org_name + street + city + state
                    #print row_no
                    #print str("Org Name: " + org_name) 
                    #print str("Street: " + street)
                    #print str("City: " + city)
                    #print str("State: " + state)
                    #print str("Zip: " + zipcode)
                    print str(str(row_no - 1) + " - Searching for: " + str("official website of "+ org_name+ city + " " + state))
                    url_1, url_2, url_3 = google_search(str(org_name + city + " " + state))
                    print url_1
                    #print url_2
                    if url_1 != "Not found":
                        urls_1_list = exract_links(url_1)
                    if url_2 != "Not found":
                        urls_2_list = exract_links(url_2)                    
                        
                    second_level_urls = format_urls(urls_1_list)
                    print second_level_urls
                    #print url_3
                    print "------------------------------------------------------------"
                    #print str(str(row_no - 1) + " Searching for: " + str(org_name + street + city +" " + state + " " + zipcode))
                    url_4, url_5, url_6 = google_search(str(org_name+ street+ city +" "+ state+ " " + zipcode))
                    #print url_4                    
                    #print "------------------------------------------------------------"
                    csv_writer.writerow([org_name, street, city, state, zipcode, url_1, second_level_urls])                        
                    #time.sleep(2)
                    row_no = row_no + 1
            
    return 

def validate_links(data_file):
    row_no = 1
    with open('eo1_with_urls.csv', 'wb') as op_dataset:
            csv_writer = csv.writer(op_dataset, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["ORGNAME", "STREET", "CITY", "STATE", "ZIP", "HITS", "OFFICIAL_LINK" ,"URL_1", "URL_2"])                        
            with open(data_file, 'rb') as in_dataset:
                csv_reader = csv.reader(in_dataset, delimiter=',', quotechar='"')
                for row in csv_reader:  
                    #print row
                    if row_no == 1:
                        row_no = row_no + 1
                        
                    else:
                        row_no = row_no + 1
                        official_link = str(row[5])
                        url_1 = str(row[6])
                        url_2 = str(row[7])
                        print str(row_no - 1) + " " + str(official_link)
                        if str(official_link) != 'NA':
                            if str(official_link) in str(url_1) or str(official_link) in str(url_2) or str(url_1) in str(official_link) or str(url_2) in str(official_link):
                                hit = 1
                            else:
                                hit = 0
                        else:
                            hit = 1
                        csv_writer.writerow([row[0], row[1], row[2], row[3], row[4], hit, row[5], row[6], row[7]])                        
                    
    
    
    return 




def main():
    #results = []
    #results = google_search_5("psg tech")
    #for result in results:
        #print result
    
    #google_search_8()
    read_csv_data("../../Dataset/eo1.csv")
    #validate_links("eo1_100.csv")
    
        
    return

if __name__ == "__main__":
    main()