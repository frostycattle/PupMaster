# Remove output file arguments, and associations.

from threading import Thread

import argparse
import sys
import requests
import os

# Keyword

keyword = "FUZZ"

headers = {"User-Agent":"PupMaster/0.1"}

# Name banner & exit banner

print("---------------------------------------------------------")
print(" _____                __  __              _              ")
print("|  __ \              |  \/  |            | |             ")
print("| |__) |_   _  _ __  | \  / |  __ _  ___ | |_  ___  _ __ ")
print("|  ___/| | | || '_ \ | |\/| | / _` |/ __|| __|/ _ \| '__|")
print("| |    | |_| || |_) || |  | || (_| |\__ \| |_|  __/| |   ")
print("|_|     \__,_|| .__/ |_|  |_| \__,_||___/ \__|\___||_|   ")
print("              | |                                        ")
print("              |_|                                        ")

exitBanner = "---------------------------------------------------------"

# Create the instance of the argparser, and add the arguments

parser = argparse.ArgumentParser(description="Use this tool to discover content on your target. Have fun!")
parser.add_argument("-w", help="REQUIRED: Input the wordlist location here.")
parser.add_argument("-d", help="REQUIRED: Input the domain (URL) here.")
parser.add_argument("-filter", help="OPTIONAL: Filter the response(s) by response code.", type=int)
parser.add_argument("-output", help="OPTIONAL: Specfiy which file would you like to output the results too.")
parser.add_argument("-algorithm", help="OPTIONAL: Use a built-in algorithm to send requests faster.")
parser.add_argument("-ws", help="OPTIONAL: Specfiy mulitple wordlists. Format: ['wordlist1', 'wordlist2']")
parser.add_argument("--cloudwordlist", help="OPTIONAL: Specfiy a link to a Wordlist in the cloud")

arguments = parser.parse_args()

# Variables store the values provided by the arguments

wordlistLocation = arguments.w
domain = arguments.d
responseCodeToFilter = arguments.filter
outputFileLocation = arguments.output
wordlistsList = arguments.ws
cloudwordlistLocation = arguments.cloudwordlist
print(cloudwordlistLocation)

# Print a space

print("")

try:

	# Check if the wordlist is in the cloud or on the machine.

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

	if outputFileLocation == None:
		pass
	
	else:


		# Try to open the output file

		try:
			outputFile = open(outputFileLocation, "w")

		except Exception as ex:
#			print("ERROR OPENING OUTPUT FILE")
			pass

		print("Output file: "+str(outputFileLocation))
	
	if responseCodeToFilter == None:
		pass

	else:
		print("Filtering by code: "+str(responseCodeToFilter))


except Exception as ex:
	print("ERROR: "+str(ex))
	print(exitBanner)
	sys.exit(0)


# Begin enumurateing

sys.exit(0)

wordlist =  open(wordlistLocation, "r")
for line in wordlist:
		request = requests.get("http://"+domain+"/"+line[:-1])
		
		if responseCodeToFilter == None:
			print("/"+line[:-1] + " : " + str(request.status_code))

			if outputFileLocation == None:
				pass

			else:

				try:
					outputFile = open(outputFileLocation, "a")
					outputFile.write(request.status_code)

				except Exception as ex:
#					print("ERROR WRITING TO FILE")
					pass
			

		else:
			pass

		if request.status_code == responseCodeToFilter < 299:
			print("FOUND: " +line[:-1])

			if outputFileLocation == None:
				pass

			else:

				try:
					outputFile = open(outputFileLocation, "a")
					outputFile.write(request.status_code)

				except Exception as ex:
#					print("ERROR WRITING TO FILE")
					pass

		elif request.status_code == responseCodeToFilter:
			print("/"+line[:-1] + " : " + str(request.status_code))

			if outputFileLocation == None:
				pass

			else:

				try:
					outputFile = open(outputFileLocation, "a")
					outputFile.write(request.status_code)

				except Exception as ex:
#					print("ERROR WRITING TO FILE")
					pass
		
		else:
			pass


print(exitBanner)
