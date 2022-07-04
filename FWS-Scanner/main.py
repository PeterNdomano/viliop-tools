# importing sys
import sys
import getopt
import os
from pathlib import Path

#adding python_modules folder to path
currentDir = Path(__file__).parent;
modulesFolder = os.path.join(Path(currentDir).parent, 'python_modules')
sys.path.insert(0, modulesFolder)

import requests

def main(argv):
    help_text = "{0} make sure url is valid, use -u <targetUrl>".format(argv[0])
    targetUrl = "";

    if len(argv) > 0:
        try:
            opts, args = getopt.getopt(argv[1:], "u:", ["url="]) #getting cmd options
            for opt, arg in opts:
                if opt in ("-u", "--url"):
                    targetUrl = arg
                    print("Fingerprinting Web Server at {0}".format(targetUrl))
                    print("Please wait......")
                    server = bannerGrabbing(targetUrl)
                    if server != False:
                        scanResponse("Server is: "+server)
                    else:
                        scanResponse("Could not Fingerprint the Web Server")
                else:
                    print(help_text)
        except:
            print(help_text)
    else:
        print(help_text)

def scanResponse(response):
    print("SCAN OUTPUT:")
    print(response)

def bannerGrabbing(url):
    req = requests.get(url)
    #check headers length
    if len(req.headers) > 0:
        if 'Server' in req.headers:
            return req.headers['Server']
        else:
            return False
    else:
        return False

def malRequests(url):
    #to be implemented..
    return False



main(sys.argv)
