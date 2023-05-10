# ["ä"], ["sounds/vowels/ä_Open_central_unrounded_vowel.ogg"],
# ["ä"], ["sounds/vowels/ä_Open_central_unrounded_vowel.ogg"],
# ["ä"], ["sounds/vowels/ä_Open_central_unrounded_vowel.ogg"],

import os

VOWEL_DIR = "./sounds/vowels/"

CURRENT_DIR = VOWEL_DIR

for item in os.listdir(CURRENT_DIR):
    # print(f"[\"{item[0]}\"], [\"./sounds/vowels/{item}\"],") # First list
    # print(f"[\"{item[0]}\", \"./sounds/vowels/{item}\"],") # Second list
    # print(f"\"{item[0]}\": \"./sounds/vowels/{item}\",") # Dictionary
    # print(f"\"{item[0]}\": \"\\\\sounds\\\\vowels\\\\{item}\",") # Dictionary with os file path
    print(f"\"{item.split('_')[0]}\": \".\\\\sounds\\\\vowels\\\\{item}\",") # Dictionary with relative os file path