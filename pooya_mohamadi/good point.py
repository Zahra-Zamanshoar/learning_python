a = 1
b = [1, 2, 3, 6, 5]
print('the result of "a in b" is {}'.format(a in b))
print('the result of a not in b is {}'.format(a not in b))
a = None
b = (1,2,3,6,5)
print('the result of "a is b" is {}'.format(a is b))
print('the result of "a is not b" is {}'.format(a is not b))
a = 10
print('a: ',a)
nephews = ["Huey", "Dewey", "Louie"]
nephews.append('May Duck')
print(nephews)
nephews.extend(['May Duck','June Duck'])
print(nephews)
nephews.append(['May Duck','June Duck'])
print(nephews)
nephews.insert(0,'Scrooge McDuck')
print(nephews)
nephews[-3:] = ['4']
print(nephews)
nephews.pop(0)
print(nephews)
print("============")
#if 0:
    #print('impossible :(')
#else:
    #print('zero means False')
if -0.00000000000001:
    print('wow')
if None:
    print('impossible :(')
else:
    print('None means False')
empty_lst = []
if empty_lst:
    print('impossible :(')
else:
    print('empty means False')
lst = [1,2,3]
if len(lst) != 0: # not recommended
    print(lst[0])
lst = [1,2,3]
if lst: # recommended
    print(lst[0])
print("============")
a_tuple= (10,)
#type(a_tuple) == tuple
#a_tuple= 10,
#type(a_tuple) == tuple
#a = set([1,2,3])
print(a)
capitals = {'Iran': 'Tehran',
            'France': 'Paris',
            'Italy': 'Rome'}
more_capitals = {'Germany': 'Berlin','United Kingdom': 'London'}
capitals.update(more_capitals)
print(capitals)
# how access keys
capitals.keys()
# how to access both
capitals.items()