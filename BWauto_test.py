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

def true(): return True
lambda: True

def add(x, y):
    return x + y

# print(add(3,5))

# def add(x,y):return x+y
# print(lambda x,y : x+y)

lambda x : x<=(month, day)
def func1(x):
    return x<=(month, day)

lambda item : item[1]
def func2(item):
    return item[1]
adict = {'a':'aa', 'b':'bb'}

for i in adict.items():
    print(func2(i))
