# Task 1.1:

def read_two_ints():
    """This function reads two ints"""
    # the return shown below is a placeholder to make sure this runs
    x = input("give me x: ")
    y = input("give me y: ")
    a = int(x)
    b = int(y)
    return a, b

# Task 2.1:

def compute_multadd(a, b):
    """This function completes the calculation (a*b)/(a+b) using the user inputs from read_two_ints"""
    # the pass shown below is a placeholder to make sure this runs
    mult_result = a*b
    add_result = a+b
    print("mult result: ", mult_result)
    print("add result: ", add_result)
    print()
    return mult_result/add_result
    

# Task 3.1:

def print_fancy(a, b, ab_multadd):
    """this function recturns the results of the previous functions"""
    # the pass shown below is a placeholder to make sure this runs
    
    print("**"*8)
    print("RESULTS:")
    print("first number: ", a)
    print("second number: ",b)
    print("multadd result: ", ab_multadd)
    print("=" * 16)
    print()

def main ():
    # ADD a Docstring for this function
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y

    x, y = read_two_ints()

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    xy_multadd = compute_multadd(x, y)

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    print_fancy(x, y, xy_multadd)


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
