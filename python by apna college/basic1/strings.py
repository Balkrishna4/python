print("hello"+"world")
str1='balkrishna'
str2 = "balkrishna"
str3 = ''' this is balkrishna '''
str4 = "this balkrishna \n balkrishna" #\n used for next line
print(str4)
print(str1 + str2) # concatenation
print(len(str1))    #length of string

str = "apna college"
ch = str[9]
print(ch)
#str[4]=b #string object does not support item assignment
print(str[:4])  #[0:4]
print(str[5:])  #[5:len(str)]
print(str[-2:-5:-1])
s = "I am a coder"
print(s.endswith("er.") )#return true if string ends with substr
print(s.capitalize())  #capitalize the first charater
print(s.replace("am","these")) # replace(old,new)
print(s.find("a"))  #return 1st index of 1st occurrer
print(s.count("i"))#count the occurrence of substring


