from http.server import BaseHTTPRequestHandler
from datetime import datetime
 
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_list = parse.parse_qsl(url_components.query)
    my_dict = dict(query_list)
    

    # print(111,my_dict)
    if 'capital' in my_dict:
      capital = my_dict.get('capital')
      url= 'https://restcountries.com/v3.1/capital/'
      res = requests.get(url+capital)
      data = res.json()
      cuntry=data[0]["name"]["common"]
      messaag=f'the cuntry of {capital} is {cuntry}'

    #   print(222,data)
    if 'cuntry' in my_dict:
        cuntry = my_dict.get('cuntry')
        url= 'https://restcountries.com/v3.1/name/'
        res = requests.get(url+cuntry)
        data = res.json()
        capital=data[0]["capital"][0]
        messaag=f' {capital} is the capital of {cuntry}'
    
      
    self.wfile.write(str(messaag).encode())
    return


