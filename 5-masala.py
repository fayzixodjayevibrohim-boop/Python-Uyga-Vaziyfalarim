import os
os.system("cls")

lst = [ [1,2,3], [4,5,6], [10,11,12], [7,8,9] ]

eng_katta = lst[0]
eng_katta_sum = sum(lst[0])

for i in lst:
    s = 0
    for j in i:
        s += j
    
    if s > eng_katta_sum:
        eng_katta_sum = s
        eng_katta = i

print(eng_katta)