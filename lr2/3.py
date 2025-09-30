import random
import time

def generate_matrix(rows, cols):
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

def extract_first_elements(matrix):
    return [row[0] for row in matrix if row]  # Проверка на пустые строки

def multiply_by_row_length(matrix, first_elems):
    return [elem * len(row) for elem, row in zip(first_elems, matrix)]

def test_matrix_operations(size):
    rows = cols = size
    print(f"\n{'=' * 50}")
    print(f"Тестирование для матрицы {size}x{size}")
    print(f"{'=' * 50}")

    # Генерация матрицы
    start = time.perf_counter()
    matrix = generate_matrix(rows, cols)
    gen_time = time.perf_counter() - start

    # Извлечение первых элементов
    start = time.perf_counter()
    first_elems = extract_first_elements(matrix)
    extract_time = time.perf_counter() - start

    # Умножение на длину строки
    start = time.perf_counter()
    result = multiply_by_row_length(matrix, first_elems)
    multiply_time = time.perf_counter() - start

    total_time = gen_time + extract_time + multiply_time

    print(f"Размер матрицы: {len(matrix)}x{len(matrix[0]) if matrix else 0}")
    print(f"Первые 3 строки матрицы:")
    for i in range(min(3, len(matrix))):
        print(f"  Строка {i}: {matrix[i][:5]}...")
    print(f"Первые элементы строк: {first_elems[:5]}...")
    print(f"Результат умножения: {result[:5]}...")

    print(f"\nВРЕМЯ ОПЕРАЦИЙ:")
    print(f"Генерация матрицы: {gen_time:.6f} сек")
    print(f"Извлечение первых элементов: {extract_time:.6f} сек")
    print(f"Умножение на длину строки: {multiply_time:.6f} сек")
    print(f"Общее время: {total_time:.6f} сек")

    if total_time > 0:
        print(
            f"Соотношение: {gen_time / total_time:.2f}:{extract_time / total_time:.2f}:{multiply_time / total_time:.2f}")

    return gen_time, extract_time, multiply_time, total_time


# Тестирование на разных размерах
print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ - ЗАДАНИЕ 3")
print("=" * 60)

sizes = [100, 300, 500]
results = []

for size in sizes:
    gen_time, extract_time, multiply_time, total_time = test_matrix_operations(size)
    results.append((size, gen_time, extract_time, multiply_time, total_time))

# Сводная таблица
print(f"\n{'=' * 80}")
print(
    f"{'Размер':<10} | {'Генерация':<12} | {'Извлечение':<12} | {'Умножение':<12} | {'Общее время':<12} | {'Соотношение'}")
print(f"{'-' * 80}")
for size, gen_time, extract_time, multiply_time, total_time in results:
    if total_time > 0:
        ratio = f"{gen_time / total_time:.1f}:{extract_time / total_time:.1f}:{multiply_time / total_time:.1f}"
    else:
        ratio = "N/A"
    print(
        f"{size:<10} | {gen_time:<12.6f} | {extract_time:<12.6f} | {multiply_time:<12.6f} | {total_time:<12.6f} | {ratio}")
