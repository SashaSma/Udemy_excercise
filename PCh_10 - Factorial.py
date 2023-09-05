given_number=int(input("Give me a number to get factorial:"))
def factorial (fact_num):                   # Function definition
    result=1                                # Giving a default value to the result to initialize the variable
    for counter in range(fact_num, 1, -1):  # Execute this loop X times from given number to 1,decrease 1 each iteration
        result *=counter                    # result = result * counter

    return result                           # Save the value of result variable on memory

print("Factorial of", given_number, "is:", factorial(given_number))

# Create a function which takes one positive integer as its input and returns its factorial.
# (Multiplication of all previous positive numbers including the last), ex: 3 factorial (3*2*1) = 6.
#
# To make sure that your function works correctly, you should call it with the inputs 3, 4, and 5 and print
# what is returned by those calls.  For those inputs, you should get 6, 24, and 120, respectively.
#
# To make more interactive this exercise the system will ask the user to type the desired number to get factorial.
#
#
# Requesting a number to get factorial of.