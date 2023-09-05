ent_num = int(input("Please write a whole number")) # ent_num is a variable which holds a user entered integer.

int_init = ent_num # This variable stores the initial value of pos_int before it is used in the loop so that later it
                   # can be used to display pos_int's initial value in the output.
summed = 0 # This is a variable which will be used to hold the sum of all the integers from pos_int.


while ent_num >0: # The while loop will run while pos_int's stored integer value is greater than 0

    summed += ent_num  # This is the equivalent of summed = summed + pos_int
                       # In other words: new value of summed = old value of summed + new value of pos_int

    ent_num -=1 # This will decrement pos_int so that pos_int will eventually equal 0 and the while loop will stop running its code.

print(int_init) # displays the initial value of pos_int
print(summed)   # displays the sum of integers from pos_int
