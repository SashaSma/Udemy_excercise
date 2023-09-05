#1
the_string="North Dakota"
#2
print(the_string.rjust(17))
#3
print(the_string.ljust(17,"*"))
#4
center_plus= the_string.center(16,"+")
#5
print(center_plus)
#6
print(the_string.lstrip("North"))
#7
print(center_plus.rstrip("+"))
#8
print(center_plus.strip("+"))
#9
print(the_string.replace("North","South"))