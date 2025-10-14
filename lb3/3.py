import random
import time
import matplotlib.pyplot as plt

def generate_matrix(n: int):
    return [[random.randint(-20, 20) for _ in range(n)] for _ in range(n)]

def process_matrix(matrix):
    n = len(matrix)
    avg_val = sum(sum(row) for row in matrix) / (n * n)
    start = time.perf_counter()
    processed = [["avg" if x >= avg_val else 0 for x in row] for row in matrix]
    elapsed = time.perf_counter() - start
    flat = [el for row in processed for el in row]
    avg_count = flat.count("avg")
    return avg_val, elapsed, avg_count

def benchmark():
    print("\n=== Задание 3. Вложенные генераторы списков ===")
    sizes = [10, 50, 100, 200]
    results = []
    for n in sizes:
        m = generate_matrix(n)
        avg_val, elapsed, avg_count = process_matrix(m)
        results.append((n, avg_val, elapsed, avg_count))
        print(f"{n}x{n} | среднее={avg_val:.4f} | время={elapsed:.6f}s | 'avg'={avg_count}")
        if n == 10:
            print("\nПример обработанной матрицы (первые 4 строки):")
            for row in [["avg" if x >= avg_val else 0 for x in m[i]] for i in range(4)]:
                print(row)

    # График зависимости времени от n²
    x = [r[0] for r in results]
    y = [r[2] for r in results]
    plt.plot(x, y, marker="o")
    plt.xlabel("Размер матрицы (n)")
    plt.ylabel("Время (сек)")
    plt.title("Сложность O(n²)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    benchmark()
