#include <iostream>
#include <fstream>
#include <sstream>
#include <string.h>
#include <vector>

using namespace std;

template<int size>
bool eval_sudoku(vector<vector<int> > grid)
{
    int sub_square_size = size == 4 ? 2 : 3;
    
    //check each row
    
    for(int row = 0; row < size; ++row)
    {
        bool nums[size];
        memset(nums, 0, size);
        for(int c = 0; c < size; ++c)
        {
            int num = grid[row][c];
            
            if(nums[num-1])
            {
                //cout << "dupe val in row " << row << " col " << c << endl;;
                return false;
            }
            
            nums[num-1] = true;
        }
    }
    
    //check each col
    
    for(int col = 0; col < size; ++col)
    {
        bool nums[size];
        memset(nums, 0, size);
        for(int r = 0; r < size; ++r)
        {
            int num = grid[r][col];
            
            if(nums[num-1])
            {
                //cout << "dupe val in col " << col << " row" << r << endl;;
                return false;
            }
            
            nums[num-1] = true;
        }
    }
    
    //check each sub-square
    for(int sqx = 0; sqx < sub_square_size; ++sqx)
    {
        for(int sqy = 0; sqy < sub_square_size; ++sqy)
        {
            bool nums[size];
            memset(nums, 0, size); 
            for(int i=0;i<sub_square_size; ++i)
            {
                for(int j=0;j<sub_square_size; ++j)
                {
                    int num = grid[sqx*sub_square_size+i][sqy*sub_square_size+j];
                    
                    if(nums[num-1])
                    {
                        //cout << "dupe val in square " << sqx << "," << sqy << i << "," << j << endl;
                        return false;
                    }
                    
                    nums[num-1] = true;
                }
            }
            
        }
    }
    return true;           
}

template<int size>
vector<vector<int> > load_grid(stringstream& s)
{
    vector< vector<int> > grid;
    
    for(int i=0;i<size;++i)
    {
        grid.push_back(vector<int>());
        for(int j=0;j<size; ++j)
        {
            char dummy;
            int val;
            s >> dummy;
            s >> val;
            grid[i].push_back(val);
            //cout << grid[i][j] << " ";
        }
        //cout << endl;
    }
    
    return grid;
}

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);
    
    string line;
    
    while (getline(file,line))
    {
        stringstream linestr(line);
    
        bool valid;
        vector<vector<int> > grid;
        int size;
        
        linestr >> size;
        
        if(size == 4)
        {
            grid = load_grid<4>(linestr);
            valid = eval_sudoku<4>(grid);
        }
        else
        {
            grid = load_grid<9>(linestr);
            valid = eval_sudoku<9>(grid);
        }
        
        cout << (valid ? "True" : "False") << endl;
    }
}
