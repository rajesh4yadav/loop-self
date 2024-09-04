for x in range(6):
    print(x)
    
print('using the parameter')
for x in range (5,10):
    print(x)

print('passing parameter for increament in sequence')
for x in range (2,15,3):
    print(x)
print('else in for loop')    
for x in range(6):
    print(x)
else:
    print('finished')
    
    
print("break in for loop")
 
for x in range(6):
     if x == 3:
         break
     print(x)
else:
    
     print("here else is not executed")