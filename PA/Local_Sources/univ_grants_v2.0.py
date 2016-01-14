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


def read_csv_data(data_file, donor_col, recepient_col, grands_col, purp_col = 0):
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
                        umad.append([unvi_list[0], don_org_name, grants, purpose])
                    if str(recp_org_name).upper() in unvi_list[1]:
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

def npo2npo():
    #TODO
    
    
    return 


def main():
    
    #print "Govt Grants"
    #print "--------------"    
    read_csv_data("../../Dataset/Guidestar/guidestar_990/f990_Sched_I_Part_II_Gov_Grant.txt", 1, 4, 12, 16)
    #print "------------------"
    
    #print "Private Grants"
    #print "--------------"
    read_csv_data("../../Dataset/Guidestar/guidestar_990PF/PF990_Part_XV_Grants_Paid.txt", 1, 4, 8, -1)
    #print "-------------------"
    

    with open('university_grants.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["ORG_NAME", "DONORS", "GRANT", "PURPOSE"]) 
        for univ in univ_grants_info:
            csv_writer.writerow([ univ[0], univ[1], univ[2], univ[3] ])     
            
            
    with open('university_grants_umad_umich.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["ORG_NAME", "DONORS", "GRANT", "PURPOSE"]) 
        for univ in univ_grants_info:
            if univ[0] == unvi_list[0]:
                csv_writer.writerow([ univ[0], univ[1], univ[2], univ[3] ])     
                
        for univ in univ_grants_info:
            if univ[0] == unvi_list[1]:
                csv_writer.writerow([ univ[0], univ[1], univ[2], univ[3] ])         
            
    with open('university_hospital_grants.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["ORG_NAME", "DONORS", "GRANT", "PURPOSE"]) 
        for hos in univ_hos:
            csv_writer.writerow([ hos[0], hos[1], hos[2], hos[3] ])         
    
    
    #print "University Grants"
    #print "-----------------"
    #for univ in univ_donors:
        #print "University : " + str(univ) 
        #print "Donors List : "
        #for donor in univ_donors[univ]:
            #print str(donor).replace('[',"").replace("]","").replace("'","")
        #print "Total Grants : " + str(sum(univ_grants[univ]))
        #print "-----------------------"
        
        
    return

if __name__ == "__main__":
    main()