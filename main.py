# This program will have the user guess the random word by guessing seperate letters. Each letter should be underlined so the user knows how many letters there are, there should be a specific amount of tries the user can attempt. Each letter should be marked as used after using it, each blank should be filled with the letter if guessed correctly. Figure out the modules to import. 

import random
# Function definions here

# Description: Loads words from the text file into a list and chooses a random word from that list.
# Parameters: filename
# Return value: word (string)
def getWord(filename):
  wordFile = open(filename, 'r')
  wordList = []
  for line in wordFile:
      # .strip() removes \n from the string
      wordList.append(line.strip())
  wordFile.close()
  return random.choice(wordList)

# Description: Convert the number of letters in the given word to the same amount of dashes as a list.
# Parameters: Random word
# Return value: A list of dashes to replace each letter of the word
def initDashes(word):
  dashes = []
  for i in word:
    dashes.append("_")
  return dashes

# Description: Tells us whether the user's guess was valid
# Parameters: guess, display, wrongGuesses
# Return value: boolean (True: valid, False: invalid)
def validate_guess(guess, display, wrongGuesses):
  if (not guess.isalpha()) or (len(guess) != 1):
    return False
  elif (guess in display) or (guess in wrongGuesses):
    return False
  else:
    return True

# Description: Checks if user's guess is correct/incorrect, and updates the display OR wrongGuesses
# Parameters: guess, display, wrongGuesses, answer
# Return value: boolean
def check_correct(guess, display, wrongGuesses, answer):
  if guess not in answer:
    wrongGuesses.append(guess)
    return False
  else:
    for i in range(len(display)):
      if guess == answer[i]:
        display[i] = guess
    return True

# In here, we put everything together, and actually make the game
def Hangman():
  print("This is the Hangman game. You must guess the word before the man hanging, dies. Good luck!")
  
  lives = 8
  answer = getWord("words.txt")
  display = initDashes(answer)
  wrongGuesses = []
  playing = True

  while playing and lives > 0: # Game loop
    for i in display:
      print(i, end = ' ')
    print()

    print("Wrong Guesses: ")
    for i in wrongGuesses:
      print(i, end = ' ')
    print()

    print("Number of lives left:", lives)
    
    guess = input("Guess a letter: ")
    valid = validate_guess(guess, display, wrongGuesses)

    while not valid: # same thing as while valid == False
      print("Your response was not valid. Type a one letter guess you have not already tried.")
      guess = input("Guess a letter: ")
      valid = validate_guess(guess, display, wrongGuesses)
    
    correct = check_correct(guess, display, wrongGuesses, answer)

    if correct:
      print("Congrats!")
    else:
      lives -= 1
      if lives > 0:
        print("Guess again.")
    
    if lives == 0:
      print("You ran out of lives! L")
      print("The word was", answer)
    
    if "_" not in display:
      playing = False
      print("You figured it out! yay")

Hangman()