import argparse
import requests
import sys

print("---------------------------------------------------------")
print(" _____                __  __              _              ")
print("|  __ \              |  \/  |            | |             ")
print("| |__) |_   _  _ __  | \  / |  __ _  ___ | |_  ___  _ __ ")
print("|  ___/| | | || '_ \ | |\/| | / _` |/ __|| __|/ _ \| '__|")
print("| |    | |_| || |_) || |  | || (_| |\__ \| |_|  __/| |   ")
print("|_|     \__,_|| .__/ |_|  |_| \__,_||___/ \__|\___||_|   ")
print("              | |                                        ")
print("              |_|                                        ")

banner = "---------------------------------------------------------"

print(banner)

# Keyword

defaultKeyword = "FUZZ"

# Create the instance of the argument parser


parser = argparse.ArgumentParser(description="Use this tool to discover content on your target. Have fun!")


class Enumarate:
    def __init__(self, line):
        wordlist = open(list, "r")
    
        for line in wordlist:
            checkForStatusCode(line[:1])

        wordlist.close()

    def checkForStatusCode(url):
        try:
            request = requests.get(url)

            return str(request.status_code)

        except Exception as ex:
            print(ex)
            sys.exit(0)
    

def downloadCloudWordlist(url):
    request = requests.get(url)

    return request.text

def checkForHTTPInUrl(url):

    # Chech if the url provided has http:// or https://

    if not "http://" in url:
        return False

    else:
        return True


def addArguments():

    parser.add_argument("-w", help="REQUIRED: Wordlist.")
    parser.add_argument("-d", help="REQUIRED: Domain")
    parser.add_argument("--cloudwordlist", help="OPTINAL: Cloudwordlist. The cloudwordlist will be downloaded on the machine.")


addArguments()

# Check if an parameter has being provided to the cloudwordlist argument

args = parser.parse_args()


# Check if cloudwordlist is provided

if args.cloudwordlist != None:
    if checkForHTTPInUrl(args.cloudwordlist) == False:
        print("ERROR: HTTP:// not found in the url, Exiting.")
        sys.exit(1)

    else:
        cloudwordlist = open("cloudwordlist.txt", "w")
        cloudwordlist.write(downloadCloudWordlist(args.cloudwordlist))
        cloudwordlist.close()

        # Begin enumurating, and pass in the cloudwordlist as the list to enumarate.

        # Create the instance of class Enumurate

        enumarate = Enumarate()

        enumarate.__init__(args.cloudwordlist)


else:
    pass
