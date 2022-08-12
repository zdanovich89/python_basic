from random import randrange


def start_game():
    guess_namber = randrange(1, 101)
    print(guess_namber)
    answer = int(input("Guess the integer from 1 to 100: "))

    while answer not in range(1, 101):
        if answer > 100 or answer < 1:
            print("Please enter number in range from 1 to 100")
            answer = int(input("Guess the integer from 1 to 100: "))

    while answer != guess_namber:
        if answer < guess_namber:
            multiply = guess_namber // answer
            sum = guess_namber % answer
            if multiply >= 2 and sum == 0:
                print("Sorry, you didn't guess, try again!")
                answer = int(
                    input("Try multiply " + str(answer) + " by " + str(multiply) + " : "))

            elif multiply >= 2 and sum > 0:
                print("Sorry, you didn't guess, try again!")
                answer = int(input("Try multiply " + str(answer) + " by " +
                                   str(multiply) + " and add " + str(sum) + " : "))

            else:
                print("Sorry, you didn't guess, try again!")
                answer = int(input("Try add " + str(sum) +
                                   " at " + str(answer) + " : "))

        if answer > guess_namber:
            divisor = answer // guess_namber
            min = answer % guess_namber

            if divisor >= 2 and min == 0:
                print("Sorry, you didn't guess, try again!")
                answer = int(input("Try divide " + str(answer) +
                                   " to " + str(divisor) + " : "))

            elif divisor >= 2 and min != 0:
                print("Sorry, you didn't guess, try again!")
                answer = int(input("Try less " + str(min) + " from " +
                                   str(answer) + " and divide to " + str(divisor) + " : "))

            else:
                print("Sorry, you didn't guess, try again!")
                answe = int(
                    input("Try less " + str(min) + " from " + str(answer) + " : "))
                break

    print("Congratulations, you guessed, it's number: " + str(guess_namber))


start_game()
