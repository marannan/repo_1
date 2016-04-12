PRODUCT_TYPE_WEIGHT = 0.5
KEYWORD_WEIGHT = 0.2
COWORD_WEIGHT = 0.1
MATERIAL_WEIGHT = 0.1
BRAND_WEIGHT = 0.1
NEGATIVE_WEIGHT = 0.2

# List of possible product types that could be associated with a laptop case
laptop_cases_types = ['Laptop Sleeves', 'Bags, Cases & Skins', 'Rolling Business Cases',
                      'Soft Sided Briefcase',
                      'Leather|15.4|Briefcases|Top Loading|Removable Shoulder Strap|Laptop Compatible',
                      'Laptop Cases', 'Hard Cases', 'Laptop Backpacks', 'Briefcases', 'Rolling Business Cases',
                      'Cases', 'Hard Shell', 'Messenger Bags', 'Messenger Bag', 'Attach Cases',
                      'Laptop Sleeve|Water Resistant', 'Water Resistant|Hardsided|Designed For Mac',
                      'Backpacks', 'Notebook carrying backpack', 'Notebook carrying case']

laptop_cases_product_types = ['Laptop Bags & Cases', 'Electronics Carrying Cases', 'Laptop Computers', 'Computer Cases',
                              'Backpacks', 'Handbags']

important_keywords = ['notebook', 'notebooks', 'computer', 'computers', 'macbook', 'macbooks', 'laptop', 'laptops',
                      'backpack', 'mac', 'macs', 'netbook']

co_words = ['sleeve', 'case', 'zippered', 'pocket', 'zipper', 'zipperless']

product_material_list = ['neoprene', 'nylon', 'polyester', 'duraceltex', 'leather', 'suede', 'cowhide', 'fabric',
                         'synthetic', 'quilted microfibre', 'cotton canvas', 'vinyl', 'twisted poly',
                         'leather top or full grain', 'ballistic nylon']

product_brand_list = ['mckleinusa', 'targus', 'mobile edge', 'case logic', 'kensington', 'higher ground', 'mcklein',
                      'david king', 'sumdex', 'netpack', 'designer sleeves', 'butterfly', 'solo', 'royce leather',
                      'travelon', 'maccase', 'caribee', 'leatherbay', 'antenna', 'team promark', 'ebags',
                      'franklincovey', 'designer sleeves', 'shoreline', 'travelon', 'ice red', 'casauri',
                      'protec', 'travelers choice', 'centon', 'ed hardy', 'looptworks']

negative_keywords = ['ipad', 'iphone', 'hard', 'drives', 'drive', 'dvd', 'cable', 'tablet', 'gtablet', 'lock',
                     'monitor',
                     'e-book', 'reader', 'e-reader']

def is_laptop_case(product_pair):
    """
    Checks if the given product list are laptop cases
    :param product_pair: List of dictionaries of both the products
    :return: 1 if they are both laptop cases
             -1 if its not sure
             0 if either one or both the products are not laptop cases
    """
    is_product1_laptop_case = identify_laptop_case(product_pair[0])
    is_product2_laptop_case = identify_laptop_case(product_pair[1])

    if is_product1_laptop_case == 1 and is_product2_laptop_case == 1:
        return 1
    elif is_product1_laptop_case == 0 or is_product2_laptop_case == 0:
        return 0
    elif is_product1_laptop_case == -1 or is_product2_laptop_case == -1:
        return -1


def identify_laptop_case(product_item):
    """
    Checks if the given product is a laptop case by assigning weights for each key and calculating an overall
    confidence score
    :param product_pair: Dictionary containing key-value pairs for a product
    :return: 1 if they are both laptop cases
             -1 if its not sure
             0 if either one or both the products are not laptop cases
    """
    # prediction_file = open("prediction_file.txt", 'a')
    product = product_item[0]
    product_confidence_score = 0.0
    product_type = ''
    product_material = ''
    product_brand = ''
    product_long_description = ''
    product_short_description = ''
    check_brand_in_desc = False

    if 'Type' in product:
        product_type = product['Type'][0]
    if 'Product Type' in product:
        product_type = product['Product Type'][0]
    if 'Material' in product:
        product_material = product['Material'][0].lower()
    if 'Product Long Description' in product:
        product_long_description = product['Product Long Description']
    if 'Product Short Description' in product:
        product_short_description = product['Product Short Description']

    if product_type in laptop_cases_types or product_type in laptop_cases_product_types:
        product_confidence_score = product_confidence_score + PRODUCT_TYPE_WEIGHT

    if product_material in product_material_list:
        product_confidence_score = product_confidence_score + MATERIAL_WEIGHT
        check_brand_in_desc = False
    else:
        check_brand_in_desc = True

    if product_brand in product_brand_list:
        product_confidence_score = product_confidence_score + BRAND_WEIGHT

    for keyword in important_keywords:
        for word in product_long_description:
            if keyword in word:
                product_confidence_score = product_confidence_score + KEYWORD_WEIGHT

    if check_brand_in_desc:
        for brand_name in product_brand_list:
            for description in product_long_description:
                if brand_name in description:
                    product_confidence_score = product_confidence_score + BRAND_WEIGHT

    for word in co_words:
        for description in product_long_description:
            if word in description:
                product_confidence_score = product_confidence_score + COWORD_WEIGHT

    for keyword in important_keywords:
        for word in product_short_description:
            if keyword in word:
                product_confidence_score = product_confidence_score + KEYWORD_WEIGHT

    for word in co_words:
        for description in product_short_description:
            if word in description:
                product_confidence_score = product_confidence_score + COWORD_WEIGHT

    for word in negative_keywords:
        for description in product_short_description:
            if word in description.lower():
                product_confidence_score = product_confidence_score - NEGATIVE_WEIGHT

    for word in negative_keywords:
        for description in product_long_description:
            if word in description.lower():
                product_confidence_score = product_confidence_score - NEGATIVE_WEIGHT

    # print("Product confidence score = " + str(product_confidence_score))
    if product_confidence_score >= 0.7:
        # print('Product identified as laptop case.')
        return 1

    elif product_confidence_score >= 0.4 and product_confidence_score < 0.7:
        # print('Product maybe a laptop case.')
        return -1

    else:
        # print('Product not identified as laptop case.')
        return 0

