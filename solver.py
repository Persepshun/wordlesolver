# Author - Daniel Speedone
# This is my worlde solver I am designing for fun.
# Both the solver.py and words.txt must be in the same folder.

def load_words(filename="words.txt"):
    with open(filename, 'r') as f:
        # dictionary is in lowercase, converts all chars to lowercase for proper validation.
        return [word.strip().lower() for word in f if len(word.strip()) == 5]

def is_valid(word, guess, feedback):
    for i in range(5):
        g = guess[i]
        w = word[i]
        # changes feedback to uppeer so you can use whatever for feedback.
        f = feedback[i].upper()

        if f == 'G' and w != g:
            return False
        elif f == 'Y':
            if g not in word or w == g:
                return False
        elif f == 'B':
            # Handle duplicate letters (only exclude if not green/yellow elsewhere)
            total_in_word = word.count(g)
            total_confirmed = sum(
                1 for j in range(5) if guess[j] == g and feedback[j].upper() in ('G', 'Y')
            )
            # error handling for incorrect inputs.
            if total_in_word > total_confirmed:
                return False
    return True

# checks the feedback and guesses against the dictionary.
def filter_words(words, guesses):
    for guess, feedback in guesses:
        words = [word for word in words if is_valid(word, guess, feedback)]
    return words

# main function code
def main():
    # loads in predefined dictionary
    words = load_words("words.txt")
    guesses = []

    print("Welcome to Daniel's Wordle Solver!\n")
    print("Enter your 5 letter word guesses and the corresponding feedback.")
    print("Feedback key: G = Green, Y = Yellow, B = Gray")
    print("Example: If correct word is Apple, and your guess is Table, your feedback should be YBBGG. ")
    print("Type 'done' to finish and get you results.")
    print("Note: Capitalization does not matter for guesses or feedback.\n")

    # Logic that controls the guesses and feedback
    while True:
        guess = input("Guess: ").strip().lower()
        if guess == "done":
            break
        feedback = input("Feedback (e.g., BYGBG): ").strip().upper()

        # input validation/error andling
        if len(guess) != 5 or len(feedback) != 5:
            print("Both guess and feedback must be 5 characters long.")
            continue

        guesses.append((guess, feedback))

    filtered = filter_words(words, guesses)

    print(f"\n{len(filtered)} possible word(s):")
    for word in filtered:
        print(word)

# main with a pause break otherwise the program will close after guesses.
if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")