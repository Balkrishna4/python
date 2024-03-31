'''
f = open("demo.txt","r")  #file is present in same folder ,ortherwise we tocopy the complete path  C:\Users\balkr\OneDrive\Desktop\python\python by apna college\file input and output in python\demo.txt 
data = f.read()
print(data)
print(type(data))
f.close()

'''
'''
# i want to read first 5 letter only

data5 = f.read(1)
print(data5)
'''
'''
#readline()  reads one line at a time
f = open("demo.txt","r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
'''
'''
f = open("demo.txt","r")

data = f.read()    #it will print whole file
print(data)
    
line1 = f.readline()  #line1 and 2 will remain empty b/c it is already read by data
print(line1)
line2 = f.readline()
print(line2)
'''


