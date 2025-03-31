def order_tshirt(size, color, text):
    print(f'Rozmiar {size} kolor {color} i napis {text}')

a = str(input("Podaj rozmiar: "))
b = str(input("Podaj kolor: "))
c = str(input("Podaj napis: "))

order_tshirt(a,b,c)
order_tshirt(size='S', color='biały', text='czarny')


