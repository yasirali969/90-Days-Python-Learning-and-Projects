import random
a=5
b=6
print("Value of a =",a,"and b =",b)

# lists
list=["Yasir","Fahad","Asad","Umer"]
print(random.choice(list))  # will generate random no from the list
print("Value at index 3 is ="+list[3]) # find partcular element
print("Uner found at index =",list.index("Umer")) # found index of umer

# check if value exist in list or not
if "Inam"  in list:
    print("found")
else:
    print("Not found")
    
# append list
print("Last element in the list is ="+list[-1])
print("Second last name in the list ="+list[-2])

# Add element 

list.append("Python developer") # add element at the end of list
print(list)

# Add element at place of 1 index
list.insert(1,"Clay")
print(list)

# remove element
list.remove("Umer") # remove by name
list.pop() # will remove the last element
list.pop(0) # remove by index
print(list)

list[0]="Yasir";
print("Updated name =",list)

total=list.count("Umer")
print("Number of times umer exist =",total)

# Max Min
list1=[1,2,3,4]
print("Max =",max(list1))
print("Min =",min(list1))

#reverse
list1.reverse();
print(list1)

# Ascending order
list1.sort()
print(list1)

# Desceding Order
list1.sort(reverse=True)
print(list1)




# Functions
def play(name):
    return name+" is a player";

name="Yasir";
game=play(name);
print(game)