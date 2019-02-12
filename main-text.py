from hangman import Hangman


class TextInterface:
    def __init__(self):
        print("\n   *****     HANGMAN     *****   \n")
        self.word = []

    def playGame(self):
        play = input("Would like to play a game(y/n)? ")
        return play[0] in "yY"

    def setWordLenght(self, lenght):
        self.word = ["_"] * lenght
        print("Your word is: ", "".join(self.word))

    def getLetter(self):
        letter = input("Enter a letter: ")
        while True:
            if letter in self.word:
                letter = input("You already have that letter. Enter a new one: ")
            else:
                return letter.lower()

    def updateWord(self, letter, pos):
        # pos is  a list of possintions for the same letter in the word
        for p in pos:
            self.word[p] = letter
        wordStr = "".join(self.word)
        print("Your word is: ", wordStr)

    def displayResult(self, guesses):
        if guesses >= 5:
            print("You lost!")
        else:
            print("Congratulations! You guesses the word, and you had %s wrong guesses." % str(guesses))

    def getWord(self):
        return self.word

    def wrongAnswer(self, wrong_guesses):
        print("Bad choice. Try again!")

    def displayFinishedWords(self):
        print("There are no more words to guess.", end=" ")

    def displayEndMessage(self):
        print("Thanks for playing!")


if __name__ == "__main__":
    interface = TextInterface()
    hangman = Hangman(interface)
    hangman.run()
