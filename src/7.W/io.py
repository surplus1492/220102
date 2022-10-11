print("Python is really a great language,","isn't it")

x=input("something :")

fo=open("foo.txt","wb")
print("Name of the file: ",fo.name)
print("Closed or not : ",fo.closed)
print("Opening mode : ",fo.mode)
fo.close()

fo=open("foo.txt","wb")
print("Name of the file : ",fo.name)
fo.close()

fo=open("foo.txt","w")
fo.write("Python is a great language. \nYeah its great!!\n")
fo.close()

fo=open("foo.txt","r+")
str=fo.read(10)
print("Read String is : ",str)
fo.close()

fo=open("foo.txt","r+")
str=fo.read(10)
print("Read String is : ",str)
position=fo.tell()
print("Current file position : ",position)
position=fo.seek(0,0)
str=fo.read(10)
print("Again read String is : ",str)
fo.close()


import os
os.rename("test1.txt", "test2.txt")

import os
os.remove("text2.txt")

import os
os.mkdir("test")

import os
os.chdir("/home/newdir")

import os
os.getcwd()

import os
os.rmdir("/tmp/test")