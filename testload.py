from __init__ import dbHandle
myFSaaDB = dbHandle()
print(myFSaaDB.read(myFSaaDB.root))
#print([aString,aFloatingPoint,anInteger,aDictionary,aList])