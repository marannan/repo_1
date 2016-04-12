To run the matcher run python MPN_matcher.py

from MPN_matcher import ParseJson

call parse(self,walmart_json, vendor_json,*dict_path) function

obj = ParseJson()
obj.parse(walmart_json ,vendor_json, dict_path )

:param walmart_json: Walmart Json
:param vendor_json: Vendor Json
:param dict_path:Path to dictinory to be used
:return: a list of the form [prediction, confidence]
where prediction: 1 (yes), 0 (no), -1 (do not know),
confidence: a value in [0-1] (1 by default)(0.5 if found by probing or using dict)

