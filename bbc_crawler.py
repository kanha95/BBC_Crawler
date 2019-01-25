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


# remove this once done
display = Display(visible=0, size=(800, 600))
display.start()

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 2)
profile.set_preference("network.proxy.autoconfig_url", "http://mcs182012:password@www.cc.iitd.ac.in/cgi-bin/proxy.research")
profile.update_preferences()

sel2 = webdriver.Firefox(firefox_profile=profile)

with open('links.csv', 'r') as csvFile:
    divs = csv.reader(csvFile)
   

    for i in divs:
        row = []
        print(i[0])
     
        sel2.get(i[0])
        divs2 = sel2.find_elements_by_xpath('//li//div[@class=\'date date--v2\']')
        if len(divs2)==0: continue
    
        row.append(divs2[0].text)
        print(divs2[0].text) #date
        divs4 = sel2.find_elements_by_xpath('//h1[@class=\'story-body__h1\']')
        row.append(divs4[0].text)
        print(divs4[0].text) #title
        row.append(i[0])
        print(i[0]) #url
        divs3 = sel2.find_elements_by_xpath('//div[@class=\'story-body__inner\']//p') #content
        str1 = ""
        for j in divs3:
            str1 = str1 + j.text
            print(j.text)
        row.append(str1)

    #df = pd.DataFrame(row)
    #df.to_csv('file.csv', index=False)
        with open('people1.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)    
    
#divs2 = sel.find_elements_by_xpath('//dd//time')  
"""    
for i in divs2:
    print(i.get_attribute('datetime')) #datetime
    print(i.text) #date
    
"""
