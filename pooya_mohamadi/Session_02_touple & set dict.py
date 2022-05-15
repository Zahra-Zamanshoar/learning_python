tuple_ = ( (1, 2), 'abcd', 786 , 2.23, 'zahra', 70.2  )
tiny_tuple = (123, 'zahra')

print(tuple_)
print(tuple_[0])
print(tuple_[1:3])
print(tuple_[2:])
print(tiny_tuple * 2)
print(tuple_ + tiny_tuple)
print(len(tuple_))

set_ = {'Ali', 45, 5, 5, 5, 5, 15}
tiny_set = {'Ahmad', 45}
print(set_)
print('Ali' in set_)
print(set_ | tiny_set)
print(set_ ^ tiny_set)
print(set_ > tiny_set)
print(set_ < tiny_set)
print(set_ & tiny_set)
print(set_ - tiny_set)
print(len(set_))
print(set_ | tiny_set)
capitals = {'Iran': 'Tehran',
            'France': 'Paris',
            'Italy': 'Rome'}
more_capitals = {'Germany': 'Berlin','United Kingdom': 'London'}
capitals.update(more_capitals)
print(capitals)