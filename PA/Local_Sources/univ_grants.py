#ashok_marannan

import sys
import os
import csv
from pprint import pprint
import time
import re


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
"UNIVERSITY OF WISCONSIN FOUNDATION": [0],
"UNIVERSITY OF MICHIGAN": [0], 
"UNIVERSITY OF MINNESOTA": [0],
"INDIANA UNIVERSITY": [0],
"PENNSYLVANIA STATE UNIVERSITY": [0],
"PURDUE UNIVERSITY": [0],
"THE OHIO STATE UNIVERSITY": [0],
"UNIVERSITY OF CHICAGO": [0],
"UNIVERSITY OF IOWA": [0],}


def read_csv_data(data_file, donor_col, recepient_col, grands_col):
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
                    recp_org_name = str(row[recepient_col])
                    don_org_name = str(row[donor_col]) + str(" ") 
                    grants = str(row[grands_col]).split(".",1)[0]
                    if str(recp_org_name).upper() in unvi_list:
                        #donor_list = [str(don_org_name).upper(), str(grants).upper()]
                        donor_list = [str(str(don_org_name).upper() + " = " + str(grants).upper())]
                        univ_donors[str(recp_org_name).upper()].append(donor_list)
                        univ_grants[str(recp_org_name).upper()].append(int(grants))

                    row_no = row_no + 1
                    
        #for univ in univ_donors:
            #print str(univ) + " DONORS " + str(univ_donors[univ])    
        
                    
    except Exception,e: 
        print "Unexpected error:", sys.exc_info()[0]
        print str(e)
            
    return 


def main():
    
    #print "Govt Grants"
    #print "--------------"    
    read_csv_data("../Dataset/Guidestar/guidestar_990/f990_Sched_I_Part_II_Gov_Grant.txt", 1, 4, 12)
    #print "------------------"
    
    #print "Private Grants"
    #print "--------------"
    read_csv_data("../Dataset/Guidestar/guidestar_990PF/PF990_Part_XV_Grants_Paid.txt", 1, 4, 8)
    #print "-------------------"
    

    with open('university_donors.csv', 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["ORG_NAME", "DONORS", "TOTAL_GRANT"]) 
        for univ in univ_donors:
            govt_donors = []
            private_donors = []
            donors = []
            donors.append(univ_donors[univ])
            csv_writer.writerow([univ, str(donors).replace("[","").replace("]","").replace("'",""), sum(univ_grants[univ])])     
    
    print "University Grants"
    print "-----------------"
    for univ in univ_donors:
        print "University : " + str(univ) 
        print "Donors List : "
        for donor in univ_donors[univ]:
            print str(donor).replace('[',"").replace("]","").replace("'","")
        print "Total Grants : " + str(sum(univ_grants[univ]))
        print "-----------------------"
        
        
    return

if __name__ == "__main__":
    main()