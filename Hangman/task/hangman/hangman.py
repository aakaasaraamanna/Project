import random
import string


def player_menu():
    player_selection = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if player_selection not in ["play", "results", "exit"]:
        player_menu()
    elif player_selection == "play":
        gameplay()
    elif player_selection == "results":
        display_results()
    elif player_selection == "exit":
        exit()


def display_results():
    print(f"You won: {won_times} times.\nYou lost: {lost_times} times.")
    player_menu()


def gameplay():
    word_list = ["python", "java", "swift", "javascript"]
    word = random.choice(word_list)
    total_guesses = 8
    solution = "-" * len(word)
    solution_list = []
    global won_times, lost_times
    while total_guesses != 0:
        appear_var = False
        print(f"\n{solution}")
        guess = input("Input a letter: ")
        if len(guess) == 1 and guess in string.ascii_lowercase:
            count = 0
            if guess not in solution_list:
                solution_list.append(guess)
                for i in range(0, len(word)):
                    if guess == word[i]:
                        solution = solution[:i] + guess + solution[i + 1:]
                        count += 1
            else:
                print("You've already guessed this letter.")
                appear_var = True
            if solution == word:
                break
            if count == 0 and not appear_var:
                print("That letter doesn't appear in the word.")
                total_guesses -= 1
        elif len(guess) != 1:
            print("Please, input a single letter.")
        elif guess not in string.ascii_lowercase:
            print("Please, enter a lowercase letter from the English alphabet.")
    print(f"\n{solution}\nYou guessed the word {word}!\nYou survived!" if total_guesses != 0 else "You lost!")
    if total_guesses != 0:
        won_times += 1
    else:
        lost_times += 1
    player_menu()


print("H A N G M A N")
won_times = 0
lost_times = 0
player_menu()
