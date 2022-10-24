count = 0
while count < 10 :
    print(count)
    count += 1
print("End")
print("============")
name = 'zahra zamani'
for i in name:
    print(i)
print("============")
lst = ['pooya','menoo','golsa']
for _ in lst:
    print(lst)

lst_1 = [1,2,3,4]
lst_2 = [5,6,7,8]
res = []
n = 0
for i in lst_1:
   res.append(i + lst_2[lst_1.index(i)])
print(res)
