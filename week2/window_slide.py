status = True
num_list = []
output = []
while status:
    fill = input()
    try:
        num = int(fill)
        num_list.append(num)
    except ValueError:
        status = False
k = int(input())
for i in range(0,len(num_list)-k+1):
    temp = num_list[i]
    for j in range(k):
        if num_list[i+j] > temp:
            temp = num_list[i+j]
    output.append(temp)
print(output)
    
