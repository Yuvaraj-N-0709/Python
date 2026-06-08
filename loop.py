try:
   file=open("yuvaraj.txt.txt","r")
   for line in file:
       print(line)
except FileNotFoundError:
   print("Error : File NOt Found")
else:
    file.close()