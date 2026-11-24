import random
import string

# Pick the first digit from 1-9, and the next three from 0-9
genNum = random.choice(string.digits[1:]) + "".join(random.choices(string.digits, k=3))
guessedNum = ""

timesGuessed = 0

print("Welcome to the Bulls and Cows game!")
print("I have generated a 4-digit number for you to guess.")
print("A 'cow' means you guessed a correct digit in the correct position.")
print("A 'bull' means you guessed a correct digit but in the wrong position.")
print()

while(guessedNum != genNum):
    guessedNum = input("Enter your guess: ")
    timesGuessed += 1
    bulls, cows = 0, 0
    
    # for i in range(4):
    #     if guessedNum[i] == genNum[i]:
    #         cows += 1
    #     matched[i] = True


    # for i in range(4):
    #     if guessedNum[i] != genNum[i]:
    #         for j in range(4):
    #             if guessedNum[i] == genNum[j] and not matched[j]:
    #                 bulls += 1
    #                 matched[j] = True
    #                 break

    freq = [0] * 10

    # Count cows and frequency of unmatched generated digits
    for i in range(4):
        if guessedNum[i] == genNum[i]:
            cows += 1
        else:
            freq[int(genNum[i])] += 1

    # Count bulls
    for i in range(4):
        if guessedNum[i] != genNum[i]:
            digit = int(guessedNum[i])

            if freq[digit] > 0:
                bulls += 1
                freq[digit] -= 1


    print(f"Bulls: {bulls}, Cows: {cows}")
    print()

print(f"Congratulations! You guessed the number in {timesGuessed} attempts.")
