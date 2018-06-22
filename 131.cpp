#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int parseInt(vector<int>& digits, int start, int len)
{
    int n = 0;
    
    for(int i=0;i<len; ++i)
    {
        n *= 10;
        
        n += digits[start+i];
    }
    
    return n;
}

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);

    int num;    
    
    string line;
    
    while (getline(file, line))
    {
        vector<int> digits;
        int linePos = 0;        
                
        for(;line[linePos] != ' '; ++linePos)
        {
            //read in sequence of digits
            //convert character to decimal digit value
            digits.push_back(line[linePos] - '0');
        }
                
        //skip space
        while(line[linePos] == ' ') ++linePos;
        
        //read in sequence of letters. count how many letters until the operation
        int opPos = 0;
        
        while(true)
        {
            if(!isalpha(line[linePos])) break;
            
            ++opPos, ++linePos;
        }
        
        char op = line[linePos];
        
        //build two integers. first is opPos digits long, starting at 0
        //second is digits.size() - opPos digits long, starting at opPos
        
        int first = parseInt(digits, 0, opPos);
        int second = parseInt(digits, opPos, digits.size() - opPos);
                
        if(op == '+')
        {
            cout << (first+second) << endl;
        }
        else if(op == '-')
        {
            cout << (first-second) << endl;
        }
    }
}
