#include <iostream>

using namespace std;


void displayRightAngleTriangle(int lines) {
    for (int i = 1; i <= lines; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "1 ";
        }
        cout << endl;
    }
}


void displayPalindromicTriangle(int lines) {
    for (int i = 1; i <= lines; i++) {
        for (int j = lines; j > i; j--) {
            cout << " ";
        }
        for (int k = 1; k <= i; k++) {
            cout << k << " ";
        }
        cout << endl;
    }
}


void showHelp() {
    cout << "Help:\n";
    cout << "1. Display a right-angle triangle of ones\n";
    cout << "   - Shows a triangle with each row containing increasing numbers of '1's.\n";
    cout << "2. Display a palindromic triangle\n";
    cout << "   - Shows a triangle where each row contains increasing numbers starting from 1.\n";
    cout << "3. Help\n";
    cout << "   - Displays this help message.\n";
    cout << "4. Exit\n";
    cout << "   - Exits the program.\n";
}


int main() {
    int choice;
    int lines;

    while (true) {
        cout << "\nMenu:\n";
        cout << "1. Display a right-angle triangle of ones\n";
        cout << "2. Display a palindromic triangle\n";
        cout << "3. Help\n";
        cout << "4. Exit\n";
        cout << "Enter your choice (1-4): ";
        cin >> choice;

        if (choice == 1 || choice == 2) {
            cout << "Enter the number of lines: ";
            cin >> lines;
        }

        switch (choice) {
            case 1:
                displayRightAngleTriangle(lines);
                break;

            case 2:
                displayPalindromicTriangle(lines);
                break;

            case 3:
                showHelp();
                break;

            case 4:
                cout << "Exiting the program." << endl;
                return 0;

            default:
                cout << "Invalid choice. Please enter a number between 1 and 4." << endl;
                break;
        }
    }

    return 0;
}
