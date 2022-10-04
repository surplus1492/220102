import time

#localtime =time.asctime(time.localtime(time.time()))
#print("Local current time :",localtime)

localtime =time.strftime('%Y / %b / %d / %H:%M:%S',time.localtime(time.time()))
print("Local current time :",localtime)