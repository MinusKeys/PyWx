
from socketserver import DatagramRequestHandler
from sys import maxsize
from urllib import request
import requests
import bs4
import ssl
import re
import pandas as pd
from urllib3 import poolmanager

url = 'https://spotwx.com/products/grib_index.php?model=gem_lam_continental&lat=48.4179&lon=-123.35927&tz=America/Vancouver&display=table'


#what does all this mean

'''
class TLSAdapter(requests.adapters.HTTPAdapter):

    def init_poolmanager(self, connections, maxsize, block=False):
        """Create and initialize the urllib3 PoolManager."""
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        self.poolmanager = poolmanager.PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                ssl_version=ssl.PROTOCOL_TLS,
                ssl_context=ctx)

session = requests.session()
session.mount('https://', TLSAdapter())
res = session.get(url)
print(res)
'''
s = requests.Session()
a = requests.adapters.HTTPAdapter(pool_maxsize = maxsize)
s.mount('http://', a)
res = s.get(url)



'''
body = res.content.decode()

#start = body.index("var aDataSet =") #2934
#end = body.index("$(document).ready(function() {") #10257

data = body[2948:10256]

data = re.sub("'", "\"", data)

json_data = pd.read_json(data)

print(json_data)
'''