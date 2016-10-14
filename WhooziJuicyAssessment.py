#Putting empty string to make a space 
print('   ')
print('   ')
#Declaring array that will hold ages and names as given in the progam
ages  = [19,28,23,4,78,90,32,54,32,12,67,90,87,6,36,12,24]
cIn = 0
cOut = 0
#Sorting people on the Queue so that all people meets the minimum requirenment should go in first in the premises
#I sorted my array reverse so that all order people will start at first and enter the premises as ordered

ages.sort(reverse=True)
#Testing if a person on the Queue qualifys to enter using loop and if conditions with sorted array
for p in ages:
   if((p >= 18) and (p != 90)):
     print('You are allowed to enter !!')
     cIn += 1
   else:
        print('You are not allowed to enter you must be 18 or above and not be 90 and stand on the Queue')
        cOut += 1
        
        

#Displaying all people meets the entry rules and order people will enter first
print('   ')
print('   ')
print('Displaying all people meets the entry rules')
for k in ages:
   if((k >=18) and (k !=90)):
      print(k)
      
              
  
#Calculating the Value of  X and Displaying X using index  position on the array
print('   ')
print('Number of people will enter the premises', cIn )
print('Number of people will not enter the premises', cOut)
agesX = [19,28,23,4,78,90,32,54,32,12,67,90,87,6,36,12,24]    
x  = agesX[14] + agesX[16]
print('The Value of  X is', x )
	
      
   
	
	
   
