import re


with open(name) as product_pairs:
    
line = "34972919-23136815#UnbeatableSale.com?34972919?{"Condition":["New"],"Brand":["Emerge Tech"],"Country of Origin: Components":["USA and/or Imported"],"Product Short Description":["Emerge ETCABLESPLIT Retractable Headphone Splitter"],"Actual Color":["Multicolor"],"Product Segment":["Electronics"],"Color":["Multicolor"],"Product Name":["Emerge ETCABLESPLIT Retractable Headphone Splitter"],"Product Type":["Headphones"],"Manufacturer Part Number":["ETCABLESPLIT"],"Manufacturer":["Emerge Tech"],"Category":["Headphones"],"Product Long Description":["This Emerge retractable 3.5mm male to dual 3.5mm female audio cable is the perfect solution for extending the length of earbud or audio cables."],"GTIN":["00181204300001"],"Warranty Information":["Y"],"UPC":["181204300001"]}?23136815#UnbeatableSale.com?{"Product Type":["Headphones"],"Product Name":["Emerge Technologies Inc Retractable In-Ear Style Earbud For Hands Free Mobile Ph"],"Brand":["Emerge Tech"],"Product Long Description":["SKU: JNSN21172"],"Product Segment":["Electronics"]}?MISMATCH"
prod_1_json = re.findall(r"'(.*)'.*{", line)