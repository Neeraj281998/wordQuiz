import random


def Food_game():
    want_to_continue = "Y"
    while want_to_continue == "Y":
        FOOD = ["Cheese", "Egg", "Butter", "Margarine", "Yogurt", "Cottage", " cheese", "Ice cream", "Cream", "Sandwich",
                "Sausage", "Hamburger", "Hot dog", "Bread", "Pizza", "Steak", "Roast chicken", "Fish", "Seafood", "Ham", "Kebab"]
        # Picking random string from the List
        random_Food = random.choice(FOOD)
        # Picking the index of the string which is randomly picked
        index_random_Food = FOOD.index(random_Food)

        suffled = list(random_Food)  # Converting that picked string in List
        random.shuffle(suffled)  # Shuffleing the Picked String
        suffled = ''.join(suffled)  # Joining the String agian
        question = suffled.upper()  # Converting the the String into Upper case

        while True:
            print("Guess the Food : ", question)  # Question

            # User will guess the word and input here
            answer = input("Guess the word : ")
            if (answer == FOOD[index_random_Food]):
                # If the word gussed by the user is Write the then this will be executed
                print("Congratulations !! You gussed it right ")
                break
            elif (answer == "Give up"):  # If the User Give up then Answer will be showen to the user
                print("Try Hard Next Time..!!")
                print()
                print("The word was ==> ", random_Food)
                print()
                break
            else:  # If user guessed word is Wrong then this statement is executed
                print("Try it again")

        want_to_continue = input(
            "Want to continue game // Back to Main Menu (Y/Back) :")  # This input is asking weather u wanna continue playing this Game of wanna go back to main Menu
