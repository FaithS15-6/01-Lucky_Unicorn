
show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Have you played this game before? ").lower()

    # If they say yes, output 'Program continues'
    # if they say no, output 'display instructions'
    # If the answer is invalid, print an answer.

    if show_instructions == "yes":
        print("Program continues")

    elif show_instructions == "y":
        print("program continues")

    elif show_instructions == "no":
        print("display instructions")

    elif show_instructions == "n":
        print("display instructions")

    else:
        print("Please answer yes / no")

    print("You chose {}".format(show_instructions))
