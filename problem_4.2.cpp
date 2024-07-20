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
        cout<< numbers[i] << ","; 
    }
    cout << "] \n";
    int s,e;
     cout << "Enter start index: "; 
        cin >> s; 
        cout << "Enter end index: "; 
        cin >> e; 
     cout << "\nSublist: [";
    
    for (int i = s; i <= e; i++) {
        cout << numbers[i] << ",";
             } 
    cout<<"]";
    
    return 0; 
}
  