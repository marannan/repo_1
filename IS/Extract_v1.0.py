import json
import os
import sys

json_product_data = []
colors_dict = []

match_counter = 0
not_sure_counter = 0
not_match_counter = 0
error_parsing_counter = 0
extracted_colors = []
right_counter = 0
wrong_counter = 0 
idk_counter = 0 

def uni_to_ascii(input):
     if isinstance(input,unicode):
          return input.encode('ascii')
     elif isinstance(input, list):
          return [uni_to_ascii(ele) for ele in input]
     elif isinstance(input, dict):
          return {uni_to_ascii(key):uni_to_ascii(val) for key,val in input.items()}

def get_colors_dict(colors_dict_file):
     with open(colors_dict_file) as colors_dictionary:
          while True:
               line = colors_dictionary.readline()
               if len(line) == 0:
                    break 
               color, newline = line.split("\n", 1)
               colors_dict.append(color)
     
def find_color(product, product_no):
     global extracted_colors
     try:
          product_1_short_desp = product["Product Short Description"]
          
          for line in product_1_short_desp:
               for word in line.split():
                    #matched_color = filter(lambda x: x in word.lower(),colors_dict)
                    #if matched_color:
                    if word.lower() in colors_dict:
                         #extracted_colors.append(matched_color[0])
                         #product_color = matched_color[0]
                         extracted_colors.append(word)
                         product_color = word                         
                         #print "Product %s: Color = %s" %(str(product_no), str(product_color).lower()) + " (after extraction)"               
                         return product_color  
     except:
          product_1_short_desp = "" #no short product description, continue
                    
     try:
          product_1_long_desp = product["Product Long Description"]
          
          for line in product_1_long_desp:
                    for word in line.split():
                         #matched_color = filter(lambda x: x in word.lower(),colors_dict)
                         #if matched_color:
                         if word.lower() in colors_dict:
                              #extracted_colors.append(matched_color[0])
                              #product_color = matched_color[0]
                              extracted_colors.append(word)
                              product_color = word                         
                              #print "Product %s: Color = %s" %(str(product_no), str(product_color).lower()) + " (after extraction)"               
                              return product_color  
          
          product_color = "Not found"
          #print "Product %s: Color = %s" %(str(product_no), str(product_color).lower()) + " (after extraction)"               
          return product_color
                         
     except:
          product_color = "Not found"
          #print "Product %s: Color = %s" %(str(product_no), str(product_color).lower()) + " (after extraction)"               
          return product_color
        
def find_actual_color(product, product_no):
     
     try:     
          temp_str, product_color = str(product["Actual Color"]).split("'",1)
          product_color, temp_str = product_color.split("'",1)
          #print "Product %s: Actual Color = " %(str(product_no)) + str(product_color).lower()
          return product_color
          
     except:
          product_color = find_color(product, product_no)
          return product_color
  

     
def find_match(product_1, product_2):
     global match_counter, not_sure_counter, not_match_counter
     product_1_color_extracted = False
     product_2_color_extracted = False
     try:     
          temp_str, product_1_color = str(product_1["Color"]).split("'",1)
          product_1_color, temp_str = product_1_color.split("'",1)
          #print "Product 1: Color = " + str(product_1_color).lower()
          
     except:
          product_1_color = find_color(product_1,1) #extracting color
          product_1_color_extracted = True
          
     try:     
          temp_str, product_2_color = str(product_2["Color"]).split("'",1)
          product_2_color, temp_str = product_2_color.split("'",1)
          #print "Product 2: Color = " + str(product_2_color).lower()
                    
     except:
          product_2_color = find_color(product_2,2) #extracting color
          product_2_color_extracted = True


     if product_1_color.lower() == "other" or product_1_color.lower() == "multicolor": #or product_1_color.lower() == "not found":
          product_1_color = find_color(product_1,1) #extracting color
          product_1_color_extracted = True
          if product_1_color.lower() == "not found":
               product_1_color = find_actual_color(product_1,1) #extracting actual color
               product_1_color_extracted = True
               
     if product_1_color_extracted == True and product_1_color.lower() != "not found" and product_2_color.lower() == "not found": #if color 1 is extracted from product then find its occurance in the product 2
          if product_1_color.lower() in str(product_2).lower():
               match_counter = match_counter + 1
               #print "Product 1: Color = " + str(product_1_color).lower() +" found in Product 2"
               #if product_2_color_extracted == True:
                    #print "Product 2: Color = " + str(product_1_color).lower() + " (extracted)"
               return "match"               
               
              
     if product_2_color.lower() == "other" or product_2_color.lower() == "multicolor": #or product_2_color.lower() == "not found":
               product_2_color = find_color(product_2,2) #extracting color
               product_2_color_extracted = True
               if product_2_color.lower() == "not found":
                    product_2_color = find_actual_color(product_2,2) #extracting actual color  
                    product_2_color_extracted = True
     
     
     if product_2_color_extracted == True and product_2_color.lower() != "not found" and product_1_color.lower() == "not found": #if color 2 is extracted from product then find its occurance in the product 1
          if product_2_color.lower() in str(product_1).lower():
               match_counter = match_counter + 1
               #print "Product 2: Color = " + str(product_2_color).lower() +" found in Product 1"
               #if product_1_color_extracted == True:
                    #print "Product 1: Color = " + str(product_2_color).lower() + " (extracted)"
               return "match"            
     
     
     if product_1_color.lower() == product_2_color.lower() or product_1_color.lower() in product_2_color.lower() or product_2_color.lower() == product_1_color.lower() and (product_1_color.lower() != "not found" and product_2_color.lower() != "not found" and product_1_color.lower() != "other" and product_2_color.lower() != "other"):
          match_counter = match_counter + 1
          return "match"
     
     elif product_1_color.lower() == "not found" or product_2_color.lower() == "not found" or product_1_color.lower() == "other" or product_2_color.lower() == "other":
          not_sure_counter = not_sure_counter + 1
          return "idk"
     
     else:
          not_match_counter = not_match_counter + 1
          return "mismatch"
        

def extract(input_file):
     global error_parsing_counter, right_counter, wrong_counter, idk_counter
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
                    #print "Product parsing error at line %s ",(i)
                    error_parsing_counter = error_parsing_counter + 1
     
               #print "****************"
               #print "Product " +str(i)
               #print json_data_1
               #print "****************"
     
     
               leading_str,trailing_str = trailing_str.split("{",1)
     
               trailing_str = "{" + trailing_str
     
               json_data_2, trailing_str = trailing_str.split("?",1)
               
               labelled_data, leading_str = trailing_str.split("?",1)
               
               
               #print "Product " +str(i)
               #print json_data_2
               #print "****************"
     
               try:
                    json_product_data.append(uni_to_ascii(json.loads(json_data_2)))
                    product_2 = uni_to_ascii(json.loads(json_data_2))
             
               except:
                    #print "Product parsing error at line %s ",(i)
                    error_parsing_counter = error_parsing_counter + 1
                    
               
               is_match = find_match(product_1, product_2)
               print labelled_data.lower() +" " + is_match.lower()
               
               if labelled_data.lower() == is_match.lower():
                    right_counter = right_counter + 1
                    
               elif is_match.lower() == "idk":
                    idk_counter = idk_counter + 1
                    
               else:
                    wrong_counter = wrong_counter + 1
               
               #print "****************"
     
               i = i + 1
              

def main():
     input_file = sys.argv[1]
     input_file_1 = "sample_elec_pairs_labelled.txt"
     input_file_2 = "elec_pairs_40K.txt"
     colors_dict_file = "colors_dict.txt"
     get_colors_dict(colors_dict_file)
     extract(input_file)
     print "extracting data from file is completed!"
     print "error parsing       : ", error_parsing_counter
     print "right prediction    : ", right_counter
     print "wrong prediction    : ", wrong_counter
     print "i dont know         : ", idk_counter
     print "coverage            : ", float((325 - idk_counter)/325) * 100
     print "accuracy            : ", (right_counter/(325 - error_parsing_counter -  idk_counter))* 100
     print "colors extrated for : ", len(extracted_colors)
     print "extrated colors     : ", list(set(extracted_colors))
     print "accuracy : to be calculated"

if __name__ == "__main__":
     main()
