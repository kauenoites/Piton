def primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num %2 == 0 or num %3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num %(i+2) == 0:
            return False
        i += 6
    return True

num = int(input("Digite um número: "))
if primo(num):
    print(f"{num} é um numero primo. ")
else:
    print(f"{num} não é um número primo. ")