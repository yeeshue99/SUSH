phrase = "*This page of your* ***S.U.S.H.*** *seems to be hidden behind some sort of magic. Perhaps the page will become deciphered later in your studies?*"

from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]

for file in onlyfiles:
    if file.endswith(".md"):
        with open(file, "w") as f:
            f.write(phrase)
            f.close()
            print("File " + file + " created.")
    else:
        print("File " + file + " is not a valid file.")
