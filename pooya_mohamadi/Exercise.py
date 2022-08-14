"""Write a python program to detect integer items in a list of string items,
 cast them into int, and print/return them out. """
print('===============================')
valid_characters = "0123456789"
lst = ["11", '122p17398479823749827349827', '101565pooya5132146', "pooya", '10.5', '17']
lst_2 = []
for lst_item in lst:
    for item_character in lst_item:
        if item_character not in valid_characters:
            lst_2.append(lst_item)
            break
for lst_item in lst:
    if lst_item not in lst_2:
        print(int(lst_item))
print('===============================')
"""Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing 
if any numbers that come after 237 in the sequence. Go to the editor Sample numbers list """
s = [386, 462, 47, 418, 907, 344, 236, 375, 823,
     566, 597, 978, 328, 615, 953, 345, 399, 162, 758,
     219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81,
     379, 843, 831, 445, 742, 717, 958, 743, 527]
for counter in s:
    if counter != 47:
        print(counter)
    if counter == 47:
        break
print('===============================')
"""Write a Python program to sum of two given integers.
 However, if the sum is between 15 to 20 it will return 20."""
num_1 = 3
num_2 = 5
while True:
    sum_1 = num_1 + num_2
    num_1 += 1
    num_2 += 2
    if 15 <= sum_1 <= 20:
        print(20)
    elif sum_1 > 40:
        break
    else:
        print(sum_1)
print('===============================')
"""Write a Python program to count the members of a list and print them"""
lst = [1, 5, 6, 1, 1, 's', 's', 'pooya']
find = []
for i in lst:
    count = 0
    if i not in find:
        find.append(i)
        for j in lst:
            if i == j:
                count += 1
        print(i, ">>>", count)
print('===============================')
"""Make a two-player Rock-Paper-Scissors game.
Ask players to play and get their stands by calling the input function two times(each time for each player),
compare the two inputs,
print out a message of congratulation to the winner,
and ask whether the players want to play a new round.
If player returns y or yes, it mean they want to play another round.
Otherwise, break the loop and exit the code with an appropriate goodbye message!"""
name_1 = input('please write your favorit name: ')
name_2 = input('please write your favorit name: ')
player_1 = input('Please select your choice: ')
player_2 = input('Please select your choice: ')
game =['sang','kaghaz' , 'gheichi']
count = 0
while True :
    if count == 1:
        m = input('You want the game over?y/n?')
    if m == 'y':
        print("Thank you for playing this game")
        break
    if player_1 not in game or player_2 not in game:
        raise ValueError(f"The choice should be among these options but your choice{game}")
    if player_1 == player_2:
        print('equal')
    if player_1 == 'sang' and player_2 == 'kaghaz':
        count += 1
        print(f'{name_1}  win')
    if player_1 == 'kaghaz' and player_2 == 'sang':
        count += 1
        print(f'{name_1}  win')
    if player_1 == 'gheichi' and player_2 == 'kaghaz' :
        print(f'{name_1} win')
    else:
        print(f'{name_2} win')
print('===============================')
""""Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence
 of numbers which the next number in the sequence is the sum of the previous two numbers to it. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)"""
number_of_elements = int(input('Enter how many elements of Fibonnaci you want: '))
lst = [1]
if number_of_elements == 1:
    print(lst)
else:
    for j in range(number_of_elements-1):
        if j == 0:
            lst.append(lst[j] + lst[j-1]-1)
        else:
            lst.append(lst[j] + lst[j-1])
    print(lst)
print('===============================')
""""Check a pre-defined password with user inputs for
 3 times; let them pass if they're correct with less than 3 tries.
  Inform the user of being blocked if they enter more password incorrectly more than 4 times"""
PASSWORD = "P@s$W0rd"
i = 1
while True:
    user_pass = input("insert your password:")
    if i == 3:
        print(' your blocked!I warned you:/')
        break
    if user_pass == PASSWORD :
        print('Hello, welcome home:) #Billie Eilish')
    if user_pass != PASSWORD :
        print('Please note that your password is wrong')
        i+=1
