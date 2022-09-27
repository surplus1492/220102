import sys

list=[1,2,3,4]
it=iter(list)
print(next(it))

for x in it:
    print(x,end=" ")

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

def fibonacci(n):
    a,b,counter=0,1,0

    while True:
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1
f=fibonacci(5)

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()