import time
from __init__ import dbHandle
# initialize our handle and define the checkpoint function.
myFSaaDB = dbHandle()

def myCheckpoint(v,myFSaaDB=myFSaaDB):
    myFSaaDB.dump(v)

def myCheckPointRetrieveFunction(myFSaaDB=myFSaaDB):
    values = myFSaaDB.read(myFSaaDB.root)
    if("primes" in values.keys()):
        global primes
        primes = values["primes"]
    if ("check" in values.keys()):
        global check
        check = values["check"]

myFSaaDB.setCheckpointFunction(myCheckpoint)
myFSaaDB.setCheckpointRetrieveFunction(myCheckPointRetrieveFunction)
# initialize our program variables.
primes = [2]
check = 3
#Override variables with values from the Disk
myFSaaDB.retrieveCheckpoint()
#Computation
print(primes)
print(check)
while(len(primes)<1000000):
    if not(0 in [check % k for k in primes]):
        primes.append(check)
    check+=2
    #Once and a while use the checkpoint.
    if(check%1993 == 0):
        myFSaaDB.checkpoint(vars())
        if("n" in input("continue?")):
            break

print("Complete!")