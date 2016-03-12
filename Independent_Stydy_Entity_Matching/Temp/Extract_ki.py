import json
import os
import sys

json_product_data = []
laptop_cases_dict = ["laptop bags & cases", "laptop-bags-cases", "laptop cases", "laptop bags and cases", "laptop-cases", "laptop-case", "laptop case" ]

match_counter = 0
not_sure_counter = 0
not_match_counter = 0
extracted_colors = []

def uni_to_ascii(input):
    if isinstance(input,unicode):
        return input.encode('ascii')
    elif isinstance(input, list):
        return [uni_to_ascii(ele) for ele in input]
    elif isinstance(input, dict):
        return {uni_to_ascii(key):uni_to_ascii(val) for key,val in input.items()}

 

def find_match(product_1, product_2):
    global match_counter, not_sure_counter, not_match_counter
    product_1_laptop_case = False
    product_2_laptop_case = False
    

    try:     
        for word in laptop_cases_dict:
            if word in product_1.lower():
                product_1_laptop_case = True
                    
    except:
        product_1_laptop_case = False
        
    print "product_1_laptop_case: " + str(product_1_laptop_case)
        
        
    try:     
        for word in laptop_cases_dict:
            if word in product_2.lower():
                product_2_laptop_case = True
                        
    
    except:
        product_2_laptop_case = False
            
    print "product_2_laptop_case: " + str(product_2_laptop_case)

    if product_1_laptop_case == True and product_2_laptop_case == True:
        match_counter = match_counter + 1
        return "Match"
    
    else:
        not_match_counter = not_match_counter + 1
        return "Not a match/ I dont know"


def extract(input_file):
    with open(input_file) as data_file:
        i = 1
        while True:
            line = data_file.readline()

            if len(line) == 0:
                break

            leading_str,trailing_str = line.split("{",1)

            trailing_str = "{" + trailing_str

            #print trailing_str

            json_data_1, trailing_str = trailing_str.split("?",1)

            try:
                json_product_data.append(uni_to_ascii(json.loads(json_data_1)))
                product_1 = uni_to_ascii(json.loads(json_data_1))
            except:
                print "Product parsing error at line %s ",(i)

            print "****************"
            print "Product " +str(i)
            print json_data_1
            print "****************"


            leading_str,trailing_str = trailing_str.split("{",1)

            trailing_str = "{" + trailing_str

            json_data_2, trailing_str = trailing_str.split("?",1)

            print "Product " +str(i)
            print json_data_2
            print "****************"

            try:
                json_product_data.append(uni_to_ascii(json.loads(json_data_2)))
                product_2 = uni_to_ascii(json.loads(json_data_2))

            except:
                print "Product parsing error at line %s ",(i)


            is_match = find_match(json_data_1, json_data_2)
            print "Match : " + is_match
            print "****************"

            i = i + 1


def main():
    input_file = "sample_elec_pairs.txt"
    extract(input_file)
    print "Extracting data from file is completed!"
    print "match      : ", match_counter
    print "not a match / not sure : ", not_match_counter
    print "accuracy : to be calculated"

if __name__ == "__main__":
    main()
