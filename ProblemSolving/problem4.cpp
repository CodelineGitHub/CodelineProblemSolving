//Solve of Problem 4: Generating Even Squares

#include <iostream>
#include <vector>
using namespace std;

// Pocess input string into a list of integers
vector<int> pocessInput(const string& input) {
    vector<int> numbers;
    int num= 0;
    bool isNum = false;

    for (int ch : input) {
        if (isdigit(ch)) {
            num = num * 10 + (ch - '0');
            isNum = true;
        } else if (ch == ',' || ch == ']') {
            if (isNum) {
                numbers.push_back(num);
                num = 0;
                isNum = false;
            }
        }
    }
    if (isNum) {
        numbers.push_back(num);
    }
    return numbers;
}

// squares of even numbers
vector<int> SquaresOfEven(const vector<int> & numbers) {
    vector<int> squares;
    for (int num : numbers) {
        if (num %2==0) {
            squares.push_back(num * num);
        }
    }
    return squares;
}

// slice a list
vector<int> sliceList(const vector<int>& numbers, int start, int end) {
    vector<int> sublist;
    for (int i = start; i < end && i < numbers.size(); ++i) {
        sublist.push_back(numbers[i]);
    }
    return sublist;
}

int main() {
    
//get list of inputs
    string input;
    cout << "Enter the list of integers in the format [1,2,3,...]: ";
    getline(cin, input);
    input = input.substr(1, input.size() - 2);

//process inputs
    vector<int> numbers = pocessInput(input);
    
//square even inputs
    vector<int> squaresOfEven = SquaresOfEven(numbers);
    cout << "List of squares of even numbers: [";
    for (size_t i = 0; i < squaresOfEven.size(); ++i) {
        cout << squaresOfEven[i];
        if (i < squaresOfEven.size()-1) cout << ", ";
    }
    cout << "]\n" << endl;
    
//get index to show    
    int start, end;
    cout << "Enter the start index for sublist: ";
    cin >> start;
    
    cout << "Enter the end index for sublist: ";
    cin >> end;

    vector<int> sublist = sliceList(numbers, start, end);
    cout << "Sublist: [";
    
    for (size_t i=0; i<sublist.size(); ++i) {
       
        cout << sublist[i];
        if (i <sublist.size()-1) cout << ", "; 
    }
    cout << "]" << endl;
    return 0;
}