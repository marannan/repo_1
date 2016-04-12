#! /usr/bin/python
from __future__ import division
import csv
import re
import itertools
import json


##########################################################################
# Match Function for given values in Assembled Product in JSON
##########################################################################
def match_ap(a, b):
 	
	ctr = 0
	w = [float(i) for i in a]
	v = [float(i) for i in b]
	w = sorted(w)
	v = sorted(v)
	
	if (w == v):
	#matched completely with 100% confidence
		return [1, 1]
	else:
	
		for x in a:
			for y in b:
				abs_diff = abs(float(x)-float(y))
				if abs_diff <= 1.0:
					ctr = ctr + 1
					break	
	
	if ctr == 3:
		#Matched with distance <= 1.0 and greater than 0.1, not 100% confidence
		return [1, 0.8]
	else:
		#Nomatch
		return [0, 1]



##########################################################################
# Match Function for extracted values using REGEX
##########################################################################
def match_ex(a, b):
       
      	ctr = 0

	if a == [0.0, 0.0, 0.0] or b == [0.0, 0.0, 0.0]:
		#Don't Know or missing values or ambiguous values
		#Confidence is not 100% because missing values could be because of Regex didn't find the correct values 
		return [-1, 0.8]

	elif (a == b):
		#print a
		#print b
		return [1, 1]
	else:
		for x in a:
			for y in b:
				abs_diff = abs(float(x)-float(y))
				if abs_diff <= 1.0:
					ctr = ctr + 1
					break	


	if ctr == 3:
	 	#Match
		return [1, 0.8]
	else:
		#Nomatch, in case Regex didn't find correct values
		return [0, 0.8]


############################################################################
# Extract hlw values from Assembled Product
############################################################################
def exap(x):
	list1 = re.findall(r'\bAssembled Product \b[A-Z][a-z]*[":]\W\W\W(\d*\.\d+|\d*)', x)
	return list1

###########################################################################
# Extract hlw values using Regex
###########################################################################
def exregex(x):
	list2 = re.findall(r'(\d*\.*-*\d*)\s*\D*\s*[HWLD]\s*[x|X]\s*(\d*\.*-*\d*)\s*\D*\s*[HWLD]\s*[x|X]\s*(\d*\.*-*\d*)\s*\D*\s*[HWLD]', x)
	if list2:
		#print "list2: ", list2
		return list2

	list3 = re.findall(r'(\d*\.*-*\d*)-*\s*[x|X]\s*(\d*\.*-*\d*)-*\s*[x|X]\s*(\d*\.*-*\d*)-*\s*[(][HLWD]\s*[x|X]*\s*[HLWD]\s*[x|X]*\s*[HLWD]', x)
	if list3:
		#print "list3: ", list3
		return list3

	list4 = re.findall(r'Height:\D*\s*(\d*\.*-*\d*)-*\D*\s*Width:\D*\s*(\d*\.*-*\d*)-*\D*\s*Depth:\D*\s*(\d*\.*-*\d)*-*\D*\s*', x)
	if list4:
		#print "list4: ", list4
		return list4

	list5 = re.findall(r'Height:\D*\s*(\d*\.*-*\d*)-*\D*\s*Width:\D*\s*(\d*\.*-*\d*)-*\D*\s*Length:\D*\s*(\d*\.*-*\d)*-*\D*\s*', x)
	if list5:
		#print "list5: ", list5
		return list5

	list6 = re.findall(r'(\d*\.*-*\d*)-*\s*[x|X]\s*(\d*\.*-*\d*)-*\s*[(][HLWD]\s*[x|X]*\s*[HLWD]', x)
	if list6:
		#print "list6: ", list6
		return list6

	list7 = re.findall(r'(\d*\.*\d*)\s*x\s*(\d*\.*\d*)\s*x\s*(\d*\.*\d*)', x)
	if list7:
		#print "list7: ", list7
		return list7


###########################################################################
# Predict Match Function
###########################################################################

def predict_HLW_match(walmart_json, vendor_json):

		# Call extract function from Assempled Product values
		walmart_hlw = exap(walmart_json)
		vendor_hlw = exap(vendor_json)

		if walmart_hlw and vendor_hlw:
			result_list = match_ap(walmart_hlw, vendor_hlw)  # this will output prediction and confidence score
			return (result_list)

		else:

			#WALMART - extraction
			# Call extract function using regex if not in Assembeled Product
			walmart_hlw1 = walmart_hlw
			if not walmart_hlw:
				wnewlist = exregex(walmart_json)
				if wnewlist:
					for tuple in wnewlist:
						walmart_hlw1 = [w.replace("-", ".") for w in tuple]
			
			# If any of the element in extracted list is empty string then replace it with 0 or if list is empty then add 0s 
			j = 0
			for i in walmart_hlw1:
				if i == '':
					walmart_hlw1[j] = '0'
				j = j+1
			if not walmart_hlw1:
				walmart_hlw1 = [0, 0, 0]
			
			# VENDOR - extraction
	                # Call extract function using regex if not in Assembeled Product
			vendor_hlw1 = vendor_hlw
			if not vendor_hlw:
				vnewlist = exregex(vendor_json)
				if vnewlist:
					for tuple in vnewlist:
						vendor_hlw1 = [v.replace("-", ".") for v in tuple]
	
			# If any of the element in extracted list is empty string then replace it with 0 or if list is empty then add 0s
			k = 0
			for i in vendor_hlw1:
				if i == '':
					vendor_hlw1[k] = '0'
				k = k+1
			if not vendor_hlw1:
				vendor_hlw1 = [0, 0, 0]
			
			
			walmart_hlw3 = [float(i) for i in walmart_hlw1]
			vendor_hlw3 = [float(i) for i in vendor_hlw1]
		
		  	for m in walmart_hlw3:
				if (m > 0.0 and m < 1.0):
					m = 1.0
				else:
					round(m)

			for n in vendor_hlw3:
				if (n > 0.0 and n < 1.0):
					n = 1.0
				else: 
					round(n)
	
		  	
		  	walmart_hlw = sorted(walmart_hlw3)
			vendor_hlw = sorted(vendor_hlw3)

			result_list = match_ex(walmart_hlw, vendor_hlw)

		 	return (result_list)

###################################################################################################33	
