import os
#f=open("C:\\Users\Microsoft\\Documents\\PYTHON\\60 day code\\File Handling\\Yasir.txt","a")


                        # Reading Data
# data=f.read()
#line1=f.readline()  # print first line
#line2=f.readline()  # print second line
# f.read(5)  print only first 5 characters
#print(line1)
#print(line2)


                        # Writing Data
#data=f.write("\n I am learning Pytho Programming For Machine Learning") # for Writing the files
# print(data)


                        # "with" Syntax
                        
with open ("C:\\Users\Microsoft\\Documents\\PYTHON\\60 day code\\File Handling\\Yasir.txt","r")as f:
    data=f.read()
    print(data)
    
                        # Deleting file through os module
os.remove("Yasir.txt")

f.close()