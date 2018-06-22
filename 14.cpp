#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

string crnt;
bool used[128];
bool first;

void perm(vector<char>& chars)
{
    if(crnt.length() == chars.size())
    {
        if(!first)
            cout << ",";
    
        cout << crnt;
        first = false;
        return;
    }

    for(int i=0;i<chars.size(); ++i)
    {
        if(used[i]) continue;
        
        crnt.push_back(chars[i]);
        used[i] = true;
        
        perm(chars);
        
        crnt.pop_back();
        used[i] = false;        
    }    
}

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);

    string line;
    
    memset(used, 0, 128);
    
    while (getline(file, line))
    {
        vector<char> chars;
        
        for(int i=0;i<line.length(); ++i)
        {
            chars.push_back(line[i]);
        }
        
        //default character ordering works for this problem
        sort(chars.begin(), chars.end());        
        first = true;        
        perm(chars);
        cout << endl;
    }
}
