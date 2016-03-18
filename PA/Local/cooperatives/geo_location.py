import sys
import os
import csv
from pprint import pprint
import time
import re
import traceback
import json
import urllib2
import urllib
import httplib2

zip_codes = {}


def load_zip_codes(data_path = "zip_codes"):

    files = []
    data_files = os.listdir(data_path)
    
    for file in data_files:
        files.append( data_path+"/"+file)
    
        
    for file_name in files:      
        with open(file_name, "r") as zip_code_file:
            zip_code_file_csv = csv.reader(zip_code_file, delimiter=',', quotechar='"')   
            row_imported = 0
            for row in zip_code_file_csv:
                try:
                    zip = int(row[0])
                    lat = float(row[1])
                    long = float(row[2])
                    
                    if zip not in zip_codes:
                        zip_codes[zip] = [lat, long]
                        #print "zip code already found!"
                        #print str(zip) + " " + str(lat) + " " + str(long)
                        #print str(zip) + " " + str(zip_codes[zip][0]) + " " + str(zip_codes[zip][1])
                    
                    row_imported = row_imported + 1
                
                except:
                    pass
                    #print "error importing zip code %s" %(str(row))
                
            #print "no of rows imported %s" %(row_imported)
            
    try:
        #check if the json dict for zip codes are same as the ones we've loaded from csv files, if not update the json dict
        zip_codes_json = json.load(open("zip_codes_backup/zip_codes.json",'r'))
        if zip_codes != zip_codes_json:
            json.dump(zip_codes, open("zip_codes_backup/zip_codes.json",'w'))

    except:
        print "zip_codes.json is missing"
         
                   
def get_geo_location(zip=None):
    
    if zip == None:
        return '.' ,'.'
    
    zip = int(zip)
    
    try:
        return zip_codes[zip][0], zip_codes[zip][1] 
    
    except:
        return '.', '.'
    
def get_geo_location_google(zip):

    key = "&key=AIzaSyAzoFo_UjW1J-JZfBxemAgeIh8rcWuYxko"
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + str(zip) + str(key)
    

    try:
        response = urllib2.urlopen(url)
        html = response.read()
    
    except:
        return '.', '.', "google server error"
    

    try:
        json_obj = json.loads(html)   
        
        if json_obj['status'] == "OVER_QUERY_LIMIT":
            return '.', '.', "google server error"

        else:            
            lat = json_obj[u'results'][0][u'geometry'][u'location'][u'lat']
            long = json_obj[u'results'][0][u'geometry'][u'location'][u'lng']
        
    except:
        return '.', '.', "zip code not found in google error"
    
    
    return lat, long, "no error"


def test_zip_codes(test_zip_codes, mode = "local"):
    
    if mode == "local":
        for zip in test_zip_codes:
            zip = int(zip)
            if zip in zip_codes:
                print "zip code found from local zip code dump : " + str(zip) + " " + str(zip_codes[zip][0]) + " " + str(zip_codes[zip][1])
            else:
                print "zip code not found from local zip code dump : %s" %(zip)
                
    else:
        for zip in test_zip_codes:
            lat, long, error = get_geo_location_google(zip)
            
            if error == "no error":
                print "zip code found from google : " + str(zip) + " " + str(lat) + " " + str(long)
            
            else:
                print "zip code not found from google : %s error: %s" %(zip, error)
                

if __name__ == "__main__":
    result = load_zip_codes()
    print "no of zip codes in the local zip code dump : %s" %(len(zip_codes))
    
    test_zip_codes(['17171', '07943' , '06985'], "local")
    test_zip_codes(['17171', '07943' , '06985'], "google")
    print "done"
    
    