import urllib
import requests
import csv
import copy
import sys
import random
from bs4 import BeautifulSoup as bs



url = 'https://en.wikipedia.org/wiki/List_of_algorithms'

req = requests.get(url)
soup = bs(req.text, 'lxml')

l = []

## other method, find the div that englobes everything
# and parse line by line, going deeper if possible, to keep
# the structure
global_div = soup.find('div', {"class":"mw-parser-output"})

domain = ''
subdomain = ''
sub_subdomain = ''
title = ''
link = ''
description = ''

for elem in global_div:
    if(elem.name == "h2"):
        # We encounter an h2, so we reinit the entry
        subdomain = ''
        sub_subdomain = ''
        if elem.contents[0].text != 'See also':
            domain = elem.contents[0].text
        #print(elem.contents[0].text)
    elif(elem.name == "h3"):
        sub_subdomain = ''
        subdomain = elem.contents[0].text
        #print(" " + elem.contents[0].text)
    elif(elem.name == "h4"):
        sub_subdomain = elem.contents[0].text
        #print("     " + elem.contents[0].text)
    elif(elem.name == "ul"):
        for child in elem.descendants:
            if child.name == "li":
                # il has no child, its the last, so it's an entry
                if child.ul is None and child.a is not None:
                    print(child)
                    title = child.a['title']
                    link = url+child.a['href']
                    description = child.a.contents[0]
                    if title == description:
                        description = ''
                    l.append(dict(
                        Domain=domain,
                        Subdomain=subdomain,
                        Sub_subdomain=sub_subdomain,
                        Algorithm="",
                        Title=title,
                        Description=description,
                        Link=link
                    ))
#print(l)
with open('algorithms.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.writer(f)
    w.writerow(l[0].keys())
    for x in l:
        w.writerow(x.values())

random.shuffle(l)
with open('algorithms_shuffled.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.writer(f)
    for x in l:
        w.writerow(x.values())