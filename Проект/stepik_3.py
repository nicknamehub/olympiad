f = open('dataset_136818_10.txt')
sum_height = [0] * 11
count_height = [0] * 11
result = [0] * 11
for line in f:
    class_index = line.find(chr(9))
    class_num = int(line[:class_index])
    height_index = line.rindex(chr(9))
    height = int(line[height_index:])
    sum_height[class_num - 1] += height
    count_height[class_num - 1] += 1
for i in range(11):
    if count_height[i] != 0:
        result[i] = (float(sum_height[i]))/(float(count_height[i]))
for i in range(11):
    if result[i] != 0:
        print(i+1, result[i])
    else:
        print(i+1, '-')
