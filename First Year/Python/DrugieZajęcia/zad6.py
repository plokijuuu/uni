wezly = float(input("Podaj siłę wiatru w węzłach: "))

if wezly < 1:
    print("Cisza")
elif 1 <= wezly <= 3:
    print("Zefir")
elif 4 <= wezly <= 27:
    print("Bryza")
elif 28 <= wezly <= 47:
    print("Wichura")
elif 48 <= wezly <= 63:
    print("Sztorm")
else:
    print("Huragan")