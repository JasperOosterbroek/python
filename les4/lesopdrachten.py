# def hello(name):
#     if type(name) == str:
#
#         return 'Welcome, '+ name +', to the world of python'
#     else:
#         return 'ingevoerde waarde is geen string'
#
#
# inputname = input('Vul je naam in: ')
# print(hello(inputname))

# def rng(lst):
#     return   max(lst) - min(lst)
#
# print(rng([4,0,2,-2]))
def swapFS(list):
    if len(list) > 1:
        list[0],list[1] = list[1],list[0]

mylist = ['one','two','three']
print(mylist)