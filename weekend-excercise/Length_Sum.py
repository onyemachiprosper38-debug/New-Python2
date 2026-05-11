import random
multiply = 1
count = 0
sum_of_number = 0
number_list = []
for numbers in range(10):

    number = random.randint(1, 50)
    number_list.append(number)
    count += 1
print(number_list)

print("the lengh of list is ", count)


for num in range(0,len(number_list),1):
    sum_of_number += num
print(sum_of_number)


for num in range(1,len(number_list),1):
    sum_of_number += num
print(sum_of_number)



for num in range(1,len(number_list),2):
    multiply *= num
print(multiply)


average = 1
for num in number_list:
    sum_of_number += num
    average =sum_of_number + num
print(average)



