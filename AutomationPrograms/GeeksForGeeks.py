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

