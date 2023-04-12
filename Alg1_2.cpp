#include<iostream>
#include<algorithm>

using std::cout;
using std::cin;
using std::string;
using std::max;


int main()
{
    int REPLACE;
    string MYSTR;
    cin >> REPLACE;
    cin >> MYSTR;
    int lenght = size(MYSTR);
    int maximum = 0;



    for(int symbol = 97; symbol < 123; symbol++)
    {
        int j = 0;
        for(int i = 0; i < lenght; i++)
        {
            while (REPLACE >= 0 && j != lenght)
            {
                if (MYSTR[j] != (char)symbol and REPLACE != 0)
                {
                    REPLACE--;
                    j++;
                }
                else if (MYSTR[j] != (char)symbol && REPLACE == 0)
                {
                    break;
                }
                else
                {
                    j++;
                }
            }
            maximum = max(j - i, maximum);
            if (MYSTR[i] != (char)symbol)
            {
                REPLACE++;
            }
            
        }
    }

    cout << maximum;

    

    return 0;
}