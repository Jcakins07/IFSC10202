import random

print("Winners and Losers - Human is Even, Computer is Odd")

human_score = 0
computer_score = 0

for round_num in range(1, 6):
    print("Round:", round_num)
    
    while True:
        try:
            human = int(input("Enter your guess (1-5): "))
            if 1 <= human <= 5: break
            print("Number must be between 1 and 5.")
        except: print("Invalid input. Enter a number.")

    computer = random.randint(1, 5)
    total = human + computer

    print(f"Human Guess: {human} - Computer Guess: {computer}")
    print("Sum is Even" if total % 2 == 0 else "Sum is Odd")

    if total % 2 == 0:
        human_score += 1
    else:
        computer_score += 1

    print(f"Human Score: {human_score} - Computer Score: {computer_score}\n")

print("Human Wins" if human_score > computer_score else "Computer Wins" if computer_score > human_score else "It's a Tie!")
