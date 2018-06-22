#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main(int argc, char ** argv)
{
    int i = 1;
    char* addr = reinterpret_cast<char*>(&i);
    bool a = *addr; //is a bit set in the first byte of the integer
    bool b = *(addr+3); //or the last byte of the integer
    
    cout << (a ? "LittleEndian" : "BigEndian") << endl;
}
