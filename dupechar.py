#!/usr/bin/env python3

fileName="strings.txt"

def checkString(inString):
    for pos in range(0, len(inString)):
        chkChar = inString[pos]
        result = 0
        # str.find returns the lowest index in the string where the substring
        # is found. We start searching from the current position+1
        # it returns the position in the string (index counting from 0)
        result = inString.find(chkChar, pos+1)
        if(result>0):
            return(pos,chkChar)
    return (None, None)

with open(fileName) as strFile:
    myStrings = strFile.readlines()

myStrings = [x.strip() for x in myStrings]

for tstString in myStrings:
    position = None
    (position, dupeChar) = checkString(tstString)

    print("String:",tstString)
    if (position != None):
        print("Character:",dupeChar,"Position:",position+1)
    else:
        print("No duplicate characters")
