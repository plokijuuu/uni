def order_tshirt(size, color, text):
    if size == 'domyślny':
        size = 'M'
    if color == 'domyślny':
        color = 'czarny'
    if text == 'domyślny':
        text = "Uwielbiam Pythona"
    print(f'Rozmiar {size} kolor {color} i napis {text}')


order_tshirt(size='L', color='czarny', text='domyślny')
order_tshirt(size='domyślny', color='czerwony', text='domyślny')
