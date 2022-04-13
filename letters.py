class Letter: 
    def __init__(self, character = None):
        self.__character = character
    
    def setCharacter(self, character):
        self.__character = character

    def getCharacter(self):
        return self.__character

class WordleLetter(Letter):
        
    def __init__(self, character = None, position = None):
        super().__init__(character)
        self.__position = position
        self.__falsePos = []

    def setCharacter(self, character):
        super().setCharacter(character)

    def setPosition(self, position):
        self.__position = position

    def setFalsePosition(self, positions):
        self.__falsePos = positions

    def getCharacter(self):
        return super().getCharacter()

    def getPosition(self):
        return self.__position

    def getFalsePosition(self):
        return self.__falsePos

    def __str__(self):
        outStr = self.getCharacter() + "\n"
        if self.__position != None:
            outStr = outStr + "Position : " + str(self.__position) + "\n"
        if len(self.__falsePos) > 0:
            outStr = outStr + "Wrong positions : " + str(self.__falsePos) + "\n"
        return outStr
