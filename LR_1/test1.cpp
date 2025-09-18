#include <iostream>
#include <vector>
#include <cstdlib> 
#include <ctime>
#include <chrono>

int last_occurrence(const std::vector<int>& arr, int target) {
    for (int i = static_cast<int>(arr.size()) - 1; i >= 0; --i) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1; 
}

std::vector<int> generate_random_list(int n, int min_val = 0, int max_val = 100) {
    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        arr[i] = min_val + rand() % (max_val - min_val + 1);
    }
    return arr;
}

int main() {
    srand(static_cast<unsigned int>(time(nullptr)));

    std::vector<int> sizes = {10, 1000, 100000};
    int min_val = 0;
    int max_val = 500;
    for (int n : sizes) {
        std::vector<int> arr = generate_random_list(n, min_val, max_val);

        int random_index = rand() % n;
        int target = arr[random_index];

        auto start = std::chrono::high_resolution_clock::now();

        int index = last_occurrence(arr, target);

        auto end = std::chrono::high_resolution_clock::now();

        std::chrono::duration<double> elapsed = end - start;

        std::cout << "Размер списка: " << n << std::endl;
        std::cout << "Искомый элемент: " << target << std::endl;
        std::cout << "Найденный индекс последнего вхождения: " << index << std::endl;
        std::cout << "Время поиска: " << elapsed.count() << " секунд" << std::endl;
    }


    return 0;
}