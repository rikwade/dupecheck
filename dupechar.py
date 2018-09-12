#!/usr/bin/env python

fileName="strings.txt"

def checkString(inString):
    strDict = {}
    firstDupe = None

    print("String: ",inString)
    for pos in range(0, len(inString)):
        chkChar = inString[pos]
        result = 0
        result = inString.find(chkChar, pos+1)
        if(result>0):
            return(pos+1,chkChar)
    return (None, None)

with open(fileName) as strFile:
    myStrings = strFile.readlines()

myStrings = [x.strip() for x in myStrings]

for tstString in myStrings:
    position = None
    (position, dupeChar) = checkString(tstString)
    if (position != None):
        print("Character: ",dupeChar,"Position: ",position)
