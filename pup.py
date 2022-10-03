
# Remove output file arguments, and associations.

from threading import Thread
from os.path import exists

import argparse
import sys
import requests
import os

banner = "---------------------------------------"

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

wordlistLocation = arguments.w
domain = arguments.d
responseCodeToFilter = arguments.filter
#wordlistsList = arguments.ws

# The cloudwordlist argument is currently broken. Do not use it.

cloudwordlistLocation = arguments.cloudwordlist
keyword = arguments.keyword
codeList = arguments.filters
output = arguments.output


def convertFiltersToList(string):

	if codeList == None:
		return

	else:

		filters = list(string.split(" "))
		return filters


responseList = convertFiltersToList(codeList)

# Print a space

print("")

try:

	print(banner)

	# Check to see if an custom "FUZZ" keyword was provided.

	if keyword == None:
		keyword = defaultKeyword

	else:
		pass

	# Check if "FUZZ" is defined in the given url

	if keyword in domain:
		pass

	else:
		print("ERROR: Could not find " + keyword + " in " + domain + "!")
		sys.exit(0)

	if output == None:
		pass

	else:
		try:
			if exists(output):
				print("Output file: " + output)
				pass


			else:
				createFile = input("Could not find the output file. Create one? ")

				if createFile.__eq__("yes") or createFile.__eq__(" yes") or createFile.__eq__("y") or createFile.__eq__(" y"):
					try:
						outputFile = open(output, "x")
						outputFile.close()

					except Exception as ex:
						print("ERROR: Error while creating file! " + ex)
						sys.exit(0)

		except Exception as ex:
			print(ex)
			sys.exit(0)

	# Check if the wordlist is in the cloud or installed on the machine.

	if wordlistLocation == None and cloudwordlistLocation == None:
		print("ERROR: Wordlist location not specifed!")
		sys.exit(0)

	else:
		if wordlistLocation == None:
			
			try:
				cloudwordlistRequest = requests.get(cloudwordlistLocation)
				cloudwordlist = cloudwordlistRequest.text
				print(cloudwordlist)

			except Exception as ex:
				print(ex)

			print("Cloudwordlist: " + cloudwordlistLocation)

		else:
			print("Wordlist: " + wordlistLocation)
	
	print("Domain: " + domain)

		# Try to open the output file
	if responseCodeToFilter == None:
		pass

	else:
		print("Filtering by code: "+str(responseCodeToFilter))


except Exception as ex:
	print("ERROR: "+str(ex))
	print(exitBanner)
	sys.exit(0)


# Begin enumurateing

print(banner)

wordlist =  open(wordlistLocation, "r")
for line in wordlist:

		url = domain.replace(keyword, line[:-1])

		try:

			request = requests.get("http://"+url)
		
		except Exception as ex:
			print("ERROR: " + str(ex))

		if responseCodeToFilter == None:
			print(url + " : " + str(request.status_code))

		else:
			pass

		if request.status_code == responseCodeToFilter < 299:
			print("FOUND: " +line[:-1])


		elif request.status_code == responseCodeToFilter:
			print("/"+line[:-1] + " : " + str(request.status_code))

			
		else:
			pass


print(banner)
