import sys
import os
import csv
from pprint import pprint
import time
import re
import traceback
import pandas as pd
from plot import *
from geo_location import *
import numpy as np
import glob

zip_codes_missing = []

def find_year(file_name):
    
    for year in range(1990, 2100):
        if str(year) in file_name:
            return year


def get_data(data_path):
    
    data = {}
    years = []
    files = []
    
    
    data_files = os.listdir(data_path)
    file_dict = dict(zip(data_files, range(len(data_files))))
    
    for file_name, idx in file_dict.items():
        data_file =  data_path + '/' + file_name

        #skipping temp files
        if "~" in str(data_file):
            continue
        
        year = find_year(file_name)
        years.append(year)
        files.append(data_file)
        
        try:
            data[year] = pd.read_csv(data_file, sep=',', low_memory=False, quotechar='"')
            print "loading data from file %s : done" %(data_file)
        except:
            traceback.print_exc(file=sys.stdout)
    

    return data, files, years


def get_data_consolidate(data_path, columns):
    
    years = []
    files = []
    
    
    data_files = os.listdir(data_path)
    file_dict = dict(zip(data_files, range(len(data_files))))

    data_all = pd.DataFrame()
    
    for file_name, idx in sorted(file_dict.items()):
        data_file =  data_path + '/' + file_name
        year = find_year(file_name)
        years.append(year)
        files.append(data_file)
        
        try:
            data = pd.read_csv(data_file, sep = ',', low_memory = False, quotechar = '"')
            if 'ADDRESS' not in data:
                data['ADDRESS'] = "NA"
            
            if 'OTHSAL' not in data:
                data['OTHSAL'] = 0
                 
            if 'COMPENS' not in data:
                data['COMPENS'] = 0            
                
            #data['OTHSAL+COMPENS'] = data[['OTHSAL','COMPENS']].sum(axis=1)

            if 'ASS_EOY' not in data:
                data['ASS_EOY'] = 0                

            if 'TOTREV' not in data:
                data['TOTREV'] = 0                

            data['YEAR'] = year

            data_all = data_all.append(data[columns], ignore_index=True)
            print "loading data from file %s : done" %(data_file)
            
        
        except:
            traceback.print_exc(file=sys.stdout)
     
    return data_all, files, years


def create_colsoildate_data(data_path, columns):
    
    data ,files, years = get_data_consolidate(data_path, columns)
    
    #write to a new data file
    print "generating consolidated data file..."

    #sort by ein and rearrange columns
    data = data.sort_values(by=['EIN'], ascending=[True])
    data = data[columns]    
    
    ein_list = data['EIN'].tolist()
    
    #print len(ein_list)
    #print len(set(ein_list))
    
    colsoildated_data_file = data_path + "Core_501(c)_others_all_in_one.csv"
    data.to_csv(colsoildated_data_file, mode = 'w', index=False)
    
    print "consolidated data file is generated at : %s" %(colsoildated_data_file)

    return colsoildated_data_file


def generate_location_data(data_path):
    
    #get data from files
    data ,files, years = get_data(data_path)

    print "generating latitude and longitude for organisations based on ZIP code"
    for year in sorted(years):
        #length_ein = len(data[year]['EIN'])
        length = len(data[year].index)
        
        if 'ZIP' in data[year]:
            length_zip = len(data[year]['ZIP'])
            lat_list, long_list = get_geo(list(data[year]["ZIP"].astype(str)), year)
            
            length_lat = len(lat_list)
            length_long = len(long_list)
        
        else:
            lat_list = ['.'] * length
            long_list = ['.'] * length
            
            length_lat = len(lat_list)
            length_long = len(long_list)   
            
        
        if length != length_lat or length != length_long or length_lat != length_long:
            print "error: records length dont match for year : " + str(year) + " " +str(length) + " " + str(length_lat) + " " + str(length_long)
            print "exiting.."
            exit()
        
        
        #if 'LATITUDE', 'LONGITUDE' already on the data file dont add them
        #if 'LONGITUDE' not in data[year]:
        data[year]['LONGITUDE'] = pd.Series(long_list)        


        #if 'LATITUDE' not in data[year]:
        data[year]['LATITUDE'] = pd.Series(lat_list)
        
        df_lat = data[year]["LATITUDE"].tolist()
        df_lon = data[year]["LONGITUDE"].tolist()
        
        if '.' in df_lat or '.' in df_lon:
            print "error"
                
        
        #write the new data to a new file
        for file in files:
            if str(year) in file:
                old_file_name = file
                break
            
        new_file_name = old_file_name.split('/')
        new_file_name = new_file_name[len(new_file_name)-1].split('.')[0]
        new_data_path = data_path + "_with_geo_loc" + "/"
        new_file_name = new_data_path + new_file_name + "_with_geo_loc.csv"
        
        if os.path.exists(new_data_path) == False:
            os.makedirs(new_data_path)
            
        data[year].to_csv(new_file_name, mode = 'w', index=False)
        print "new data file with latitude and longitude : %s" %(new_file_name)
    
    
    print "warning: no of missing zip codes : %s" %(len(zip_codes_missing))
    print "\n".join(zip_codes_missing)

    print "generating latitude and longitude for organisations based on ZIP code... done"
    return new_data_path



def get_trends_data(data_path):
    
    OTHSAL = {}
    COMPENS = {}
    ASS_EOY = {}
    TOTREV = {}
    
    compense_year_wise = {}
    assets_year_wise = {}
    revenue_year_wise = {}     
    
    #get data from files
    data, files, years = get_data(data_path)
    
    print "generating year wise data for othsal_compens, ass_eoy, totrev..." 
    for year in sorted(years):
        try:
            try:
                sal_list = data[year]["OTHSAL"]
                OTHSAL[year] = map(int, filter(lambda a: a != '.', sal_list))
            except:
                OTHSAL[year] = [0] * 1 #len(data[year]["EIN"])
                pass
    
            try:
                comp_list = data[year]["COMPENS"]
                COMPENS[year] = map(int, filter(lambda a: a != '.', comp_list))
            except:
                COMPENS[year] = [0] * 1 #en(data[year]["EIN"])
                pass
    
            try:
                ass_list = data[year]["ASS_EOY"]
                ASS_EOY[year] = map(int, filter(lambda a: a != '.', ass_list))
            except:
                ASS_EOY[year] = [0] * 1 #len(data[year]["EIN"])
                pass
    
            try:
                totrev_list = data[year]["TOTREV"]
                TOTREV[year]  = map(int, filter(lambda a: a != '.', totrev_list))
            except:
                TOTREV[year] = [0] * 1 #len(data[year]["EIN"])
                pass
    
        except:
            print year
            traceback.print_exc(file=sys.stdout)           
            exit()

    for year in sorted(years):
        compense_year_wise[year] = sum(OTHSAL[year]) + sum(COMPENS[year])
        assets_year_wise[year] = sum(ASS_EOY[year])
        revenue_year_wise[year] = sum(TOTREV[year])


    print "generating year wise data for othsal_compens, ass_eoy, totrev... : done" 
    return compense_year_wise, assets_year_wise, revenue_year_wise


def get_geo(zip_code_list, year):
    
    #loading zip code from local zip code dump files, not needed
    #load_zip_codes()
    
    lat_list = []
    long_list = []
    
    
    missing_count = 0
    missing_count_parsing = 0
    missing_count_na = 0
    for zip_code_count, code in enumerate(zip_code_list):
        #code = unicode(code, 'utf-8')
        
        try:
            zip_code = code.split('-')[0]
        
        except:
            #print "error: invalid or null zip code : " + zip_code
            lat_list.append(0.0)
            long_list.append(0.0)
            missing_count_parsing = missing_count_parsing + 1            
            continue
            
    
        if zip_code == 'nan' or zip_code == '' or zip_code == '.' or zip_code == '0' or zip_code == '00' or zip_code == '000' or zip_code == '0000' or zip_code == '00000':
            #print "error: invalid or null zip code : " + zip_code
            lat = 0.0
            long = 0.0
            missing_count_na = missing_count_na + 1
        

        else:
            
            #get latitude and longitude from zip code dump files we loaded earlier
            lat, long = get_geo_location(zip_code)
    
            if lat == 0.0 or long == 0.0:
                #print "warning: zip code not found in zip code files : " + str(zip_code)
                
                #print "getting them from google"                
                lat, long, error = get_geo_location_google(zip_code)
                #time.sleep(1)
                
                if error == "zip code not found in google error":
                    #print "error: zip code not found in google for " + " zip code : " + zip_code
                    #zip code is not found so add to the list of missing zip for debug
                    if zip_code not in zip_codes_missing:
                        zip_codes_missing.append(zip_code)
                        
    
                if error == "google server error" :
                    #print "error: google server not responding for " + " zip code : " + zip_code
                    #zip code is not found so add to the list of missing zip for debug                    
                    if zip_code not in zip_codes_missing:
                        zip_codes_missing.append(zip_code)                    
        
            
            
        lat_list.append(lat)
        long_list.append(long)
        
    if '.' in lat_list or '.' in long_list:
        print "warining '.' is added as lat/long value"
        #exit()
        
        
    return lat_list, long_list

def write_to_file(othsal_compens,ass_eoy,totrev):
    
    writer = csv.writer(open('othsal_compens.csv', 'wb'))
    for key, value in othsal_compens.items():
        writer.writerow([key, value])    
        
    
    writer = csv.writer(open('ass_eoy.csv', 'wb'))
    for key, value in ass_eoy.items():
        writer.writerow([key, value])        


    writer = csv.writer(open('totrev.csv', 'wb'))
    for key, value in totrev.items():
        writer.writerow([key, value])
        
    
    return 


def read_from_file():
    reader = csv.reader(open('othsal_compens.csv', 'rb'))
    othsal_compens = dict(reader)
    
    reader = csv.reader(open('ass_eoy.csv', 'rb'))
    ass_eoy = dict(reader)
    
    reader = csv.reader(open('totrev.csv', 'rb'))
    totrev = dict(reader)


    return othsal_compens, ass_eoy, totrev


def visualize_trends(data_path):
      
    #check for locally saved files if there dont calculate again
    local_files_found = False
    #files = [f for f in os.listdir('.') if os.path.isfile(f)]
    #if 'othsal_compens.csv' in files and 'ass_eoy.csv' in files and 'totrev.csv' in files:
        #local_files_found = True
        
    if local_files_found == False:
        othsal_compens, ass_eoy, totrev = get_trends_data(data_path)
        
    else:
        othsal_compens, ass_eoy, totrev = read_from_file()
        
    
    #save the data to local file
    if local_files_found == False:
        write_to_file(othsal_compens,ass_eoy,totrev)
    
    print "plotting year wise trends in compensation, assets and revenue for organisations..."
    
    othsal_compens_trend = plot_trend(othsal_compens)
    
    ass_eoy_trend = plot_trend(ass_eoy)
    
    totrev_eoy_trend = plot_trend(totrev)

    print "plotting year wise trends in compensation, assets and revenue for organisations... : done"
    print "othsal_compens_trend : " + str(othsal_compens_trend)
    print "ass_eoy_trend : " + str(ass_eoy_trend)
    print "totrev_eoy_trend : " + str(totrev_eoy_trend)

    return othsal_compens_trend, ass_eoy_trend, totrev_eoy_trend


def create_geo_data_and_consolidate_all_data_files(data_path):
    
    new_data_path = generate_location_data(data_path)
    
    #specify the columns needed for the colsolidation
    columns = ['EIN', 'NAME', 'ADDRESS', 'CITY', 'STATE', 'ZIP', 'YEAR', 'OTHSAL', 'COMPENS', 'ASS_EOY', 'TOTREV', 'LATITUDE', 'LONGITUDE']
    
    consolidate_data_file = create_colsoildate_data(new_data_path, columns)
    
    return consolidate_data_file


def visualize_maps(consolidate_data_file):

    print "plotting maps data for compensation, assets and revenue for organisations for all years..."
    compensation_map = plot_matplotlib(consolidate_data_file, "OTHSAL+COMPENS")
    assests_map = plot_matplotlib(consolidate_data_file, "ASS_EOY")
    total_rev_map = plot_matplotlib(consolidate_data_file, "TOTREV")

    return compensation_map, assests_map, total_rev_map


if __name__ == "__main__":
    
    data_path_1 = "/media/ashok/My_Drive/Downloads/NCCS/Core_501(c)_others"
    data_path_1_sample = "/media/ashok/My_Drive/Downloads/NCCS/Core_501(c)_others_sample"
    
    try:
        arg = sys.argv[1]
        #print arg

    except:
        print "error: invalid argument"
        print "args : 1 for visualizing year wise trends in compensation, assets and revenue for organisations"
        print "args : 2 for visualizing maps based on compensation, assets and revenue for organisations accross all years"
        print "args : 3 for both"
        exit()
    
    
    if arg == "1":
        visualize_trends(data_path_1)
        
    
    elif arg == "2":
        con_data_file  = create_geo_data_and_consolidate_all_data_files(data_path_1)
        #visualize_maps(con_data_file)
        

    elif arg == "3":
        visualize_trends(data_path_1)
        con_data_file  = create_geo_data_and_consolidate_all_data_files(data_path_1)
        visualize_maps(con_data_file)        
    
    
    else:
        print "args : 1 for visualizing year wise trends in compensation, assets and revenue for organisations"
        print "args : 2 for visualizing maps based on compensation, assets and revenue for organisations accross all years"
        print "args : 3 for both"
    
    
    
    
