import re

class URLExtract(object):
    def __init__(self):

        None
    
    def extract_home_page(self,url):
        
        home_page = re.findall(r'(www.)',url)
        return home_page
    
if __name__ == "__main__":
    url_extract = URLExtract()
    print url_extract.extract_home_page("www.facebook.com/something/something")
    
        