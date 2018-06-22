#include <iostream>
#include <fstream>
#include <list>
#include <sstream>

using namespace std;

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);
    
    string line;
    
    while (getline(file,line))
    {
        stringstream str(line);
        
        list<char> chars;
        string s;
        int m;
        char dummy;
        
        while(true)
        {
            //push stream into string. handles space, but also 
            //will handle the number which can be multiple characters
            str >> s;
            
            if(isdigit(s[0]))
            {
                //the last character
                m = atoi(s.c_str());
                break;
            }
            else
            {
                chars.push_back(s[0]);
            }
        }
        
        if(m > chars.size())
        {
            cout << endl;
            continue;
        }
        
        //start at the end (reverse iterator) and step back m times.
        int count = 1;
        auto it = chars.rbegin();
        for(; count < m; ++it, ++count)
        {
        }
        
        cout << *it << endl;
        
    }
}
