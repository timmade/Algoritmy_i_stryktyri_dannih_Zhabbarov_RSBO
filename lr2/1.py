import random
import time

def generate_list(n):
    return [random.randint(1, 100) for _ in range(n)]

def remove_ending_with_7(data):
    return [x for x in data if x % 10 != 7]

def multiply_odd_positions(data):
    modified = data.copy()
    for i in range(1, len(modified), 2):
        modified[i] *= 10
    return modified

def find_minimum(data):
    return min(data) if data else None

# Тестирование
sizes = [1000, 10000, 100000]
print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ - ЗАДАНИЕ 1")
print("=" * 60)

for n in sizes:
    print(f"\n{'=' * 50}")
    print(f"Тестирование для n = {n}")
    print(f"{'=' * 50}")

    start_total = time.perf_counter()

    # Генерация
    start = time.perf_counter()
    original_data = generate_list(n)
    gen_time = time.perf_counter() - start

    # Удаление чисел, оканчивающихся на 7
    start = time.perf_counter()
    filtered_data = remove_ending_with_7(original_data)
    filter_time = time.perf_counter() - start

    # Умножение на нечётных позициях
    start = time.perf_counter()
    modified_data = multiply_odd_positions(filtered_data)
    multiply_time = time.perf_counter() - start

    # Поиск минимума
    start = time.perf_counter()
    min_val = find_minimum(modified_data)
    min_time = time.perf_counter() - start

    total_time = time.perf_counter() - start_total

    # Вывод результатов
    print(f"1. Генерация списка: {gen_time:.6f} сек")
    print(f"   Первые 5 элементов: {original_data[:5]}")
    print(f"2. Удаление чисел, оканчивающихся на 7: {filter_time:.6f} сек")
    print(f"   Удалено элементов: {len(original_data) - len(filtered_data)}")
    print(f"   Первые 5 после фильтрации: {filtered_data[:5]}")
    print(f"3. Умножение на нечётных позициях: {multiply_time:.6f} сек")
    print(f"   Первые 5 после умножения: {modified_data[:5]}")
    print(f"4. Поиск минимума: {min_time:.6f} сек")
    print(f"   Минимальное значение: {min_val}")
    print(f"Общее время: {total_time:.6f} сек")

    # Проверка деления на ноль
    if total_time > 0:
        ratio_str = f"{gen_time / total_time:.2f}:{filter_time / total_time:.2f}:{multiply_time / total_time:.2f}:{min_time / total_time:.2f}"
    else:
        ratio_str = "N/A (время слишком мало)"

    print(f"Соотношение времён: {ratio_str}")
