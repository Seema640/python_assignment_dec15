my_list = [4,2,4,0,2,4,5,7,8,9,23,8,5,4,2,2,34,4,45]
num_max, num_min=my_list[0],my_list[0]

for each in my_list:
    if each > num_max:
        each, num_max=num_max, each

    if each < num_min:
        each, num_min=num_min, each


print('The maximum number is: {}\n The minimum number is: {}'.format(num_max,num_min))
