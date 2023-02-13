# Найдите сумму цифр трёхзначного числа

number = int(input("Введите трёхзначное число: "))
thirdDigit = number % 10
secondDigit = number % 100 // 10
firstDigit = number // 100
print("Сумма цифр трёхзначного числа: ", firstDigit + secondDigit + thirdDigit)
