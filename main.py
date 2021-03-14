"""
Hangman
Nicholas Nicorvo
2021
"""
import random

def intro():
    # Introduce the player to the game
    print('Welcome to Hangman!\n')
    print('DIRECTIONS:')
    print('There will be a word whose letters you have to guess.')
    print('You have 6 shots at not messing up.')
    print('Have fun!\n')

def initGuessWord(guessword):
    tempWordValue = ''
    for i in guessword:
        tempWordValue += '*'
    return tempWordValue

def processWord(guessLetter, finalWord, currentWord):
    tempWord = ''
    for i in range(0, len(currentWord)):
        if currentWord[i] == '*':
            if finalWord[i] == guessLetter:
                tempWord += guessLetter
            else:
                tempWord += '*'
        else:
            tempWord += currentWord[i]
    return tempWord

def displayWord(currentWord):
    print('Word progress: {}'.format(currentWord))

def main():
    # Game logic variables:
    tries = 6
    # First list is easy words, second list is medium words, third list is hard words:
    words = ['cow', 'apple', 'school', 'distraction', 'assignment', 'message', 'kickshaw', 'chthonic', 'diphthong']
    # Program starts here:
    intro()
    # Choose a random word out of words and assign its value:
    randomChoice = random.randint(0, len(words))
    todaysWord = words[randomChoice]
    # Creating the unfilled word:
    guessWord = initGuessWord(todaysWord)
    displayWord(guessWord)
    # Main Loop of the Game:
    while (tries > 0):
        print('{} tries left'.format(tries))
        # Get user input:
        userInput = input('Enter a single lowercase letter to guess if it\'s in the word of the day: ')
        # Only single letters allowed:
        if len(userInput) > 1:
            print('Only enter a single letter! Try again! \n')
        else:
            if (userInput in todaysWord) and (userInput not in guessWord):
                print('\nCorrect!\n')
                guessWord = processWord(userInput, todaysWord, guessWord)
                displayWord(guessWord)
                if guessWord == todaysWord:
                    print('You have won!')
                    break
            else:
                print('\nWRONG! Try again!\n')
                displayWord(guessWord)
                tries -= 1

    # Program ends here:
    if tries == 0:
        print('Sorry, you have ran out of tries. Better luck next time!')
    else:
        print('Congrats on winning! Hope to see you again soon!')

if __name__ == "__main__": main() # Where the main 'fun'ction begins (and ends)