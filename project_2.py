import random


def number_checking(player, computer):
    bulls = 0
    cows = 0
    for position_p, letter_p in enumerate(player):
        if letter_p in computer:
            cows += 1
            for position_c, letter_c in enumerate(computer):
                if letter_p == letter_c and position_p == position_c:
                   bulls += 1
                   cows -= 1
    print(f"{bulls} bulls, {cows} cows")


def beg_number(comp):
    print("SPECIALITIES OF THIS WORD:")
    if comp[0] == "0":
        print("THIS NUMBER STARTS WITH 0.")
    repetition = dict()
    for let in comp:
        if let in repetition.keys():
            repetition[let] = repetition[let] + 1
        else:
            repetition[let] = 1
    for one in repetition:
        if repetition.get(one) > 1:
            print(f"THERE ARE {repetition.get(one)} SAME NUMBERS.")


TRIES = 0
GAME_ON = True
LENGHT = random.randint(3, 5)
SPACE = '-' * 20
SECRET = ""
for number in range(1, LENGHT + 1):
    SECRET += str(random.randint(0, 9))

print(LENGHT)
print(SECRET)
print(f"""{SPACE}
HELLO THERE!
{SPACE}
I HAVE GENERATED A RANDOM {LENGHT} DIGIT NUMBER FOR YOU.""")
beg_number(SECRET)
print(f"""LET'S PLAY A BULLS AND COWS GAME.
{SPACE}""")

while GAME_ON:
    player_in = input("ENTER A NUMBER:\n")
    if player_in.isdigit():
        number_checking(player_in, SECRET)
        if player_in == SECRET:
            GAME_ON = False
    else:
        print("SORRY, ONLY NUMBERS. GOODBYE...")
        quit()
    TRIES += 1
print(f"NICE, YOU DID IT. YOU'VE GUESSED THE RIGHT NUMBER IN {TRIES} GUESSES!!")

if TRIES == 1:
    print("YOU ARE AMAZING")
elif TRIES < 4:
    print("THAT IS STILL GREAT")
else:
    print("WELL IT IS A HARD GAME")
