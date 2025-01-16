""" 
libary for checko.ru API functions.
Documentation: https://github.com/webcartel-https/pycheckoapi
Author: https://github.com/webcartel-https
version: 0.1
"""
from requests import get
from requests.exceptions import ConnectionError as rq_conn
from pca_exceptions import MethodException, MessageException
from json import dump


class Base:
    def __init__(self):
        pass


    def is_connection_secure(self,connection): 
        if connection or connection is None:
            return "https"
        else:
            return "http"

    def check_method(self,method):  
        method_check = ("company","entrepreneur","person","search",
        "finances","contracts","inspections","enforcements","legal-cases","bank")
        if not method in method_check:
            raise MethodException(method=method)
        return True
        
    def parameters_check(self,params):
        params_check = ("ogrn","inn","kpp","okpo")
        if not params in params_check:
            return False
        else:
            return True
        
    def message(self,meta):
        try:
            if not meta['message']:
                return True
            else:
                raise MessageException(msg=meta['message'])
        except KeyError:
            return True
            
        
class Checko:
    def __init__(self, method:str, api_key:str, parameters:str,
                 id:str, source = None, secure_connect = None):   
        self.b = Base()
        self.secure_connect = self.b.is_connection_secure(connection=secure_connect)
        self.method = method
        self.api_key = api_key
        self.parameters = parameters
        self.id = id
        self.source = source
        if self.source:
            self.URL =f"{self.secure_connect}://api.checko.ru/v2/{self.method}?key={self.api_key}&{self.parameters}={self.id}&source=true"
        else:
            self.URL =f"{self.secure_connect}://api.checko.ru/v2/{self.method}?key={self.api_key}&{self.parameters}={self.id}"
        self.method_check = self.b.check_method(method=method)
        self.params_check = self.b.parameters_check(params=parameters)
        

    def request(self):  
        try:
            r = get(self.URL)
        except rq_conn:
            raise rq_conn("Check your internet connection and try again")
        return r


    def default_parse(self,data):
        js = data.json()
        m = js["meta"] 
        if self.b.message(meta=m):
            d = js["data"]
            if self.method == "finances":
                d = js["bo.nalog.ru"]["Отчет"]
            if self.source:
                try:
                    s = js["source_data"]
                    for i in s:
                        print(f"> | {i}{s[i]}")
                except KeyError:
                    print("1")
            for i in d:
                print(f"> | {i}:{d[i]}")
            return js
        
    def get_data(self,request):
        return request.json()['data']
    
    def get_meta(self,request):
        return request.json()['meta']
    
    def get_request_count(self,request):
        return request.json()['meta']['today_request_count']
    
    def get_balance(self,request):
        return request.json()['meta']['balance']

    def save_file(self,js,filename): 
        with open(f"{filename}.json",'w',encoding="utf-8") as json_file:
            dump(js,json_file,ensure_ascii=False)

    def status_code(self,request):
        return request.status_code