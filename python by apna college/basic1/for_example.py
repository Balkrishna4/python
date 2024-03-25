#print the element of the following list using a loop
#[1,4,9,16,25,36,49,64,81,100]
list = [1,4,9,16,25,36,49,64,81,100]
for el in list:
    print(el)



#search for a number x in this tuple using loop [1,4,9,16,25,36,49,64,81,100]
        

list = [1,4,9,16,25,36,49,64,81,100]
x = int(input("enter the number that u want tio search"))
idx=0
for el in list :
    if(el==x):
        print("found at idx " , idx)
        break
    idx+=1
else :
    print("not found")    


#wap  to find  the sum of the first n number 
    

n = int(input("enter the number:" ))
sum = 0 
for i in range(1,n+1):
    sum+=i 
print(sum)      

#wap to find the factorial of first n number
n = int(input("enter the number:"))
product =1
'''
for i in range(1,n+1):
    product*=i 
print(product)   
'''
while(n>=1):
    product*=n
    n-+1     
print(product)    