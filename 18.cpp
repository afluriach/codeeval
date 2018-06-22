#include <iostream>
#include <fstream>
#include <sstream>
#include <list>

using namespace std;

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);
    
    string line;
    
    while (getline(file,line))
    {
        stringstream linestr(line);
        
        int base, factor;
        char dummy;
        
        linestr >> base >> dummy >> factor;
        
        //no division
        
        for(int f=1; ; ++f)
        {
            if(f*factor >= base)
            {
                cout << f*factor << endl;
                break;
            }
        }
    }
}
