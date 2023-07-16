def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')
user = int(input("Number:"))

DecimalToBinary(user)

