import random


def Fruit_game():
    want_to_continue = "Y"
    while want_to_continue == "Y":
        Fruits = ["Apple", "Apricots", "Avocado", "Banana", "Blackberries", "Blackcurrant", " Blueberries", "Breadfruit", "Cream", "Cantaloupe",
                  "Carambola", "Cherimoya", "Cherries", "Clementine", "Coconut", "Cranberries", "Date", "Feijoa", "Mango", "Pineapple", "Orange"]
        # Picking random string from the List
        random_Fruit = random.choice(Fruits)
        # Picking the index of the string which is randomly picked
        index_random_Fruit = Fruits.index(random_Fruit)

        suffled = list(random_Fruit)  # Converting that picked string in List
        random.shuffle(suffled)  # Shuffleing the Picked String
        suffled = ''.join(suffled)  # Joining the String agian
        question = suffled.upper()  # Converting the the String into Upper case

        while True:
            print("Guess the Fruit : ", question)  # Question

            # User will guess the word and input here
            answer = input("Guess the word : ")
            if (answer == Fruits[index_random_Fruit]):
                # If the word gussed by the user is Write the then this will be executed
                print("Congratulations !! You gussed it right ")
                break
            elif (answer == "Give up"):  # If the User Give up then Answer will be showen to the user
                print("Try Hard Next Time..!!")
                print()
                print("The word was ==> ", random_Fruit)
                print()
                break
            else:  # If user guessed word is Wrong then this statement is executed
                print("Try it again")

        want_to_continue = input(
            "Want to continue game // Back to Main Menu (Y/Back) :")  # This input is asking weather u wanna continue playing this Game of wanna go back to main Menu
