#include <iostream>
#include <string>
#include <map>

using namespace std;
map<char,string> mapa;
int main()
{
    string slowo;
    cin>>slowo;
    mapa['A'] = "2";
    mapa['B'] = "22";
    mapa['C'] = "222";
    mapa['D'] = "3";
    mapa['E'] = "33";
    mapa['F'] = "333";
    mapa['G'] = "4";
    mapa['H'] = "44";
    mapa['I'] = "444";
    mapa['J'] = "5";
    mapa['K'] = "55";
    mapa['L'] = "555";
    mapa['M'] = "6";
    mapa['N'] = "66";
    mapa['O'] = "666";
    mapa['P'] = "7";
    mapa['Q'] = "77";
    mapa['R'] = "777";
    mapa['S'] = "7777";
    mapa['T'] = "8";
    mapa['U'] = "88";
    mapa['V'] = "888";
    mapa['W'] = "9";
    mapa['X'] = "99";
    mapa['Y'] = "999";
    mapa['Z'] = "9999";

    for (auto i: slowo)
    {
        cout<<mapa[i];
    }

    return 0;
}
