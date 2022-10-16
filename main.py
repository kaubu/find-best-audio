from itertools import combinations

lists = [
    ["Living Languages", [
        "English\t\tThe man went to the store to get some lettuce.",
        "Mandarin\t\t那人去商店买些生菜。(Nà rén qù shāngdiàn mǎi xiē shēngcài.)",
        "Hindi\t\tवह आदमी कुछ सलाद लेने के लिए दुकान पर गया। (vah aadamee kuchh salaad lene ke lie dukaan par gaya.)",
        "Spanish\t\tEl hombre fue a la tienda a comprar lechuga.",
        "French\t\tL'homme est allé au magasin pour acheter de la laitue.",
        "Arabic\t\tذهب الرجل إلى المتجر ليأخذ بعض الخس. (dhahab alrajul 'iilaa almatjar liakhudh baed alkhasa.)",
        "Russian\t\tМужчина пошел в магазин за салатом. (Muzhchina poshel v magazin za salatom.)",
        "Indonesian\t\tPria itu pergi ke toko untuk membeli selada.",
        "German\t\tDer Mann ging in den Laden, um Salat zu holen.",
        "Japanese\t\t男はレタスを買いに店に行った。(Otoko wa retasu o kai ni mise ni itta.)",
        "Korean\t\t그 남자는 상추를 사러 가게에 갔다. (geu namjaneun sangchuleul saleo gagee gassda.)",
        "Italian\t\tL'uomo è andato al negozio per prendere della lattuga.",
        "Polish\t\tMężczyzna poszedł do sklepu po sałatę.",
        "Dutch\t\tDe man ging naar de winkel om wat sla te halen.",
        "Greek\t\tΟ άντρας πήγε στο μαγαζί να πάρει λίγο μαρούλι. (O ántras píge sto magazí na párei lígo maroúli.)",
        "Danish\t\tManden gik til butikken for at hente noget salat.",
    ]],
    ["Ancient Languages", [
        "Ancient Greek\tἀγεωμέτρητος μηδεὶς εἰσίτω. (Ageōmétrētos mēdeìs eisítō.)",
        "Egyptian\t\t𓂧𓆓𓈖𓆑 𓈃𓈖 𓅬𓆑 𓇓𓏏𓆤𓏏 𓉐𓄣𓋴𓈖 (d(m)ḏ.n.f tꜣ-wj n zꜣ.f nsw.t-bj.t(j) pr-jb.sn(j))",
        "Latin\t\tNihil tam absurde dici potest, quod non dicatur ab aliquo philosophorum.",
        "Old English\t\tIc bidde þe mara slawlice to sprecanne",
        "Middle English\tSumer is icumen in, lhude sing, cuccu! Groweþ sed and bloweþ med, and springþ þe wde nu!",
        "Old Norse\t\tElds er þörf, þeims inn er kominn ok á kné kalinn;",
        "Sanskrit\t\tतथा परयाते शिबिरं दरॊणपुत्रे महारथे (tathā prayāte śibiraṃ droṇaputre mahārathe)",
        "Sumerian\t\t𒀭𒂗𒆤 𒈗 𒆳𒆳𒊏 𒀊𒁀 𒀭𒀭𒌷𒉈𒆤 (den-lil2 lugal kur-kur-ra ab-ba dig̃ir-dig̃ir-re2-ne-ke4)",
    ]],
    ["Conlangs", [
        "Esperanto",
        "Ido",
    ]],
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

selected_set = set(selected_list[1])
list_combinations = list(combinations(selected_set, 2))

RANDOMIZE = True # Randomize the questions
CLEAR_SCREEN = True # Clear screen after each question
DEBUG = True

if RANDOMIZE:
    from random import shuffle
    shuffle(list_combinations)

if CLEAR_SCREEN:
    import os

if DEBUG:
    for language in selected_list[1]:
        print(f"[00] {language}")
    input("Continue?")

# print(list_combinations)

questions_len = len(list_combinations)

for i, match_up in enumerate(list_combinations):
    if CLEAR_SCREEN:
        os.system("cls" if os.name == "nt" else "clear")
    
    if DEBUG and i != 0:
        print("Current DEBUG ranking:")
        for i, item in enumerate(ordered_list):
            print(f"#{i+1}: {item}")
        print()

    print(f"Which do you prefer? {i+1}/{questions_len}")
    for i, match in enumerate(match_up):
        print(f"[{i+1}] {match}") # Don't really need to do this, because
                                        # it's fixed at two choices
    
    left_choice = match_up[0]
    right_choice = match_up[1]
    
    while True:
        try:
            user_choice = int(input(">> "))

            if user_choice == 1: # Left choice is better, and must be placed on top
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
        # ordered_list.insert(ordered_list.index(winner)+1, loser)
        ordered_list.append(loser) # Add to the very end
    elif loser in ordered_list:     # If only the loser exists
        ordered_list.insert(ordered_list.index(loser), winner)
    else:   # If neither exist
        ordered_list.append(winner)
        ordered_list.append(loser)

print("\nFinal rankings:")
for i, item in enumerate(ordered_list):
    print(f"#{i+1}: {item}")