// Solve of Problem 3: Interactive Triangle Display

#include <iostream>
using namespace std;

void RightAngleTriangle(int lines) {
    for (int i = 1; i <= lines; ++i) {
        for (int j = 1; j <= i; ++j) {
            cout << "1";
        }
        cout << endl;
    }
}

void PalindromicTriangle(int lines) {
    for (int i = 1; i <= lines; ++i) {
        // Print increasing numbers
        for (int j = 1; j <= i; ++j) {
            cout << j;
        }
        // Print decreasing numbers
        for (int j = i - 1; j >= 1; --j) {
            cout << j;
        }
        cout << endl;
    }
}

int main() {
    int choice, lines;
// display Menu to let user choose   
    do {
        cout << "Menu:\n";
        cout << "1. Display a right-angle triangle of ones\n";
        cout << "2. Display a Palindromic Triangle\n";
        cout << "3. Help\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

// show result depend on user choice
            if (choice==1){
                cout << "Enter the number of lines: ";
                cin >> lines;
                RightAngleTriangle(lines);
                break;
                
            } else if (choice==2){
                cout << "Enter the number of lines: ";
                cin >> lines;
                PalindromicTriangle(lines);
                break;
                
            } else if (choice==3){
                cout << "\n Help \n";
                cout << "A Palindromic Triangle is triangular array of numbers where each row forms a palindrome.The first few lines of a Palindromic Triangle are: \n";
                PalindromicTriangle(5);
                cout << "You can use this pattern to draw a Palindromic Triangle for any number of lines.";
                break;
                
            } else if (choice==4){
                cout << "Exiting the program.\n";
                break;
            }else{
                cout << "Incorrect, please try again.\n";
            }
    } while (choice != 4);

    return 0;
}
