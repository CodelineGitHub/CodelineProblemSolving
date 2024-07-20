#include <regex>  
#include <iostream>  
using namespace std;  

// Function to check Username 
   int validates(string username)
{
    int special = 0, l = username.length();
    //check length is 0 or more than 50
    if (l == 0 || l > 50)
        return 0;

    for (int i = 0; i < l; i++)
    {
        char s = username.at(i);

        //no spaces allowed
        if (s == ' ')
            return 0;
            }
    return 1;
}
// Function to check Password
bool validatePassword(string password)  
{  
    // regex pattern for password validation  
    regex pattern("(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&+=])(?=\\S+$).{8,}");  
   
    // check if the password matches the pattern  
    if (regex_match(password, pattern))  
    {  
        return true;  
    }  
    else  
    {  
        return false;  
    }  
}  
 // Function to check the email id 

bool isValid(const string& email) 
{ 
  
    // Regular expression definition 
    const regex pattern( 
        "(\\w+)(\\.|_)?(\\w*)@(\\w+)(\\.(\\w+))+"); 
  
    // Match the string pattern 
    // with regular expression 
    return regex_match(email, pattern); 
} 
  
int main()  
{  
    string UserName;  
    cout << "Enter Your UserName: ";  
    getline(cin, UserName); 
    
    string password;  
    cout << "Enter Your Password: ";  
    getline(cin, password);  
    
    string email;  
    cout << "Enter Your Email: ";  
    getline(cin, email);  
    //username fun
    if (validates(UserName))
        cout << "Username is Valid"<< endl;  
    else
        cout <<"Username is Invalid"<< endl;  
     //password fun
    if (validatePassword(password))  
    {  
        cout << "Password is valid." << endl;  
    }  
    else  
    {  
        cout << "Password is invalid." << endl;  
    }  
   //Email fun
   // Function Call 
    bool ans = isValid(email); 
  
    // Print the result 
    if (ans) { 
        cout << "Email is valid." << endl; 
    } 
    else { 
        cout << "Email is invalid." << endl; 
    } 
    return 0;  
}  
  