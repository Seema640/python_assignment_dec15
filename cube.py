arbitary_list = [1, 2, 4, 4, 3, 5, 6]

def cube(num):
    list1=[]
    for each in num:
        temp=pow(each,3)
        list1.append(temp)
    return list1

final_list=cube(arbitary_list)
print("The appended final list is " )
print(final_list)

