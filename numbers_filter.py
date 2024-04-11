n = int(input())
numbers = [int(input()) for _ in range(n)]

command = input()

if command == "even":
    result = [x for x in numbers if x % 2 == 0]
elif command == "odd":
    result = [x for x in numbers if x % 2 != 0]
elif command == "negative":
    result = [x for x in numbers if x < 0]
elif command == "positive":
    result = [x for x in numbers if x >= 0]
else:
    result = "Invalid command"

print(result)
