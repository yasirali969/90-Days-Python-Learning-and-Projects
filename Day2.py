#             Dictionaries
dict={"Yasir":21,"Fahad":19,"Umer":14};
print(dict)
print("Age of Yasir :",dict["Yasir"])
print("Age of Yasir using get :",dict.get("Yasir"))

# Adding new element in the dictionary
dict["Asad"]=22;
print(dict)

#Updating value
dict["Yasir"]=34
print("Updated dictionary :",dict)

# Removing element from dictionary
dict.pop("Asad")
print(dict)

# check if exist or not
if "Yasir" in dict:
    print("Yasir is Found")
else :
    print("Sorry not found!")
    
# Looping through the dictionary
for key,value in dict.items():
    print(key,":",value)
    
# dictionary length
print(len(dict))

# Nested Dictionary
dict1={
    1:{"Name":"Yasir","Age":34},
    2:{"Name":"Asad","Age":45}
}

print(dict1[1]["Name"])