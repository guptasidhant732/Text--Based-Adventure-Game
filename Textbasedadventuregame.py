
import random

def display_status(health, score):
    print("Health:", health)
    print("Score:", score)


def cave(health, score):
    damage = random.randint(10, 40)

    print("\nYou entered the cave!")
    print("A monster attacks! Damage:", damage)

    health -= damage

    if health > 0:
        print("You survived the monster attack!")
        score += 20
        print("You found a key! +20 Score")
    else:
        health = 0
        print("You have lost all your health!")

    return health, score


def river(health, score):
    print("\nYou reached the river!")
    print("You found a treasure! +50 Score")

    score += 50

    return health, score


def adventure_game():
    health = 100
    score = 0

    print("================================")
    print("    TEXT-BASED ADVENTURE GAME")
    print("================================")
    print("You are in a mysterious forest.")
    print("Starting Health:", health)
    print("Starting Score:", score)

    while health > 0:

        print("\nChoose your action:")
        print("1. Enter Cave")
        print("2. Cross River")
        print("3. Quit Game")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            health, score = cave(health, score)

        elif choice == "2":
            health, score = river(health, score)

        elif choice == "3":
            print("\nYou left the adventure!")
            break

        else:
            print("Invalid choice. Enter 1, 2 or 3.")
            continue

        display_status(health, score)

        if health <= 0:
            print("\nGAME OVER!")
            break

    print("\n================================")
    print("       FINAL GAME RESULT")
    print("================================")
    print("Final Score:", score)
    print("Final Health:", health)
    print("Thanks for playing!")


# Start the game
if __name__ == "__main__":
    adventure_game()
