import datetime

#start time
time_started = datetime.datetime.now().replace(microsecond=0)

import re
import json
import traceback
import sys
import operator
import editdistance as ed
import py_stringmatching.simfunctions as pyst
import numpy
import scipy
import sklearn.ensemble as en
import sklearn.neural_network as nn
import numpy as np
import pandas as pd

from brand.BrandNameMatcher import match_products as brand_matcher
from color.color_module import find_match as color_matcher
from dimension.HLW_module import predict_HLW_match as dimension_matcher
from weight.weight_module import predict_weight_match as weight_matcher
from mpn.MPN_matcher import ParseJson as mpn_matcher
mpn = mpn_matcher()
from upc.UPC_matcher import ParseJson as upc_matcher
upc = upc_matcher()
from variation.variation_module import predict_match as variation_matcher


pair_id_missing = []
d = {}
#All Brand dictionary
abn = [line.strip().split("\t")[0] for line in open("elec_brand_dic.txt")]
abn = [re.sub('[^a-zA-Z ]', "", x) for x in abn]

#Product Segment: Electronics Domain
electronics_domain = ["books", "music", "musical", "movies", "accessories", "default", "toys", "games", "tools", "hardware"
                      "cameras", "photography", "optics", "services", "warranties", "health", "beauty", "watches"]


def matcher(json_1, json_2):
    try:
        result_brand = brand_matcher(json_1, json_2, None)
        #result_brand = [-1,1]
    except:
        result_brand = [-1,1]
    
    try:    
        result_color = color_matcher(json_1, json_2)
        #result_color = [-1,1]
    except:
        result_color = [-1,1]

    try:
        result_dimension = dimension_matcher(json_1, json_2)
        #result_dimension = [-1,1]
    except:
        result_dimension = [-1,1]
    
    try:
        result_weight = weight_matcher(json_1, json_2)
        #result_weight = [-1,1]
    except:
        result_weight = [-1,1]
    
    try:
        result_mpn = mpn.parse(json_1, json_2)
        #result_mpn = [-1,1]
    except:
        result_mpn = [-1,1]
    
    try:
        result_upc = upc.parse(json_1, json_2)
        #result_upc = [-1,1]
    except:
        result_upc = [-1,1]
        
    try:    
        #0 indicates that products vary a lot, 1 indicates that the variation is not much and -1 indicates not sure
        result_variation = variation_matcher(json_1, json_2)
        #result_variation = [-1,1]
    except:
        result_variation = [-1,1]

    return [result_brand[0], result_color[0], result_dimension[0], result_weight[0], result_mpn[0], result_upc[0], result_variation[0]]
    #return [result_brand[0], result_mpn[0], result_upc[0]]
    #return result_brand[0], result_mpn[0], result_upc[0], result_variation[0]

def extract_json():
    try:
        lines_processed = 1
        with open("elec_pairs_stage4.txt") as product_pairs:
            for line in product_pairs:
            #for line in [next(product_pairs) for x in xrange(1000)]:
                #(pairid, wid, json_1, vid, json_2, label) =  line.split("?")
                (pairid, wid, json_1, vid, json_2) =  line.split("?")
                #get_attributes(json_1)
                #get_attributes(json_2)
                #d[pairid] = [json_1, json_2, label]
                d[pairid] = [json_1, json_2]
                #print lines_processed
                lines_processed = lines_processed + 1

    except Exception,e:
        traceback.print_exc(file=sys.stdout)
        
    
    #print "total lines : " + str(lines_processed)

def uni_to_ascii(input):
    if isinstance(input,unicode):
        return input.encode('ascii')
    elif isinstance(input, list):
        return [uni_to_ascii(ele) for ele in input]
    elif isinstance(input, dict):
        return {uni_to_ascii(key):uni_to_ascii(val) for key,val in input.items()}

def print_matches():
    bmc = 0
    bm = 0

    for k in d:
        try:
            #print d[k][2].split("\n")
            if d[k][2].split("\n")[0] == "MATCH":
                bm += 1
                json_obj1 = json.loads(d[k][0])
                json_obj2 = json.loads(d[k][1])
                #if ed.eval(uni_to_ascii(json_obj1['Brand'])[0].lower(), uni_to_ascii(json_obj2['Brand'])[0].lower()) > 4:
                #j1 = uni_to_ascii(json_obj1['Brand'])[0].lower()
                #j2 = uni_to_ascii(json_obj2['Brand'])[0].lower()
                j1 = uni_to_ascii(json_obj1['Product Long Description'])[0].lower()
                j2 = uni_to_ascii(json_obj2['Product Long Description'])[0].lower()
                j1 = re.sub('^a-zA-z0-9 ','',j1)
                j2 = re.sub('^a-zA-z0-9 ','',j2)

                #print "%s <<->> %s" %(j1, j2)
                #if not (j1.startswith(j2.split()[0]) or j2.startswith(j1.split()[0])):
                if not pyst.tfidf(j1.split(), j2.split()) > 0.1:
                    bmc += 1
                    #print "BN %d : %s <<->> %s" % (bmc, j1, j2)
                    #print "%d -> %s <<->> \n %s ->> TFIDF: %f" %(bmc, j1, j2, pyst.tfidf(j1.split(), j2.split()))
        except:
            #print "##"
            pass
    #print bm

def generate_features():
    
    X = []
    y = []
    count = 0
    for k in d:
        try:
            v = d[k]
            prod1 = json.loads(v[0])
            prod2 = json.loads(v[1])
        except:
            pair_id_missing.append(k)
            print k
            continue

        #continue    
        
        #Assigning a label for given pair
        #if v[2].split("\n")[0] == "MATCH":
            #y.append(1)
        #else:
            #y.append(0)

        #Generate features for the given pair
        x_i = []


        #entity matcher from old project
        #result_brand, result_color, result_dimension, result_weight, result_mpn, result_upc, result_variation \
        results = []
        time_modules_started = datetime.datetime.now().replace(microsecond=0)
        results = matcher(v[0], v[1])
        time_modules_ended = datetime.datetime.now().replace(microsecond=0)
        #print "time taken for modules : " + str(time_modules_ended-time_modules_started)        
        x_i.extend(results)



        #Brand Name feature
        #prefix matching
        time_brand_started = datetime.datetime.now().replace(microsecond=0)
        try:
            try:
                brand1 = uni_to_ascii(prod1['Brand'])[0].lower()
            except:
                brand1 = uni_to_ascii(extract_brand(prod1['Product Name']))
            try:
                brand2 = uni_to_ascii(prod2['Brand'])[0].lower()
            except:
                brand2 = uni_to_ascii(extract_brand(prod2['Product Name']))
            if brand1 == "" or brand2 == "":
                raise Exception.message("error : no brand")

            temp = pyst.jaro_winkler(brand1, brand2)
            x_i.append(int(temp))
            #if (brand1.startswith(brand2.split()[0]) or brand2.startswith(brand1.split()[0])):
                #x_i.append(1)
            #else:
                #x_i.append(0)
        except:
            x_i.append(-1)
            pass
    
        time_brand_ended = datetime.datetime.now().replace(microsecond=0)
        #print "time taken for brand : " + str(time_brand_ended-time_brand_started)        
        
        
        #TFIDF Features
        #tfidf_keys = ['Product Name', 'Product Type' , 'Product Segment', 'Product Long Description']
        #for attr in tfidf_keys:
            #try:
                #p_name1 = uni_to_ascii(prod1[attr])[0].lower()
                #p_name2 = uni_to_ascii(prod2[attr])[0].lower()
                #p_name1 = re.sub('^a-zA-z0-9 ','',p_name1)
                #p_name2 = re.sub('^a-zA-z0-9 ','',p_name2)
                #x_i.append(pyst.tfidf(p_name1.split(), p_name2.split()))
            #except:
                #x_i.append(-1)

        #JaroWinkler Features
        tfidf_keys = ['Product Name', 
                      'Product Type' , 
                      'Product Segment', 
                      'Product Long Description', 
                      'Product Short Description', 
                      'Category', 
                      'GTIN', 
                      'Manufacturer', 
                      'Warranty Information', 
                      'Condition',
                      'Country of Origin: Components']
        
        #adding jaro_wrinkler score
        time_jaro_winkler_started = datetime.datetime.now().replace(microsecond=0)
        for attr in tfidf_keys:
            try:
                p_name1 = uni_to_ascii(prod1[attr])[0].lower()
                p_name2 = uni_to_ascii(prod2[attr])[0].lower()
                p_name1 = re.sub('^a-zA-z0-9 ','',p_name1)
                p_name2 = re.sub('^a-zA-z0-9 ','',p_name2)
                temp = pyst.jaro_winkler(p_name1, p_name2)
                #print temp
                x_i.append(temp)
            except:
                x_i.append(-1)
            
        time_jaro_winkler_ended = datetime.datetime.now().replace(microsecond=0)
        #print "time taken for jaro_winkler : " + str(time_jaro_winkler_ended-time_jaro_winkler_started)        
                
        
        ##adding jaro score
        #time_jaro_started = datetime.datetime.now().replace(microsecond=0)
        #for attr in tfidf_keys:
            #try:
                #p_name1 = uni_to_ascii(prod1[attr])[0].lower()
                #p_name2 = uni_to_ascii(prod2[attr])[0].lower()
                #p_name1 = re.sub('^a-zA-z0-9 ','',p_name1)
                #p_name2 = re.sub('^a-zA-z0-9 ','',p_name2)
                #temp = pyst.jaro(p_name1, p_name2)
                ##print temp
                #x_i.append(temp)
            #except:
                #x_i.append(-1) 
        
        #time_jaro_ended = datetime.datetime.now().replace(microsecond=0)
        #print "time taken for jaro : " + str(time_jaro_ended-time_jaro_started)            
                
                
        #adding levenshtein score
        #time_levenshtein_started = datetime.datetime.now().replace(microsecond=0)
        #for attr in tfidf_keys:
            #try:
                #p_name1 = uni_to_ascii(prod1[attr])[0].lower()
                #p_name2 = uni_to_ascii(prod2[attr])[0].lower()
                #p_name1 = re.sub('^a-zA-z0-9 ','',p_name1)
                #p_name2 = re.sub('^a-zA-z0-9 ','',p_name2)
                #temp = pyst.levenshtein(p_name1, p_name2)
                ##print temp
                #x_i.append(temp)
            #except:
                #x_i.append(-1)                
        #time_levenshtein_ended = datetime.datetime.now().replace(microsecond=0)
        ##print "time taken for levenshtein : " + str(time_levenshtein_ended-time_levenshtein_started)
        
    
        ##adding needleman_wunsch score
        #time_needleman_wunsch_started = datetime.datetime.now().replace(microsecond=0)
        #for attr in tfidf_keys:
            #try:
                #p_name1 = uni_to_ascii(prod1[attr])[0].lower()
                #p_name2 = uni_to_ascii(prod2[attr])[0].lower()
                #p_name1 = re.sub('^a-zA-z0-9 ','',p_name1)
                #p_name2 = re.sub('^a-zA-z0-9 ','',p_name2)
                #temp = pyst.needleman_wunsch(p_name1, p_name2)
                ##print temp
                #x_i.append(temp)
            #except:
                #x_i.append(-1)                    
        
        #time_needleman_wunsch_ended = datetime.datetime.now().replace(microsecond=0)
        ##print "time taken for needleman_wunsch : " + str(time_needleman_wunsch_ended-time_needleman_wunsch_started)        

        
        #add pair id at the last
        x_i.append(k)
        
        #Finally append to training set
        X.append(x_i)
        if count % 1000 == 0:
            pass
        print str(count)
        count += 1
    return X,y

def extract_brand(prod_name):
    pns = prod_name.split()
    pns = [re.sub('[^a-zA-z ]','',x) for x in pns]
    brand = ""
    for i in range(0,min(len(pns)/2,len(pns)-2)):
        x = str(pns[i])
        scores = [ed.eval(x.lower(), z.lower()) for z in abn]
        if (min(scores) < 1):
            i = scores.index(min(scores))
            brand = abn[i];
            break

        x = str(pns[i]) + " " + str(pns[i+1])
        scores = [ed.eval(x.lower(), z.lower()) for z in abn]
        if (min(scores) < 1):
            i = scores.index(min(scores))
            brand = abn[i];
            #print brand + " " + bn
            break

        x = str(pns[i]) + " " + str(pns[i+1]) + " " + str(pns[i+2])
        scores = [ed.eval(x.lower(), z.lower()) for z in abn]
        if (min(scores) < 1):
            i = scores.index(min(scores))
            brand = abn[i];
            break

        x = str(pns[i])
        if len(x) > 5:
            for y in abn:
                ys = y.split()
                if len(ys) == 0:
                    continue
                if str(ys[0]).lower() == x.lower():
                    brand = y
                    break

        if brand != "":
            break
    return brand


if __name__ == "__main__":
    
    print "entity matcher"
    extract_json()
    X,y = generate_features()
    
    #write the feature data set to a file
    data_set = pd.DataFrame(X)
    
    data_set.to_csv("data_set_unlabelled_stage_4.csv", index = False)
    
    exit()
    
    #file_1 = open("missing_pair_stage_4.txt", mode='wb')
    #for pair_id in pair_id_missing:
        #file_1.write(str(str(pair_id) + "\n"))
        #print pair_id
    #print "data_set is written to file"

    #time_ended = datetime.datetime.now().replace(microsecond=0)
    #print "time taken : " + str(time_ended-time_started)    
    #exit()
    
    #print X[:10]
    x_t = X[:len(X)/2]
    y_t = y[:len(X)/2]
    x_te = X[len(X)/2:]
    y_te = y[len(X)/2:]
    rfc = en.RandomForestClassifier()
    #rfc = en.AdaBoostClassifier()
    #print len(x_t)
    #print len(x_t[0])
    rfc.fit(np.vstack(x_t),np.array(y_t))
    y_p = rfc.predict(np.vstack(x_te))

    TP = 0
    FP = 0
    FN = 0
    TN = 0
    for (a, b) in zip(y_te, y_p):
        #print '%d - %d' %(a,b)
        if a == b and b == 1:
            TP += 1
        elif b == 1:
            FP += 1
        elif b== 0 and a == b:
            TN += 1
        else:
            FN += 1
    
    print "tp  = %d fp = %d"%(TP,FP)
    print "precision: %f" %(float(TP)/float(TP + FP))
    print "recall: %f" %(float(TP)/(TP + FN))

    

    data_set = pd.DataFrame(X)
    data_set["LABEL"] = pd.Series(y)
    data_set.to_csv("data_set.csv", index= False)

    time_ended = datetime.datetime.now().replace(microsecond=0)
    print "time taken : " + str(time_ended-time_started)
    