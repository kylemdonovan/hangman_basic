import random
#import dictionary? set wordlist to dict
word_list = ["aardvark", "baboon", "chimpanzee"]


stages = ['''
 +----+
 |    |     
 |    o     
 |   /|\     
 |   / \     
 | YOU DIE        
 ========
''', '''
 +----+
 |    |     
 |    o     
 |   /|\     
 |   /      
 |         
 ========
''','''
 +----+
 |    |     
 |    o     
 |   /|\     
 |       
 |         
 ========
''','''
 +----+
 |    |     
 |    o     
 |   /|     
 |       
 |         
 ========
''','''
 +----+
 |    |     
 |    o     
 |   /     
 |        
 |         
 ========
''','''
 +----+
 |    |     
 |    o     
 |        
 |       
 |         
 ========
''',]
#HOW GOOD ARE YOU?
#set lives based on this?
lives = 6

chosen_word = random.choice(word_list)

display = []
numberOf_Underscores = len(chosen_word)
displayCount = 0

while displayCount != numberOf_Underscores:
  display += "_"
  displayCount = displayCount + 1

while "_" in display and lives != 0:
  guess = input("Guess a letter: ").lower()

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
      print(display)
      if "_" not in display:
        print("You win!")
  if guess not in chosen_word:
    lives = lives - 1
    print("That letter isn't in our word.")
    print(stages[lives])


#things to add:
# check if character entry is > len(1) then revoke guess
# add challenge to increase/decrease lives (will need new hangman ascii)
# add a list which stores previous guesses and says hey you already guessed this
