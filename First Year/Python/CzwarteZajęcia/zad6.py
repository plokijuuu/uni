def nawiasy(ciag):
    slo = {'}':'{',']':'[',')':'(','>':'<'}
    listt = []
    for i in ciag:
        if i in "{[(<":
            listt.append(i)
        else:
            if listt and slo[i] == listt[-1] :
                listt.pop()
            else:
                return False
    if not listt:
        return True

    return False

print(nawiasy("{{{{[[<>]]}}}}"))
