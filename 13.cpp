#include <iostream>
#include <fstream>
#include <sstream>
#include <set>

using namespace std;

//split a string at the first occurance of delimiter, not including delim
pair<string,string> split(const string& in, char delim)
{
    for(int i=0;i<in.length(); ++i)
    {
        if(in[i] == delim)
        {
            return pair<string,string>(string(in.begin(), in.begin()+i), string(in.begin()+i+1, in.end()));
        }
    }
}

string scrub(string in, const set<char>& remove)
{
    string str = "";
    
    for(auto it = in.begin(); it != in.end(); ++it)
    {
        if(remove.find(*it) == remove.end())
        {
            str += *it;
        }
    }
    
    return str;
}

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);
    
    string line;
    
    while (getline(file,line))
    {
        pair<string,string> strPair = split(line, ',');
        set<char> toRemove;
        //ignore leading space from removal targets string
        for(int i=1; i < strPair.second.length(); ++i)
        {
            toRemove.insert(strPair.second[i]);
        }
        
        cout << scrub(strPair.first, toRemove) << endl;
    }
}
