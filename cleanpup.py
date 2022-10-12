# the defination of shit is here

from threading import Thread
from os.path import exists

import argparse
import sys
import requests
import os

banner = "------------------------------------------"

print(banner)

print("██████╗ ██╗   ██╗██████╗ ██████╗ ██╗   ██╗")
print("██╔══██╗██║   ██║██╔══██╗██╔══██╗╚██╗ ██╔╝")
print("██████╔╝██║   ██║██████╔╝██████╔╝ ╚████╔╝ ")
print("██╔═══╝ ██║   ██║██╔═══╝ ██╔═══╝   ╚██╔╝ " )
print("██║     ╚██████╔╝██║██╗  ██║        ██║ "  )
print("╚═╝      ╚═════╝ ╚═╝╚═╝  ╚═╝        ╚═╝"  )



# The default keyword for the program. You can change this to a custom one using the argument --keyword.
defaultKeyword = "FUZZ"

headers = {"User-Agent":"PupMaster/0.1"}


# Create the instance of the argparser, and add the arguments for the fuzzer



parser = argparse.ArgumentParser(description="Use this tool to discover content on your target. Have fun!")

parser.add_argument("-w", help="REQUIRED: Input the wordlist location here.")
parser.add_argument("-d", help="REQUIRED: Input the (URL) here.")
parser.add_argument("--filter", help="OPTIONAL: Filter the response(s) by response code.", type=int)
parser.add_argument("--filters", help="WORK IN PROGRESS: Specify a list of codes to filter the response(s) by.")
parser.add_argument("--algorithm", help="OPTIONAL: Use a built-in algorithm to send requests faster.")
parser.add_argument("--cloudwordlist", help="WORK IN PROGRESS: Link a wordlist in the cloud.")
parser.add_argument("--keyword", help="OPTIONAL: Specfiy your own 'FUZZ' keyword.")
parser.add_argument("--output", help="OPTIONAL: Link an output file.")

arguments = parser.parse_args()

# Variables store the values provided by the arguments

domain = arguments.d

print(banner)

def sendRequest(url):
	try:
		r = requests.get("http://" + url)

		return r.status_code

	except:
		print("FAILED: " + url)

def checkForKeywordInDomain(domain):
	if defaultKeyword in domain:
		return True

	else:
		return False

class CheckForKeyWordInDomain:
	def __init__(self):
		pass

	def checkForKeyWordInDomain(self, domain):
		if defaultKeyword in domain:
			return True 

		else:
			return False

class Enumerate:
	def __init__(self, line, domain, filter):

			url = domain.replace(defaultKeyword, line)

			print(url)

			code = sendRequest(url=url)

			if filter == None:								
				print("TRIED: " + line + ": " + str(code))
			
			elif filter <= 299:
				if code == filter:
					print("FOUND: " + line)

		

class ParseWordlist:
	def __init__(self, wordlistLoc):

		wordlist = open(wordlistLoc, "r")

		for line in wordlist:
			enumerate = Enumerate(line[:-1], arguments.d, arguments.filter)


# Check if the keyword is in the domain, and start if true

if CheckForKeyWordInDomain().checkForKeyWordInDomain(arguments.d) == True:
	parseWordlist = ParseWordlist(arguments.w)

else:
	print("ERROR: Keyword not found in domain.")
