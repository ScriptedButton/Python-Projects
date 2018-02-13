# Cole Brooks - 2018
# MIT License - https://opensource.org/licenses/MIT

import sys
import time

class PyCrypt:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def removeDuplicate(self, value):
        used = []
        newvalue = ""
        for i in value:
            if not i in used:
                newvalue += i
            used.append(i)
        return newvalue

    def decrypt(self, word, key):
        newword = ""
        newstr = ""
        for i in self.alphabet.lower():
            if i not in key:
                newstr += i
        newalpha = key + newstr[::-1]
        for i in word:
            if i == " ":
                newword += " "
            elif i == ".":
                newword += "."
            if i.isalpha():
                if i.islower():
                    index = newalpha.lower().index(i.lower())
                    newword += self.alphabet[index].lower()
                elif i.isupper():
                    index = newalpha.lower().index(i.lower())
                    newword += self.alphabet[index].upper()

        return newword

    def encrypt(self, word, key):
        newword = ""
        newstr = ""
        for i in self.alphabet.lower():
            if i not in key:
                newstr += i
        newalpha = key + newstr[::-1]
        for i in word:
            if i == " ":
                newword += " "
            elif i == ".":
                newword += "."
            if i.isalpha():
                if i.islower():
                    index = self.alphabet.lower().index(i.lower())
                    newword += newalpha[index].lower()
                elif i.isupper():
                    index = self.alphabet.lower().index(i.lower())
                    newword += newalpha[index].upper()

        return newword


# Main Code

pc = PyCrypt()
try:
    type = sys.argv[1]
    keyword = pc.removeDuplicate(sys.argv[2])
    inp = sys.argv[3]
    output = sys.argv[4]
except IndexError as err:
    print("Missing argument: ", err)
    exit(0)

inp_text = open(inp, 'r').read()
save_text = open(output, 'w')

start = time.time()
if type == "-d":
    save_text.write((pc.decrypt(inp_text, keyword)))
    print("Text from", inp, " was successfully decrypted to", output)
elif type == "-e":
    save_text.write((pc.encrypt(inp_text, keyword)))
    print("Text from", inp, "was successfully encrypted to", output)
end = time.time()
elapsed = end - start
print("Actions completed within:", elapsed, "seconds")
