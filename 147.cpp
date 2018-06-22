#include <iostream>
#include <fstream>
#include <cstdio>

using namespace std;

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);
    
    string line;
    
    while (getline(file,line))
    {
        int lower = 0;
        int upper = 0;

        for(auto ch = line.begin(); ch != line.end(); ++ch)
        {            
            if(isalpha(*ch))
            {
                isupper(*ch) ? ++upper : ++lower;
            }
        }
        
        int total = lower + upper;
        printf("lowercase: %.2lf uppercase: %.2lf\n", lower*100.0/(total), upper*100.0/(total));
    }
}
