#set is the collection of the unordered items
#each element in the set must be unique and immutable
#set mai sirf boolean, int ,float,str,tuple only value are are stored 
c ={1,2,3,4,5}
print(c)
print(type(c))
c1 ={1,2,3,4,5,4,5,"f","f"}
print(c1)
print(type(c1))
print(len(c1))  #total number of items


c = {} #empty dic
a = set()  #empty set
print(a)
print(type(a))
# sets are mutable
#sets 's element are immutable

c = set()
c.add(1)
c.add(1)
c.add(2)
print(c)
c.remove(1)
#c.remove(6) it will error b/c not available in set
c.add((1,2,3,4,5))
print(c)
c.pop()
print(c)
c.clear()
print(c)



# set.union(set2) # combines both set values and return new
#set.intersection(set2) # combines common values and return new

set1={1,2,3,4,5}
set2={5,4,36,7,8}
print(set1.union(set2))
print(set1.intersection(set2))







