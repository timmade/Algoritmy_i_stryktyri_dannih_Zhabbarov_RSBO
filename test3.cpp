#include <iostream>
#include <vector>
#include <map>
#include <cstdlib>
#include <ctime>

using namespace std;

map<int, int> countSlow(const vector<int>& arr) {
    map<int, int> countMap;
    for (size_t i = 0; i < arr.size(); i++) {
        int num = arr[i];
        countMap[num] = 0;
        for (size_t j = 0; j < arr.size(); j++) {
            if (arr[j] == num) {
                countMap[num]++;
            }
        }
    }
    return countMap;
}

map<int, int> countFast(const vector<int>& arr) {
    map<int, int> countMap;
    for (size_t i = 0; i < arr.size(); i++) {
        countMap[arr[i]]++;
    }
    return countMap;
}

int main() {
    srand(time(0));
    int sizes[] = {10000, 50000, 100000};
    int numSizes = 3;

    for (int i = 0; i < numSizes; i++) {
        int size = sizes[i];
        vector<int> arr(size);
        for (int j = 0; j < size; j++) {
            arr[j] = rand() % 100 + 1;
        }

        clock_t start = clock();
        map<int, int> slowCount = countSlow(arr);
        clock_t end = clock();
        double slowTime = double(end - start) / CLOCKS_PER_SEC;

        start = clock();
        map<int, int> fastCount = countFast(arr);
        end = clock();
        double fastTime = double(end - start) / CLOCKS_PER_SEC;

        cout << "Размер списка: " << size << endl;
        cout << "  Медленный метод: " << slowTime << " сек" << endl;
        cout << "  Быстрый метод: " << fastTime << " сек" << endl;
        cout << "  Ускорение: " << slowTime / fastTime << "x" << endl;
        cout << "-----------------------------------" << endl;
    }

    return 0;
}