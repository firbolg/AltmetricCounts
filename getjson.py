#test api fetching json object, test pyaltmetric creating pyalmetric objects

import urllib
import urllib.request
import json 

from pyaltmetric import Altmetric, Citation

url = ('https://api.altmetric.com/v1/doi/10.1101/2020.10.07.20208231')

json_obj = urllib.request.urlopen(url)

data = json.load(json_obj)

a = Altmetric ()

c = Citation(a.doi('10.1101/2020.02.09.20021261'))

print (c)

