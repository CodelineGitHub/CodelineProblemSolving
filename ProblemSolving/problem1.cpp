// Solve of Problem 1: User Login Validation

#include <iostream>
#include <regex>
#include <string>
using namespace std;

bool ValidUsername(const string & username){
    return !username.empty() && username.length()<=50;
}

bool ValidPassword(const string & password){
    
    if (password.length()<8) return false;

    bool SpecialSymbol=false, DigitNum=false, Uppercase=false, Lowercase=false;
    
    for (char ch:password){
        if (ispunct(ch)) SpecialSymbol= true;
        if (isdigit(ch)) DigitNum= true;
        if (isupper(ch)) Uppercase= true;
        if (islower(ch)) Lowercase= true;
    }
    return SpecialSymbol && DigitNum && Uppercase && Lowercase;
}

bool ValidEmail(const string & email) {
    const regex pattern("(\\w+)(\\.|_)?(\\w*)@(\\w+)(\\.(\\w+))+");
    return regex_match(email, pattern);
}


void Result(bool isValid, const string& field) {
    if (isValid) {
        cout << field << " is valid." << endl;
    } else {
        cout << field << " is invalid." << endl;
    }
}

int main() {
    string Username, Password, Email;

// Enter inputs
    cout << "Enter Username: ";
    getline(cin,Username);
    cout << "Enter Password: ";
    cin>>Password;
    cout << "Enter Email: ";
    cin>> Email;

// Check validation
    bool isUsernameValid = ValidUsername(Username);
    bool isPasswordValid = ValidPassword(Password);
    bool isEmailValid = ValidEmail(Email);
	    
	    cout << "\n";
	    
// Show Result
    Result(isUsernameValid, "Username");
    Result(isPasswordValid, "Password");
    Result(isEmailValid, "Email");

    return 0;
}

