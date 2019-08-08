myfunction = input('''Enter your function here.
    eg: if eqn is
    f(x) = y = x^3 - 2(x^2) - 4x + 23
    then type
            x ** 3 - 2 * (x ** 2) - 4 * x + 23
    : ''')

a = 0
b = 0
f_a = -1
f_b = -1

# Compare the signs of f(a) with f(b)
while ((f_a < 0) and (f_b < 0)) or ((f_a > 0) and (f_b > 0)):
    print("f(a) and f(b) have same signs. Enter the correct range again.")

    # Ask the lower and upper range to search in that fixed range
    a = int(input("Enter lower limit 'a': "))
    b = int(input("Enter upper limit 'b': "))

    # For calculating f(a)
    x = a
    f_a = int(eval(myfunction))
    print("f({}) = {}".format(a, f_a))

    # For calculating f(b)
    x = b
    f_b = int(eval(myfunction))
    print("f({}) = {}".format(b, f_b))

# If the signs are different execute below block
else:
    print('''
        f(a) = f({0}) = {1:3} and
        f(b) = f({2}) = {3:3} have opposite signs.

        So the root of the function must be within the interval [{0}, {2}]
          '''.format(a, f_a, b, f_b))

iteration = int(input(" Enter the number of iteration you want(> 0): "))
# Title
print("iteration     an              bn          cn=(an + bn)/2          fn       ")
for i in range(1, iteration + 1):
    # Bisect
    c = (a + b) / 2
    x = c
    f_c = float(eval(myfunction))   # float because int rounds and that is dumb

    print("     {:<2}    {:<7.7f}     {:<7.7f}       {:<7.7f}        {:<7.7f}".format(i, a, b, c, f_c))

# Check if the midpoint c falls on the right of a or right of b
    if f_c < 0:
        a = c
    else:
        b = c

print("the root of function is {:4.3f}. ".format(c))
input("Finished. Press Enter to Exit.")
