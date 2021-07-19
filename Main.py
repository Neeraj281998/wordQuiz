import animal as animalGame  # Animal Module is imported
import Food as foodGame  # Food Module is imported
import Fruits as fruitGame  # Fruit Module is imported
import Colour as colourGame  # Colour Module is imported
import Shapes as shapesGame  # Shapes Module is imported
import bodyParts as bodyPartGame  # BodyParts Module is imported
print("---------------Welcome to the Guess The Word---------------")
print()
print("Categories")
print("------------------------------------------------------------")
print("1. Animal")
print("2. Food")
print("3. Fruits")
print("4. Colour")
print("5. Shapes")
print("6. Body Parts")
print("7. Exit Game")
print()
print("------------------------------------------------------------")
print("*NOTE :  This Game is Case sensitive")
print()
print("Ex : hand  =>  Input will be not be accepted ")
print("Ex : Hand  =>  Input will be accepted ")
Exit = "N"

while True:  # While Loop
    print("------------------------------------------------------------")
    user_choice = (
        int(input("Choose the Index Number from above Categories list :")))
    print("------------------------------------------------------------")

    if user_choice == 1:  # If user Input 1 The the Animal Module will run
        print()
        print("Welcome to Guess Animal Name ")
        print()
        print('If u are not able to guess the word then type this ==> "Give up"')
        print()
        animalGame.Animal_Game()

    elif user_choice == 2:  # If user Input 2 The the Food Module will run
        print()
        print("Welcome to Guess Food Name ")
        print()
        print('If u are not able to guess the word then type this ==> "Give up"')
        print()
        foodGame.Food_game()

    elif user_choice == 3:  # If user Input 3 The the Fruit Module will run
        print()
        print("Welcome to Guess Fruit Name   ")
        print()
        print('If u are not able to guess the word then type this ==> "Give up"')
        print()
        fruitGame.Fruit_game()

    elif user_choice == 4:  # If user Input 4 The the Colour Module will run
        print()
        print("Welcome to Guess Color Name ")
        print()
        print('If u are not able to guess the word then type this ==> "Give up"')
        print()
        colourGame.Color_game()

    elif user_choice == 5:  # If user Input 5 The the Shapes Module will run
        print()
        print("Welcome to Guess Shapes Name ")
        print()
        print('If u are not able to guess the word then type this ==> "Give up"')
        print()
        shapesGame.Shapes_game()
    elif user_choice == 6:  # If user Input 6 The the Body Part Module will run
        print()
        print("Welcome to Guess Body Part Name ")
        print()
        print('If u are not able to guess the word then type this ==> "Give up"')
        print()
        bodyPartGame.Body_Parts_game()
    elif user_choice == 7:  # If user Input 7 then this Program will be Ended
        print("------------------------------------------------------------")
        print("Thank you..!!!   Visit Again ")
        print("------------------------------------------------------------")
        break
    else:
        # If the use input Wrong index then this statement will be excuted
        print("Index Number you choose is not valid ...Please Put the valid Index Number")
