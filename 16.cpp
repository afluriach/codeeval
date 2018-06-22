#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);
    
    string line;
    
    while (getline(file,line))
    {
        stringstream linestr(line);
        
        int n;
        linestr >> n;
        
        int n_bits = 0;
        
        while(n != 0)
        {
            if(n & 1) n_bits++;
            n /= 2;
        }
        
        cout << n_bits << endl;
    }
}
