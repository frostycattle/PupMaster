import argparse

print("---------------------------------------------------------")
print(" _____                __  __              _              ")
print("|  __ \              |  \/  |            | |             ")
print("| |__) |_   _  _ __  | \  / |  __ _  ___ | |_  ___  _ __ ")
print("|  ___/| | | || '_ \ | |\/| | / _` |/ __|| __|/ _ \| '__|")
print("| |    | |_| || |_) || |  | || (_| |\__ \| |_|  __/| |   ")
print("|_|     \__,_|| .__/ |_|  |_| \__,_||___/ \__|\___||_|   ")
print("              | |                                        ")
print("              |_|                                        ")

# Create the instance of the argparser, and add the arguments

parser = argparse.ArgumentParser(description="none")
parser.add_argument("-w", help="Input the wordlist location here")
parser.add_argument("-d", help="Input the domain here")

arguments = parser.parse_args()

# Wordlist and other data provided by the arguments


wordlist = arguments.w
domain = arguments.d

print("")
print("Wordlist: " + wordlist)
print("Domain: " + domain)

print("---------------------------------------------------------")
