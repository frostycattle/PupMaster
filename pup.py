import requests
import pyfiglet
import sys

print("-" * 58)
print(pyfiglet.figlet_format("PAGE FINDER"))
print("-" * 62)

url = input("URL: ")

try:
    requests.get(url)

except Exception as ex:
    print(ex)
    sys.exit(1)

wordlistLocation = input("Wordlist: ")

try:
    wordlist = open(wordlistLocation, "r")
    words = []

    for line in wordlist:
        words.append(line[:-1])
        print(words)


    permision = input("Start y/n: ")

    if permision.__eq__(" y") or permision.__eq__("y"):
        print("Starting")

        try:
            for element in words:
                request = requests.get(url + "/" + element)

                code = request.status_code.__str__()

                print(url + "/" + element + " " + request.status_code.__str__())


        except Exception as ex:
            print(ex)

    else:
        print("Exiting...")


except Exception as ex:
    print(ex)
