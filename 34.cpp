#include <iostream>
#include <fstream>
#include <set>
#include <sstream>

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

set<int> parseInts(stringstream& in)
{
    set<int> ints;
    
    while(true)
    {
        int val;
        char dummy;
        in >> val;
        ints.insert(val);
        
        if(in) in >> dummy;
        else break;
    }
    
    return ints;
}

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);
    
    string line;
    
    while (getline(file,line))
    {
        pair<string,string> strings = split(line, ';');
        stringstream str(strings.first);
        stringstream target_str(strings.second);
        int target;
        set<int> ints = parseInts(str);
        target_str>>target;
        bool first_result = true;
        
        //foreach number in the set, check if the difference is also present
        //to avoid double-counting and preserve ordering, the only numbers that
        //we need to consider as the first number of a pair are where n < N/2
        
        for(auto it = ints.begin(); it != ints.end() && *it < target/2; ++it)
        {
            int diff = target - *it;
            
            if(ints.find(diff) != ints.end())
            {
                if(!first_result)
                    cout << ";";

                cout << *it << "," << diff;
                first_result = false;
            }
        }
        
        if(first_result)
        {
            //no result was found
            cout << "NULL";
        }
        
        cout << endl;
    }
}
