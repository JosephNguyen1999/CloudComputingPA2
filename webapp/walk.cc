#include <iostream>
using std::cin;
using std::cout;
#include <string>
using std::string;

int main()
{
    string name1, name2;
    std::cout << "Enter a name:";
    getline(std::cin, name1);
    std::cout << "Enter a name:";
    getline(std::cin, name2);
    std::cout << " and went for a walk.\n";
}