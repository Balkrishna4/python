#wap to find the factorial of n 
def fact(n):
    pro=1
    for i in range(1,n+1):
      pro*=i 
    return pro
print(fact(5))  