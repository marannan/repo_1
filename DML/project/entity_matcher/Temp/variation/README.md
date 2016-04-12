Author: Arjun Gurumurthy
CS ID : arjun
Mail  : arjun@cs.wisc.edu , arjung1990@gmail.com

Module: Variation Module
Build No: v1.0
Release Date: 12-06-2015

Introduction:
	This module takes a product pair and returns whether the two products vary in only a few attributes. It attempts to do the same by first checking if most words overlap, and if not, falls back to retrieving values of individual attributes and then making a decision.
    
    If the products are different products altogether, a list [0,1] is returned. ( where 0 indicates that products vary a lot, 1 is the confidence score)
    If the products are essentially the same with only a few variants, a list [1,1] is returned. ( where 1 indicates that the variation is not much, 1 is the confidence score)  
    If any exception or error arises when computing the value, a list [-1,1] is returned. (where -1 indicates cannot predict variation/no variation, 1 is the confidence score)


Usage:
	1) Install the module using setup.py install
	or
	1) Copy the package to project directory
	2) Import API predict_match from variation_module
	3) output, confidence = find_match(json_str_a, json_str_b)


Bug reporting:
	File bugs at arjun@cs.wisc.edu



