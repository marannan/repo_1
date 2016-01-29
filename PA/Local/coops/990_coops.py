import sys
import os
import csv
from pprint import pprint
import time
import re
import traceback


def get_total_revenue(org_name, org_ein):
    total_revenue = ""
    file_for_total_revenue = "../../Dataset/Guidestar/guidestar_990/f990_Part_I.txt"
    
    
    try:
        with open(file_for_total_revenue, 'rb') as coop_990_revenue:
            csv_reader = csv.reader(coop_990_revenue, delimiter='|', quotechar='"')
            for row in csv_reader:    
                part_1_org_ein = str(row[0]).lower()
                part_1_org_name = str(row[1]).lower()
                #print str(part_1_org_name + "\t" + part_1_org_ein)
                #print "-----------------------------"
                
                if org_ein == part_1_org_ein or org_name == part_1_org_name:
                    total_revenue  = str(row[3]) 
                    try:
                        return total_revenue.split('.',1)[0]
                    except:
                        return total_revenue
        
        
    
    except Exception,e: 
        traceback.print_exc(file=sys.stdout)
        return total_revenue
        
    return total_revenue

def get_employment(org_name, org_ein):
    all_year_employees = ""
    file_for_employement = "../../Dataset/Guidestar/guidestar_990/f990_Part_V.txt"
    
    
    try:
        with open(file_for_employement, 'rb') as coop_990_employment:
            csv_reader = csv.reader(coop_990_employment, delimiter='|', quotechar='"')
            for row in csv_reader:    
                part_v_org_ein = str(row[0]).lower()
                part_v_org_name = str(row[1]).lower()
                #print str(part_v_org_name + "\t" + part_v_org_ein)
                #print "-----------------------------"
                
                if org_ein == part_v_org_ein or org_name == part_v_org_name:
                    all_year_employees  = str(row[5]) 
                    return all_year_employees
        
        
    
    except Exception,e: 
        traceback.print_exc(file=sys.stdout)
        return all_year_employees
        
    return all_year_employees


def get_assets(org_name, org_ein):
    total_assets_eoy = ""
    file_for_assets = "../../Dataset/Guidestar/guidestar_990/f990_Part_X.txt"
    
    
    try:
        with open(file_for_assets, 'rb') as coop_990_assets:
            csv_reader = csv.reader(coop_990_assets, delimiter='|', quotechar='"')
            for row in csv_reader:    
                part_x_org_ein = str(row[0]).lower()
                part_x_org_name = str(row[1]).lower()
                #print str(part_x_org_name + "\t" + part_x_org_ein)
                #print "-----------------------------"
                
                if org_ein == part_x_org_ein or org_name == part_x_org_name:
                    total_assets_eoy  = str(row[36]) 
                    try:
                        return total_assets_eoy.split('.',1)[0]
                    except:
                        return total_assets_eoy
        
        
    
    except Exception,e: 
        traceback.print_exc(file=sys.stdout)
        return total_assets_eoy
        
    return total_assets_eoy

def write_coop_data(coop_data):
    
    try:
        with open('990_coop_with_other_data.csv', 'wb') as coop_data_file:
            csv_writer = csv.writer(coop_data_file, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["C_EIN", "C_ORG_NAME", "TOTAL_REVENUE", "ALL_YEAR_EMPLOYEES", "TOTAL_ASSETS_EOY"]) 
            for data in coop_data:
                csv_writer.writerow(data)
                
    except Exception,e: 
        traceback.print_exc(file=sys.stdout)
        
    
    return
        


def get_coop_data(coop_990_base_file):
    
    row_no = 1
    coop_data = []
    
    try:
        with open(coop_990_base_file, 'rb') as coop_990_base:
            csv_reader = csv.reader(coop_990_base, delimiter=',', quotechar='"')
            for row in csv_reader:
                #print row
                #for item in row:
                    #print item
                #if row_no == stop_row:
                    #return
                if row_no == 1:
                    row_no = row_no + 1
                    continue
                data = []
                org_name = str(row[0]).lower()
                org_ein = str(row[1]).lower()
                
                total_revenue  = get_total_revenue(org_name, org_ein)
                employment  = get_employment(org_name, org_ein)
                total_assets = get_assets(org_name,org_ein)
                #print str("total_revenue: " + total_revenue)
                #print str("employment: " + employment)
                #print str("total_assets: " + total_assets)
                print str(org_ein + "\t" + org_name + "\t" + total_revenue + "\t" + employment + "\t" + total_assets)
                #print "-----------------------------"                
                data = [org_ein, org_name, total_revenue, employment, total_assets]
                coop_data.append(data)
                
    
    except Exception,e: 
        traceback.print_exc(file=sys.stdout)
        
    
    return coop_data

if __name__ == "__main__":
    coop_990_base_file = "990_coop_base.csv"
    coop_data = get_coop_data(coop_990_base_file)
    write_coop_data(coop_data)
    