import sys
import os
import csv
from pprint import pprint
import time
import re
import traceback


def get_total_revenue(org_name, org_ein, catagory = "990"):
    total_revenue = "NA"

    if catagory == "990":
        file_for_total_revenue = "../../Dataset/Guidestar/guidestar_990/f990_Part_I.txt"
        total_revenue_col_no = 3
    
        try:
            with open(file_for_total_revenue, 'rb') as coop_revenue:
                csv_reader = csv.reader(coop_revenue, delimiter='|', quotechar='"')
                for row in csv_reader:    
                    part_1_org_ein = str(row[0]).lower()
                    part_1_org_name = str(row[1]).lower()
                    #print str(part_1_org_name + "\t" + part_1_org_ein)
                    #print "-----------------------------"
                    
                    if org_ein == part_1_org_ein: #or org_name == part_1_org_name:
                        total_revenue  = str(row[total_revenue_col_no]) 
                        try:
                            return total_revenue.split('.',1)[0]
                        except:
                            return total_revenue
                
                
            
        except Exception,e: 
            traceback.print_exc(file=sys.stdout)
            return total_revenue
            
        return total_revenue        

        
    elif catagory == "990pf":
        file_for_total_revenue = "../../Dataset/Guidestar/guidestar_990PF/BMF.txt"
        total_revenue_col_no = 42
        total_rev = 0
    
    
        try:
            with open(file_for_total_revenue, 'rb') as coop_revenue:
                csv_reader = csv.reader(coop_revenue, delimiter='|', quotechar='"')
                for row in csv_reader:    
                    part_1_org_ein = str(row[0]).lower()
                    part_1_org_name = str(row[1]).lower()
                    #print str(part_1_org_name + "\t" + part_1_org_ein)
                    #print "-----------------------------"
                    
                    if org_ein == part_1_org_ein: #or org_name == part_1_org_name:
                        total_rev = total_rev + int(str(row[total_revenue_col_no]).split(".",1)[0])
                        #total_revenue  = str(row[total_revenue_col_no]) 
                        #try:
                            #return total_revenue.split('.',1)[0]
                        #except:
                            #return total_revenue
            
            
        
        except Exception,e: 
            traceback.print_exc(file=sys.stdout)
            return total_revenue
        
        try:
            return str(total_rev).split('.',1)[0]
        except:
            return str(total_rev)        


def get_employment(org_name, org_ein, catagory = "900"):
    all_year_employees = "NA"
    
    if catagory == "990":
        file_for_employement = "../../Dataset/Guidestar/guidestar_990/f990_Part_V.txt"
    
        try:
            with open(file_for_employement, 'rb') as coop_employment:
                csv_reader = csv.reader(coop_employment, delimiter='|', quotechar='"')
                for row in csv_reader:    
                    part_v_org_ein = str(row[0]).lower()
                    part_v_org_name = str(row[1]).lower()
                    #print str(part_v_org_name + "\t" + part_v_org_ein)
                    #print "-----------------------------"
                    
                    if org_ein == part_v_org_ein: #or org_name == part_v_org_name:
                        all_year_employees  = str(row[5]) 
                        return all_year_employees
            
            
        
        except Exception,e: 
            traceback.print_exc(file=sys.stdout)
            return all_year_employees
            
        return all_year_employees
    
    elif catagory == "990pf":
        file_for_employement = "../../Dataset/Guidestar/guidestar_990PF/PF990_Part_VIII_Employees.txt" 
        employees_count = 0
        
        try:
            with open(file_for_employement, 'rb') as coop_employment:
                csv_reader = csv.reader(coop_employment, delimiter='|', quotechar='"')
                for row in csv_reader:    
                    part_v_org_ein = str(row[0]).lower()
                    part_v_org_name = str(row[1]).lower()
                    #print str(part_v_org_name + "\t" + part_v_org_ein)
                    #print "-----------------------------"
                    
                    if org_ein == part_v_org_ein: # or org_name == part_v_org_name:
                        employees_count = employees_count + 1
                    
                    
                
        except Exception,e: 
            traceback.print_exc(file=sys.stdout)
            return all_year_employees
                    
        return str(employees_count)


def get_assets(org_name, org_ein, catagory = "900"):
    total_assets_eoy = "NA"
    
    if catagory == "990":
        file_for_assets = "../../Dataset/Guidestar/guidestar_990/f990_Part_X.txt"
        total_assets_col_no = 36
        
        try:
            with open(file_for_assets, 'rb') as coop_990_assets:
                csv_reader = csv.reader(coop_990_assets, delimiter='|', quotechar='"')
                for row in csv_reader:    
                    part_x_org_ein = str(row[0]).lower()
                    part_x_org_name = str(row[1]).lower()
                    #print str(part_x_org_name + "\t" + part_x_org_ein)
                    #print "-----------------------------"
                    
                    if org_ein == part_x_org_ein: # or org_name == part_x_org_name:
                        total_assets_eoy  = str(row[total_assets_col_no]) 
                        try:
                            return total_assets_eoy.split('.',1)[0]
                        except:
                            return total_assets_eoy
            
            
        
        except Exception,e: 
            traceback.print_exc(file=sys.stdout)
            return total_assets_eoy
            
        return total_assets_eoy        

        
    elif catagory == "990pf":
        file_for_assets = "../../Dataset/Guidestar/guidestar_990PF/BMF.txt"
        total_assets_col_no = 30
        total_assets = 0
    
    
    
    try:
        with open(file_for_assets, 'rb') as coop_990_assets:
            csv_reader = csv.reader(coop_990_assets, delimiter='|', quotechar='"')
            for row in csv_reader:    
                part_x_org_ein = str(row[0]).lower()
                part_x_org_name = str(row[1]).lower()
                #print str(part_x_org_name + "\t" + part_x_org_ein)
                #print "-----------------------------"
                
                if org_ein == part_x_org_ein: # or org_name == part_x_org_name:
                    total_assets = total_assets + int(str(row[total_assets_col_no]).split(".",1)[0])
                    
        
        
    
    except Exception,e: 
        traceback.print_exc(file=sys.stdout)
        return total_assets_eoy
    
    
    if total_assets == 0:    
        return total_assets_eoy
    
    else:
        return str(total_assets)
    

def write_coop_data(coop_data, coop_out_file):
        
    try:
        with open(coop_out_file, 'wb') as coop_data_file:
            csv_writer = csv.writer(coop_data_file, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["C_EIN", "C_ORG_NAME", "TITLE HIT", "NTEECC/ACT_CODE HIT", "PURPOSE/ACHIEVEMENT HIT", "TOTAL_REVENUE", "ALL_YEAR_EMPLOYEES", "TOTAL_ASSETS_EOY"]) 
            for data in coop_data:
                csv_writer.writerow(data)
                
    except Exception,e: 
        traceback.print_exc(file=sys.stdout)
        
    
    return
        


def get_coop_data(coop_990_base_file, catagory = "990"):
    
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
                title_hit  = str(row[4]).lower()
                NTEECC_ACT_code_hit  = str(row[5]).lower()
                purpose_achivement_hit  = str(row[6]).lower()
                
                
                total_revenue  = get_total_revenue(org_name, org_ein, catagory)
                employment  = get_employment(org_name, org_ein, catagory)
                total_assets = get_assets(org_name,org_ein, catagory)
                
                data = [org_ein, org_name, title_hit, NTEECC_ACT_code_hit, purpose_achivement_hit, total_revenue, employment, total_assets]
                print data
                coop_data.append(data)
                
    
    except Exception,e: 
        traceback.print_exc(file=sys.stdout)
        
    
    return coop_data

if __name__ == "__main__":
    
    coop_900_data = get_coop_data("coop_900_base.csv", "990")
    coop_900_pf_data = get_coop_data("coop_990_pf_base.csv","990pf")
    
    write_coop_data(coop_900_data, "coop_990.csv")
    write_coop_data(coop_900_pf_data, "coop_990_pf.csv")
    