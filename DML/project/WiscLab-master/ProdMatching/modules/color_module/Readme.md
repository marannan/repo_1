Author: Ashok Marannan
CS ID : marannan
Mail  : marannan@wisc.edu , ashok.marannan@hotmail.com

Module: Color Match
Build No: v1.0
Release Date: 12-06-2015

Introduction:
	This module extracts values for attributes "Color" and "Actual Color" in the product pair and predicts a match based on the extracted values. This module uses default dictionary for colors "colors_dict.txt" available in the package folder. Alternatively user can pass dicctionary file as an optional argument for the API specified below.

Usage:
	1) Install the module using setup.py install
	or
	1) Copy the package to project directory
	2) Import API find_match from color_module
	3) output, confidence = find_match(json_str_a, json_str_b, dictionary="path_to_user_dict.txt")


Bug reporting:
	File bugs at ashok.marannan@hotmail.com



