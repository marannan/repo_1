__author__ = 'ashok'

import os

def get_brands_dict(path_to_file="all_brand_dic.txt"):

    lines = [line.rstrip('\n') for line in open(path_to_file)]
    brands_list = []
    brands_map = {}
    
    for line in lines:
        words = line.split()
        length = len(words)
        brand_name = ''
        
        for i in range(length-1):
            brand_name += ' ' + words[i]
        brand_name = brand_name.lower().strip()
        #brand_name = brand_name.strip()
        freq = words[-1]

        if brand_name in brands_map:
            #print brands_map[brand_name]
            if int(brands_map[brand_name]) < int(freq):
                brands_map[brand_name] = freq
        
        else:
            brands_map[brand_name] = freq

        brands_list.append(brand_name)

    if '' in brands_map:
        brands_map.pop('')
        
    
    return brands_list, brands_map

    