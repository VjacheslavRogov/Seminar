# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

def sum_digit_in_numbers(number):
    first_num = number // 100
    second_num = number % 100 // 10
    third_num = number % 10
    sum = first_num + second_num + third_num
    return sum

num = int(input("Введите шестизначное число: "))
if num < 1000000 and num > 99999:
    first_half_num = num // 1000
    second_half_num = num % 1000

    first_sum = sum_digit_in_numbers(first_half_num)
    second_sum = sum_digit_in_numbers(second_half_num)

    if first_sum == second_sum:
        print('YES')
    else:
        print('NO')
else:
    print('Введены неверные данные')