#V=l*w*h, kde l-delka, w-sirka, h-vyska

l=int(input("Enter an integer that represents length in feet"))
w=int(input("Enter an integer that represents width in feet"))
h=int(input("Enter an integer that represents height in feet"))


def prism_volume(l,w,h):
     return l*w*h


print("The volume of rectangular prism is "+str(prism_volume(l, w, h))+" cubic feet.")