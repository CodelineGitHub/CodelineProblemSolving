#include <iostream>

using namespace std;


void decimalToBinary(int decimal) {

    if (decimal == 0) {
        cout << "Output: 0" << endl;
        return;
    }


    string binary = "";
    while (decimal > 0) {
        int remainder = decimal % 2;
        binary = to_string(remainder) + binary;
        decimal = decimal / 2;
    }


    cout << "Output: " << binary << endl;

}


int main() {

    int decimalNumber;

    cout << "Input: ";
    cin >> decimalNumber;

    if (decimalNumber < 0) {
        cout << "Please enter a positive number." << endl;
        return 1;
    }

    decimalToBinary(decimalNumber);

    return 0;
}
