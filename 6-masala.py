import os
os.system("cls")

def qoshish(lst, s):
    return [s + str(i) for i in lst]

lst = [1,2,3,4]
s = input("String kiriting: ")

print(qoshish(lst, s))
