from functools import reduce
# a = lambda x: "even" if x%2==0 else "odd"
# print(a(5))

# add = lambda a,b,c:a+b+c
# print(add(8,6,5))


# divisor = lambda x:x
# def divide(divident):
#     return divident/divisor(6)
# divide(10)
# print(divide(5))

# def loud(func):
#     return func.upper()
# def quite(func):
#     return func.lower()
# talk = lambda word:word
# print(loud(talk("raj")))


num = [1,2,3,4,5,6,7,8,9,10]
even_num = list(filter(lambda x:x%2==0,num))
new_list = list(map(lambda x:x+10,even_num))
sum_of_list = reduce(lambda a,b:a+b,new_list)

print(even_num)
print(new_list)
print(sum_of_list)

