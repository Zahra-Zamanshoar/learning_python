counter = 100
name = 'zahra'
hight = '185.0'
print(counter)
print(name)
print(hight)
a = b = c = 1
print(a,b,c)
a, b, c = 1,2,'zahra'
print(a,b,c)
a = 10
b = 20
a , b = b, a
print(a,b)
var = 'Hello World! '
print(var)
print(var*2)
print(var + var +"2")
print(len(var))
print(var[2])
print(var[:2])
print(var[2:])
print(var[2:5])
print(var[-1])
print(var[2:5:2])
print(var[::-1])
print(var[:5] + "-"+var[5:])
student_grade = 19
ssn = 10
print("student grade is {}".format(student_grade))
print("student grade is {0} ssn got is {1}".format(student_grade,ssn))
print("student grade is {} ssn got is {}".format(student_grade,ssn))
print(f"student grade is {student_grade}, ssn got is {ssn}")
first_name,last_name = 'zahra','zamani'
print(f'my first name is {first_name}, my last name is {last_name}')
nephews = ['zahra','fatemeh','kosar']
print(nephews.index('zahra'))
nephews.append('1')
print(nephews)
nephews.extend(['soudabeh',1,'mehdi'])
print(nephews)
nephews.insert(1,"2")
print(nephews)
list = []
if len(list) == 0:
    print("no")
