#include <iostream> 
using namespace std; 
 
int main() 
{ 
    // defining array size 
    int size = 5; 
    int numbers[size]; 
    for (int i = 0; i < size; i++) { 
        cout << "Enter a number: "; 
        cin >> numbers[i]; 
    } 
  
    // Print The list of  integers
    cout << "The list of  integers: [ "; 
    for (int i = 0; i < size; i++) { 
        cout<< numbers[i] << ", "; 
    }
    cout << "] \nList of squares of even number: [";
    
    for (int i = 0; i < size; i++) {
       // to check the number is even or not and square it
        if (numbers[i] % 2 == 0) {
           cout << numbers[i]*numbers[i] << ", ";
            
        }
    } 
    cout<<"]";
    
    return 0; 
}