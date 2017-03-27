from __init__ import dbHandle
myFSaaDB = dbHandle()
vals = myFSaaDB.read(myFSaaDB.root)
""" // doesn't work see handle.revar...
for k in [i for i in obj if i != None]:
    if (type(obj[k]) == list):
        exec(str(k)[1:] + "=" + str(obj[k]))
    elif (obj[k] == None):
        print("Not assigning None values to " + str(k))
    elif (type(obj[k]) == str):
        exec(str(k) + "=\"\"\"" + str(obj[k]) + "\"\"\"")
    else:
        exec(str(k) + "=" + str(obj[k]))
    print(str(k) + "=" + str(obj[k]))
"""
aString=vals["aString"]
aFloatingPoint=vals["aFloatingPoint"]
anInteger=vals["anInteger"]
aDictionary=vals["aDictionary"]
aList=vals["aList"]
print([aString,aFloatingPoint,anInteger,aDictionary,aList])