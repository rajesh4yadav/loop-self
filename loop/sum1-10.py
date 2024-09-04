
result=[]
input=[1,2,3,4,5,6,7,8,9]
total=len(input)
for i in input:
    if i ==input[total-i]:
        break
    if i+ input[total-i]==10:
        result.append((i, input[total-i]))
print(result)

list=[]
for i in range(1,10):
    for j in range(i+1,10):
        if i+j==10:
            # print(i,j)
            # print('other')
            # print(f'{i},{j}')
            list.append((i,j))
            
print(list)