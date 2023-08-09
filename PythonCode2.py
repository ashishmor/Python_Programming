#copy content of one file in another file. 
#first method

with open ("first.txt", 'r') as firstfile, open ("second.txt", 'w') as secondfile:
  for line in firstfile:
    secondfile.write(line)
    
# second method

with open ("first.txt", 'r') as firstfile, open ("second.txt", 'w') as secondfile:
  for line in firstfile:
    secondfile.write(line)
    
# how to run multiple python file in a folder one after another 

# method 1 - write a bash script for this


#! /bin/bash

for py_file in $(find ../one -name *.py)

do 

  python $py_file 
  
done 

# program to reverse content of a file and copy in another file 

with open ("file.txt", 'r') as myfile:
  data = myfile.read()
  
 rev_data = data [::-1]
 
F1 = open ("rev_file", 'w')

F1.write(rev_data)

F1.close()

#comment to push

# new comment 
  

  
  
  