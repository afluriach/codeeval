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
        
        //ones based bit position
        
        int n, pos1, pos2;
        char dummy;
        
        linestr >> n >> dummy >> pos1 >> dummy >> pos2;
        
        bool match = ((n >> (pos1-1)) & 1) == ((n >> (pos2-1)) & 1);
        
        cout << (match ? "true" : "false") << endl; 
    }
}
