import random
from timeit import default_timer as timer


def number_checking(player, computer):
    bulls = 0
    cows = 0
    if len(player) == len(computer) and player.isdigit():
        for position_p, letter_p in enumerate(player):
            if letter_p in computer:
                cows += 1
                for position_c, letter_c in enumerate(computer):
                    if letter_p == letter_c and position_p == position_c:
                        bulls += 1
                        cows -= 1

        print(f"{bulls} BULLS, {cows} COWS")
    else:
        if len(player) > len(computer) and player.isdigit():
            print(f"THERE ARE MORE NUMBERS IN YOU INPUT THAN THERE IS IN THE SECRET NUMBER."
                  f"TRY AGAIN ...")
        elif len(player) < len(computer) and player.isdigit():
            print(f"THERE ARE LESS NUMBERS IN YOU INPUT THAN THERE IS IN THE SECRET NUMBER."
                  f"TRY AGAIN ...")
        elif not player.isdigit():
            print("YOUR INPUT IS INVALID. (ONLY NUMBERS)")


def beg_number(comp):   # tady jsem si jaksi vymyslel funkci, ktera mela radit hraci (je mi líto jí smazat)
    dig_not = 0
    print("SPECIALITIES OF THIS WORD:")
    if comp[0] == "0":
        print("THIS NUMBER STARTS WITH 0.")
    repetition = dict()
    for let in comp:
        if not let.isdigit():
            dig_not += 1
        if let in repetition.keys():
            repetition[let] = repetition[let] + 1
        else:
            repetition[let] = 1
    if dig_not > 0:
        print(f"THERE IS/ARE {dig_not} NOT-DIGIT CHARACTER/S")
    for one in repetition:
        if repetition.get(one) > 1:
            print(f"THERE ARE {repetition.get(one)} SAME NUMBERS.")


def number_making():
    setcret = set()
    secret = []
    while len(setcret) != 4:
        setcret.add(str(random.randint(0, 9)))
    for prvek in setcret:
        secret += prvek
    if secret[0] == "0":
        secret.reverse()
        secret = "".join(secret)
        return secret
    else:
        secret = "".join(secret)
        return secret


TRIES = 0
GAME_ON = True
SPACE = '-' * 50
LENGHT = 4  # tady by šel random generator at nemame jenom 4-mistna cisla
SECRET = number_making()
#
print(f"PSST IT IS {SECRET}")
print(f"""{SPACE}
HELLO THERE!
{SPACE}
I HAVE GENERATED A RANDOM {LENGHT} DIGIT NUMBER FOR YOU.""")
beg_number(SECRET)
print(f"""LET'S PLAY A BULLS AND COWS GAME.
{SPACE}""")
start = timer()
while GAME_ON:
    player_in = input("ENTER A NUMBER: (IF YOU WANT TO QUIT, TYPE 'QUIT')\n")
    if player_in == "QUIT":
        print(f"WELL SEE YOU NEXT TIME. THE NUMBER WAS {SECRET}")
        quit()
    else:
        number_checking(player_in, SECRET)
        if player_in == SECRET:
            GAME_ON = False
    TRIES += 1
    print(SPACE)
end = timer()
overall = end - start
print(f"""NICE, YOU DID IT. YOU'VE GUESSED THE RIGHT NUMBER IN {TRIES} GUESSES!!
AND IT TOOK YOU {overall} seconds.""")

if TRIES == 1 or overall < 20:
    print("YOU ARE AMAZING")
elif TRIES < 4:
    print("THAT IS STILL GREAT")
else:
    print("WELL IT IS A HARD GAME")
