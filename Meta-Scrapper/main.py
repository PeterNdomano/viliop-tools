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

def scanResponse(response):
    print("SCAN OUTPUT:")
    print(response)

def showHelp(argv):
    help_text = "Use -u <targetUrl> and -d <outputDirectory> to specify targetUrl and directory where metadata and metafiles will be saved.\n Also make sure you're connected to the internet"
    help_text = "{0} "+help_text.format(argv[0]);
    print(help_text);


main(sys.argv)
