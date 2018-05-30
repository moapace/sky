from __future__ import print_function

print ("Hello world")

DATA = ["one", "two", "three"]

for filename in DATA:
    print ("Loading[",DATA.index(filename), end='')
    print ("] is ", filename)
