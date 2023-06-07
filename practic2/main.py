a = 3


def my_func():
    global a
    a = a + 1
my_func()
i = 0
while i < 3:
    my_func() 
    i = i + 1
print(a)
 





my_list = [1, 2, '3', 'mylist', a]
for a in my_list:
    print(a)