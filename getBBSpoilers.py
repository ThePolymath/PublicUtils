#Birchbox spoilers util by ThePolymath
#2016

import requests
import sys

def main(args):
    newStr = args[1] + "-" + args[2];
    host = "https://www.birchbox.com/shop/birchbox-1/{d}/{d}-bb"
    host = host.replace("{d}", newStr);
    for x in range(1,71):
        response = requests.head(host + str(x))
        if response.status_code != 404:
            print host + str(x) + "\n"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: python getBBSpoilers.py month year \n example: python getBBSpoilers.py april 2016"
    else:
        main(sys.argv)