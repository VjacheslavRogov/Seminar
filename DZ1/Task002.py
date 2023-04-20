# Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input("Введите трехзначное число: "))
if num < 1000 and num > 99:
    first_num = num // 100
    second_num = num % 100 // 10
    third_num = num % 10
    sum = first_num + second_num + third_num
else:
    print('Введены некорректные данные')

print(sum)
