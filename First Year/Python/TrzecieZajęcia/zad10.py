def is_palindrome(slo):
    if slo == slo[::-1]:
        return True
    else:
        return False

slo = str(input("Podaj slowo: "))
print(is_palindrome(slo))