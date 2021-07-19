import random


def Body_Parts_game():
    want_to_continue = "Y"
    while want_to_continue == "Y":
        Body_parts = ["Hair", "Eyes", "Hand", "Legs", "Nose", "Eyes", "Mouth", "Arm", "Tooth",
                      "Waist", "Shoulder", "Stomach", "throat", "Knee", "Ear", "Foot", "Head", "Face", "Neck"]
        # Picking random string from the List
        random_parts = random.choice(Body_parts)
        # Picking the index of the string which is randomly picked
        index_random_parts = Body_parts.index(random_parts)

        suffled = list(random_parts)  # Converting that picked string in List
        random.shuffle(suffled)  # Shuffleing the Picked String
        suffled = ''.join(suffled)  # Joining the String agian
        question = suffled.upper()  # Converting the the String into Upper case

        while True:
            print("Guess the Body Part : ", question)  # Question

            # User will guess the word and input here
            answer = input("Guess the word : ")
            if (answer == Body_parts[index_random_parts]):
                # If the word gussed by the user is Write the then this will be executed
                print("Congratulations !! You gussed it right ")
                break
            elif (answer == "Give up"):  # If the User Give up then Answer will be showen to the user
                print("Try Hard Next Time..!!")
                print()
                print("The word was ==> ", random_parts)
                print()
                break
            else:  # If user guessed word is Wrong then this statement is executed
                print("Try it again")

        want_to_continue = input(
            "Want to continue game // Back to Main Menu (Y/Back) :")  # This input is asking weather u wanna continue playing this Game of wanna go back to main Menu
