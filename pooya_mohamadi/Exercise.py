lst = ['11','10','10.5']
# lst_1 = []
for i in lst:
    try:
        i = int(i)
        print(i)
    except:
        pass

s = [386, 462, 47, 418, 907, 344, 236, 375, 823,
     566, 597, 978, 328, 615, 953, 345, 399, 162, 758,
     219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527 ]
for counter in s :
    if counter != 47:
        print(counter)
    if counter == 47:
        break
num_1 = 3
num_2 = 5
while True:
    sum_1 = num_1 + num_2
    num_1 += 1
    num_2 += 2
    if 15<=sum_1<=20:
        print(20)
    elif sum_1 > 40:
        break
    else:
        print (sum_1)


lst=[1,5,6,1,1,'s','s','pooya']
find=[]
for i in lst:
    count=0
    if i not in find:
        find.append(i)
        for j in lst:
            if i==j:
                count +=1
        print(i, ">>>", count)

