from flask import Flask,render_template
from sys import maxsize
import ssl
import requests
import re
import pandas as pd
from urllib3 import poolmanager


url = 'https://spotwx.com/products/grib_index.php?model=gem_lam_continental&lat=48.4179&lon=-123.35927&tz=America/Vancouver&display=table'

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

s = requests.Session()
#a = requests.adapters.HTTPAdapter(pool_maxsize = maxsize)
s.mount('http://', TLSAdapter)
res = s.get(url)

body = res.content.decode()

start = body.find('var aDataSet = ') + len('var aDataSet = ')
end = body.find('$(document)')
buff = 5
body = body[start:end-buff]

body = re.sub("'", "\"", body)

json_data = pd.read_json(body)


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html",response = json_data)

if __name__ == '__main__':
   app.run()