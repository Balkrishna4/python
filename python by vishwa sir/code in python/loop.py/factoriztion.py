'''print("enter the number ")
year =int(input())
i=1;
answer=1
while(i<=n):
    answer=answer*i
    i+=1
print(answer)   ''' 

num=int(input("Enter the number "))
if(num<0):
    print("Not defined")
else:
    fact=1
    while(num>0):
     fact=fact*num
     num-=1
  print(fact)     