salary=[15000, 20000, 17000, 18900, 30000]

def new_salary(salary):
    return salary+.23*salary


print("The new salary of each employee after 23% raise are: ")
for each_salary in salary:
    temp= new_salary(each_salary)
    print("{:.2f}".format(temp))
