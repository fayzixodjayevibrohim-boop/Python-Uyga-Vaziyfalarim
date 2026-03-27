import os
os.system("cls")

a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

sonlar = [i for i in range(a, b+1) if i % 2 == 0]

print("sonlar =", sonlar)