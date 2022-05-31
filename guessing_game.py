import random
class GuessingGame():

    def __init__(self, answer):
        self.answer = answer
        self.is_solved = False

    def guess(self):
        while self.is_solved == False:
            user_guess = int(input('Enter your guess: '))
            if user_guess < self.answer:
                print('Higher')
            elif user_guess > self.answer:
                print('Lower')
            elif user_guess == self.answer:
                print("You guessed it! Congratssssss")
                self.is_solved = True


def main():
    myObj = GuessingGame(random.randint(1,100))
    print(myObj.guess())
 


if __name__ == "__main__":
    main()