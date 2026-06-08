try:
   file=open("yuvaraj.txt.txt","a")
   file.write("this is from yuvaraj  karur")
   file.close()
   
   file=open("yuvaraj.txt.txt","r")
   for line in file:
      print(line)
      
except FileNotFoundError:
   print("Error : File NOt Found")
else:
    file.close()