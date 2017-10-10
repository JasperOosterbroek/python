# try:
#     strAge = input('Enter your name: ')
#     intAge = int(strAge)
#     print('You are {} years old.'.format(intAge))
# except ValueError:
#     print('De ingevoerde waarde is geen getal')
# except:
#     print('Er is iets fout gegaan probeer het opnieuw')

def dictionary_manipulation(my_dictionary, string,number):
    try:
        my_dictionary[string] = 2* number
        print(type(my_dictionary[string]))
    except(ValueError, KeyError):
        print("ERROR")
    else:
        my_dictionary[number] = 2 * string
    finally:
        print(my_dictionary)

dictionary_manipulation({'first':1,"second":2},"last", 8)