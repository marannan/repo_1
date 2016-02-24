import re
import json
import traceback
import sys
import operator


attributes = {}
error_parsing = 0


def get_attributes(json_in):
    global error_parsing
    try:
        json_obj = json.loads(json_in)
        for attribute in json_obj:
            if str(attribute).lower() not in attributes:
                attributes[str(attribute).lower()] = []
            attributes[str(attribute).lower()].append(json_obj[attribute])               
               
            #if str(attribute).lower() in attributes:
                #attributes[str(attribute).lower()] = attributes[str(attribute).lower()] + 1 
            #else:
                #attributes[str(attribute).lower()] = 1 
    
    except Exception,e: 
        error_parsing = error_parsing + 1
        #print "error: parsing " + str(json_in)
        #traceback.print_exc(file=sys.stdout)           

def extract_json():
    try:
        lines_processed = 0
        with open("elec_pairs_stage1.txt") as product_pairs:
            for line in product_pairs:
                (pairid, wid, json_1, vid, json_2, label) =  line.split("?")
                get_attributes(json_1)
                get_attributes(json_2)
                lines_processed = lines_processed + 1
       
        
            

    except Exception,e: 
        traceback.print_exc(file=sys.stdout)   
    
    sort_attr = attributes.items()
    sort_attr = sorted(sort_attr, key = lambda x: len(x[1]))
    sort_attr = sort_attr[::-1]
    
            
    print "total products: " + str(lines_processed * 2)
    print "error parsing : " + str(error_parsing )    
    print "---------------------------" 
    #print "total attributes: " + str(total_attributes)
    print "top 10 attributes" 
    print "---------------------------" 
    
    for i in xrange(10):
        percent_found  = ( float(len(sort_attr[i][1])) / float(lines_processed * 2) ) * 100
        percent_missing = 100 - percent_found        
        print "name: " + str(sort_attr[i][0])
        print "no of occurance: " + str(len(sort_attr[i][1]))
        print "percent missing: " + str(percent_missing)
        print "attribute type: " + str(type(sort_attr[i][1][0][0]))
        print "----------------------------------------" 


    #for (key,value) in reversed(sorted_attributes):
        #count  = count + 1
        #if count == 11:
            #break
        #
        #print str(key) + " : " + str(value) + " percent missing : " + str(percent_missing) 

if __name__ == "__main__":
    extract_json()
            
    
        