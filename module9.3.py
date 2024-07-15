first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (abs(len(f) - len(x)) for f, x in zip(first, second) if len(f) != len(x))
second_result = (first[i] == second[i] for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))