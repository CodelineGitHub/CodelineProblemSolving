#include <iostream>
using namespace std;

// Function to display the menu 
void menu() 
{ 
    cout << "1.Display a aright-angle traiangle of ones\n"; 
    cout << "2.Display a Palindromic traiangle \n"; 
    cout << "3.Help\n"; 
    cout << "4.Exit\n"; 
    
} 
// Function to display the result 
void result(int choice) 
{ 
 
    // Display the result 
    switch (choice) { 
    case 1: { 
        int i,j,rows;
    cout<<"Enter the number of lines : ";
        cin>>rows;
        for(i=1;i<=rows;i++)
        {
    for(j=1;j<=i;j++)
       cout<<"1";
       cout<<"\n";
          }
        break; 
    } 
    case 2: { 
        int rows;

    cout<<"Enter the row number: ";
    cin>>rows;
    for(int i=0;i<=rows;i++)
    {
       for(int j=1;j<=i;j++)
        cout<<j;
        for(int j=i-1;j>0;j--)
        cout<<j;
    cout<<"\n";
    }
        break; 
    } 
    case 3: { 
       cout<<"Help:\n A Palindromic traiangle is traiangle array of numbers where each row forms apalindrome.\n The first few lines of a Palindromic traiangle are:\n ";
        for(int i=0;i<=4;i++)
             {
            for(int j=1;j<=i;j++)
         cout<<j;
             for(int j=i-1;j>0;j--)
             cout<<j;
             cout<<"\n";
             }
              cout<<"You can use this pattren to draw a Palindromic traiangle for any number of lines. ";
        break; 
    } 
    case 4: { 
       cout<<"Exiting the program. ";
       exit(0);
        break; 
    } 
   
    default: 
     cout<<"Wrong Input\n";
      
    } 
} 

int main() {
      // Display the menu 
        menu(); 
     // Enter the choice 
        int choice; 
        cout << "Enter your choice:  "; 
         cin >> choice;

    // Display the result according to the choice 
        result(choice); 
 
    return 0;
   
    
}