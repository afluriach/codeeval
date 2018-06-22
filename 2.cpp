#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> lines;

bool strLenComp(const string& a, const string& b)
{
    return a.length() > b.length();
}

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);
    
    string line;
    int n;
    
    //first line
    getline(file, line);
    stringstream first(line);
    
    first >> n;
    
    while (getline(file,line))
    {
        lines.push_back(line);           
    }
    
    //not as memory-efficient as using a min-max heap but much simpler to code
    sort(lines.begin(), lines.end(), strLenComp);
    
    for(int i=0;i<n; ++i)
    {
        cout << lines[i] << endl;
    }
}
