import random

print("Winners and Losers - Human is Even, Computer is Odd")
human_score = computer_score = 0
for i in range(1, 6):
    print(f"Round: {i}")
    while True:
        try:
            human = int(input("Enter your guess (1-5): "))
            if 1 <= human <= 5: break
            print("Number must be 1-5.")
        except:
            print("Invalid input.")
    computer = random.randint(1, 5)
    total = human + computer
    even = total % 2 == 0
    print(f"Human Guess: {human} - Computer Guess: {computer}")
    print("Sum is Even" if even else "Sum is Odd")
    if even:
        human_score += 1
    else:
        computer_score += 1
    print(f"Human Score: {human_score} - Computer Score: {computer_score}")
print("Human Wins" if human_score > computer_score else "Computer Wins" if computer_score > human_score else "It's a Tie!")