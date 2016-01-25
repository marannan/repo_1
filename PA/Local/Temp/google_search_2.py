import urllib
import mechanize
from bs4 import BeautifulSoup
import re


def main(query=""):
   from xgoogle.search import GoogleSearch, SearchError
   try:
      gs = GoogleSearch("quick and dirty")
      gs.results_per_page = 50
      results = gs.get_results()
      for res in results:
         #print res.title.encode('utf8')
         #print res.desc.encode('utf8')
         print res.url.encode('utf8')
         print
   except SearchError, e:
      print "Search failed: %s" % e
    
   return


if __name__ == "__main__":
   main()