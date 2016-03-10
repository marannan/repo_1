import sys
import os
import csv
from pprint import pprint
import time
import re
import traceback
import pandas



def get_data(file_name):
    #data = {}
    data = []

    #try:
        #data = pandas.read_csv(file_name, sep='|')
        
    #except:
        #traceback.print_exc(file=sys.stdout)   
        
        
    try:    
        with open(file_name, 'rb') as csvfile:
            csv_data = csv.reader(csvfile, delimiter='|', quotechar='"')
            for row in csv_data:
                data.append(row)        

    except:
        traceback.print_exc(file=sys.stdout)           

    
    return data

def extract_grants_990PF():
    univs =    ["univ", "colleg"]
    hopitals = ["hospital", "clinic"]
    science =  ["science", "research", "technology", "innovation"]
    edu =      ["institute", "education"]
    
    data = get_data("../../Dataset/Guidestar/guidestar_990PF/PF990_Part_XV_Grants_Paid.txt")
          
    data.pop(0) #remove the header
    
    
    univ_orgs = []
    hosital_orgs = []
    science_orgs = []
    education_orgs = []
    other_orgs = []
            
    for org in data:
        org_name = str(org[4]).lower()
        
        found = False
        
        for word in univs:
            if found == False:
                if word in org_name:
                    #print org_name
                    univ_orgs.append(org)
                    found = True
                    
        
        if found == False:
            for word in hopitals:
                if found == False:
                    if word in org_name:
                        #print org_name
                        hosital_orgs.append(org)
                        found = True
                        
        
        if found == False:
            for word in science:
                if found == False:
                    if word in org_name:
                        #print org_name
                        science_orgs.append(org)
                        found = True        
            
        
        if found == False:
            for word in edu:
                if found == False:
                    if word in org_name:
                        #print org_name
                        education_orgs.append(org)
                        found = True            
        
            
        if found == False:
            #print org_name
            other_orgs.append(org)

            
        
    

    univ_org_cash = 0
    for org in univ_orgs:
        org_name = org[4]
        cash = org[8]
        
        if cash == "":
            cash = 0
        else:
            cash = int(org[8].split(".",1)[0])
            
        univ_org_cash = univ_org_cash + cash
    
    hosital_org_cash = 0
    for org in hosital_orgs:
        org_name = org[4]
        cash = org[8]
        
        if cash == "":
            cash = 0
        else:
            cash = int(org[8].split(".",1)[0])        
            
        hosital_org_cash = hosital_org_cash + cash
    
    science_org_cash = 0
    for org in science_orgs:
        org_name = org[4]
        cash = org[8]
        
        if cash == "":
            cash = 0
        else:
            cash = int(org[8].split(".",1)[0])        
            
        science_org_cash = science_org_cash + cash
    
    education_org_cash = 0 
    for org in education_orgs:
        org_name = org[4]
        cash = org[8]
        
        if cash == "":
            cash = 0
        else:
            cash = int(org[8].split(".",1)[0])        

        education_org_cash = education_org_cash + cash
        
    other_org_cash = 0
    for org in other_orgs:
        org_name = org[4]
        cash = org[8]
        
        if cash == "":
            cash = 0
        else:
            cash = int(org[8].split(".",1)[0])        

        other_org_cash = other_org_cash + cash        
        
        
    print "990PF grants"
    print "total orgs :" + str(len(data)) 
    
    print str(len(univ_orgs)) + " : " + str(univ_org_cash)   
    print str(len(hosital_orgs)) + " : " + str(hosital_org_cash)   
    print str(len(science_orgs)) + " : " + str(science_org_cash)   
    print str(len(education_orgs)) + " : " + str(education_org_cash) 
    print str(len(other_orgs)) + " : " + str(other_org_cash) 
    
    print "------------"
    
    return

def extract_grants_990():
    univs =    ["univ", "colleg"]
    npos =     ["501", "3"]
    gov =      ["gov", "mun", "town", "county", "comm", "public", "state"]
    
    data = get_data("../../Dataset/Guidestar/guidestar_990/f990_Sched_I_Part_II_Gov_Grant.txt")
           
    data.pop(0) #remove the header
    
    
    univ_orgs = []
    npo_orgs = []
    gov_orgs = []
    other_orgs = []

            
    for org in data:
        org_name = str(org[1]).lower()
        sec = str(org[11]).lower()
        
        
        found = False
        
        for word in univs:
            if found == False:
                if word in org_name:
                    #print org_name
                    univ_orgs.append(org)
                    data.remove(org)
                    found = True
                
     
    
    #print "total univ orgs :" + str(len(univ_orgs)) 
    #print "total orgs :" + str(len(data)) 
    
    for org in data:
        org_name = str(org[1]).lower()
        sec = str(org[11]).lower()
        
        
        found = False                    
     
        
        if found == False:
            for word in npos:
                if found == False:
                    if word in sec:
                        #print org_name
                        npo_orgs.append(org)
                        found = True
                        
        
        if found == False:
            for word in gov:
                if found == False:
                    if word in sec:
                        #print org_name
                        gov_orgs.append(org)
                        found = True        
                       
        
            
        if found == False:
            #print org_name
            other_orgs.append(org)

            
        
    
    univ_org_cash = 0
    univ_non_org_cash = 0
    for org in univ_orgs:
        org_name = org[4]
        org_cash = org[12]
        non_org_cash = org[13]
        
        if org_cash == "":
            org_cash = 0
        else:
            org_cash = int(org[12].split(".",1)[0])
            
        
        if non_org_cash == "":
            non_org_cash = 0
        else:
            non_org_cash = int(org[13].split(".",1)[0])        
            
        univ_org_cash = univ_org_cash + org_cash
        univ_non_org_cash = univ_non_org_cash + non_org_cash
    
        
        
    npo_org_cash = 0
    npo_non_org_cash = 0
    for org in npo_orgs:
        org_name = org[4]
        org_cash = org[12]
        non_org_cash = org[13]
        
        if org_cash == "":
            org_cash = 0
        else:
            org_cash = int(org[12].split(".",1)[0])
            
        
        if non_org_cash == "":
            non_org_cash = 0
        else:
            non_org_cash = int(org[13].split(".",1)[0])        
            
        npo_org_cash = npo_org_cash + org_cash
        npo_non_org_cash = npo_non_org_cash + non_org_cash    
    
        
    
    gov_org_cash = 0
    gov_non_org_cash = 0
    for org in gov_orgs:
        org_name = org[4]
        org_cash = org[12]
        non_org_cash = org[13]
        
        if org_cash == "":
            org_cash = 0
        else:
            org_cash = int(org[12].split(".",1)[0])
            
        
        if non_org_cash == "":
            non_org_cash = 0
        else:
            non_org_cash = int(org[13].split(".",1)[0])        
            
        gov_org_cash = gov_org_cash + org_cash
        gov_non_org_cash = gov_non_org_cash + non_org_cash     
        
        
    
    other_org_cash = 0
    other_non_org_cash = 0
    for org in other_orgs:
        org_name = org[4]
        org_cash = org[12]
        non_org_cash = org[13]
        
        if org_cash == "":
            org_cash = 0
        else:
            org_cash = int(org[12].split(".",1)[0])
            
        
        if non_org_cash == "":
            non_org_cash = 0
        else:
            non_org_cash = int(org[13].split(".",1)[0])        
            
        other_org_cash = other_org_cash + org_cash
        other_non_org_cash = other_non_org_cash + non_org_cash      
        
        
    print "990 grants"
    print "total orgs :" + str(len(data)) 
    
    print str(len(univ_orgs)) + " : " + str(univ_org_cash)  + " : " + str(univ_non_org_cash)   
    print str(len(npo_orgs)) + " : " + str(npo_org_cash)  + " : " + str(npo_non_org_cash)
    print str(len(gov_orgs)) + " : " + str(gov_org_cash)   + " : " + str(gov_non_org_cash)
    print str(len(other_orgs)) + " : " + str(other_org_cash) + " : " + str(other_non_org_cash)
    
    print "---------"

    return

if __name__ == "__main__":
    extract_grants_990()
    extract_grants_990PF()
    
    
    
