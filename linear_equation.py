x=[1, 2.3, 5.6, 7, 78]

def solve_for_y(x_values):
    m= 45
    c=0.5
    for x in x_values:
        print("The value of y={:.2f} for x= {:.2f}".format(m*x+c,x))


solve_for_y(x)
