import json
import os
import sys
import re

json_product_data = []
colors_dict = []
extracted_colors = []
product_count = 0
error_parsing_count = 0
match_count = 0
nomatch_count = 0
right_count = 0
wrong_count = 0 
idk_count = 0 
false_positive = 0
false_negative = 0
attr_1 = "Color"
attr_2 = "Actual Color"
p1_attr_values  = []
p2_attr_values  = []

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
     
def extract_attribute_val(product, attr_1, attr_2, product_info):
     
     global extracted_colors
     
     extracted_attr_values = []
       
     try:
          #product_desp = product[product_info]     
          #for line in product_desp:
               #for word in line.split():
                    ##matched_color = filter(lambda x: x in word.lower(),colors_dict)
                    ##if matched_color:
                    #if word.lower() in colors_dict:
                         ##extracted_colors.append(matched_color[0])
                         ##product_color = matched_color[0]
                         #extracted_attr_value = word                         
                         ##print "Product %s: Color = %s" %(str(product_no), str(product_color).lower()) + " (after extraction)"               
                         #extracted_attr_values.append(extracted_attr_value)
                         #extracted_colors.append(word)
                         
          product_desp = product[product_info]     
          for color in colors_dict:
               if " "+color.lower()+" " in str(product_desp).lower():  
               #if re.search(color, str(product_desp), re.IGNORECASE):
                    extracted_attr_value = color.lower()                         
                    #print "Product %s: Color = %s" %(str(product_no), str(product_color).lower()) + " (after extraction)"               
                    extracted_attr_values.append(extracted_attr_value)
                    extracted_colors.append(extracted_attr_value)
     
     #except:
          #product_long_desp = "" #no long product description, continue
          ##print "Product %s: Color = %s" %(str(product_no), str(product_color).lower()) + " (after extraction)"
     
     except Exception, e:
          error = "Couldn't do it: %s" % e     
     
     return extracted_attr_values

def extract_attribute_value(product, attr_1, attr_2):
     product_info = ["Product Long Description", "Product Short Description", "Product Name", "Manufacture Part Number"]
     extracted_attr_values = []
     
     for info in product_info:
          extracted_attr_values = extracted_attr_values + extract_attribute_val(product, attr_1, attr_2, info)
          
     return extracted_attr_values
     
     
def get_attribute_value(product, attribute):
     attribute_values = []
     attribute_found = False
     try:     
          temp_str, attribute_val = str(product[attribute]).split("'",1)
          attribute_val, temp_str = attribute_val.split("'",1)   
          if attribute_val.lower() == "other":
               attribute_found = False
          else:
               if '/' in attribute_val:
                    attribute_val_1, attribute_val_2 = attribute_val.split("/",1)   
                    attribute_values.append(attribute_val_1.lower())
                    attribute_values.append(attribute_val_2.lower())
               else:
                    attribute_values.append(attribute_val.lower())
               attribute_found = True
               
     except:
          attribute_found = False
     
     return (attribute_values, attribute_found)
          
def find_match(p1, p2, attr_1, attr_2):
     p1_attr_values = []
     p2_attr_values = []
     p1_attr_1_values = []
     p1_attr_2_values = []
     p1_attr_1_found = False
     p1_attr_2_found = False     
     p2_attr_1_values = []
     p2_attr_2_values = []     
     p2_attr_1_found = False
     p2_attr_2_found = False  
     
     

     #getting color attribute value for product 1
     (p1_attr_1_values,p1_attr_1_found)  = get_attribute_value(p1,attr_1)
     
     #getting actual color attribute value for product 1
     (p1_attr_2_values,p2_attr_2_found)  = get_attribute_value(p1,attr_2)
     
     p1_attr_values = p1_attr_1_values + p1_attr_2_values
     
     #extracting color attribute values for product 1 if color or actual color attributes are not available/valid
     if len(p1_attr_values) == 0 or "Multicolor" in p1_attr_values:
          p1_attr_values = p1_attr_values + extract_attribute_value(p1, attr_1, attr_2)
     
     
     
     #getting color attribute value for product 1
     (p2_attr_1_values,p1_attr_1_found)  = get_attribute_value(p2,attr_1)
     
     #getting actual color attribute value for product 1
     (p2_attr_2_values,p2_attr_2_found)  = get_attribute_value(p2,attr_2)
     
     p2_attr_values = p2_attr_1_values + p2_attr_2_values
     
     
     #extracting color attribute values for product 1 if color or actual color attributes are not available/valid
     if len(p2_attr_values) == 0 or "Multicolor" in p2_attr_values:
          p2_attr_values = p2_attr_values + extract_attribute_value(p2, attr_1, attr_2)
     

     #case 1: find intersection of two lists
     for val_1 in p1_attr_values:
          for val_2 in p2_attr_values:
               if val_1 in val_2:
                    return ("match", p1_attr_values, p2_attr_values)
     
     #case 2: probe for extracted colors from product 1 in product 2
     for val_1 in p1_attr_values:
          if val_1 in str(p2).lower():
               p2_attr_values.append(val_1)
               return ("match", p1_attr_values, p2_attr_values)
          
     #case 3: probe for extracted colors from product 2 in product 1
     for val_1 in p2_attr_values:
          if val_1 in str(p1).lower():
               p1_attr_values.append(val_1)
               return ("match", p1_attr_values, p2_attr_values)
          
     
     #case 4: use dictionary to find if there is a match
     for color in colors_dict:
          if " "+color+" " in str(p1).lower() and " "+color+" " in str(p2).lower():
               p1_attr_values.append(color)
               p2_attr_values.append(color)
               return ("match", p1_attr_values, p2_attr_values)

          
     #case 5: return idk if nothing is extracted for attribute
     if len(p1_attr_values) == 0 or len(p2_attr_values) == 0:
          return ("idk", p1_attr_values, p2_attr_values)
     
     #case 6: return nomatch finally
     return ("nomatch", p1_attr_values, p2_attr_values)
     

def calculate_metrics(labelled_data, predicted_data, p1_attr_values, p2_attr_values):

          if (predicted_data.lower() == "match" and labelled_data.lower() == "match"): 
               right_count = right_count + 1
     
          if (predicted_data.lower() == "match" and labelled_data.lower() == "nomatch"): 
               wrong_count = wrong_count + 1     
               false_negative = false_negative + 1
     
          if (predicted_data.lower() == "match" and labelled_data.lower() == "idk"): 
               wrong_count = wrong_count + 1     
               false_positive = false_positive + 1  
     
          if (predicted_data.lower() == "nomatch" and labelled_data.lower() == "nomatch"): 
               right_count = right_count + 1  
     
          if (predicted_data.lower() == "nomatch" and labelled_data.lower() == "match"): 
               wrong_count = wrong_count + 1     
               false_positive = false_positive + 1  
     
          if (predicted_data.lower() == "nomatch" and labelled_data.lower() == "idk"): 
               wrong_count = wrong_count + 1     
               false_positive = false_positive + 1 
     
          if (predicted_data.lower() == "idk" and labelled_data.lower() == "idk"): 
               right_count = right_count + 1  
               idk_count = idk_count + 1
     
          if (predicted_data.lower() == "idk" and labelled_data.lower() == "match"): 
               wrong_count = wrong_count + 1
               false_positive = false_positive + 1 
     
          if (predicted_data.lower() == "idk" and labelled_data.lower() == "nomatch"): 
               wrong_count = wrong_count + 1
               false_negative = false_negative + 1
          
          print str(product_count) + " " + labelled_data + " " + predicted_data
          print p1_attr_values
          print p2_attr_values      


def calculate_metrics_1(product_count, predicted_data, p1_attr_values, p2_attr_values):
     global match_count, nomatch_count, idk_count

     if predicted_data.lower() == "match":
          match_count = match_count + 1  

     if predicted_data.lower() == "nomatch":
          nomatch_count = nomatch_count + 1  

     if predicted_data.lower() == "idk":
          idk_count = idk_count + 1  

     print str(product_count) + " " + predicted_data
     print p1_attr_values
     print p2_attr_values     

def display_results():
     global product_count, error_parsing_count, right_count, wrong_count, idk_count, false_negative, false_negative, extracted_colors
     
     print "pairs processed     : ", product_count
     print "error parsing       : ", error_parsing_count
     print "coverage            : ", 100 * float(product_count - error_parsing_count - idk_count)/float(product_count-error_parsing_count)
     print "right prediction    : ", right_count
     print "wrong prediction    : ", wrong_count
     print "i dont know         : ", idk_count
     print "false_positive      : ", false_positive
     print "false negative      : ", false_negative
     print "accuracy            : ", 100 * float(right_count)/float(product_count - error_parsing_count -  idk_count)
     print "colors extrated for : ", len(extracted_colors)
     print "extrated colors     : ", list(set(extracted_colors)) 
     
def display_results_1():
     global product_count, error_parsing_count, match_count, nomatch_count, idk_count
     
     print "pairs processed     : ", product_count
     print "error parsing       : ", error_parsing_count
     print "coverage            : ", 100 * float(product_count - error_parsing_count - idk_count)/float(product_count-error_parsing_count)
     print "match               : ", match_count
     print "nomatch             : ", nomatch_count
     print "i dont know         : ", idk_count
     print "colors extrated for : ", len(extracted_colors)
     print "extrated colors     : ", list(set(extracted_colors)) 
     
        
def predict_match(input_file):
     global error_parsing_count, right_count, wrong_count, idk_count, product_count, false_positive, false_negative
     p1_attr_1_values = []
     p1_attr_2_values = []     
     with open(input_file) as data_file:
          i = 1
          while True:
               line = data_file.readline()
               
               if len(line) == 0:
                    break
     
               leading_str,trailing_str = line.split("{",1)
          
               trailing_str = "{" + trailing_str
                               
               json_data_1, trailing_str = trailing_str.split("?",1)
               
               try:
                    json_product_data.append(uni_to_ascii(json.loads(json_data_1)))
                    product_1 = uni_to_ascii(json.loads(json_data_1))
               except:
                    #print "Product parsing error at line %s ",(i)
                    error_parsing_count = error_parsing_count + 1
     
               #print "****************"
               #print "Product " +str(i)
               #print json_data_1
               #print "****************"
     
     
               leading_str,trailing_str = trailing_str.split("{",1)
     
               trailing_str = "{" + trailing_str
     
               json_data_2, trailing_str = trailing_str.split("?",1)
               
               #leading_str, labelled_data = trailing_str.split("?",1)
               
               #labelled_data, trailing_str = trailing_str.split("?",1)
               
               #labelled_data, trailing_str = labelled_data.split("\n",1)
               
               #if(labelled_data == "MISMATCH"):
                    #labelled_data = "nomatch"               
               
               #print "Product " +str(i)
               #print json_data_2
               #print "****************"
     
               try:
                    json_product_data.append(uni_to_ascii(json.loads(json_data_2)))
                    product_2 = uni_to_ascii(json.loads(json_data_2))
             
               except:
                    #print "Product parsing error at line %s ",(i)
                    error_parsing_count = error_parsing_count + 1
                    
               
               (predicted_data, p1_attr_values, p2_attr_values) = find_match(product_1, product_2, attr_1, attr_2)
               product_count = product_count + 1
               
               #print str(product_count) + " " + labelled_data.lower() +" " + is_match.lower()
               
               #calculate_metrics(labelled_data, predicted_data, p1_attr_values, p2_attr_values)
               
               calculate_metrics_1(product_count, predicted_data, p1_attr_values, p2_attr_values)
                                  
             
               #print "****************"
     
               i = i + 1
              

def main():
     input_file = sys.argv[1]
     input_file_1 = "sample_elec_pairs_labelled.txt"
     input_file_2 = "elec_pairs_40K.txt"
     colors_dict_file = "colors_dict.txt"
     get_colors_dict(colors_dict_file)
     predict_match(input_file)
     display_results_1()
     print "extracting data from file is completed!"
     return 

if __name__ == "__main__":
     main()
