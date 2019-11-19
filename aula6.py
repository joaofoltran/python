secret_number = 7
guess_count = 3

print(f"You have a total of {guess_count} guesses.")
while guess_count != 0:
    guess = int(input("Your guess: "))
    guess_count -= 1
    if guess == secret_number:
        print("Congrats! You won.")
        break
    else:
        if guess_count != 1:
            print(f"Try again! You have {guess_count} more guesses.")
        else:
            print(f"You only have one more guess.")
else:
    print(f"You failed. The number was {secret_number}.")
