
import requests
import bs4
r = requests.get('https://spotwx.com/products/grib_index.php?model=gem_lam_continental&lat=48.4179&lon=-123.35927&tz=America/Vancouver&display=table')
body = r.content

#start = body.index("var aDataSet =") #2934
#end = body.index("$(document).ready(function() {") #10257

#data = body[2948:10257]

soup = bs4.BeautifulSoup(body,'html.parser')

s = soup.find('div',class_='container')

#t = s.find('table',id='example')

print(ss)






