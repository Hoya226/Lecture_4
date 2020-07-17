list_a = [10, 20, 30]
list_b = [10, 20, 30]

if list_a is list_b:
    print('list_a is list_b')

else:
    print('list_a is not list_b')


print('list_a 는{}'.format(id(list_a)))
print('list_b 는{}'.format(id(list_b)))


num_a = {"a":1, "b":1}
num_b = {"a":1, "b":1}
if num_a is num_b:
    print('num_a is num_b')

else:
    print('num_a is not num_b')



num_a = (1, 2, 3)
num_b = (1, 2, 3)
if num_a is not num_b:
    print('num_a is num_b')

else:
    print('num_a is not num_b')



#if 3 is not 3:
 #   print('list_a is list_b')

#else:
 #   print('list_a is not list_b')



#if list_a == list_b:
 #   print('list_a is list_b')

#else:
 #   print('list_a is not list_b')