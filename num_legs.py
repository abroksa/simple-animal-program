def return_name_of_animal(num_legs):
    if num_legs == 4:
        return("dog or cat")
    elif num_legs == 2:
        return("human")
    elif num_legs == 8:
        return("spider")
    else:
        return("invalid input")

num_legs = int(input("How many legs does your animal have (2, 4, or 8)?\n"))
print("Your animal is a",return_name_of_animal(num_legs))