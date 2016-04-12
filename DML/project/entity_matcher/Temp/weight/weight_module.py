__author__ = 'kavin'

#encoding=utf8"
import json
import re

def predict_weight_match(json_str_1,json_str_2):

    """
    This function will match the weights of two given products using a regular expression.
    Two product information (in JSON format) are passed as input to the function.
    The output returns a list in the format : [return_value,1]
    where 1 represents the confidence score value is described as follows
    :param: json_str_1, json_str_2
    :return: [1,1] if both the products have same weights
             [0,1] if two products have different weights
             [-1,1] if one or both of the products have weight values missing in the product description

    """

    result_list = []
    c1 = 0
    c2 = 0
    c3 = 0
    regex = 'Weight[^:;,.]*?:[^:,.]*?\s*-*([0-9]+\.*[0-9]*)\s*((?:g|tons|ton|lbs|lb|pounds|pound|ounce|oz|gram|grams)*(?:/cm2|/m2|/m|/cm|/mm|/mm2)*(?:\&sup2)*)\s*[\.|<>]*'
    match1 = re.findall(regex,json_str_1,re.I)
    match1 = list(set(match1))
    #print match1
    match2 = re.findall(regex,json_str_2,re.I)
    match2 = list(set(match2))
    #print match2
    if not match1 or not match2:
        result_list.append(-1)
        result_list.append(1)
        #print result_list
        c3+=1
    else:
        count = 0
        count1 = 0
        count2 = 0
        for val in match1:
            for val1 in match2:
                if not val[0] or not val[1] or not val1[0] or not val1[1]:
                    count1+=1

                elif float(val[0]) == float(val1[0]) and (str(val[1]).lower() == str(val1[1]).lower() or re.findall('^lb',val[1],re.I)==re.findall('^lb',val1[1],re.I) or re.findall('^pound',val[1],re.I)==re.findall('^pound',val1[1],re.I) or re.findall('^g',val[1],re.I)==re.findall('^g',val1[1],re.I) or re.findall('^o',val[1],re.I)==re.findall('^o',val1[1],re.I)):
                    count+=1
                elif (re.findall('^lb',val[1],re.I) or re.findall('^pound',val[1],re.I)) and (re.findall('^pound',val1[1],re.I) or re.findall('^lb',val1[1],re.I)) :
                    if float(val[0])==float(val1[0]):
                        count+=1
                    else:
                        count2+=1
                else:
                    count2+=1

        if count > 0:
            result_list.append(1)
            result_list.append(1)
            #print result_list
            c1+=1
            
        elif count2 > 0:
            result_list.append(0)
            result_list.append(1)
            #print result_list
            c2+=1
        
        else:
            result_list.append(-1)
            result_list.append(1)
            #print result_list
            c3+=1
            
    #print result_list
    return result_list