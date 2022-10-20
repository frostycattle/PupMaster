
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
parser.add_argument("--algorithm", help="OPTIONAL: Use a built-in algorithm to send requests faster.")
parser.add_argument("--keyword", help="OPTIONAL: Specfiy your own 'FUZZ' keyword.")
parser.add_argument("--output", help="OPTIONAL: Link an output file.")

arguments = parser.parse_args()

# Variables store the values provided by the arguments

domain = arguments.d

print(banner)

def returnCode(code):
	return 

def sendRequest(url):

	try:
		r = requests.get("http://" + url)

		return r.status_code

	except Exception as ex:
		pass

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
	def __init__(self, line, domain, filter, outputFileLoc):

			if outputFileLoc == None:
				pass

			else:
				output = open(outputFileLoc, "a")


			url = domain.replace(defaultKeyword, line)

			code = sendRequest(url=url)

			if filter == None:								
				print("TRIED: " + line + ": " + str(code))

			elif filter <= 299:
				if code == filter:
					print("FOUND: " + line)	

					if outputFileLoc == None:
						pass

					else:
						output.write(str(url + "\n"))
					

class ParseWordlist:
	def __init__(self, wordlistLoc, outputLoc):

		wordlist = open(wordlistLoc, "r")

		for line in wordlist:
			enumerate = Enumerate(line[:-1], arguments.d, arguments.filter, outputLoc)



# Check if output file is provided

if arguments.output == None:
	pass

	if CheckForKeyWordInDomain().checkForKeyWordInDomain(arguments.d) == True:
		parseWordlist = ParseWordlist(arguments.w, None)

	else:
		print("ERROR: Keyword not found in domain.")


else:

	if CheckForKeyWordInDomain().checkForKeyWordInDomain(arguments.d) == True:
		parseWordlist = ParseWordlist(arguments.w, arguments.output)

	else:
		print("ERROR: Keyword not found in domain.")


# Check if the keyword is in the domain, and start if true
