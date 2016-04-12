
from brand.BrandNameMatcher import match_products as brand_matcher
from color.color_module import find_match as color_matcher
from dimension.HLW_module import predict_HLW_match as dimension_matcher
from weight.weight_module import predict_weight_match as weight_matcher
from mpn.MPN_matcher import ParseJson as mpn_matcher
mpn = mpn_matcher()
from upc.UPC_matcher import ParseJson as upc_matcher
upc = upc_matcher()
from variation.variation_module import predict_match as variation_matcher


def entity_matcher(file_name):
    
    results = {1: "MATCH" , 0: "MISMATCH", -1: "IDK"}
    variations = {1: "SIMILAR" , 0: "NOTSIMILAR", -1: "IDK"}

    with open(file_name) as product_pairs:
        i = 1
        correct_count = 0
        incorrect_count = 0
        for line in [next(product_pairs) for x in xrange(100)]:
            (pairid, wid, json_1, vid, json_2, label) =  line.split("?")
            actual_label = label.split('\n')[0]

            result_brand = brand_matcher(json_1, json_2, None)
            result_color = color_matcher(json_1, json_2)
            result_dimension = dimension_matcher(json_1, json_2)
            result_weight = weight_matcher(json_1, json_2)
            result_mpn = mpn.parse(json_1, json_2)
            result_upc = upc.parse(json_1, json_2)
            #0 indicates that products vary a lot, 1 indicates that the variation is not much and -1 indicates not sure
            result_variation = variation_matcher(json_1, json_2)
            
            print "**************************"
            print "product pair no : " + str(i)
            print "actual label    : " + label.split('\n')[0]
            #print "brand           : " + str(results[result_brand[0]])
            #print "color           : " + str(results[result_color[0]])
            #print "dimension       : " + str(results[result_dimension[0]])
            #print "weight          : " + str(results[result_weight[0]])
            #print "mpn             : " + str(results[result_mpn[0]])
            #print "upc             : " + str(results[result_upc[0]])
            #print "variation       : " + str(variations[result_variation[0]])

            if result_mpn[0] == 1 or result_upc[0] == 1:
                print "predicted label : " + "MATCH"
                predicted_label = "MATCH"
                if actual_label == predicted_label:
                    correct_count = correct_count + 1 
                else:
                    incorrect_count = incorrect_count + 1 
                i = i + 1
                continue
            
            if result_mpn[0] == 0 or result_upc[0] == 0:
                print "predicted label : " + "MISMATCH"
                predicted_label = "MISMATCH"
                if actual_label == predicted_label:
                    correct_count = correct_count + 1     
                else:
                    incorrect_count = incorrect_count + 1                     
                i = i + 1
                continue   
            
            if result_variation[0] == 1:
                print "predicted label : " + "MATCH"
                predicted_label = "MATCH"
                if actual_label == predicted_label:
                    correct_count = correct_count + 1 
                else:
                    incorrect_count = incorrect_count + 1 
                i = i + 1
                continue
                
            
            print "predicted label : " + "IDK"    
            
            i = i + 1
            print "**************************"
    
    print "*********************************"
    print "results"
    print "*********************************"
    print "total pair count     : " + str(i-1)
    print "correct prediction   : " + str(correct_count)
    print "incorrect prediction : " + str(incorrect_count)
    print "*********************************"

if __name__ == "__main__":
    file_name = "files/elec_pairs_stage1.txt"
    entity_matcher(file_name)
