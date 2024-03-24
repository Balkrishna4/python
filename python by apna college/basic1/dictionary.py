d = {
    "name" : "balkrishna",
    "cgpa" : 10 ,
    "marks" : [12,34,5,667]
}
print(type(d))
#they are unorderes ,mutable(changeable) and don't allow duplicate keys
d["name"]="bal"
print(d)
print(d["cgpa"])


null_dict = {}
print(null_dict)


#nested dictionary
s = {
    "name" : "balkrishna",
    "score" : {
        "chem" : 23,
        "math" : 345,
        "physic" : 23
                }

}
print(s["score"]["math"])
print(list(s.keys()))
print(list(s.values()))
print(s.items())
print(s.get("name"))
dic={"city":"mumbai"}
s.update(dic)
print(s)



