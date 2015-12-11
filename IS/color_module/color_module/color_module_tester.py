import sys
from color_module import find_match

def main():
    
    #example product match code    
    product_1 = '{"Brand":["Case Logic"],"Warranty Length":["25 Years"],"Country of Origin: Components":["USA or Imported"],"Product Short Description":["<li>Protect valuable data with this durable external hard drive case<li>Hard-shell exterior with zippered closure<li>Accessory compartment for AC power adapter and cables"],"Actual Color":["Black"],"Color":["Black"],"Product Segment":["Electronics"],"Product Name":["Case Logic Black Compact Portable Hard Drive Case"],"Product Type":["Electronics Carrying Cases"],"Manufacturer Part Number":["PHDC-1"],"Manufacturer":["Case Logic"],"Category":["Hard Disk Drive Cases & Bags"],"Assembled Product Width":["3.75"],"Product Long Description":["You can protect your drive on the go and then take it out at your destination to retrieve files and documents. Transport your information with ease with the Case Logic Black Compact Portable Hard Drive Case.<br><b>Case Logic Black Compact Portable Hard Drive Case:</b><ul><li>Protect valuable data with this durable external hard drive case</li><li>Hard-shell exterior with zippered closure</li><li>Case Logic compact portable hard drive case has accessory compartment for AC power adapter and cables</li><li>For small portable hard disk drives</li><li>3.75W x 6H x 1.25D</li></ul>"],"Assembled Product Length":["1.25"],"GTIN":["00085854105460"],"Assembled Product Height":["6.0"],"Composite Wood Code":["1"],"Warranty Information":["Case Logic insists on outstanding quality. Every product, unless otherwise indicated with a separate bullet point on a specific product information page, is warranted against defects in materials and workmanship for as long as the original owner owns the product. Every product marked with a bullet point is warranted against defects in materials and workmanship for the term indicated in the bullet point. The warranty applies only when the products have been put to the use intended by Case Logic as designated by the product packaging. If the defective product is no longer available, we will replace it with a similar product or one of equal value. This warranty gives you specific legal rights, and you may also have other rights which vary from state to state. This warranty applies to product purchased in the U.S. only."],"UPC":["085854105460"]}'
    product_2 = '{"Brand":["Case Logic"],"Item ID":["5347115"],"Product Segment":["Electronics"],"Product Type":["Electronics Carrying Cases"],"Product Name":["Case Logic Compact Portable Hard Drive Case"],"Manufacturer Part Number":["PHDC-1-BLACK"],"Manufacturer":["Case Logic"],"Assembled Product Width":["1.7"],"Product Long Description":["Protect your portable hard drive store your necessary cords and never lose a single byte of information. <br /><ul><li><b>Product Material:</b> Molded EVA</li><li><b>Product Weight:</b> 0.30 lbs.</li><li><b>Laptop Compartment Dimensions:</b> 5.5&quot; x 3.75&quot; x 1.25&quot;</li><li>Compact case to store or transport smaller portable hard drives</li><li>Slimline design allows case to easily fit into any backpack or briefcase</li><li>Durable hardshell exterior to protect valuable data</li><li>Interior strap secures portable hard drive in place</li><li>Zippered closure</li><li>Available in: Asia/Pacific Canada Europe Latin America US</li></ul>"],"Assembled Product Length":["4.5"],"Assembled Product Height":["6.25"],"UPC":["0008585410546"]}'
    user_dict = '/media/ashokmarannan/My_Drive/Ashok/OneDrive/Github/IS/colors_dict.txt'
    
    (output, confidence) = find_match(product_1, product_2, dictionary = user_dict)
    print output
    

if __name__ == "__main__":
    main()