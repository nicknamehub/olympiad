loop_start = False
sum_of_sqr = 0
sum_of_nums = 0
while ((sum_of_nums != 0) or (loop_start == False)):
    loop_start = True
    num = int(input())
    sum_of_nums += num
    sum_of_sqr += num ** 2
print(sum_of_sqr)
