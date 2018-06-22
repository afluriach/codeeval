#include <iostream>
#include <fstream>
#include <set>
#include <map>

using namespace std;

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);
    
    string line;
    
    while (getline(file,line))
    {
        //use set to store which characters have been seen
        //map to store index of when letter was first seen
        set<char> repeating;
        map<char, int> seen;
        
        for(int i=0;i<line.length(); ++i)
        {
            char ch = line[i];
            //first time seeing character
            if(seen.find(ch) == seen.end())
            {
                seen[ch] = i;
            }
            else //if(repeating.find(ch) == repeating.end())
            {
                repeating.insert(ch);
            }
        }
        
        int minIndex = line.length();
        char first;
        for(auto it = seen.begin(); it != seen.end(); ++it)
        {
            if(repeating.find(it->first) != repeating.end()) continue;
            
            if(it->second < minIndex)
            {
                minIndex = it->second;
                first = it->first;
            }
        }
        
        cout << first << endl;
    }
}
