#lst = ['11', 'pooya', '10', '10.5']
#s = [str(i) for i in lst]
#while True:
   # res = int(''.join(s))
    #if res == 10.5 :
       # continue
   # print(res)
s = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527 ]
for counter in s :
    if s != 237:
        print(counter)
    if s == 237:
        break
num_1 = 3
num_2 = 5
while True:
    sum = num_1 + num_2
    print(sum)
    num_1 +=1
    num_2 +=2
    if 15<=sum<=20:
        print (20)
    elif sum > 40:
        break

example = [1,5,6,1,1,'s','s','pooya']
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
for i in example:
    if i == example[0]:
        count_1 +=1
    elif i == example[2]:
        count_2 +=1
    elif i == example[3]:
        count_3 +=1
    elif i == example[4]:
        count_4 +=1
print(f" { example[1]} >>>>>>>>>>>>  {count_1}")
print(f"{ example[2] } >>>>>>>>>>>>  {count_2}")
print(f"{ example[3] }>>>>>>>>>>>>>  {count_3}")
print(f"{ example[4]} >>>>>>>>>>> {count_4}")