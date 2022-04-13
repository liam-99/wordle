import letters

ALPHABETS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def stringToIntList(ins):
    t = ins.split()
    outList = []
    for c in t:
        outList.append(int(c) - 1)
    return outList

def containAny(letters, word):
    for l in letters:
        if l in word:
            return True
    return False

def containAll(letters, word):
    for l in letters:
        if l.getCharacter() not in word:
            return False
    return True

def checkPossible(letters, word):
    for letter in letters:
        if letter.getPosition() is None:
            if word.index(letter.getCharacter()) in letter.getFalsePosition():
                return False
        else:
            if word.index(letter.getCharacter()) != letter.getPosition():
                return False
    return True
 
print("*** Welcome to WORDLE word searcher ***")
print("input :")
print("- 1st line must be a set of letters seperated by space which are not in word in any spot")
print("- 2nd and others line must be a set of value seperated by comma")
print("\tformat : letter included in word, correct index of letter in the word (if not found 0), incorrect indexs of letter seperated by space")
print("- to end entering input enter end/END (case doesn't matter)")
print("example :\nf i n o w\ns, 5, 1\nt, 0, 3 5\nend")
print()

start = 'Yes'
while start == 'Yes' or start == 'Y':
    x = input().upper() # input (single characters seperated by space) - 'A B C'
    falseLetters = []
    if x != "NONE":
        falseLetters = x.split()
        
    trueLetters = []

    x = input() # input - ch, true position (not found 0), false positions
    while x.upper() != "END":
        ins = x.split(',')
        l = letters.WordleLetter(ins[0].upper())
        if ins[1] != ' 0':
            l.setPosition(int(ins[1]) - 1)
        else:
            l.setFalsePosition(stringToIntList(ins[2]))

        trueLetters.append(l)

        x = input()
            
    # eliminate not possible words
    filenames = ALPHABETS.copy()
    for letter in falseLetters:
        filenames.remove(letter)

    possible_words = set()
    for file in filenames:
        f = open("words\\" + file + ".txt", 'r')
        words = f.read().split()

        for word in words:
            if not containAny(falseLetters, word): # eliminate words with false letters
                
                if len(trueLetters) > 0:
                    if containAll(trueLetters, word):
                        if checkPossible(trueLetters, word):
                            possible_words.add(word)
                else:
                    possible_words.add(word)
                
        f.close()

    print(len(possible_words), "possible word(s) found")
    tab_count = 0
    for word in possible_words:
        print(word, end='\t')
        if tab_count < 5:
            tab_count += 1
        else:
            tab_count = 0
            print(end='\n')
    print(end='\n')
    
    start = input("Do you want to find again? [Y/N] : ").upper()


    
