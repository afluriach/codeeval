#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);
    
    string line;
    
    while (getline(file,line))
    {
        bool upper = true;
        
        for(int i=0;i<line.length(); ++i)
        {
            char ch;
            
            if(isalpha(line[i]))
            {
                //enforce case on alphabetic character and switch desired case
                if(upper)
                    ch = toupper(line[i]);
                else
                    ch = tolower(line[i]);
                    
                upper = !upper;
            }
            else
            {
                //do not modify non-alphabetic characters
                ch = line[i];
            }
            cout << ch;
        }
        cout << endl;
    }
}
