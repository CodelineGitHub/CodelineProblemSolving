#include <iostream>
#include <vector>

using namespace std;

vector<int> getEvenSquares(const vector<int>& numbers) {
    vector<int> squares;

    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] % 2 == 0) {
            squares.push_back(numbers[i] * numbers[i]);
        }
    }

    return squares;
}

vector<int> sliceList(const vector<int>& numbers, int start, int end) {
    vector<int> sublist;

    if (start < 0 || end > numbers.size() || start > end) {
        cout << "Invalid slice indices." << endl;
        return sublist;
    }

    for (int i = start; i < end; i++) {
        sublist.push_back(numbers[i]);
    }

    return sublist;
}

int main() {
    int n;

    cout << "Enter the number of integers: ";
    cin >> n;

    vector<int> numbers(n);

    cout << "Enter the integers: ";
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }

    vector<int> evenSquares = getEvenSquares(numbers);

    cout << "Squares of even numbers: ";
    for (int i = 0; i < evenSquares.size(); i++) {
        cout << evenSquares[i] << " ";
    }
    cout << endl;

    int startIndex, endIndex;

    cout << "Enter start index for slicing: ";
    cin >> startIndex;
    cout << "Enter end index for slicing: ";
    cin >> endIndex;

    vector<int> slicedList = sliceList(numbers, startIndex, endIndex);

    cout << "Sliced list: ";
    for (int i = 0; i < slicedList.size(); i++) {
        cout << slicedList[i] << " ";
    }
    cout << endl;

    return 0;
}
