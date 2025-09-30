import random
import time

def generate_three_digit(n):
    return [random.randint(100, 999) for _ in range(n)]

def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def replace_slice_with_digit_sum(data):
    modified = data.copy()
    start, end = -40, -20
    # Обработка случаев, когда список слишком короткий
    if len(modified) >= 40:
        modified[start:end] = [sum_of_digits(x) for x in data[start:end]]
    return modified

def insert_after_palindromes(data):
    result = []
    for x in data:
        result.append(x)
        if is_palindrome(x):
            result.append(1)
    return result

def add_second_and_second_last(data):
    if len(data) >= 2:
        return data + [data[1], data[-2]]
    return data

# Тестирование
print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ - ЗАДАНИЕ 2")
print("=" * 60)

n = 180
print(f"Тестирование для n = {n}")

# Генерация
start = time.perf_counter()
data = generate_three_digit(n)
gen_time = time.perf_counter() - start

# Замена среза
start = time.perf_counter()
modified_data = replace_slice_with_digit_sum(data)
slice_time = time.perf_counter() - start

# Вставка после палиндромов
start = time.perf_counter()
result_data = insert_after_palindromes(modified_data)
insert_time = time.perf_counter() - start

# Добавление элементов
start = time.perf_counter()
final_data = add_second_and_second_last(result_data)
add_time = time.perf_counter() - start

total_time = gen_time + slice_time + insert_time + add_time

print(f"Исходный список (первые 10): {data[:10]}")
print(f"После замены среза (первые 10): {modified_data[:10]}")
print(f"После вставки палиндромов (первые 10): {result_data[:10]}")
print(f"Финальный список (первые 10): {final_data[:10]}")
print(f"Длина исходного списка: {len(data)}")
print(f"Длина финального списка: {len(final_data)}")
print(f"Количество палиндромов: {sum(1 for x in data if is_palindrome(x))}")

print(f"\nВРЕМЯ ОПЕРАЦИЙ:")
print(f"Генерация: {gen_time:.6f} сек")
print(f"Замена среза: {slice_time:.6f} сек")
print(f"Вставка после палиндромов: {insert_time:.6f} сек")
print(f"Добавление элементов: {add_time:.6f} сек")
print(f"Общее время: {total_time:.6f} сек")

if total_time > 0:
    print(f"Соотношение: {gen_time/total_time:.2f}:{slice_time/total_time:.2f}:{insert_time/total_time:.2f}:{add_time/total_time:.2f}")
