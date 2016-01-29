#ashok_marannan

import sys
import os
import csv
from pprint import pprint
import time
import re
import traceback


science_dict = ["science", "research", "education", "training", "certification", "accreditation", "exploration"]   

unvi_list = [
"UNIVERSITY OF WISCONSIN FOUNDATION", 
"UNIVERSITY OF MICHIGAN",
"UNIVERSITY OF MINNESOTA", 
"INDIANA UNIVERSITY",
"PENNSYLVANIA STATE UNIVERSITY",
"PURDUE UNIVERSITY",
"THE OHIO STATE UNIVERSITY",
"UNIVERSITY OF CHICAGO",
"UNIVERSITY OF IOWA"]


univ_donors = {
"UNIVERSITY OF WISCONSIN FOUNDATION": [],
"UNIVERSITY OF MICHIGAN": [],
"UNIVERSITY OF MINNESOTA": [],
"INDIANA UNIVERSITY":[],
"PENNSYLVANIA STATE UNIVERSITY":[],
"PURDUE UNIVERSITY":[],
"THE OHIO STATE UNIVERSITY":[],
"UNIVERSITY OF CHICAGO":[],
"UNIVERSITY OF IOWA":[]}

univ_grants = {
"UNIVERSITY OF WISCONSIN": [0],
"UNIVERSITY OF MICHIGAN": [0], 
"UNIVERSITY OF MINNESOTA": [0],
"INDIANA UNIVERSITY": [0],
"PENNSYLVANIA STATE UNIVERSITY": [0],
"PURDUE UNIVERSITY": [0],
"THE OHIO STATE UNIVERSITY": [0],
"UNIVERSITY OF CHICAGO": [0],
"UNIVERSITY OF IOWA": [0],}

univ_grants_info = []
umad = []
umich = []
univ_hos = []
umad_grants_dict = {}
umich_grants_dict = {}

irs_sec_501 = []
irs_sec_univ_col = []
irs_sec_gov = []
irs_sec_other = []

irs_sec_501_texts = ['501', 'C3', '3']
irs_sec_univ_col_texts = ['UNIVERSITY', 'COLLEGE']
irs_sec_gov_texts = ['GOVERNMENT', 'GOV']

f990_Sched_I_Part_II_Gov_Grant_file_name = ""
pf990_Part_XV_Grants_Paid_file_name = ""
option  = 1



def extract_univ_grants(data_file, donor_col, recepient_col, grands_col, purp_col = 0):
    row_no = 1
    
    try:
        with open(data_file, 'rb') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter='|', quotechar='"')
            for row in csv_reader:
                #print row
                #for item in row:
                    #print item
                #if row_no == stop_row:
                    #return
                if row_no == 1:
                    row_no = row_no + 1
                else:
                    purpose = ""
                    recp_org_name = str(row[recepient_col])
                    don_org_name = str(row[donor_col]) + str(" ") 
                    grants = str(row[grands_col]).split(".",1)[0]
                    try:
                        if purp_col != -1:
                            purpose = str(row[purp_col]) + str(" ") 
                        else:
                            purpose = "NA"
                    except:
                        purpose = "NA"
                        
                    if str(recp_org_name).upper() in unvi_list:
                        univ_grants_info.append([str(recp_org_name).upper(), don_org_name, grants, purpose])
                        
                    if str(recp_org_name).upper() in unvi_list[0]:
                        if str(don_org_name).upper() in umad_grants_dict:
                            umad_grants_dict[str(don_org_name).upper()].append(grants)
                        else:
                            umad_grants_dict[str(don_org_name).upper()] = [grants]
                            
                        umad.append([unvi_list[0], don_org_name, grants, purpose])
                        
                    if str(recp_org_name).upper() in unvi_list[1]:
                        if str(don_org_name).upper() in umad_grants_dict:
                            umich_grants_dict[str(don_org_name).upper()].append(grants)
                        else:
                            umich_grants_dict[str(don_org_name).upper()] = [grants]
                            
                        umich.append([unvi_list[1], don_org_name, grants, purpose])                    
                    
                    if "hospital" in str(recp_org_name).lower():
                        None
                        #print str(recp_org_name) + str(don_org_name) + str(grants) + str(purpose)
                        if "university" in str(recp_org_name).lower() or "college" in str(recp_org_name).lower():
                            None
                            univ_hos.append([str(recp_org_name).upper(), don_org_name, grants, purpose])
                            #univ_grants_info.append([str(recp_org_name).upper(), don_org_name, grants, purpose])
                            #print str(recp_org_name) + str(don_org_name) + str(grants) + str(purpose)
                            #if "wisconsin" in str(recp_org_name).lower():
                                #umad.append([unvi_list[0], don_org_name, grants, purpose])
                                ##print str(recp_org_name) + str(don_org_name) + str(grants) + str(purpose)
                            #if "michigan" in str(recp_org_name).lower():
                                #umich.append([unvi_list[1], don_org_name, grants, purpose])                    
                                ##print str(recp_org_name) + str(don_org_name) + str(grants) + str(purpose)
                       
                        ##donor_list = [str(don_org_name).upper(), str(grants).upper()]
                        #donor_list = [str(str(don_org_name).upper() + " = " + str(grants).upper())]
                        #univ_donors[str(recp_org_name).upper()].append(donor_list)
                        #univ_grants[str(recp_org_name).upper()].append(int(grants))

                    row_no = row_no + 1
                    
        #for univ in univ_donors:
            #print str(univ) + " DONORS " + str(univ_donors[univ])    
        
                    
    except Exception,e: 
        traceback.print_exc(file=sys.stdout)
        #print "Unexpected error:", sys.exc_info()[0]
        #print str(e)
            
    return 

def extract_irs_sections(data_file, don_col, don_ein_col, rec_col, rec_ein_col, irc_sec_col, org_cash_col, non_org_cash_col, purp_col):
    row_no = 1
    
    try:
        with open(data_file, 'rb') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter='|', quotechar='"')
            for row in csv_reader:
                #print row
                #for item in row:
                    #print item
                #if row_no == stop_row:
                    #return
                if row_no == 1:
                    row_no = row_no + 1
                else:
                    purpose = ""
                    recp_org_name = str(row[rec_col])
                    don_org_name = str(row[don_col]) + str(" ") 
                    don_org_ein = str(row[don_ein_col])
                    org_cash = str(row[org_cash_col]).split(".",1)[0]
                
                    try:
                        if purp_col != -1:
                            purpose = str(row[purp_col]) + str(" ") 
                        else:
                            purpose = "NA"
                        
                        if rec_ein_col != -1:
                            recp_org_ein = str(row[rec_ein_col])
                        else:
                            recp_org_ein = "NA"                        

                        if irc_sec_col != -1:
                            irs_sec = str(row[irc_sec_col])
                        else:
                            irs_sec = "NA"                        
                        
                        if non_org_cash_col != -1:
                            non_org_cash = str(row[non_org_cash_col]).split(".",1)[0]
                        else:
                            non_org_cash = "NA"                                                
                            
                            
                    except:
                        purpose = "NA"
                        recp_org_ein = "NA"                        
                        irs_sec = "NA" 
                        non_org_cash = "NA"                                                
                        
                    sec_found = False
                    
                    if(sec_found == False):
                        for text in irs_sec_501_texts:
                            if(sec_found == False):
                                if text in str(irs_sec).upper():
                                    irs_sec_501.append([don_org_ein, don_org_name, recp_org_ein, recp_org_name, org_cash, non_org_cash, purpose])
                                    sec_found = True
                    
                    if (sec_found == False):
                        for text in irs_sec_univ_col_texts:
                            if(sec_found == False):
                                if text in str(irs_sec).upper():
                                    irs_sec_univ_col.append([don_org_ein, don_org_name, recp_org_ein, recp_org_name, org_cash, non_org_cash, purpose])                    
                                    sec_found = True
                               
                    if (sec_found == False):
                        for text in irs_sec_gov_texts:
                            if(sec_found == False):
                                if text in str(irs_sec).upper():
                                    irs_sec_gov.append([don_org_ein, don_org_name, recp_org_ein, recp_org_name, org_cash, non_org_cash, purpose])
                                    sec_found = True

                    if (sec_found == False):
                        irs_sec_other.append([don_org_ein, don_org_name, recp_org_ein, recp_org_name, org_cash, non_org_cash, purpose])
                        sec_found = True

                    row_no = row_no + 1
                    
                
                    
    except Exception,e: 
        traceback.print_exc(file=sys.stdout)
        #print "Unexpected error:", sys.exc_info()[0]
        #print str(e)
            
    return 

def irs_sec():
    
    #extract_irs_sections("../../Dataset/Guidestar/guidestar_990/f990_Sched_I_Part_II_Gov_Grant.txt", 1, 0, 4, 10, 11, 12, 13, 16)
    #extract_irs_sections("../../Dataset/Guidestar/guidestar_990PF/PF990_Part_XV_Grants_Paid.txt",    1, 0, 4, -1, -1, 8, -1, -1)    

    extract_irs_sections(f990_Sched_I_Part_II_Gov_Grant_file_name, 1, 0, 4, 10, 11, 12, 13, 16)
    extract_irs_sections(pf990_Part_XV_Grants_Paid_file_name,      1, 0, 4, -1, -1, 8, -1, -1)    

    with open('irs_sec_501.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["C_EIN", "C_ORG_NAME", "EIN", "ORG_NAME", "ORG_CASH", "NON_ORG_CASH", "PURPOSE"]) 
        for grant in irs_sec_501:
            csv_writer.writerow([ grant[0], grant[1], grant[2], grant[3], grant[4], grant[5], grant[6] ])      
            
    
    with open('irs_sec_univ_col.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["C_EIN", "C_ORG_NAME", "EIN", "ORG_NAME", "ORG_CASH", "NON_ORG_CASH", "PURPOSE"]) 
        for grant in irs_sec_univ_col:
            csv_writer.writerow([ grant[0], grant[1], grant[2], grant[3], grant[4], grant[5], grant[6] ])      


    with open('irs_sec_gov.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["C_EIN", "C_ORG_NAME", "EIN", "ORG_NAME", "ORG_CASH", "NON_ORG_CASH", "PURPOSE"]) 
        for grant in irs_sec_gov:
            csv_writer.writerow([ grant[0], grant[1], grant[2], grant[3], grant[4], grant[5], grant[6] ])   
            

    with open('irs_sec_other.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["C_EIN", "C_ORG_NAME", "EIN", "ORG_NAME", "ORG_CASH", "NON_ORG_CASH", "PURPOSE"]) 
        for grant in irs_sec_other:
            csv_writer.writerow([ grant[0], grant[1], grant[2], grant[3], grant[4], grant[5], grant[6] ])      

    

    return

def univ_grants():
    
    #extract_univ_grants("../../Dataset/Guidestar/guidestar_990/f990_Sched_I_Part_II_Gov_Grant.txt", 1, 4, 12, 16)
    #extract_univ_grants("../../Dataset/Guidestar/guidestar_990PF/PF990_Part_XV_Grants_Paid.txt", 1, 4, 8, -1)

    extract_univ_grants(f990_Sched_I_Part_II_Gov_Grant_file_name, 1, 4, 12, 16)
    extract_univ_grants(pf990_Part_XV_Grants_Paid_file_name, 1, 4, 8, -1)
    
    with open('university_grants.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["ORG_NAME", "DONORS", "GRANT", "PURPOSE"]) 
        for univ in univ_grants_info:
            csv_writer.writerow([ univ[0], univ[1], univ[2], univ[3] ])  
            
      
            
    with open('university_grants_umad_umich_new.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["ORG_NAME", "DONOR", "GRANTS", "NO OF GRANTS", "TOTAL",  "PURPOSE"]) 
        for donor in umad_grants_dict:
            grants = umad_grants_dict[donor]
            total_grant = 0
            for grant in grants:
                total_grant = total_grant + int(grant) 
            csv_writer.writerow([ unvi_list[0], donor, str(grants).replace("[","").replace("]","").replace("'",""), len(grants), total_grant ])     
                
        for donor in umich_grants_dict:
            grants = umich_grants_dict[donor]
            total_grant = 0
            for grant in grants:
                total_grant = total_grant + int(grant) 
            csv_writer.writerow([ unvi_list[1], donor, str(grants).replace("[","").replace("]","").replace("'",""), len(grants), total_grant ])     
            
    #with open('university_hospital_grants.csv', 'wb') as csvfile:
        #csv_writer = csv.writer(csvfile, delimiter=',',
                                #quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #csv_writer.writerow(["ORG_NAME", "DONORS", "GRANT", "PURPOSE"]) 
        #for hos in univ_hos:
            #csv_writer.writerow([ hos[0], hos[1], hos[2], hos[3] ])         
        
        
    return    
    

def npo2npo():
    #TODO
    
    
    return 

def display_help():
    print "Usage:"
    print "Argument 1)f990_Sched_I_Part_II_Gov_Grant file path from guidestar"
    print "Argument 2)PF990_Part_XV_Grants_Paid file path from guidestar"
    print "Argument 3)option ('1' university grants information extraction. '2' IRS section wise data segeration of grants)"
    
    print "Example:"
    print "python grants_extraction.py gov_grants.txt grants_paid.txt 1"
    
    sys.exit(0)
    return 

def get_args():
    global f990_Sched_I_Part_II_Gov_Grant_file_name, pf990_Part_XV_Grants_Paid_file_name, option
    
    try:
        f990_Sched_I_Part_II_Gov_Grant_file_name = sys.argv[1]
        if(os.path.isfile(f990_Sched_I_Part_II_Gov_Grant_file_name) == False):
            print "Error: %s cannot be opened" %(f990_Sched_I_Part_II_Gov_Grant_file_name)
            display_help()
            
        pf990_Part_XV_Grants_Paid_file_name = sys.argv[2]
        if(os.path.isfile(pf990_Part_XV_Grants_Paid_file_name) == False):
                    print "Error: %s cannot be opened" %(pf990_Part_XV_Grants_Paid_file_name)
                    display_help()

        try:
            option = int(sys.argv[3])
            
        except ValueError:
            print("Error: option is not an valid")
            
            display_help()
    
    except Exception,e: 
        display_help()
        #traceback.print_exc(file=sys.stdout)
               
    return

def main():
    
    get_args()
    
    if option == 1:
        univ_grants()
        
    elif option == 2:
        irs_sec()

    else:
        display_help()

    return 
    
    

if __name__ == "__main__":
    main()