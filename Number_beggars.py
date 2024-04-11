def distribute_beggar_money(numbers, n):
    result = [0] * n
    for i, number in enumerate(numbers):
        result[i % n] += number
    return result

numbers_input = input().strip()
n = int(input().strip())
numbers = list(map(int, numbers_input.split("[, ]")))
print(*distribute_beggar_money(numbers, n))
