f = open("demo.txt","w")
f.write("i want to learn javascript")

f = open("demo.txt","a")
f.write("\n After that nodejs")
f.close()


f = open("sample.txt","a")  #how to create the new file
f.close()


f = open("demo.txt","r+")
f.write("abc")
f.close