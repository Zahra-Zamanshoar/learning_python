lst = ['zahra','fatemeh',1,2]
for i in range(len(lst)):
    print(lst[i])
lst_1 = [1,2,3,4]
lst_2 = [5,6,7,8]
for i in range(len(lst_1)):
    print(lst_1[i] + lst_2[i])
counter = 0
while True:
    print(counter)
    counter += 1
    if counter >= 10:
        break
print('End')

for counter in range(10):
     if counter == 5:
        continue
     print(counter)
for _ in range(3):
    for counter in range(10):
        if counter == 5:
            continue
        print(counter)