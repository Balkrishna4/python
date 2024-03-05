'''num=abs(int(input("enter the number")))
digits=0
while(num!=0):
    num=num//10
    digits+=1
print(digits) '''


num=abs(int(input("enter the number ")))
digits=1
while(num>9):
    num//=10
    digits+=1
print(digits)    
