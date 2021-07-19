import random


def Color_game():
    want_to_continue = "Y"
    while want_to_continue == "Y":
        COLOR = ["Orange", "Red", "Blue", "Black", "Yellow", "Pink", "Green",
                 "Purple", "Silver", "Brown", "White", "Olive", "Gray", "Marron"]
        # Picking random string from the Lis
        random_Color = random.choice(COLOR)
        # Picking the index of the string which is randomly picked
        index_random_color = COLOR.index(random_Color)

        suffled = list(random_Color)  # Converting that picked string in List
        random.shuffle(suffled)  # Shuffleing the Picked String
        suffled = ''.join(suffled)  # Joing the String agia
        question = suffled.upper()  # Converting the the String into Upper cas

        while True:
            print("Guess the COLOR : ", question)  # Question

            # User will guess the word and input here
            answer = input("Guess the word : ")
            if (answer == COLOR[index_random_color]):
                # If the word gussed by the user is Write the then this will be executed
                print("Congratulations !! You gussed it right ")
                break
            elif (answer == "Give up"):  # If the User Give up then Answer will be showen to the user
                print("Try Hard Next Time..!!")
                print()
                print("The word was ==> ", random_Color)
                print()
                break
            else:  # If user guessed word is Wrong then this statement is executed
                print("Try it again")

        want_to_continue = input(
            "Want to continue game // Back to Main Menu (Y/Back) :")  # This input is asking weather u wanna continue playing this Game of wanna go back to main Menu
