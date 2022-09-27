def printme(str):
    "This prints a passed string into this function"
    print(str)
    return

printme("This is first call to the user defined function!")
printme("Again second call to the same function")


def changeme(mylist):
    "This change a passed list into this function"
    print("Values inside the function before change: ",mylist)

    mylist[2]=50
    print("Values inside the function after change: ",mylist)
    return

mylist=[10,20,30]
changeme(mylist)
print("Values outside the funciton: ",mylist)


def changeme1(mylist):
    "This change a passed list into this function"
    mylist=[1,2,3,4]
    print("Values inside the function before change: ",mylist)
    return

mylist1=[10,20,30]
changeme1(mylist)
print("Values outside the funciton: ",mylist1)


def printme1(str):
    "This prints a passed string into this function"
    print(str)
    return

printme1()


def printme2(str):
    "This prints a passed string into this function"
    print(str)
    return

printme2(str="My string")


def printinfo(name,age):
    "This prints a passed info into this function"
    print("Name: ",name)
    print("Age: ",age)
    return

printinfo(age=50, name="miki")


def printinfo1(name,age=25):
    "This prints a passed info into this function"
    print("Name: ",name)
    print("Age: ",age)
    return

printinfo1(age=50, name="miki")
printinfo1(name="miki")


def printinfo2(arg1,*vartuple):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(arg1)
    
    for var in vartuple:
        print(var)
    return

printinfo2(10)
printinfo2(70,60,50)


sum=lambda arg1,arg2:arg1+arg2

print("Value of total : ",sum(10,20))
print("Value of total : ",sum(20,20))


def sum1(arg1,arg2):
    total=arg1+arg2
    print("Inside the function : ",total)
    return total

total=sum1(10,20)
print("Outsided the function : ",total)


total1=0

def sum2(arg1,arg2):
    total1=arg1+arg2
    print("Inside the function local total : ",total1)
    return total1

sum2(10,20)
print("Outside the function global total : ",total1)