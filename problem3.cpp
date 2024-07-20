#include <iostream>
void displayRightAngleTriangle(int size) {
    for (int i = 1; i <= size; ++i) {
        for (int j = 0; j < i; ++j) {
            std::cout << "1 ";
        }
        std::cout << std::endl;
    }
}

void displayPalindromicTriangle(int size) {
    for (int i = 1; i <= size; ++i) {
        for (int j = size; j > i; --j) {
            std::cout << " ";
        }
        for (int j = 1; j <= i; ++j) {
            std::cout << j;
        }
        for (int j = i - 1; j >= 1; --j) {
            std::cout << j;
        }
        std::cout << std::endl;
    }
}

void displayHelp() {
    std::cout << "1. Right-angle triangle of ones: Prints rows of ones." << std::endl;
    std::cout << "2. Palindromic Triangle: Prints numbers ascending and then descending." << std::endl;
    std::cout << "3. Help: Shows this help message." << std::endl;
    std::cout << "4. Exit: Exits the program." << std::endl;
}

int main() {
    int choice, size;

    std::cout << "Menu:\n1. Right-angle triangle of ones\n2. Palindromic Triangle\n3. Help\n4. Exit\n";

    while (true) {
        std::cout << "Enter your choice (1-4): ";
        std::cin >> choice;

        if (choice == 1) {
            std::cout << "Enter size: ";
            std::cin >> size;
            displayRightAngleTriangle(size);
        } else if (choice == 2) {
            std::cout << "Enter size: ";
            std::cin >> size;
            displayPalindromicTriangle(size);
        } else if (choice == 3) {
            displayHelp();
        } else if (choice == 4) {
            std::cout << "Exiting..." << std::endl;
            break; // Exit the loop
        } else {
            std::cout << "Invalid choice. Try again." << std::endl;
        }

        std::cout << std::endl; // Add a blank line for readability
    }

    return 0;
}
