# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word_letters = []
    for letter in secret_word:
        secret_word_letters.append(letter)
    secret_word_letters.sort()
    letters_guessed.sort()
    #print(secret_word_letters)
    #print(letters_guessed)
    if secret_word_letters == letters_guessed:
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    result = ['_ ' for l in secret_word]
    is_correct = False

    for index, letter in enumerate(secret_word):
        if letter in letters_guessed:
            result[index] = letter
            print('Great! You guessed a letter in the secret word.')
            is_correct = True
    print(''.join(result))
    return result, is_correct

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    letters = [l for l in string.ascii_lowercase if l not in letters_guessed]
    return letters

def get_num_unique_letters(secret_word):
    result = []
    for l in secret_word:
        if l not in result:
            result.append(l)
    return len(result)

    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    num_guesses = 6
    user_warnings = 3
    letters_guessed = []
    num_letters = len(secret_word)
    vowels = ['a', 'e', 'i', 'o', 'u']
    print('The word contains', num_letters, 'letters')

    while num_guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print('You have', user_warnings, 'warnings left')
        print('You have', num_guesses, 'guesses')
        print('Available letters: ', ''.join(get_available_letters(letters_guessed)))
        user_input = input('Please, guess a letter: ').lower()

        #User Input Validation
        if user_input not in string.ascii_letters and user_warnings > 0:
            user_warnings -= 1
            print('Invalid input. Please insert a letter.')
            num_guesses += 1

        #Check if letter is in the secret word
        if user_input not in letters_guessed:
            letters_guessed.append(user_input)
            guessed_word, isCorrect = get_guessed_word(secret_word, letters_guessed)
            print(isCorrect)
            if isCorrect == True:
                num_guesses += 1
            else:
                print('That was a bad guess and you lose a guess. Try again!')
                if user_input in vowels:
                    num_guesses -= 1
        else:
            print('You have already guessed that letter!')
            if user_warnings > 0:
                user_warnings -= 1
                num_guesses += 1

        print('Letters guessed so far:', letters_guessed)
        num_guesses -= 1

    #Check if user won
    if is_word_guessed(secret_word, letters_guessed):
        score = num_guesses * get_num_unique_letters(secret_word)
    else:
        print('Sorry, you ran out of guesses. You lose :(')


secret_word = 'putchuca'
hangman(secret_word)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
