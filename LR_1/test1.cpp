#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

void countEvenOdd(const std::vector<int>& arr, int& even, int& odd) {
    even = 0;
    odd = 0;
    for (size_t i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0) {
            even++;
        } else {
            odd++;
        }
    }
}

int main() {
    srand(time(0));
    int sizes[] = {1000000, 10000000, 100000000};
    int numSizes = 3;

    for (int i = 0; i < numSizes; i++) {
        int size = sizes[i];
        std::vector<int> arr(size);
        for (int j = 0; j < size; j++) {
            arr[j] = rand() % 100000 + 1;
        }

        int even, odd;
        clock_t start = clock();
        countEvenOdd(arr, even, odd);
        clock_t end = clock();
        double duration = double(end - start) / CLOCKS_PER_SEC;

        std::cout << "Размер списка: " << size << std::endl;
        std::cout << "  Четные: " << even << ", Нечетные: " << odd << std::endl;
        std::cout << "  Время выполнения: " << duration << " сек" << std::endl;
        std::cout << "  Сложность: O(n)" << std::endl;
        std::cout << "-----------------------------------" << std::endl;
    }

    return 0;
}