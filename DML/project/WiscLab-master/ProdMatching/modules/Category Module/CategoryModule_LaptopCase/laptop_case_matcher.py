import re

product_key = []


def check_UPC(product1, product2):
    """
    Checks if the products have UPC and if they do checks if they are the same
    :param product1: Dictionary containing key-value pairs for product 1
    :param product2: Dictionary containing key-value pairs for product 2
    :return: 1 if UPC matches else 0
    """
    global product_key
    if 'UPC' in product_key:
        if 'UPC' in product1[0].keys():
            if 'UPC' in product2[0].keys():
                if product1[0]['UPC'] == product2[0]['UPC']:
                    return 1
                else:
                    return 0


def check_MPN(product1, product2):
    """
    Checks if the products have Manufacturer Part Number and if they do checks if they are the same
    :param product1: Dictionary containing key-value pairs for product 1
    :param product2: Dictionary containing key-value pairs for product 2
    :return: 1 if MPN matches else 0
    """
    global product_key
    if 'Manufacturer Part Number' in product_key:
        if 'Manufacturer Part Number' in product1[0].keys():
            if 'Manufacturer Part Number' in product2[0].keys():
                if product1[0]['Manufacturer Part Number'] == product2[0]['Manufacturer Part Number']:
                    return 1
                else:
                    return 0


def get_color_score(product1, product2):
    """
    Checks if the products have Color attribute and if they do checks if they are the same
    :param product1: Dictionary containing key-value pairs for product 1
    :param product2: Dictionary containing key-value pairs for product 2
    :return: 1 if color matches else 0
    """
    color_score = 0
    global product_key
    if 'Color' in product_key:
        if 'Color' in product1[0].keys():
            if 'Color' in product2[0].keys():
                if product1[0]['Color'] == product2[0]['Color']:
                    color_score = color_score + 1.0
                else:
                    color_score = color_score + 0.0

    if 'Actual Color' in product_key:
        if 'Actual Color' in product1[0].keys():
            if 'Actual Color' in product2[0].keys():
                if product1[0]['Actual Color'] == product2[0]['Actual Color']:
                    color_score = color_score + 1.0
                else:
                    color_score = color_score + 0.0

    return color_score


def get_brand_score(product1, product2):
    """
    Checks if the products have Brand attribute and if they do checks if they are the same
    :param product1: Dictionary containing key-value pairs for product 1
    :param product2: Dictionary containing key-value pairs for product 2
    :return: 1 if Brand matches else 0
    """

    global product_key
    if 'Brand' in product_key:
        if 'Brand' in product1[0].keys():
            if 'Brand' in product2[0].keys():
                if product1[0]['Brand'] == product2[0]['Brand']:
                    return 1
                else:
                    return 0


def get_material_score(product1, product2):
    """
    Checks if the products have Material attribute and if they do checks if they are the same
    :param product1: Dictionary containing key-value pairs for product 1
    :param product2: Dictionary containing key-value pairs for product 2
    :return: 1 if Material matches else 0
    """
    global product_key

    if 'Product Long Description' in product_key:
        if 'Product Long Description' in product1[0].keys():
            if 'Product Long Description' in product2[0].keys():
                p1ld = product1[0]['Product Long Description'][0]
                p2ld = product2[0]['Product Long Description'][0]
                # print(p1ld)
                if 'Material' in product_key:
                    if 'Material' in product1[0].keys():
                        if 'Material' in product2[0].keys():
                            if product1[0]['Material'] == product2[0]['Material']:
                                return 1
                            else:
                                return 0
                        else:
                            if 'Product Long Description' in product2[0].keys():
                                p = re.findall(r'<li>.*Product Material\W*\w*\W*(.*?)</li>', p2ld)
                                if len(p) > 0:
                                    if product1[0]['Material'] == p[0]:
                                        return 1
                                    else:
                                        return 0
                    else:
                        if 'Material' in product2[0].keys():
                            if 'Product Long Description' in product1[0].keys():
                                p = re.findall(r'<li>.*Product Material\W*\w*\W*(.*?)</li>', p1ld)
                                if len(p) > 0:
                                    if product2[0]['Material'] == p[0]:
                                        return 1
                                    else:
                                        return 0
                        else:
                            p1 = []
                            p2 = []
                            if 'Product Long Description' in product2[0].keys():
                                p2 = re.findall(r'<li>.*Product Material\W*\w*\W*(.*?)</li>', p2ld)
                            if 'Product Long Description' in product1[0].keys():
                                p1 = re.findall(r'<li>.*Product Material\W*\w*\W*(.*?)</li>', p1ld)
                            if len(p1) > 0 and len(p2) > 0:
                                if p1[0] == p2[0]:
                                    return 1
                                else:
                                    return 0


def get_manufacturer_score(product1, product2):
    """
    Checks if two products have the Manufacturer attribute and if they do, checks if they are the same
    :param product1: Dictionary containing key-value pairs for product 1
    :param product2: Dictionary containing key-value pairs for product 2
    :return: 1 if manufacturer matches else 0
    """

    global product_key
    if 'Manufacturer' in product_key:
        if 'Manufacturer' in product1[0].keys():
            if 'Manufacturer' in product2[0].keys():
                if product1[0]['Manufacturer'] == product2[0]['Manufacturer']:
                    return 1
                else:
                    return 0


def get_product_length_score(product1, product2):
    """
    Checks if two products have Length attribute and if they do, checks if they are the same
    :param product1: Dictionary containing key-value pairs for product 1
    :param product2: Dictionary containing key-value pairs for product 2
    :return: 1 if length matches, 0 if not
    """

    global product_key
    if 'Assembled Product Length' in product_key:
        if 'Assembled Product Length' in product1[0].keys():
            if 'Assembled Product Length' in product2[0].keys():
                if product1[0]['Assembled Product Length'] == product2[0]['Assembled Product Length']:
                    return 1
                else:
                    return 0


def get_product_height_score(product1, product2):
    """
    Checks if two products have height attribute and if they do, checks if they are the same
    :param product1: Dictionary containing key-value pairs for product 1
    :param product2: Dictionary containing key-value pairs for product 2
    :return: 1 if height matches, 0 if not
    """

    global product_key
    if 'Assembled Product Height' in product_key:
        if 'Assembled Product Height' in product1[0].keys():
            if 'Assembled Product Height' in product2[0].keys():
                if product1[0]['Assembled Product Height'] == product2[0]['Assembled Product Height']:
                    return 1
                else:
                    return 0


def get_product_width_score(product1, product2):
    """
    Checks if two products have width attribute and if they do, checks if they are the same
    :param product1: Dictionary containing key-value pairs for product 1
    :param product2: Dictionary containing key-value pairs for product 2
    :return: 1 if width matches, 0 if not
    """

    global product_key
    if 'Assembled Product Width' in product_key:
        if 'Assembled Product Width' in product1[0].keys():
            if 'Assembled Product Width' in product2[0].keys():
                if product1[0]['Assembled Product Width'] == product2[0]['Assembled Product Width']:
                    return 1
                else:
                    return 0


def get_weight_score(product1, product2):
    """
    Extracts weight from product long description and checks if they match
    :param product1: Dictionary containing key-value pairs for product 1
    :param product2: Dictionary containing key-value pairs for product 2
    :return: 1 if weight matches, 0 if not
    """

    if 'Product Long Description' in product_key:
        if 'Product Long Description' in product1[0].keys():
            if 'Product Long Description' in product2[0].keys():
                p1ld = product1[0]['Product Long Description'][0]
                p2ld = product2[0]['Product Long Description'][0]

                p1 = re.findall(r'<li>.*Product Weight\W*\w*\W*(.*?)</li>', p1ld)
                p2 = re.findall(r'<li>.*Product Weight\W*\w*\W*(.*?)</li>', p2ld)

                if p1 and p2:
                    if len(p1) > 0 and len(p2) > 0:
                        if p1[0] == p2[0]:
                            return 1
                        else:
                            return 0

                else:
                    return 0
    else:
        return 0


def get_laptop_compartment_dimension_score(product1, product2):
    """
    Extracts laptop compartment dimension from product long description and checks if they match
    :param product1: Dictionary containing key-value pairs for product 1
    :param product2: Dictionary containing key-value pairs for product 2
    :return:  1 if laptop compartment dimension matches, 0 if not
    """

    if 'Product Long Description' in product_key:
        if 'Product Long Description' in product1[0].keys():
            if 'Product Long Description' in product2[0].keys():
                p1ld = product1[0]['Product Long Description'][0]
                p2ld = product2[0]['Product Long Description'][0]
                p1 = re.findall(r'<li>.*Laptop Compartment Dimensions:\W*\w*\W*(.*?)</li>', p1ld)
                p2 = re.findall(r'<li>.*Laptop Compartment Dimensions:\W*\w*\W*(.*?)</li>', p2ld)

                if p1 and p2:
                    if len(p1) > 0 and len(p2) > 0:
                        if p1[0] == p2[0]:
                            return 1
                        else:
                            return 0

                else:
                    return 0
    else:
        return 0


def is_match(product_keys, product_json_list):
    """
    Checks if two products refer to the same entity
    :param product_keys: List of attributes describing both the products
    :param product_json_list:  List containing dictionaries of key-value pairs of both the products
    :return: 1 if they refer to same product
             0 if they are different
             -1 if not sure
    """
    global product_key
    product_key = product_keys
    confidence_score = 0.0
    color_score = 0.0
    material_score = 0.0
    brand_score = 0.0
    manufacturer_score = 0.0
    weight_score = 0.0
    lcd_score = 0.0

    product1 = product_json_list[0]
    product2 = product_json_list[1]

    if check_UPC(product1, product2) == 1:
        return 1

    if check_MPN(product1, product2) == 1:
        return 1

    color_score = get_color_score(product1, product2)
    material_score = get_material_score(product1, product2)
    brand_score = get_brand_score(product1, product2)
    length_score = get_product_length_score(product1, product2)
    height_score = get_product_height_score(product1, product2)
    width_score = get_product_width_score(product1, product2)
    manufacturer_score = get_manufacturer_score(product1, product2)
    weight_score = get_weight_score(product1, product2)
    lcd_score = get_laptop_compartment_dimension_score(product1, product2)

    select_confidence_score = color_score + material_score + brand_score + length_score + height_score + width_score + \
                              manufacturer_score + weight_score + lcd_score

    for key in product_keys:
        if key in product1[0].keys():
            if key in product2[0].keys():
                if product1[0][key] == product2[0][key]:
                    confidence_score = confidence_score + 1

    if confidence_score > select_confidence_score:
        if confidence_score > 4:
            return 1
        elif confidence_score >= 2 and confidence_score <= 4:
            return -1
        else:
            return 0
    else:
        if select_confidence_score > 4:
            return 1
        elif select_confidence_score > 2 and select_confidence_score <= 4:
            return -1
        else:
            return 0
