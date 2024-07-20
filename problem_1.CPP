#include <iostream>
#include <string>

using namespace std;


bool username(const string &user) {
    
    if (user.empty() || user.length() > 50) {
        
        return false;
    }
    return true;
}


bool password(const string &pass) {

    bool hasSpecial = false, hasDigit = false, hasUpper = false, hasLower = false;

    if (pass.length() < 8) {
        
        return false;
    }

    for (char ch : pass) {
        if (ispunct(ch)) 
            hasSpecial = true;
        if (isdigit(ch)) 
            hasDigit = true;
        if (isupper(ch)) 
            hasUpper = true;
        if (islower(ch)) 
            hasLower = true;
    }

    if (!hasSpecial || !hasDigit || !hasUpper || !hasLower) {
        
        return false;
    }

    return true;
}


bool email(const string &mail) {

    size_t atPos = mail.find('@');
    size_t dotPos = mail.find('.', atPos);

    if (atPos == string::npos || dotPos == string::npos || 
        atPos == 0 || dotPos == atPos + 1 || dotPos == mail.length() - 1) {
        
        return false;
    }

    return true;
}


int main() {

    string userInput, passInput, mailInput;

    cout << "Enter Username: ";
    cin >> userInput;

    cout << "Enter Password: ";
    cin >> passInput;

    cout << "Enter Email: ";
    cin >> mailInput;


    bool isUserValid = username(userInput);
    bool isPassValid = password(passInput);
    bool isMailValid = email(mailInput);


    if (isUserValid) {
        cout << "Username is valid." << endl;
    } else {
        cout << "Username is invalid." << endl;
    }


    if (isPassValid) {
        cout << "Password is valid." << endl;
    } else {
        cout << "Password is invalid." << endl;
    }

    if (isMailValid) {
        cout << "Email is valid." << endl;
    } else {
        cout << "Email is invalid." << endl;
    }

    return 0;
}