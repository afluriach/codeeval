#include <iostream>
#include <fstream>
#include <map>
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
        
        //count of how many times each number has appeared
        //number -> count
        map<int,int> num_counts;
        int input_size = 0;
        
        while(true)
        {
            int val;
            char d;
            
            str >> val;
            ++input_size;
            
            auto search = num_counts.find(val);
            
            if(search != num_counts.end())
            {
                ++search->second;
            }
            else
            {
                num_counts[val] = 1;
            }
            
            //process separating comma, or end of line
            if(str) str >> d;
            else break;
        }
        
        //find number that appears L/2 times. there can be only one
        bool found = false;
        for(auto it = num_counts.begin(); it != num_counts.end(); ++it)
        {
            if(it->second > input_size/2)
            {
                cout << it->first;
                found = true;
                break;
            }
        }
        
        if(!found)
        {
            cout << "None";
        }
        cout << endl;
    }
}
