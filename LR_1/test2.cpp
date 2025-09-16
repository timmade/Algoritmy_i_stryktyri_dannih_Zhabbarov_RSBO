#include <iostream>
#include <vector>
#include <numeric>
#include <cstdlib>
#include <ctime>

using namespace std;

long long sumManual(const vector<int>& arr) {
    long long sum = 0;
    for (size_t i = 0; i < arr.size(); i++) {
        sum += arr[i];
    }
    return sum;
}

long long sumBuiltIn(const vector<int>& arr) {
    return accumulate(arr.begin(), arr.end(), 0LL);
}

int main() {
    srand(time(0));
    int sizes[] = {1000000, 10000000, 100000000};
    int numSizes = 3;

    for (int i = 0; i < numSizes; i++) {
        int size = sizes[i];
        vector<int> arr(size);
        for (int j = 0; j < size; j++) {
            arr[j] = rand() % 1000 + 1;
        }

        clock_t start = clock();
        long long sum1 = sumManual(arr);
        clock_t end = clock();
        double duration1 = double(end - start) / CLOCKS_PER_SEC;

        start = clock();
        long long sum2 = sumBuiltIn(arr);
        end = clock();
        double duration2 = double(end - start) / CLOCKS_PER_SEC;

        cout << "Размер списка: " << size << endl;
        cout << "  Ручная сумма: " << sum1 << ", Время: " << duration1 << " сек" << endl;
        cout << "  Встроенная сумма: " << sum2 << ", Время: " << duration2 << " сек" << endl;
        cout << "  Отношение (ручная/встроенная): " << duration1 / duration2 << endl;
        cout << "-----------------------------------" << endl;
    }

    return 0;
}