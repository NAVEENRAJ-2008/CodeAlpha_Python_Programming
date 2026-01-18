import random
import os
import time

# --- ASCII ART FOR GALLOWS ---
# This significantly increases the visual quality and code length.
HANGMAN_STAGES = [
    """
       --------
       |      |
       |      
       |    
       |      
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |     /|
       |      |
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |     / 
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |     / \\
    - - - - -
    """
]

# --- WORD DATA ---
WORD_DATA = {
    "Programming": ["python", "javascript", "algorithm", "compiler", "variable", "function", "database"],
    "Animals": ["elephant", "giraffe", "kangaroo", "leopard", "penguin", "octopus", "dolphin"],
    "Countries": ["india", "canada", "germany", "australia", "brazil", "japan", "egypt"],
    "Movies": ["inception", "gladiator", "avengers", "interstellar", "parasite", "joker"]
}

class HangmanGame:
    def __init__(self):
        self.wins = 0
        self.losses = 0

    def clear_screen(self):
        # Clears terminal for a cleaner look
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_difficulty(self):
        print("\nChoose Difficulty:")
        print("1. Easy (10 lives)")
        print("2. Medium (6 lives)")
        print("3. Hard (4 lives)")
        choice = input("Select (1-3): ")
        if choice == '1': return 10
        if choice == '3': return 4
        return 6

    def get_category(self):
        print("\nChoose Category:")
        categories = list(WORD_DATA.keys())
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        
        try:
            choice = int(input("Select number: "))
            return categories[choice - 1]
        except:
            return "Programming"

    def play_round(self):
        category_name = self.get_category()
        word = random.choice(WORD_DATA[category_name]).lower()
        lives = self.get_difficulty()
        max_lives = lives
        guessed_letters = []
        word_completion = "_" * len(word)
        
        self.clear_screen()
        
        while lives > 0 and "_" in word_completion:
            print(f"\nCategory: {category_name} | Lives: {lives} | Score: {self.wins}W-{self.losses}L")
            
            # Draw the hangman based on life percentage
            if max_lives == 6:
                print(HANGMAN_STAGES[6 - lives])
            else:
                # Scaled drawing for non-standard life counts
                stage_idx = int(((max_lives - lives) / max_lives) * 6)
                print(HANGMAN_STAGES[stage_idx])

            print(f"Word: {' '.join(word_completion)}")
            print(f"Guessed: {', '.join(guessed_letters)}")
            
            guess = input("\nEnter a letter (or type 'hint'): ").lower().strip()

            # --- HINT SYSTEM ---
            if guess == 'hint':
                if lives > 2:
                    remaining = [l for l in word if l not in word_completion]
                    hint_char = random.choice(remaining)
                    print(f"HINT: The word contains '{hint_char}' (Cost: 2 lives)")
                    lives -= 2
                    time.sleep(2)
                    continue
                else:
                    print("Not enough lives for a hint!")
                    time.sleep(1)
                    continue

            # --- VALIDATION ---
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                time.sleep(1)
                continue
            
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try again.")
                time.sleep(1)
                continue

            guessed_letters.append(guess)

            # --- LOGIC ---
            if guess in word:
                print(f"Yes! '{guess}' is in the word.")
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
            else:
                print(f"No. '{guess}' is not there.")
                lives -= 1
            
            time.sleep(1)
            self.clear_screen()

        # --- END OF ROUND ---
        if "_" not in word_completion:
            print(f"CONGRATULATIONS! You guessed '{word}'!")
            self.wins += 1
        else:
            print(HANGMAN_STAGES[6] if max_lives == 6 else HANGMAN_STAGES[-1])
            print(f"GAME OVER! The word was: {word}")
            self.losses += 1

    def start(self):
        print("Welcome to the Ultimate Hangman Challenge!")
        while True:
            self.play_round()
            again = input("\nPlay another round? (y/n): ").lower()
            if again != 'y':
                print(f"\nFinal Score: {self.wins} Wins | {self.losses} Losses")
                print("Thanks for playing!")
                break
            self.clear_screen()

# Run the game
if __name__ == "__main__":
    game = HangmanGame()
    game.start()