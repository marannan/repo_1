# Brand name matcher

Brand name matcher takes the two product description and gives the output if the brand name in those 2 products matches. It also gives the confidence score of the prediction made.
The main runnable file is 'Main.py' which has a method called 'brand_name_match', this method takes following arguments :
  - Product A JSON string
  - Product B JSON string
  - Optional, path of the dictionary with respect to the location of the Main.py file

Returns, a list with first element as the prediction (0 mismatch, 1 match, -1 don't know) and the second element as the confidence score on the scale from 0 to 1 (including)

All the other file in this modules serves as the helper to the Main file. One file called 'Test_api.py' contains the example usage of the Main file. 

> All the files used internally can be found under files folder.


### Version
0.0.1

### Dependencies

Following pacakges are required to run the module :

* re
* json
* logging
* editdistance
* nose

