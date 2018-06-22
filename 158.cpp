#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>

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

//perform one iteration of bubble sort
bool bubbleSort(vector<int>& nums)
{
    bool sorted = true;

    for(int i=0;i<nums.size()-1; ++i)
    {
        if(nums[i] > nums[i+1])
        {
            swap(nums[i], nums[i+1]);
            sorted = false;
        }
    }
    
    return sorted;
}

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);

    string line;
    
    while (getline(file, line))
    {
        pair<string,string> strings = split(line, '|');
        stringstream num_stream(strings.first), count_stream(strings.second);
        int n, val;
        vector<int> nums;
        
        count_stream >> n;
        
        while(num_stream >> val)
        {
            nums.push_back(val);
        }
                
        for(int i=0;i<n; ++i)
        {
            //in case the sort finishes with fewer iterations than requested.
            if(bubbleSort(nums)) break;
        }
        
        bool first = true;
        
        for(auto it = nums.begin(); it != nums.end(); ++it)
        {
            if(!first)
            {
                cout << " ";
            }
            first = false;
            
            cout << *it;
        }
        cout << endl;
    }
}
