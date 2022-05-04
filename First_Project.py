ansewr =int(input("\"player1: please choice a number (1-19): \"" ))
is_correct = False
try_player2 = 0
print("===============")

while try_player2 <5 and is_correct == False:
    guess = int(input("\" please guess\""))
    print("===============")
    if guess == ansewr:
        print("\"you won!\"")
        print("===============")
        is_correct = True
    elif guess > ansewr:
        print("\"your guess is greater than the answer\"")
        print("===============")
        try_player2+=1
    elif guess < ansewr:
        print("\"your guess is smaller than the answer\"")
        print("===============")
        try_player2 += 1

if is_correct== False:
    print("\"You loser!\"")





