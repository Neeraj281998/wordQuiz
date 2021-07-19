import random


def Animal_Game():
    want_to_continue = "Y"
    while want_to_continue == "Y":
        Animal = ["Kangaroo", "Cow", "Dog", "Dolphin", "Donkey", "Eagle",
                  "Fish", "Fly", "Fox", "Frog""Gerbil", "Goose", "Gopher", "Gorilla"]

        # Picking random string from the List
        random_Animal = random.choice(Animal)
        # Picking the index of the string which is randomly picked
        index_random_Animal = Animal.index(random_Animal)

        suffled = list(random_Animal)  # Converting that picked string in List
        random.shuffle(suffled)  # Shuffleing the Picked String
        suffled = ''.join(suffled)  # Joing the String agian
        question = suffled.upper()      # Converting the the String into Upper case

        while True:
            print("Guess the animal : ", question)  # Question

            # User will guess the word and input here
            answer = input("Guess the word : ")
            if (answer == Animal[index_random_Animal]):
                # If the word gussed by the user is Write the then this will be executed
                print("Congratulations !! You gussed it right ")
                break
            elif (answer == "Give up"):  # If the User Give up then Answer will be showen to the user
                print("Try Hard Next Time..!!")
                print()
                print("The word was ==> ", random_Animal)
                print()
                break
            else:  # If user guessed word is Wrong then this statement is executed
                print("Try it again")

        want_to_continue = input(
            "Want to continue game // Back to Main Menu (Y/Back) :")  # This input is asking weather u wanna continue playing this Game of wanna go back to main Menu
