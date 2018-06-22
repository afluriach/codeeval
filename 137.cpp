#include <iostream>
#include <fstream>
#include <map>

using namespace std;

//key is dotted decimal IP, and val is number of times it
//has been seen
map<string,int> addrs;

//try to extract decimal address as a single number
unsigned int decimalAddr(string in, int pos)
{
    unsigned int accumulator = 0;
    
    while(isdigit(in[pos]))
    {
        accumulator *= 10;
        accumulator += in[pos] - '0';
        ++pos;
    }
    
    return accumulator;
}

//extract four dotted decimals
pair<bool,unsigned int> decimalDotAddr(string in, int pos)
{
    unsigned int accumulator = 0;
    int octets = 0;
    
    //each octet can be parsed as if it were a single
    //decimal address, should be in the range 0-255
    
    while(octets < 4)
    {
        accumulator *= 256;
        
        unsigned int val = decimalAddr(in, pos);
        
        //first octet must be 1, but it wouldn't parse as
        //decimal if the first octect was 0.
     
           
        if(val > 255)
        {
            //not valid dotted format
            return pair<bool,unsigned int>(false,0);
        }
        
        accumulator += val;
        ++octets;
        
        if(octets < 4)
        {
            //a dot should directly follow the last digit followed by another digit
            //move pos to first character after the dot
            
            while(isdigit(in[pos])) ++pos;
            
            if(in[pos] == '.' && isdigit(in[pos+1]))
            {
                ++pos;
            }
            else
            {
                return pair<bool,unsigned int>(false,0);
            }
        }
    }
}

//check if there is an IP starting at the given position,
//in any of the known formats.
//if so, extract it and add it to map
void checkAddr(string in, int pos)
{
    if(in[pos] == '0')
    {
        //leading zero either means hex or octal
        
        if(in[pos+1] == 'x')
        {
            //hex
        }
        else
        {
            //octal
        }
    }
    else
    {
        //decimal or binary
    }
}

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);

    string line;
    
    while (getline(file, line))
    {
    }
    
    return 0;
}
