import random
import hangmanArt
import hangmanWords

chosen_word = random.choice(hangmanWords.word_list)
display = []
lives = 6
gameEnd = False

print(hangmanArt.logo)

#create blanks
for _ in chosen_word:
    display += "_"

while not gameEnd:
    guess = input("Guess a letter: ").lower()
    
    #Check if the letter already guessed before
    if guess in display:
        print(f"You've already guessed a letter '{guess}'")

    #Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if the letter guessed doesn't exist in the word       
    if guess not in chosen_word:
        print(f"You guessed letter '{guess}', it is not in the word. You lost a life.")
        lives -= 1
        if lives == 0:
            gameEnd = True
            print("You lose.")
            
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        gameEnd = True
        print("You win!")
        
    print(hangmanArt.stages[lives])