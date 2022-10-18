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
    cmd_args = argv[1:];
    url = ""
    dir = ""
    if(len(cmd_args) >= 2):
        opts, args = getopt.getopt(cmd_args, "d:u:", ["url=", "dir"])
        for opt, val in opts:
            if opt in ("-d", '--dir'):
                dir = val.strip();
            elif opt in ("-u", '--url'):
                url = "http://"+val.strip();

        if(len(url) > 0 and len(dir) > 0):
            print("Meta Scrapper is starting......")
            getRobotsTxt(url)
            getSitemapXml(url)
            getSecurityTxt(url)
            getHumansTxt(url)
            scanForMetaTags(url)
            scanWellKnowsDir(url)
        else:
            showHelp(argv);
    else:
        showHelp(argv)

def getRobotsTxt(url):
    print('Fetching robots.txt...')

def getSitemapXml(url):
    print('Fetching sitemap.xml...');

def getSecurityTxt(url):
    print('Fetching security.txt....')

def getHumansTxt(url):
    print('Fetching humans.txt....')

def scanForMetaTags(url):
    print('Scanning meta tags')

def scanWellKnowsDir(url):
    print('Scanning .well-known folder...')

def scanResponse(response):
    print("SCAN OUTPUT:")
    print(response)

def showHelp(argv):
    help_text = "{0} Use -u <targetUrl> and -d <outputDirectory> to specify targetUrl and directory where metadata and metafiles will be saved.\n Also make sure you're connected to the internet".format(argv[0]);
    print(help_text);


main(sys.argv)
