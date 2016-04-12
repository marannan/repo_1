import re
import json
from itertools import chain
import math

'''
Code for comparing two products and returning if they have minor variations or not.
@author: Arjun.
'''
UPC = 'UPC'
MPN = 'Manufacturer Part Number'
product_name = 'Product Name'
product_type = 'Product Type'
COLOR = 'Color'
ACTUAL_COLOR = 'Actual Color'
DIMENSIONS = ['Height','Width','Length','Size']

# Return the logistic regression result, given the jacard measure of parameters.
def sigmoid(prod_attrs):
    (attr_match, color, dim, product) = prod_attrs
    wts = [0.30,0.20,0.20,0.45]
    result = sum(wts[i]*prod_attrs[i] for i in xrange(4))
    return 1.0/(1+math.pow(math.e,-result))

# Return the numerical tokens alone as a flattened list, given input.
def get_num_tokens(input):
    tokens = []
    for token in input:
        if isinstance(token,basestring):
            tokenvals = []
            for val in token.split():
                tokenvals.append(val)
            return [float(val) for val in tokenvals if is_number(val)]
        else:
            tokens.extend(get_tokens(token))
            
# Return the tokens as a flattened list, given input.            
def get_tokens(input):
    tokens = []
    for token in input:
        if isinstance(token,basestring):
            tokenvals = [float(val) if is_number(val) else val for val in token.split()]
            tokens.extend(tokenvals)
        else:
            tokens.extend(get_tokens(token))
    return tokens
    
# Given an item, return the tokens comprising of all the values for common attributes.
def get_token_for_index(item,common_attrs):
    item = {key:val for key,val in item.items() if key in common_attrs and key!='Product Long Description'}
    return  get_tokens(item.values())

# Computes the jacard measure for similarity of two items, by concatenating all values 
# of common attributes in a single list.
def jacard_index(item1,item2):
    common_attrs = set(item1.keys()).intersection(set(item2.keys()))
    
    item1tokens = set(get_token_for_index(item1,common_attrs))
    item2tokens = set(get_token_for_index(item2,common_attrs))
    
    inter= item1tokens.intersection(item2tokens)
    union = item1tokens.union(item2tokens)
    return float(len(inter))/len(union) if inter else 0.0

# Function to convert unicode data types to ascii, for easy manipulation.
def unicodetoascii(input):
    if isinstance(input, basestring):
        return input.encode('utf-8')
    elif isinstance(input, list):
        return [unicodetoascii(ele) for ele in input]
    elif isinstance(input, dict):
        return {unicodetoascii(key):unicodetoascii(val) for (key,val) in input.iteritems()}

# Finds the common attributes, and sees if they are equivalued in the two products.
# Returns a tuple of mismatched attributes and length of the common attributes.
def get_attr_difference_count(item1,item2):
    tot_count=0
    mis_count=0
    s=[]
    item1keys = set(item1.keys())
    item2keys = set(item2.keys())
    commonkeys = item1keys.intersection(item2keys)
    for key in commonkeys:
        if not is_equivalued_tokens(item1[key],item2[key]):
            mis_count+=1
    return (mis_count,len(commonkeys))
    
# Check if two items have the same value, by tokenizing and comparing them.
def is_equivalued_tokens(item1,item2):
    return set(get_tokens(item1))==set(get_tokens(item2))
    
# Check if two items have the same value, by operating on different types and
# recursing if necessary.
def is_equivalued(item1, item2):
    try:
        if isinstance(item1,list) and isinstance(item2,list) and len(item1)==len(item2):
            return all(is_equivalued(x,y) for x,y in zip(item1, item2))
            
        if is_number(item1):
            return float(item1) == float(item2)
        if isinstance(item1,basestring):
            return item1.lower() == item2.lower()
        return item1==item2
    except ValueError:
        return False

# Return if a string can be represented as a float, else returns None.
def is_number(obj):
    try:
        return float(obj)
    except Exception:
        return None
        
# For two items, tries to find the colors from the attributes and returns a measure
# of similarity.
def color_similarity(item1,item2):
    item1colors = item1.get(COLOR,[])
    item1colors.extend(item1.get(ACTUAL_COLOR,[]))
    item2colors = item2.get(COLOR,[])
    item1colors.extend(item2.get(ACTUAL_COLOR,[]))
    colors1 = []
    colors2 = []
    for color in item1colors:
        colors1.extend(re.split('\W+',color))
    for color in item2colors:
        colors2.extend(re.split('\W+',color))
    colors1 = set(colors1)
    colors2 = set(colors2)
        
    common_dims = float(len(colors1.intersection(colors2)))
    return common_dims/len(colors1.union(colors2)) if common_dims else 0.0

# For two items, tries to find the dimensions from the attributes and returns a measure
# of similarity.
def dimensions(item1,item2):
    item1keys = [get_num_tokens(item1[key]) for key in item1.keys() if 'Warranty' not in key and any(x in key for x in DIMENSIONS)]
    item2keys = [get_num_tokens(item2[key]) for key in item2.keys() if 'Warranty' not in key and any(x in key for x in DIMENSIONS)]
    item1keys = set(chain.from_iterable(item1keys))
    item2keys = set(chain.from_iterable(item2keys))
    
    common_dims = float(len(item1keys.intersection(item2keys)))
    return common_dims/len(item1keys.union(item2keys)) if common_dims else 0.0

# For two items, tries to find the dimensions from the product name and type
# and returns a measure of similarity.
def productname(item1,item2):
    product1 = item1.get(product_name,[])
    product1.extend(item1.get(product_type,[]))
    product2 = item2.get(product_name,[])
    product2.extend(item2.get(product_type,[]))
    product1 = set(product1)
    product2 = set(product2)
    common_tokens = float(len(product1.intersection(product2)))
    return common_tokens/len(product1.union(product2)) if common_tokens else 0.0
    
def predict_match(product1_json, product2_json):
    """
    Takes a product pair in json format and returns whether the two products vary in only a few attributes. 
    It attempts to do the same by first checking if most words overlap, and if not, falls back to retrieving 
    values of individual attributes and then making a decision.

    :param:  json_str_a, json_str_b
    :return: [1,1] (products are the same or only slight variants of each other, confidence interval of 1)
          [0,1] (products are essentially different, confidence interval of 1)
          [-1,1] (not sure)

    """
    tag = re.compile("<.*?>|\&quot;")
    wjson = re.sub(tag,' ',product1_json)
    vjson = re.sub(tag,' ',product2_json)
    try:
        wo = json.loads(wjson)
        wobj = unicodetoascii(wo)
        vobj = unicodetoascii(json.loads(vjson))
        
        # Remove UPC and MPN as the module would be called only when there are no strong IDs.
        wobj.pop(UPC,None)
        vobj.pop(UPC,None)
        wobj.pop(MPN,None)
        vobj.pop(MPN,None)
        
        # If Jacard score of the pairs cross a threshold, declare them variants. Else, use 
        # parameters like proportion of matching attributes, color, dimensions and product
        # name to constructed a weighted rule scaled using a sigmoid function. The output
        # of the sigmoid indicates if the pair are variations or not.
        jac = jacard_index(wobj,vobj)
        if jac >= 0.8: return [1,1]
        else:
            mis,tot_att= get_attr_difference_count(wobj,vobj)
            incor_prop = (1.0 - float(mis)/tot_att) if mis else 0.0
            color_rat = color_similarity(wobj,vobj)
            dim_rat = dimensions(wobj,vobj)
            product_rat = productname(wobj,vobj)
        
            result = sigmoid((incor_prop,color_rat,dim_rat,product_rat))
            
            if result > 0.7: return [1,1]
            else: return [0,1]
    except:
        return [-1,1]
