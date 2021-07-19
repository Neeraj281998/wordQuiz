import random


def Shapes_game():
    want_to_continue = "Y"
    while want_to_continue == "Y":
        SHAPES = ["Circle", "Arrow", "Diamond", "Minus", "Ring", "Star", "Square",
                  "Hexagon", "Triangle", "Parallelogram", "Octagon", "Cube"]
        # Picking random string from the List
        random_shapes = random.choice(SHAPES)
        # Picking the index of the string which is randomly picked
        index_random_shapes = SHAPES.index(random_shapes)

        suffled = list(random_shapes)  # Converting that picked string in List
        random.shuffle(suffled)  # Shuffleing the Picked String
        suffled = ''.join(suffled)  # Joing the String agian
        question = suffled.upper()  # Converting the the String into Upper case

        while True:
            print("Guess the SHAPES : ", question)  # Question

            # User will guess the word and input here
            answer = input("Guess the word : ")
            if (answer == SHAPES[index_random_shapes]):
                # If the word gussed by the user is Write the then this will be executed
                print("Congratulations !! You gussed it right ")
                break
            elif (answer == "Give up"):  # If the User Give up then Answer will be showen to the user
                print("Try Hard Next Time..!!")
                print()
                print("The word was ==> ", random_shapes)
                print()
                break
            else:  # If user guessed word is Wrong then this statement is executed
                print("Try it again")

        want_to_continue = input(
            "Want to continue game // Back to Main Menu (Y/Back) :")  # This input is asking weather u wanna continue playing this Game of wanna go back to main Menu
