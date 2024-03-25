#write a recursive fxn to print all elements in list 
#hint use list and idx as parameter
 
def print_el(list,idx=0):
    if(idx == len(list)):
        return
    print(list[0])
    print_el(list,idx+1)

print_el([1,2,3,4])    