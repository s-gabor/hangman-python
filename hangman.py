class Hangman:
    def __init__(self, interface):
        self.interface = interface
        self.words = ["python", "school"]  # more words can be added/imported from a text file

    def run(self):
        while self.interface.playGame():
            if self.words == []:
                self.interface.displayFinishedWords()
                break
            self.interface.displayResult(self.playRound())
        self.interface.displayEndMessage()

    def playRound(self):
        self.word = self.words.pop(0)
        self.interface.setWordLenght(len(self.word))
        wrong_guesses = 0
        while wrong_guesses < 5:
            letter = self.interface.getLetter()
            if letter in self.word:
                self.updateLetter(letter)
            else:
                wrong_guesses += 1
                self.interface.wrongAnswer(wrong_guesses)
            if self.__wordGuessed():
                return wrong_guesses
        return wrong_guesses

    def updateLetter(self, letter):
        pos = []
        for i in range(len(self.word)):
            if letter == self.word[i]:
                pos.append(i)
        self.interface.updateWord(letter, pos)

    def __wordGuessed(self):
        wordDisplayed = "".join(self.interface.getWord())
        return wordDisplayed.lower() == self.word
