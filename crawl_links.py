import sys
import pycurl
#import cStringIO
import json
import ast
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import jellyfish
from pyvirtualdisplay import Display
import csv
import pandas as pd

# remove this once done
display = Display(visible=0, size=(800, 600))
display.start()

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 2)
profile.set_preference("network.proxy.autoconfig_url", "http://mcs182012:password@www.cc.iitd.ac.in/cgi-bin/proxy.research")
profile.update_preferences()

sel = webdriver.Firefox(firefox_profile=profile)

#sel = webdriver.Chrome()
#sel2 = webdriver.Chrome()
#fh=open("query.txt","r");
itr=1
query = "+".join(sys.argv[1].split('_'))


#pages = sys.argv[1]
pages = 1
output = ''
itr = 1

while itr <= 15:
    itr = itr + 1

    start_urls = "http://www.bbc.co.uk/search/news/?page="+str(itr)+"&q="+query;
    sel.get(start_urls)
    
    #print(sel.find_elements_by_xpath('//a'))
    #divs = sel.find_elements_by_xpath('//div[@id="news-content"]/ul/li[@class="DateItem"]')
#divs = sel.find_elements_by_tag_name('h1')
    divs = sel.find_elements_by_xpath('//h1//a')
    #divs = sel.find_elements_by_xpath('/html/body/div[6]/section[2]/ol/li[1]/article/div/h1/a')[0].text
    count = 0

    for i in divs:
        row = []
    
        url = i.get_attribute('href')
        #sel.close()
    
        row.append(url)
        print(url) #url
    

    #df = pd.DataFrame(row)
    #df.to_csv('file.csv', index=False)
        with open("links.csv", 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)    
    
#divs2 = sel.find_elements_by_xpath('//dd//time')  
"""    
for i in divs2:
    print(i.get_attribute('datetime')) #datetime
    print(i.text) #date
    
"""
