# Practice
with open(r"C:\Users\Microsoft\Documents\PYTHON\60 day code\File Handling\Practice.txt", "r") as f:
    
    data = f.read()
    print(data)

newdata = data.replace("python", "Java")

with open("Practice.txt", "w") as f:
    f.write(newdata)
    print(newdata)


print("Done! File updated successfully.")