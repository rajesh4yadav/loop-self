people =['rajesh',
         'ram',
         'shyam',
         'hari']

for person in people:
    print(f"hello  {person}")

for index,person in enumerate(people):
    print(f'hello {index} {person}')
print('starting from 1')
for index,person in enumerate(people):
    print(f'hello {index+1} {person}')
    
    
i= 0
while i<len(people):
    print(people[i])
    i+=1 
