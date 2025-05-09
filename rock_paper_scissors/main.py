import random

# Tuple of choices
choices = ((1, 'Rock'), (2, 'Paper'), (3, 'Scissors'))

# Scores
computer_score = 0
user_score = 0
 # Random choice for computer each round
computer_choice = random.choice([1, 2, 3])

# Function to get choice name from number
def name_choice(num):
    for choice, value in choices:
        if num == choice:
            return value

# Main game logic
def logic():
    global computer_score, user_score  # Needed to modify outer variables

    while True:
        print('\nChoose one of the following:')
        print('1. Rock')
        print('2. Paper')
        print('3. Scissors')
        print('4. Exit')

        try:
            user_choice = int(input('Enter your choice: '))
            if user_choice == 4:
                print("Exiting the game.")
                break
            if user_choice not in [1, 2, 3]:
                raise ValueError('Invalid input, enter 1, 2, or 3')
        except ValueError as e:
            print(e)
            continue

        # ✅ This must be inside the loop
        computer_choice = random.choice([1, 2, 3])

        print(f"\nUser chose: {name_choice(user_choice)}")
        print(f"Computer chose: {name_choice(computer_choice)}")

        if computer_choice == user_choice:
            print("It's a tie.")
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print('User wins this round!')
            user_score += 1
        else:
            print('Computer wins this round!')
            computer_score += 1

        print(f"Score => User: {user_score}, Computer: {computer_score}")

        # End game if either gets 3 points
        if computer_score == 3:
            print(f"\n🏆 The computer wins with a score of: {computer_score}")
            break
        if user_score == 3:
            print(f"\n🏆 The user wins with a score of: {user_score}")
            break

# Run the game
logic()
