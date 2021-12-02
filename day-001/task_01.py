with open("input") as file:
    lines = file.readlines()
    arr_num = [int(line.strip()) for line in lines]

#print(arr_num)

count = 0

for i in range(len(arr_num)):
    if i+1 < len(arr_num):
        if arr_num[i+1] > arr_num[i]:
            count += 1

print(count)
