from __init__ import dbHandle
myFSaaDB = dbHandle()
aString = "For the lols"
aFloatingPoint = 1.23
anInteger = 42
aDictionary = {"AString" : "For The Lols","AFloatingPoint" : 4.56,"anInteger" : 24}
aList = [1.234,"For the lols!",420]
myFSaaDB.dump(vars())