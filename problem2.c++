#include <iostream>
#include <string>

std::string decimalToBinary(int number) {
    if (number == 0) return "0";

    std::string binary;
    while (number > 0) {
        binary = (number % 2 == 0 ? '0' : '1') + binary; 
        number /= 2;
    }
    return binary;
}

int main() {
    int decimal;
    
  
    std::cout << "Enter your Nmber: ";
    std::cin >> decimal;

   
    std::string binary = decimalToBinary(decimal);

   
    std::cout << "Input: " << decimal << std::endl;
    std::cout << "Output: " << binary << std::endl;

    return 0;
}
