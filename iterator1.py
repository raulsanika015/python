mylist=[10, 20, 30, 40]

my_iter = iter(mylist)
print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())
print(next(my_iter))
