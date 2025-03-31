n = int(input("Podaj cene zakupów: "))

if n > 100:
    k = n * 0.2
    print(f'Zniżka wynosi {k:.2f}, a całe zakupy będą kosztować {n - k:.2f}')
else:
    k = n * 0.1
    print(f'Zniżka wynosi {k:.2f}, a całe zakupy będą kosztować {n - k:.2f}')