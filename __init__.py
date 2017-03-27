import os
import pickle

# Maximum number of files per directory: 2**16
# Maximum Filesize 1Gb

class dbHandle:
    def __init__(self, targetDir=".FSaaDB"):
        try:
            os.mkdir(targetDir)
        except:
            print(targetDir+" exists, proceeding in place.")
        self.root = os.path.abspath(targetDir)
        self.baseVars = vars().keys()

    def dump(self,Variables):
        os.chdir(self.root)
        #print([k for k in Variables.keys() if not(k in list(self.baseVars)+["self"]) and not(k[0:2]=="__" and k[-2:]=="__")])
        for i in [k for k in Variables.keys() if not(k in list(self.baseVars)+["self"]) and not(k[0:2]=="__" and k[-2:]=="__")]:
            print(i)
            self.write(Variables[i], str(i) + "#" + str(type(Variables[i])).split("'")[1])

    def findAll(self):
        return(self.read(self.root))

    def read(self,targetPath):
        print("reading")
        print(targetPath)
        startPath = os.path.abspath(os.getcwd())
        if (os.path.isdir(targetPath)):
            #if(os.path.basename(targetPath)[0] == "."):
            #    print("please don't name your variables starting with a .")
            #    ret = None
            # else:
            os.chdir(targetPath)
            ret = {}
            for k in [os.path.abspath(i) for i in os.listdir(targetPath) if not(os.path.basename(i).startswith("."))]:
                print(k)
                importantPathParts = os.path.basename(k).split("#")
                ret[importantPathParts[0]] = self.read(k)
        else:
            importantPathParts = os.path.basename(targetPath).split("#")
            if (len(importantPathParts) != 2):
                raise Exception('FSaaDB_ERROR', targetPath + ' is not of key.type format')
            else:
                dataType = importantPathParts[1]
            fileHandle = open(targetPath, "r")
            if (dataType == 'int'):
                ret = int(fileHandle.read())
            elif (dataType == 'float'):
                ret = float(fileHandle.read())
            elif (dataType == 'str'):
                ret = str(fileHandle.read())
            elif (dataType == 'list'):  # A list is represented by a list of absPaths to objects
                ret = [self.read(line) for line in fileHandle.read().split("\n")[:-1]]
            else:
                try:
                    ret = pickle.load(targetPath)
                except:
                    ret = None
                # Objects in a list will be stored in a hidden folder.
        os.chdir(startPath)
        return (ret)

    def write(self,obj, targetPath):
        startPath = os.path.abspath(os.getcwd())
        if (type(obj) == dict):
            try:
                os.mkdir(targetPath)
            except:
                print(targetPath + " already exists, write operation continues in place.")
            os.chdir(targetPath)
            for k in obj:
                self.write(obj[k], os.path.abspath(k + "#" + str(type(obj[k])).split("'")[1]))
        else:
            importantPathParts = os.path.basename(targetPath).split("#")
            if (len(importantPathParts) != 2):
                raise Exception('FSaaDB_ERROR', targetPath + ' is not of key.type format')
            else:
                dataType = importantPathParts[1]
            if (dataType == 'int' or dataType == 'float' or dataType == 'str'):
                fileHandle = open(targetPath, "w")
                fileHandle.write(str(obj))
                fileHandle.close()
            elif (dataType == 'list'):  # A list is represented by a list of absPaths to objects
                try:
                    os.mkdir(
                        os.path.join(os.path.abspath(os.path.join(targetPath, os.pardir)), "." + os.path.basename(targetPath)))
                except:
                    print(os.path.join(os.path.abspath(os.path.join(targetPath, os.pardir)),
                                       "." + os.path.basename(targetPath)) + " already exists, write operation continues in place.")
                strRep = ""
                for n, k in enumerate(obj):
                    newTargetPath = os.path.join(os.path.join(os.path.abspath(os.path.join(targetPath, os.pardir)),
                                                              "." + os.path.basename(targetPath)),str(n) + "#" + str(type(k)).split("'")[1])
                    self.write(k, newTargetPath)
                    strRep += newTargetPath +"\n"
                fileHandle = open(targetPath, "w")
                fileHandle.write(strRep)
                fileHandle.close()
            else:
                try:
                    pickle.dump(obj, open(targetPath, "wb"))
                except Exception as e:
                    print(e)
        os.chdir(startPath)

    def reVar(self,obj):
        for k in[i for i in obj if i != None]:
            if(type(obj[k])==list):
                exec("global " + str(k)[1:] + "\n" + str(k)[1:] + "=" + str(obj[k]))
            elif(obj[k]==None):
                print("Not assigning None values to "+str(k))
            elif(type(obj[k])==str):
                exec("global " + str(k) + "\n" + str(k) + "=\"\"\"" + str(obj[k])+"\"\"\"")
            else:
                exec("global " + str(k) + "\n" + str(k) + "=" + str(obj[k]))
            print("global " + str(k) + "\n" + str(k) + "=" + str(obj[k]))

    def setCheckpointFunction(self,f):
        self.checkpointFunction = f

    def checkpoint(self,v):
        self.checkpointFunction(v)

    def setCheckpointRetrieveFunction(self,f):
        self.checkpointRetrieveFunction = f

    def retrieveCheckpoint(self,checkpointPath = None):
        self.checkpointRetrieveFunction()

    def lilBobbyTables(self):
        if(os.path.basename(self.root)[0]=="."):
            for root, dirs, files in os.walk(self.root, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
        try:
            os.mkdir(self.root)
        except:
            print(self.root+" exists, proceeding in place.")
