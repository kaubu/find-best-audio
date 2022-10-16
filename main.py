from itertools import combinations

example_list = [
    "Adam",
    "Steve",
    "Robert",
    "Sam",
    "Luke",
]
example_lista = [
    "o",
    "i",
    "u"
]
ordered_list = list()

sample_set = set(example_list)
list_combinations = list(combinations(sample_set, 2))

# print(list_combinations)

for match_up in list_combinations:
    print("\nWhich is better?")
    for i, match in enumerate(match_up):
        print(f"[{i+1}] {match}") # Don't really need to do this, because
                                        # it's fixed at two choices
    
    left_choice = match_up[0]
    right_choice = match_up[1]
    user_choice = int(input(">> "))

    if user_choice == 1: # Left choice is better, and must be placed on top
        winner = left_choice
        loser = right_choice
    elif user_choice == 2:
        winner = right_choice
        loser = left_choice
    else:
        print("ERROR: Not a choice!")
        quit()
    
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
        ordered_list.insert(ordered_list.index(winner)+1, loser)
    elif loser in ordered_list:     # If only the loser exists
        ordered_list.insert(ordered_list.index(loser), winner)
    else:   # If neither exist
        ordered_list.append(winner)
        ordered_list.append(loser)

print("\nFinal rankings:")
for i, item in enumerate(ordered_list):
    print(f"#{i+1}: {item}")