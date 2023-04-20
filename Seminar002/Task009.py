# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N)
# 0! = 1 Решить задачу используя цикл while


number = int(input('Введите число n: '))
count = 2
result = 1
while count <= number:
    result = result * count
    count += 1
print(result)
