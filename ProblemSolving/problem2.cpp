// Solve of Problem 2: Convert decimal to binary

#include <iostream>
using namespace std;

void DecimalToBinary(int decimal) {
    int binary[32]; 
    int index= 0; 
    
    if (decimal == 0) {
        cout << "0";
        return;
    }

    // convert decimal to binary
    while (decimal > 0) {
        binary[index] = decimal % 2;
        decimal = decimal / 2;
        index++;
    }

    // Print the binary in reverse order
    for (int i = index - 1; i >= 0; i--) {
        cout << binary[i];
    }
    cout << endl;
}

int main() {
    int decimal;
    cout << "Input (Decimal): ";
    cin >> decimal;

    cout << "Output (Binary): ";
    DecimalToBinary(decimal);

    return 0;
}