import os
os.system("cls")

matn = input("Matn kiriting: ")

natija = tuple(i for i in matn if i != " ")

print(natija)