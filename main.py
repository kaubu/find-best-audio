import os
from itertools import combinations

import pygame

pygame.mixer.init()

lists = [
    ["Test Vowels", {
        "a": ".\\sounds\\vowels\\a_Open_front_unrounded_vowel.ogg",
        "e": ".\\sounds\\vowels\\e_Close-mid_front_unrounded_vowel.ogg",
        "e̞": ".\\sounds\\vowels\\e̞_Mid_front_unrounded_vowel.ogg",
    }],
    ["Vowels", {
        "a": ".\\sounds\\vowels\\a_Open_front_unrounded_vowel.ogg",
        "e": ".\\sounds\\vowels\\e_Close-mid_front_unrounded_vowel.ogg",
        "e̞": ".\\sounds\\vowels\\e̞_Mid_front_unrounded_vowel.ogg",
        "i": ".\\sounds\\vowels\\i_Close_front_unrounded_vowel.ogg",
        "o": ".\\sounds\\vowels\\o_Close-mid_back_rounded_vowel.ogg",
        "o̞": ".\\sounds\\vowels\\o̞_Mid_back_rounded_vowel.ogg",
        "u": ".\\sounds\\vowels\\u_Close_back_rounded_vowel.ogg",
        "y": ".\\sounds\\vowels\\y_Close_front_rounded_vowel.ogg",
        "ä": ".\\sounds\\vowels\\ä_Open_central_unrounded_vowel.ogg",
        "æ": ".\\sounds\\vowels\\æ_Near-open_front_unrounded_vowel.ogg",
        "ø": ".\\sounds\\vowels\\ø_Close-mid_front_rounded_vowel.ogg",
        "ø̞": ".\\sounds\\vowels\\ø̞_Mid_front_rounded_vowel.ogg",
        "œ": ".\\sounds\\vowels\\œ_Open-mid_front_rounded_vowel.ogg",
        "ɐ": ".\\sounds\\vowels\\ɐ_Near-open_central_unrounded_vowel.ogg",
        "ɑ": ".\\sounds\\vowels\\ɑ_Open_back_unrounded_vowel.ogg",
        "ɒ": ".\\sounds\\vowels\\ɒ_PR-open_back_rounded_vowel.ogg",
        "ɔ": ".\\sounds\\vowels\\ɔ_Open-mid_back_rounded_vowel.ogg",
        "ɘ": ".\\sounds\\vowels\\ɘ_Close-mid_central_unrounded_vowel.ogg",
        "ə": ".\\sounds\\vowels\\ə_Mid-central_vowel.ogg",
        "ɛ": ".\\sounds\\vowels\\ɛ_Open-mid_front_unrounded_vowel.ogg",
        "ɜ": ".\\sounds\\vowels\\ɜ_Open-mid_central_unrounded_vowel.ogg",
        "ɞ": ".\\sounds\\vowels\\ɞ_Open-mid_central_rounded_vowel.ogg",
        "ɤ": ".\\sounds\\vowels\\ɤ_Close-mid_back_unrounded_vowel.ogg",
        "ɤ̞": ".\\sounds\\vowels\\ɤ̞_Mid_back_unrounded_vowel.ogg",
        "ɨ": ".\\sounds\\vowels\\ɨ_Close_central_unrounded_vowel.ogg",
        "ɪ": ".\\sounds\\vowels\\ɪ_Near-close_near-front_unrounded_vowel.ogg",
        "ɯ": ".\\sounds\\vowels\\ɯ_Close_back_unrounded_vowel.ogg",
        "ɵ": ".\\sounds\\vowels\\ɵ_Close-mid_central_rounded_vowel.ogg",
        "ɶ": ".\\sounds\\vowels\\ɶ_Open_front_rounded_vowel.ogg",
        "ʉ": ".\\sounds\\vowels\\ʉ_Close_central_rounded_vowel.ogg",
        "ʊ": ".\\sounds\\vowels\\ʊ_Near-close_near-back_rounded_vowel.ogg",
        "ʌ": ".\\sounds\\vowels\\ʌ_Open-mid_back_unrounded_vowel2.ogg",
        "ʏ": ".\\sounds\\vowels\\ʏ_Near-close_near-front_rounded_vowel.ogg",
    }],
]

ordered_list = list()
selected_list = None

print("Select a list:")
while True:
    for i, a_list in enumerate(lists):
        print(f"[{i+1}] {a_list[0]}")
    
    try:
        selection = int(input(">> ")) - 1
    except Exception as e:
        print(f"error: {e}")
        print("You most likely did not type a number. Try again.")
        continue

    selected_list = lists[selection]
    break

selected_set = set(selected_list[1].keys())
list_combinations = list(combinations(selected_set, 2))

RANDOMIZE = True # Randomize the questions
CLEAR_SCREEN = True # Clear screen after each question

##################### CHANGE THIS IN PROD
DEBUG = False
#####################

if RANDOMIZE:
    from random import shuffle
    shuffle(list_combinations)

if DEBUG:
    for language in selected_list[1]:
        print(f"[00] {language}")
    input("Continue?")

    print(f"selected_list = \n===\n{selected_list}\n===")
    print(f"selected_set = \n===\n{selected_set}\n===")
    print(f"list_combinations = \n===\n{list_combinations}\n===")

questions_len = len(list_combinations)

for i, match_up in enumerate(list_combinations):
    if DEBUG: print(f"i={i}; match_up={match_up}")

    if CLEAR_SCREEN:
        os.system("cls" if os.name == "nt" else "clear")
    
    if DEBUG and i != 0:
        print("Current DEBUG ranking:")
        for i, item in enumerate(ordered_list):
            print(f"#{i+1}: {item}")
        print()

    while True:
        sound_1 = selected_list[1][match_up[0]]
        sound_2 = selected_list[1][match_up[1]]

        pygame.mixer.music.load(sound_1)
        print("Playing sound 1…")
        pygame.mixer.music.play()
        
        # Wait until the first sound has finished
        while pygame.mixer.music.get_busy():
            continue
        # time.sleep(1)
        
        pygame.mixer.music.load(sound_2)
        print("Playing sound 2…")
        pygame.mixer.music.play()

        sound_loop = input("Play again (p or ENTER) or continue (c)? ")

        if sound_loop == "p" or sound_loop == "":
            continue
        elif sound_loop == "c":
            break
         
    print(f"Which do you prefer? {i+1}/{questions_len}")
    for a, match in enumerate(match_up):
        if DEBUG: print(f"debug: [{a+1}] {match}")
                                        # Don't really need to do this, because
                                        # it's fixed at two choices
        print(f"[{a+1}] Sound {a+1}")

    left_choice = match_up[0]
    right_choice = match_up[1]
    
    while True:
        try:
            user_choice = int(input(">> "))

            # Left choice is better, and must be placed on top
            if user_choice == 1:
                winner = left_choice
                loser = right_choice
            elif user_choice == 2:
                winner = right_choice
                loser = left_choice
            else:
                print("error: not a choice!")
                continue
        except Exception as e:
            print(f"error: {e}")
            print("You likely did not input a number. Do so!")
            continue
        
        break
    
    if winner in ordered_list and loser in ordered_list:    # If both already 
                                                            # exist
        # Check if the new position is higher or not
        winner_pos = ordered_list.index(winner)
        loser_pos = ordered_list.index(loser)

        if winner_pos > loser_pos - 1: # If winner is lower
            ordered_list.remove(winner)
            ordered_list.insert(ordered_list.index(loser), winner)
        # If loser is lower, do nothing
    elif winner in ordered_list:    # If only the winner exists
        ordered_list.append(loser) # Add to the very end
    elif loser in ordered_list:     # If only the loser exists
        ordered_list.insert(ordered_list.index(loser), winner)
    else:   # If neither exist
        ordered_list.append(winner)
        ordered_list.append(loser)

print("\nFinal rankings:")
for i, item in enumerate(ordered_list):
    print(f"#{i+1}: {item}")