import random
import time
import matplotlib.pyplot as plt

def process_list(n: int):
    nums = [random.randint(-80, 80) for _ in range(n)]
    start_f = time.perf_counter()
    divisible = [x for x in nums if x % 7 == 0]
    t_filter = time.perf_counter() - start_f

    start_r = time.perf_counter()
    replaced = ["even" if x % 2 == 0 else "odd" for x in divisible]
    t_replace = time.perf_counter() - start_r
    return len(divisible), t_filter, t_replace

def benchmark():
    print("\n=== Задание 2. Генераторы списков ===")
    results = []
    for n in [100, 1000, 10000, 100000]:
        count, tf, tr = process_list(n)
        results.append((n, tf, tr, count))
        print(f"n={n:<7} | фильтр={tf:.6f}s | замена={tr:.6f}s | найдено {count} элементов")

    # График (можно закомментировать, если запускаешь без GUI)
    x = [r[0] for r in results]
    y1 = [r[1] for r in results]
    y2 = [r[2] for r in results]
    plt.plot(x, y1, label="Фильтрация")
    plt.plot(x, y2, label="Замена")
    plt.xlabel("Размер списка (n)")
    plt.ylabel("Время (сек)")
    plt.title("Анализ сложности O(n)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    benchmark()
