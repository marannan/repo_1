__author__ = 'ashok'
import re
from brands_dict import *
import csv

brands_list, brands_map = get_brands_dict()

def get_all_keywords(value):
    
    result = set()
    value = value.lower()
    
    if type(value) is str and value.strip() != "":
        v_list = [x.strip('.') for x in re.split(' |; |, |\*|\n|<|>|-|/|:|\'', value)]
        if len(v_list) > 0:
            result |= set(v_list)
    
    return result
    

def predict_brand(product_attri):

    key_words_v = get_all_keywords(product_attri)
    key_words_w = get_all_keywords(product_attri)
    
    intersect_words = key_words_v.intersection(key_words_w)
    
    max_value = 0
    max_probable_brand = ''
    
    for brand in brands_list:
        new_set = set(re.split(' |; |, |\*|\n|<|>|-|/|:|\'', brand)).difference(intersect_words)
        if len(new_set) == 0 and brand in brands_map:
            brand_value = int(brands_map[brand])
            if brand_value > max_value:
                max_probable_brand = brand
                max_value = brand_value

    #threshold = C.threshold_brand_value

    return max_probable_brand
    
    


if __name__ == "__main__":
    brands_names_predicted = []
    prediction = []
    incorrect_predictions = []
 
    
    product_names = [line.rstrip('\n')[:len(line)-4].lower() for line in open("pn.txt")]
    brand_names_original = [line.rstrip('\n')[:len(line)-2].lower() for line in open("bn.txt")]
 
    for product_name in product_names:
        brands_names_predicted = brands_names_predicted + [predict_brand(product_name)]
        
    correct , incorrect = 0, 0 
    
    for i in range(len(brands_names_predicted)):
        brand_ori = brand_names_original[i]
        brand_pred = brands_names_predicted[i]
        
        #if brand_ori == "" or brand_pred == "":
            
        
        if brand_ori == brand_pred  or brand_ori in brand_pred or brand_pred in brand_ori):
            correct = correct + 1
            prediction.append("yes")
            
        else:
            incorrect_predictions.append([str(i),brand_ori,brand_pred])
            incorrect = incorrect + 1
            prediction.append("no")
            
    
    
    print "total no of brands               : " + str(len(brands_names_predicted))
    print "total no of correct prediction   : " + str(correct)
    print "total no of incorrect prediction : " + str(incorrect)
    print "incorrrect predictions : "
    for incorrect in incorrect_predictions:
        print " ".join(incorrect)
        
    
    with open("brands_prediction_results.csv","wb") as brands_prediction_file:
        csv_writer = csv.writer(brands_prediction_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["PRODUCT_NAME", "BRAND_LABELED", "BRAND_PREDICTED", "PREDICTION_RESULT"])                        
        for i in range(len(product_names)):
            csv_writer.writerow([product_names[i], brand_names_original[i],brands_names_predicted[i], prediction[i]])                        
    