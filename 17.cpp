#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <limits>

using namespace std;

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);
    
    string line;
    
    while (getline(file,line))
    {
        stringstream str(line);
        int val;
        vector<int> sequence;
        
        while(str >> val)
        {
            char d;
            sequence.push_back(val);
            
            if(str)
                str >> d;
        }

        int max_sum = numeric_limits<int>::min();
        
        for(int start_pos = 0; start_pos < sequence.size(); ++start_pos)
        {
            //the sum of the current sequence
            int seq_sum = 0;
            
            for(int i = start_pos; i <sequence.size(); ++i)
            {
                seq_sum += sequence[i];
                
                max_sum = max(seq_sum, max_sum);
            }
        }        
        
        cout << max_sum << endl;
    }
    return 0;   
}
