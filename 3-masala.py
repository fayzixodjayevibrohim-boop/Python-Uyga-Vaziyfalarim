import os
os.system("cls")

def almashtir(Son):
    return [(t[0], t[1], 100) for t in Son]

Son = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

print(almashtir(Son))