from hangman import Hangman
from graphics import *
from button import Button


class Structure:
    def __init__(self, win, lowerleft, upperright):
        self.win = win
        self.ll = lowerleft
        self.ur = upperright
        self.width = lowerleft.getX() - upperright.getX()
        self.height = lowerleft.getY() - upperright.getY()
        self.drawStructure()
        self.bodyParts = self.parts()

    def drawStructure(self):
        elements = []
        p1 = self.ll
        p2 = Point(self.ll.getX() + self.width/6, self.ll.getY())
        p3 = Point(self.ll.getX() + self.width/3, self.ll.getY())
        p4 = Point(self.ll.getX() + self.width/6, self.ur.getY())
        p5 = self.ur
        p6 = Point(self.ur.getX(), self.ur.getY() + self.height/5)
        elements.append(Line(p1,p3))
        elements.append(Line(p2,p4))
        elements.append(Line(p4,p5))
        elements.append(Line(p5,p6))
        for el in elements:
            el.setWidth(3)
            el.draw(self.win)

    def parts(self):
        head = Circle(Point(self.ur.getX(), self.ur.getY() + self.height*1.5/5), self.height/10)
        p1 = Point(self.ur.getX(), self.ur.getY() + self.height*2/5)
        p2 = Point(self.ur.getX(), self.ur.getY() + self.height*4.5/5)
        body = Line(p1,p2)
        p1.move(-0.5,-1.5)
        p3 = p1.clone()
        p3.move(1,0)
        p2.move(0,1.5)
        left_arm = Line(p1,p2)
        right_arm = Line(p2,p3)
        arms = [left_arm, right_arm]
        left_leg, right_leg = left_arm.clone(), right_arm.clone()
        left_leg.move(0,-1.5)
        right_leg.move(0,-1.5)
        legs = [left_leg, right_leg]
        return [[head], [body], arms, legs]

    def drawBodyPart(self, part_no):
        pos = part_no - 1
        if part_no < 5:
            for part in self.bodyParts[pos]:
                part.draw(self.win)
                part.setOutline("green")
                part.setWidth(5)
        else:
            for item in self.bodyParts:
                for part in item:
                    part.setOutline("red")

    def undraw(self):
        for item in self.bodyParts:
            for part in item:
                part.undraw()


class GUIInterface:
    def __init__(self):
        self.win = win = GraphWin("HANGMAN", 300, 300)
        win.setCoords(0,0,10,10)
        self.buttons = []
        self.__createButtons()
        self.hangman = Structure(win, Point(2, 4.5), Point(4,9))
        self.word = []
        self.playButton = Button(win, Point(2,1), 2, 1, "Play")
        self.quitButton = Button(win, Point(8,1), 2, 1, "Quit")
        self.text = Text(Point(5, 1.75), "").draw(win)
        self.text.setStyle("bold")
        self.wordText = Text(Point(3,2.75), "").draw(self.win)

    def __createButtons(self):
        specs = [("A", 6, 9), ("B", 7, 9), ("C", 8, 9), ("D", 9, 9),
                 ("E", 6, 8), ("F", 7, 8), ("G", 8, 8), ("H", 9, 8),
                 ("I", 6, 7), ("J", 7, 7), ("K", 8, 7), ("L", 9, 7),
                 ("M", 6, 6), ("N", 7, 6), ("O", 8, 6), ("P", 9, 6),
                 ("Q", 6, 5), ("R", 7, 5), ("S", 8, 5), ("T", 9, 5),
                 ("U", 6, 4), ("V", 7, 4), ("W", 8, 4),
                 ("X", 6, 3), ("Y", 7, 3), ("Z", 8, 3)]
        for (label, x, y) in specs:
            button = Button(self.win, Point(x,y), 0.5, 0.75, label)
            self.buttons.append(button)

    def wrongAnswer(self, wrong_guesses):
        self.hangman.drawBodyPart(wrong_guesses)

    def playGame(self):
        self.playButton.activate()
        self.quitButton.activate()
        for button in self.buttons:
            button.deactivate()
        while True:
            p = self.win.getMouse()
            if self.playButton.clicked(p):
                self.playButton.deactivate()
                self.quitButton.deactivate()
                self.hangman.undraw()
                self.text.setText("")
                # self.wordText.setText(self.word)
                for button in self.buttons:
                    button.activate()
                return True
            if self.quitButton.clicked(p):
                self.win.close()
                return False

    def setWordLenght(self, lenght):
        self.word = ["_"] * lenght
        self.wordText.setText("_  " * lenght)
        self.wordText.setSize(25)
        self.wordText.setStyle("bold")

    def getLetter(self):
        while True:
            p = self.win.getMouse()
            for button in self.buttons:
                if button.clicked(p):
                    button.deactivate()
                    return str(button.getLabel().getText()).lower()

    def updateWord(self, letter, pos):
        # pos is  a list of possintions for the same letter in the word
        for p in pos:
            self.word[p] = letter.upper()
        wordStr = "  ".join(self.word)
        self.wordText.setText(wordStr)

    def displayResult(self, guesses):
        if guesses >= 5:
            self.text.setText("You lost!")
        else:
            self.text.setText("Congratulations! You guesses the word, and you had %s wrong guesses." % str(guesses))

    def getWord(self):
        return self.word

    def displayFinishedWords(self):
        Text(Point(5, 2.25), "There are no more words to guess.").draw(self.win)

    def displayEndMessage(self):
        for i in range(5):
            text = "Thanks for playing!\n" + str(5-i)
            self.text.setText(text)
            update(1)
        self.win.close()


if __name__ == "__main__":
    interface = GUIInterface()
    hangman = Hangman(interface)
    hangman.run()
