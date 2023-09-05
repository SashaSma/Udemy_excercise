"""The formula for converting from degrees Celsius to degrees Fahrenheit is as follows:
F = 1.8 * C + 32
Where F is the Fahrenheit temperature and C is the Celsius temperature.
In a .py file,
1.create a variable and assign it an integer representing a celsius temperature that is entered as user input().
2.input()'s message should prompt the user to enter an integer value.
3.then write a function called fahrenheit that takes in an integer representing a Celsius
  temperature as its argument.
4. The function will return the Fahrenheit equivalent temperature of that argument to 1 place after the decimal.
5. At the end of your program, display the Fahrenheit equivalent in a print statement
   message formatted like so: "The Fahrenheit equivalent of [user entered integer] " \
                               "degrees Celsius is [number returned by function]".
To make sure that the function works, run your program multiple times and call
the function on different user entered integer values both negative and positive.
"""
C = int(input("Enter an integer that represents the Celsius degrees."))

def Fahrenheit(C):
    return (18*C+320)/10


print("The Fahrenheit equivalent of "+ str(C) + " degrees Celsius is "+str(Fahrenheit(C))+".")
# ty str jsou tam proto, aby ty hodnoty/promenne premenil na string, text. To potrebujes, protoze skladas text a ty hod-
#noty/promenne budou v odpovedi, printovane vete, jako text, ne jako cislo/promenna.
#print("The Fahrenheit equivalent of "+ C + " degrees Celsius is "+ Fahrenheit(C) +".")
#print("The Fahrenheit equivalent of "*6) #vytiskne vetu sest krat
# print(f"The Fahrenheit equivalent of {C} degrees Celsius is  {Fahrenheit(C)}.")....tohle taky funguje

