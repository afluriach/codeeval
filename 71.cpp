#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

pair<string,string> split(const string& in, char delim)
{
    int match = in.find_first_of(delim);
    
    if(match == string::npos)
    {
        return pair<string,string>("","");
    }
    else
    {
        return pair<string,string>(string(in.begin(), in.begin()+match),
                                   string(in.begin()+match+1, in.end()));
    }
}

void reverse_subsequence(vector<int>::iterator start, int length)
{
    //perform up to floor(length/2) swaps. for an odd length sequence, the middle
    //element wouldn't need to be swapped
    
    vector<int>::iterator last = start+length-1;
    
    for(int count = 0; count < length/2; ++count, ++start, --last)
    {
        swap(*start, *last);
    }
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
        stringstream k_str(strings.second);
                
        vector<int> nums;
        int k;
        k_str >> k;
        int val;
        
        while(str>>val)
        {
            char d;
            
            nums.push_back(val);
            
            if(str)
            {
                //process separating character
                str >> d;
            }
        }
        
        for(int subseq_pos = 0; subseq_pos+k < nums.size(); subseq_pos += k)
        {
            reverse_subsequence(nums.begin()+subseq_pos, k);
        }
        
        cout << nums.front();
        
        for(auto it = nums.begin()+1; it != nums.end(); ++it)
        {            
            cout << "," << *it;   
        }
        cout << endl;
    }
}
