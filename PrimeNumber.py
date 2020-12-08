#check input num is prime or not

prime = True  #useful to set a boolean for state of prime number

num = int(input("Enter a number___")) #take user input

if( (num > 1) and (num < 9000) ):
  for a in range(2,num) :
    if(num % a) == 0:
       print(num,"is Not A Prime number")
       prime = False
  if(prime): #if prime is true then this will be executed
       print(num," is a Prime Number")

elif(num == 1):  #elif used to make more possibilitys
  print("1 is Not a Prime Number")

elif(num > 8999): 
  print("Number must lower than 4 digits , because programme may crash to calculate larger nums" )

else:
  print("You Entered Invalid Text")
