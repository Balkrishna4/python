num=abs(int(input("enter the number ")))
r=10
while(num!=0):
    ld=num%10
    r=(r*ld)*10
    num//=10
print(num)    

