def zlicz(list):
    slo = {}
    for i in list:
        if i in slo:
            slo[i] += 1
        else:
            slo[i] = 1
    return slo

def wyswietl(slownik):
    for i in slownik:
        print(f"[{i}]: {slownik[i]}")

ekw = ["kot","pies","kot","chipsy","chipsy","cukierek","kot","pies","kot"]
wyswietl(zlicz(ekw))
