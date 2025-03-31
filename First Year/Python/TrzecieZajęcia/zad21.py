import random


listt = ["kot", "lody", "skuter", "czekolada"]
list1 = []
wisielec = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")
licz = 0

def litera(slo):
    global licz
    x = str(input("Podaj literę: "))
    if x in slo:
        for i in range(len(slo)):
            if slo[i] == x:
                list1.insert(i, x)
                list1.pop(i+1)
    else:
        print(f'{x} nie znajduje się w słowie')
        print(wisielec[licz])
        licz += 1
    print(list1)

def game():
    slowo = random.choice(listt)
    for i in range(len(slowo)):
        list1.append("_")
    print("Twoje słowo:")
    print(list1)
    while licz < 8:
        litera(slowo)
        if '_' not in list1:
            print("Gratulacje! Wygrana!")
            break
    if licz == 8:
        print("Przegrałeś!")

game()


