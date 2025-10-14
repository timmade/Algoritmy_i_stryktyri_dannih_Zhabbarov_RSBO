import random
import time

def process_numbers(n: int):
    """Генерация списка и замена отрицательных значений на удвоенные."""
    nums = [random.randint(-40, 40) for _ in range(n)]
    start = time.perf_counter()
    for i, val in enumerate(nums):
        if val < 0:
            nums[i] = val * 2
    t_process = time.perf_counter() - start
    return nums, t_process

def iterator_example(nums, count=6):
    """Извлекает первые элементы через next()."""
    it = iter(nums)
    extracted = []
    start = time.perf_counter()
    for _ in range(count):
        try:
            extracted.append(next(it))
        except StopIteration:
            break
    t_iter = time.perf_counter() - start
    return extracted, t_iter

def string_processing():
    """Работа со строками."""
    strings = ["car", "bike", "train", "plane"]
    tuples = list(enumerate(strings))
    it = iter(tuples)
    extracted = [t for t in it if t[1].endswith("e")]
    return tuples, extracted

def benchmark():
    print("=== Задание 1. Итераторы ===")
    for n in [40, 400, 4000]:
        nums, t_proc = process_numbers(n)
        extracted, t_iter = iterator_example(nums)
        print(f"Размер: {n:<5} | Обработка: {t_proc:.6f}s | Итерация: {t_iter:.6f}s | Всего: {t_proc + t_iter:.6f}s")
        if n == 40:
            print("Пример списка (первые 10 элементов):", nums[:10])
            print("Извлечённые первые 6 элементов:", extracted)
    tuples, filtered = string_processing()
    print("\nКортежи:", tuples)
    print("Строки, оканчивающиеся на 'e':", filtered)

if __name__ == "__main__":
    benchmark()
