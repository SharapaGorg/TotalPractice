#include <iostream>
#include <list>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include "main.h"
#include <cstdlib>
#include <Windows.h>

using namespace std;

vector <string> AsciiLetters;

string AsciiHandler(char p) {
    stringstream ss;
    string target;
    ss << p;
    ss >> target;
    string s = "letters\\" + target + ".txt";
    LetterUpdate(s);

    return "Found completed";
}

string LetterUpdate(const string& f) {
    try {
        const int len = 50, strings = 10;
        const char ch = '\n';
        char mass[len][strings];

        ifstream fs(f, ios::in | ios::binary);

        for (int r = 0; r < 21; r++) {
            fs.getline(mass[r], len - 1, ch);
            AsciiLetters.emplace_back(mass[r]);
        }
        fs.close();
    }
    catch (exception){
        cout << "Undefined file_name" << endl;
    }
    return "Completed";
}

int main() {

    string detail;

    cout << "Enter pls detail of ascii: " << endl;
    try {
        getline(cin, detail);
    }
    catch (int detail){
        cout << "Invalid input" << endl;
    }

    for (char i : detail) {
        AsciiHandler(i);
    }

    string _a = "    ";

    int l = 0;

    if ( !AsciiLetters.empty() ) {
        for (int k = 0; k < 21; k++) {
            try {
                for (int i = l; i < AsciiLetters.size(); i += 21) {
                    _a += AsciiLetters[i].replace(AsciiLetters[i].length() - 1, AsciiLetters[i].length(), "") + "    ";
                }
            }
            catch (int a) { cout << "Caught exception number:  " << a << endl; }

            cout << _a << endl;
            l += 1;
            _a = "    ";
        }
    }
    else {
        cout << "Not found any letters" << endl;
    }

    vector<string> Color = {
            "FC", "EC", "AC", "CF", "9C", "DC", "8C"
    };


//    while (true) {
//        string r = "color " + Color[rand() % Color.size()];
//
//        system(r.c_str());
//
//        Sleep(100);
//
//    }

    return 0;
}


