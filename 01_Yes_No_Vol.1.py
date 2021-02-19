# Ask the user if they have played before
show_instructions = input ("Have you played this game before? ").lower()


# if they say no, output 'display instructions'
# If they say yes, output 'Program continues'
if show_instructions == "yes":
    print("Program continues")

elif show_instructions == "y":
    print("program continues")

elif show_instructions == "no":
    print("display instructions")

elif show_instructions == "no":
    print("display instructions")

else:
    print("Please answer yes / no")

print("You chose {}".format(show_instructions))
