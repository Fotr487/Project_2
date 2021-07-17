import random
from timeit import default_timer as timer
from time import sleep
import os


def number_checking(player, computer):
    bulls = 0
    cows = 0
    repetition = dict()
    if len(player) == len(computer) and player.isdigit():
        if player[0] != "0":
            for position_p, letter_p in enumerate(player):
                if letter_p in repetition.keys():
                    repetition[letter_p] = repetition[letter_p] + 1
                    return print("SORRY YOUR NUMBER HAS DUPLICATES."
                                 " PLEASE INPUT NEW ONE.")
                else:
                    repetition[letter_p] = 1
                if letter_p in computer:
                    cows += 1
                    for position_c, letter_c in enumerate(computer):
                        if letter_p == letter_c and position_p == position_c:
                            bulls += 1
                            cows -= 1

            print(f"{bulls} BULLS, {cows} COWS")
        else:
            return print("""SORRY YOUR NUMBER STARTS WITH 0THAT IS WRONG.
PLEASE INPUT NEW ONE.""")
    else:
        if len(player) > len(computer) and player.isdigit():
            print(f"THERE ARE MORE NUMBERS IN YOU INPUT THAN "
                  f"THERE IS IN THE SECRET NUMBER. TRY AGAIN ...")
        elif len(player) < len(computer) and player.isdigit():
            print(f"THERE ARE LESS NUMBERS IN YOU INPUT THAN "
                  f"THERE IS IN THE SECRET NUMBER. TRY AGAIN ...")
        elif not player.isdigit():
            print("YOUR INPUT IS INVALID. (ONLY NUMBERS)")


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
question = input("DO YOU WANNA SEE THE SECRET WORD? 'YES' OR 'NO'\n")
if question.lower() == "yes":
    print(SECRET)
    sleep(1)
    os.system("cls")
else:
    os.system("cls")
print(f"""{SPACE}
HELLO THERE!
{SPACE}
I HAVE GENERATED A RANDOM {LENGHT} DIGIT NUMBER FOR YOU.""")
print(f"""LET'S PLAY A BULLS AND COWS GAME.
{SPACE}""")
start = timer()
while GAME_ON:
    player_in = input("ENTER A NUMBER: (IF YOU WANT TO QUIT, TYPE 'QUIT')\n")
    if player_in.lower() == "quit":
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
