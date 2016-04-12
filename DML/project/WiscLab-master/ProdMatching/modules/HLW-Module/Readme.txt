Height-Length-Width Matching Module

This module takes the two product descitption in json format and output (prediction, confidence score). The main python script is 'HLW_module.py' which has a called method 'predict_HLW_match'.

Here are the Instructions to run:

1) Copy the package to project library
2) Import the method 'predict_HLW_match' from HLW_module as below:
	from HLW_module import predict_HLW_match
3) Call the function as below:
	Output = predict_HLW_match(product1_json, product2_json)
	
	i) Input Parameters 
		product1_json - JSON describing first product
		product2_json - JSON describing second product
	ii) Output --> [prediction, confidence]
		prediction: 
			1 -> Match
			0 -> NoMatch
		       -1 -> Not sure or Missing values
		confidence:
			1 -> complete match
		      0.8 -> if value of height/length/width is matching with difference of 0 to 1
		      	     OR
			     if it extracted incorrect values



