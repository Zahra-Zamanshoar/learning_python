##First_task
"""The code guesses the number entered by the user """
ansewr = int(input("\"player1: please choice a number (1-19): \""))
if ansewr not in range(19):
    raise ValueError(f'your number should be 1-19 but your number is {ansewr} ')
is_correct = False
try_player2 = 0
print("===============")

while try_player2 < 5 and is_correct is False:
    guess = int(input("\" please guess\""))
    print("===============")
    if guess == ansewr:
        print("\"you win!\"")
        print("===============")
        is_correct = True
    elif guess > ansewr:
        print("\"your guess is greater than the answer\"")
        print("===============")
        try_player2 += 1
    elif guess < ansewr:
        print("\"your guess is smaller than the answer\"")
        print("===============")
        try_player2 += 1

if not is_correct:
    print("\"You loser!\"")
