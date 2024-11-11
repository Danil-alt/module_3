def print_params(a=1, b="строка", c=True):
    print(a, b, c)


#print_params()
#print_params(123, 'wieiuwc', 123)
#print_params(b=23)
#print_params(c=[1,2,3,4])
values_list = [1, True, (1,2,3,)]
values_dict = {'a':False, 'b':324, 'c':'1234'}

print_params(*values_list)
print_params(**values_dict)

values_list2 = ['qwe',123]
print_params(*values_list2)