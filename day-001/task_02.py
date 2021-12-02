with open("input") as file:
    lines = file.readlines()
    arr_num = [int(line.strip()) for line in lines]

#print(arr_num)

count = 0

for i in range(len(arr_num)):
    if i + 3 < len(arr_num):
        if arr_num[i+1]+arr_num[i+2]+arr_num[i+3] > arr_num[i]+arr_num[i+1]+arr_num[i+2]:
            count += 1

print(count)
