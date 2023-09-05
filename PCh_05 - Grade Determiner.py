"""veg = input("Type veg here")

if veg == "corn":
    print("The vegetable is corn")

else:
    print("The vegetable is not corn") """

score = int(input("What was your score?"))

if score >= 90:
    print("This student's score of " + str(score) + " is an A.")
else:
    if score >= 80:
        print("This student's score of " + str(score) + " is an B.")
    else:
        if score >=70:
           print("This student's score of " + str(score) + " is an C.")
        else:
            if score >=60:
               print("This student's score of " + str(score) + " is an D.")
            else:
                if score <60:
                   print("This student's score of " + str(score) + " is an F.")