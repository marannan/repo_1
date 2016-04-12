import json
from laptop_case_identifier import is_laptop_case
from laptop_case_matcher import is_match


def extract_key_values_from_json(product_list):
    """
    Extracts key-value pairs from input JSON and constructs a dictionary
    :param product_list: List containing JSON descriptions of the products we want to compare
    :return: List containing keys in both the products
             List of dictionaries containing key - value pairs for both the products
    """
    count = 0
    product_keys = []
    product_json_list = []
    parsed_json = {}
    for i in range(0, len(product_list)):
        json_objects = []
        json_string = product_list[i]
        # print(json_string)
        try:
            parsed_json = json.loads(json_string)
            count = count + 1
        except Exception as e:
            print(e)
        # print(parsed_json)
        json_objects.append(parsed_json)
        # if 'Type' in parsed_json.keys():
        #     if parsed_json['Type'][0] == 'default':
        #         print(parsed_json['Product Long Description'])
        for key in parsed_json.keys():
            if key not in product_keys:
                product_keys.append(key)
        product_json_list.append(json_objects)
    # print(product_keys)
    return product_keys, product_json_list

def is_same_laptop_case(product1_json, product2_json):
    """
    Takes two product descriptions in JSON format, checks if both are laptop cases
    If they are not, returns 0 with confidence 1.0.
    If the program is not sure, returns -1 with confidence 1.0.

    If they are laptop cases, checks if they refer to the same product.

    :param product1_json: JSON string for product 1
    :param product2_json: JSON string for product 2
    :return: If the product descriptions refer to the same product, returns 1.0 with confidence 1.0.
             If they are not, returns 0 with confidence 1.0
             If the program is not sure, returns -1 with confidence 1.0
    """

    product_list = [product1_json, product2_json]

    product_keys, product_json_list = extract_key_values_from_json(product_list)

    are_products_laptop_case = is_laptop_case(product_json_list)

    if are_products_laptop_case == 0:
        return [0, 1.0]
    elif are_products_laptop_case == -1:
        return [-1, 1.0]
    elif are_products_laptop_case == 1:
        is_product_match = is_match(product_keys, product_json_list)
        if is_product_match == 0:
            return [0, 1.0]
        elif is_product_match == -1:
            return [-1, 1.0]
        elif is_product_match == 1:
            return [1, 1.0]


