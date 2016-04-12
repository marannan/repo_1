__author__ = 'aliHitawala'
import BrandNameMatcher


def brand_name_match(json_str_a, json_str_b, dict_path=None) :
    """
    Predicts match mismatch and gives the confidence score, given 2 JSON string input of the products.
    Takes dictionary as input (optional). Dictionary should be of the form (<brandName> <frequency>).
    :rtype : list
    :param Product A json string:
    :param Product B json string:
    :param Optional, Path of the dictionary with respect to the location of the file BrandNameDictionary.py:
    :return: a list with first element as the prediction (0 mismatch, 1 match, -1 don't know) and the second element as the confidence score on the scale from 0 to 1 (including)
    """
    return BrandNameMatcher.match_products(json_str_a, json_str_b, dict_path)