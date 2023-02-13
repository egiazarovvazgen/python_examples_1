"""
Вы пользуетесь общественным транспортом? Вероятно, Вы расплачивались
за проезд и получали билет с номером. Счастливым билетом называют
такой билет с шестизначным номером, где сумма первых трёх цифр равна
сумме последних трёх. То есть билет с номером 385916 – счастливый,
так как 3 + 8 + 5 = 9 + 1 + 6. Вам требуется написать программу,
которая проверяет счастливость билета.
"""

number = [int(i) for i in input("Введите номер билета: ")]
print(["Ваш билет - обычный :(", "Ваш билет - счастливый!"][sum(number[:3]) == sum(number[3:])])