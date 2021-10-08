'''
def switcher(argument):
    switcher  ={"Yes":"Thanks Mate, Its honorary",
                'yes':"Thanks Mate, Its honorary",'Y':'I Am Glad you liked it','y':'I Am Glad you liked it',
                'No':input('Sorry, Please Suggest Modification:\n'),
                'no':input('Sorry, Please Suggest Modification:\n'),'n':input('Sorry, Please Suggest Modification:\n'),
                'N':input('Sorry, Please Suggest Modification:\n')}
    print(switcher.get(argument,"Sorry I Can't understand"))

print("is it working?")
n =  input("Yes/No:\n")
switcher(n)'''

print("Its under maintainance\nHappy Coding")