# set= {} unordered,immutable,but Remove/Add Ok,No duplicates
# Tuple=() ordered and unchangeable.Duplicates OK. Faster

fruit={"apple","coconut","pineapple"}
fruit.add("Banana")
print(fruit)
fruit.remove("apple")
print(fruit)
print(len(fruit))

if "coconut" in fruit:
    print("Found")
else:
    print("Not Found")
    

# Union of sets
s1={1,2,3,4}
s2={3,4,5,6}
print(s1|s2)

# intersection
print(s1&s2)

# Differnce
print(s1-s2)

# Symmetric
print(s1 ^ s2)


                    # Tupling
                    
Tuple=("Apple","Banana","Coconut","Pineapple")

# Accessing element in Tuples
print(Tuple[0])
# slicing
print(Tuple[::2])
print(Tuple[0:3])

# Tuple is Immutable cannt change values one added
#Tuple[0]="Avocada"
#print(Tuple)
 
# len
print(len(Tuple))

# Indexing
print(Tuple.index("Apple"))

# Count
print(Tuple.count("Apple"))

# loop
for T  in Tuple:
     print(T)
     

# Conversion of list into tuple
list1={1,2,3,4}
new_tuple=tuple(list1)
print(new_tuple)


# Conversion of tuple into list
Tuple1=(2,3,4,2)
my_list=list(Tuple1)
print(my_list)
 