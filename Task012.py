# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# Пример:
# Ввод: 5 6 -> 2 3



first_flag = False
while not first_flag:
    first_num = int(input('Введите сумму чисел: '))
    if not (first_num > 2000 or first_num < 1):
        first_flag = True
second_flag = False
while not second_flag:
    second_num = int(input('Введите произведение чисел: '))
    if not (second_num > 1000000 or second_num < 1):
        second_flag = True

for i in range(first_num):
    for j in range(second_num):
        if first_num == i + j and second_num == i * j:
            print(i, j)
