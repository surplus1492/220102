def fib(n):
    result=[]
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result

if __name__=="__main__":
    f=fib(100)
    print(f)

#########################################

Money =2000
def AddMoney():
    Money=Money+1

print(Money)
AddMoney()
print(Money)

########################################

import math

content=dir(math)
print(content)

##########################################

