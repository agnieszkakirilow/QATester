import os
import sys
import json
from typing import Any

class Config:
    '''Config class is responsible for storing framework's and env's configuration '''
    
    request_timeout = 20
    user_name = os.environ.get('USERNAME')
    env = os.environ.get('BQA_ENV')  # in linux export BQA_ENV=aga


config = Config()

print('....config_easy...')
print(config.request_timeout)
print(config.user_name)
print(config.env)
#TODO why it prints none


class DictConfigProvider():
    def __init__(self, input_values: dict) -> None:  # it does have return type (better for error handling)
         super().__init__()  # why like this, usually super() is used why class inherits after another class
         self.values = input_values

    def get(self, item_name: str) -> Any:
        return self.values[item_name]


class OSConfigProvider():
    @staticmethod
    def get(item_name: str) -> Any:  # what does Any mean?
        value = os.getenv(item_name)
        return value 

class JSONConfigProvider():
    @staticmethod
    def _read_config(config_path):
        with open(config_path) as json_file:
            return json.load(json_file)
    
    @staticmethod
    def get(item_name: str) -> Any:
        value = JSONConfigProvider._read_config('/home/agnieszkakirilow/QATester/src/config/envs/dev.json')
        #TODO how to give relative path
        return value.get(item_name)
 
class ConfigHard:
    '''Config class is responsible for storing framework's and env's configuration '''
    def __init__(self, config_providers) -> None:
        self.config_providers = config_providers
        self.conf_dict = {}
        # register parameters block
        self._register("USERNAME")
        self._register("USER")
        self._register("URLTEST")
        self._register("BROWSER")
        self._register("URL")
        self._register('response_ok')
        

    def get(self, item_name: str)-> Any:
        if item_name not in self.conf_dict:
            raise AttributeError(f'please register {item_name} var before usage')
        return self.conf_dict[item_name]
    
    # python way
    def __getattr__(self, item_name: str):
        if item_name not in self.conf_dict:
            raise AttributeError(f'please register {item_name} var before usage')
        return self.conf_dict[item_name]
    
    def _register(self, item_name: str)-> None:
        # retrieve value of param wtih item_name and store it in class for later usage
        for provider in self.config_providers:
            value = provider.get(item_name)
            if value is not None:
                self.conf_dict[item_name] = value
                print(item_name, value)
                return
        
        raise ValueError(f'{item_name} name is missing in config providers')


dict_confprovider = DictConfigProvider({'USERNAME': 'bla', 'USER': 'ble', 'BROWSER': 'chrome', 'URL': 'https://api.github.com/search/repositories', 
                                        'LALA': 'pala', 'URLTEST': 'http://www.google.pl', 'response_ok': 200})
print('....config_all....')
config_all = ConfigHard([OSConfigProvider, JSONConfigProvider, dict_confprovider])
print('....config_two....')
config_two = ConfigHard([JSONConfigProvider, dict_confprovider])
print('....config_two....')
config_one = ConfigHard([dict_confprovider])
#config = ConfigHard([OSConfigProvider, JSONConfigProvider])

print(f'get parameter "USER": {config_all.get("USER")}')
print(f'get parameter "BROWSER": {config_all.get("BROWSER")}')
print(f'get parameter "URL": {config_all.get("URL")}')
print(sys.executable)
print(sys.path)
# print(f'get paramter "LALA": {config_all.get("LALA")}')