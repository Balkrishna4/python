with open("practice.txt","r") as f:   #here we have python to java
    data = f.read()              
new_data = data.replace("Java","Python")
print(new_data)

with open("practice.txt","r") as f:
    f.write(new_data)                    #we over write the python to java
       



