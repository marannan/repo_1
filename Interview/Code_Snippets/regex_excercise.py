import re

class URLExtract(object):
    def __init__(self):

        None
    
    def extract_home_page(self,url):
        
        #home_page = re.match(r'.*\.(.*)\..*/.*/',url)
        
    
        #home_page = re.search(r'(.*\..*\..*)(/.*/)*',url)
        home_page = re.search(r"(.*\..*\..*)/.*/.*", url);
        
        
        return home_page.group(1)
    
if __name__ == "__main__":
    url_extract = URLExtract()
    print url_extract.extract_home_page("www.facebook.com/something/something")
    
        