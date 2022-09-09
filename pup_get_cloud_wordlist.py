import requests
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-cloudwordlist", help="link to the wordlist goes here")

args = parser.parse_args()

cloudWordlist = args.cloudwordlist

def getWordlist():
    try:
        request = requests.get("http://google.com")
        
        return request
        
    except Exception as ex:
        print(ex)
    
print(str(getWordlist()))

