# encoding=utf8
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

def get_colors_from_dict(colors_dict_file):
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
          
def find_match(json_product_1, json_product_2, dictionary = "files/colors_dict.txt", attr_1 = "Color", attr_2 = "Actual Color"):
     """
     extracts values for attributes "Color" and "Actual Color" in the product pair and predicts a match based on the extracted values.
     :param:  json_str_a, json_str_b, <optional> dict=”path_to_user_dictionary", <optional> attr_1 = "name of first attribute", <optional> attri_2 = "name of second attribute"
     :return: 1 (match)
             0 (no match)
            -1 (not sure)
     
     """
       
     
     
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

     #return -1 (not sure) in case of error
     try:

          #return -1 (not sure) in case of parse error
          try:
               p1 = uni_to_ascii(json.loads(json_product_1))
               p2 = uni_to_ascii(json.loads(json_product_2))
          except:
               #return -1 (not sure) in case of parse error
               return (-1, 1)
          
          try:
               get_colors_from_dict(dictionary)
          except:
               print "error : dictionary cannot be loaded"
               none
     
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
                         #return ("match", p1_attr_values, p2_attr_values)
                         return (1,1)
          
          #case 2: probe for extracted colors from product 1 in product 2
          for val_1 in p1_attr_values:
               if val_1 in str(p2).lower():
                    p2_attr_values.append(val_1)
                    #return ("match", p1_attr_values, p2_attr_values)
                    return (1,1)
               
          #case 3: probe for extracted colors from product 2 in product 1
          for val_1 in p2_attr_values:
               if val_1 in str(p1).lower():
                    p1_attr_values.append(val_1)
                    #return ("match", p1_attr_values, p2_attr_values)
                    return (1,1)
               
          
          #case 4: use dictionary to find if there is a match
          for color in colors_dict:
               if " "+color+" " in str(p1).lower() and " "+color+" " in str(p2).lower():
                    p1_attr_values.append(color)
                    p2_attr_values.append(color)
                    #return ("match", p1_attr_values, p2_attr_values)
                    return (1,1)
     
               
          #case 5: return idk if nothing is extracted for attribute
          if len(p1_attr_values) == 0 or len(p2_attr_values) == 0:
               #return ("idk", p1_attr_values, p2_attr_values)
               return (-1,1)
          
          #case 6: return nomatch finally
          #return ("no match", p1_attr_values, p2_attr_values)
          return (0,1)
     
     #return -1 (not sure) in case of any error
     except:
          #return -1 (not sure) in case of parse error
          return(-1,0)