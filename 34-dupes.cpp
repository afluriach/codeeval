#include <iostream>
#include <fstream>
#include <set>
#include <sstream>

using namespace std;

typedef pair<set<int>,set<int> > set_pair;

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

//the problem doesn't specifically say there are no duplicates.
//the only case I can think of is N/2 appears twice.
pair<set<int>,set<int> > parseInts(stringstream& in)
{
    set<int> ints;
    set<int> dupes;
    
    while(true)
    {
        int val;
        char dummy;
        in >> val;
        
        if(ints.find(val) != ints.end())
            dupes.insert(val);
        else        
            ints.insert(val);
        
        if(in) in >> dummy;
        else break;
    }
    
    return set_pair(ints, dupes);
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
        set_pair sets = parseInts(str);
        target_str>>target;
        bool first_result = true;
        
        //foreach number in the set, check if the difference is also present
        //to avoid double-counting and preserve ordering, the only numbers that
        //we need to consider as the first number of a pair are where n < N/2
        
        for(auto it = sets.first.begin(); it != sets.first.end() && *it < target/2; ++it)
        {
            int diff = target - *it;
            
            if(sets.first.find(diff) != sets.first.end())
            {
                if(!first_result)
                    cout << ";";

                cout << *it << "," << diff;
                first_result = false;
            }
        }
        
        //finally check if target/2 duplicate pair is possible
        if(target % 2 == 0 && sets.second.find(target/2) != sets.second.end())
        {
            if(!first_result)
                cout << ";";

            cout << target/2 << "," << target/2;
            first_result = false;
        }
        
        if(first_result)
        {
            //no result was found
            cout << "NULL";
        }
        
        cout << endl;
    }
}
