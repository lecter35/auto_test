import sys
import os
import importlib
import aa
import time

def getCurrentScriptPath():
    curPath = sys.path[0]
    if os.path.isfile(curPath):
        curPath = os.path.dirname(curPath)
    return curPath

# print(getCurrentScriptPath())

selfpath = "D:\wyl"

# if selfpath not in sys.path:
#     sys.path.append(selfpath)
# print(sys.path)
# print(sys.getdefaultencoding())


# aa.func1()
# time.sleep(10)
# importlib.reload(aa)
# aa.func1()

print(os.__file__)
print(__file__)
