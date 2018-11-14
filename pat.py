def pypart2(n): 
      
    # number of spaces 
    k = 2*n - 2
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # inner loop to handle number spaces 
        # values changing acc. to requirement 
        for j in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 2
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") 
n=5
pypart2(5)
m=3
l=2*m-2
print(l)
for i in range(0,m):
    for j in range(0,l):
        print(end="_")
    l=l-2
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")
  
"""class Human:
    def sayHello(self, name=None):
        if name is not None:
            print 'Hello ' + name
        else:
            print 'Hello '
     
# Create instance
obj = Human()
 
# Call the method
obj.sayHello()
 
# Call the method with a parameter
obj.sayHello('Guido')"""