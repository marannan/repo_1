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
zip_codes_loaded = False


def save_zip_codes():
    
    with open("zip_codes/zip_codes_all.csv", mode='a') as zip_code_file:
        zip_code_file_csv = csv.writer(zip_code_file, delimiter=',', quotechar='"')
        #zip_code_file_csv.writerow(["ZIP", "LATITIDE", "LONGITUDE"])
        for zip_code in zip_codes:
            zip_code_file_csv.writerow([zip_code, zip_codes[zip_code][0], zip_codes[zip_code][1]])


def save_zip_code(zip_code, lat, long):
    
    with open("zip_codes/zip_codes_all.csv", mode='a') as zip_code_file:
        zip_code_file_csv = csv.writer(zip_code_file, delimiter=',', quotechar='"')
        #zip_code_file_csv.writerow(["ZIP", "LATITIDE", "LONGITUDE"])
        zip_code_file_csv.writerow([zip_code, lat, long])  
        

def load_local_zip_codes_file(file_name = "zip_codes/zip_codes_all.csv"):
    
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
    
    return

def load_zip_codes(data_path = "zip_codes"):

    files = []
    data_files = os.listdir(data_path)
    
    for file in data_files:
        if '.json' in str(file) or 'all' in str(file):
            continue
        
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
        save_zipcodes()

    except:
        print "error : saving zip code"
         
                   
def get_geo_location(zip=None):
    global zip_codes_loaded
    
    if zip_codes_loaded == False:
        load_local_zip_codes_file()
        zip_codes_loaded = True
    
    else:
        pass
    
    if zip == None:
        #return '.' ,'.'
        return 0.0, 0.0
    
    zip = int(zip)
    
    try:
        return zip_codes[zip][0], zip_codes[zip][1] 
    
    except:
        #return '.' ,'.'
        return 0.0, 0.0
    
def get_geo_location_google(zip):

    key = "&key=AIzaSyAzoFo_UjW1J-JZfBxemAgeIh8rcWuYxko"
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + str(zip) + str(key)
    

    try:
        response = urllib2.urlopen(url)
        html = response.read()
    
    except:
        #return '.', '.', "google server error"
        return 0.0, 0.0, "google server error"      

    try:
        json_obj = json.loads(html)   
        
        if json_obj['status'] == "OVER_QUERY_LIMIT":
            #return '.', '.', "google server error"
            return 0.0, 0.0, "google server error"      

        else:            
            lat = json_obj[u'results'][0][u'geometry'][u'location'][u'lat']
            long = json_obj[u'results'][0][u'geometry'][u'location'][u'lng']
        
    except:
        #sreturn '.', '.', "zip code not found in google error"
        return 0.0, 0.0, "zip code not found in google error"
    
    
    #saving zip code to local
    try:
        zip_codes[int(zip)] = [lat, long]
        save_zip_code(int(zip), lat, long)

    except:
        print "error: saving zip code to local file"
    
    
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
    result = load_local_zip_codes_file(file_name = "zip_codes_all.csv")
    print "no of zip codes in the local zip code dump : %s" %(len(zip_codes))
    
    test_zip_codes(['17171', '07943' , '06985'], "local")
    test_zip_codes(['17171', '07943' , '06985'], "google")
    print "done"
    
    