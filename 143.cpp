#include <iostream>
#include <fstream>
#include <vector>

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

vector<string> split_by(const string& in, char delim)
{
    vector<string> result;
    
    int start_pos = 0;
    
    for(int i=0;i<in.length(); ++i)
    {
        if(in[i] == delim)
        {
            result.push_back(string(in.begin()+start_pos, in.begin()+i));
            start_pos = i + 1;
        }
    }
    
    if(start_pos < in.length())
    {
        //the last character was not a space
        result.push_back(in.begin()+start_pos, in.end());
    }
    
    return result;
}

string remove_extra_space(const string& in)
{
    string result;
    
    bool last_char_was_space = false;
    for(auto it = in.begin(); it != in.end(); ++it)
    {
        if(*it != ' ')
        {
            result += *it;
            last_char_was_space = false;
        }
        else
        {
            if(!last_char_was_space)
            {
                result += ' ';
                last_char_was_space = true;
            }
        }
    }
    
    return result;
}

//this only works for comparing within words
bool canForm(const string& full, const string& abbreviated)
{
    //skip any position in the full string that does not match the 
    //next character in the abbreviated string. but we must match
    //every character in the abbreviated string before we reach the end
    //of the full string
    int abbreviated_pos = 0;
    
    for(int full_pos=0;full_pos<full.length(); ++full_pos)
    {
        if(abbreviated_pos == abbreviated.length())
        {
            //the whole string has been matched
            break;
        }
    
        if(full[full_pos] == abbreviated[abbreviated_pos])
        {
            //character in abbreviated utterance has been matched
            ++abbreviated_pos;
        }
    }
    
    return abbreviated_pos == abbreviated.length();
}

//if we reach a space in the abbreviated utterance, continue until it is
//matched with the space in the full string.

//but if we reach a space in the full string while in the middle of an 
//abbreviated word, that will not work

//that means (starting at the beginning of the full string),
//foreach word in the abbreviated string, determine if it can be 
//abbreviated to match, or if the whole word needs to be blanked

//thus, it has to match within words, since spaces cannot be introduced out of place
//splice strings into words
bool canForm(const vector<string>& full, const string& abbreviated)
{
    int abb_word = 0;

    for(auto word = full.begin(); word != full.end(); ++word)
    {
        if(abb_word == abbreviated.length())
        {
            break;
        }
    
        //try to form the next abbreviated word 
        if(canForm(*word, abbreviated[abb_word]))
        {
            ++abb_word;
        }
    }    
    
    return abb_word == abbreviated.length();
}


//similar procedure, but in this case change character to
//underscore if it is not matched in the full string
void censor_utterance(string& full, const string& abbreviated)
{
    //skip any position in the full string that does not match the 
    //next character in the abbreviated string. but we must match
    //every character in the abbreviated string before we reach the end
    //of the full string
    int abbreviated_pos = 0;
    
    for(int full_pos=0;full_pos<full.length(); ++full_pos)
    {
        if(abbreviated_pos == abbreviated.length())
        {
            //the whole string has been matched
            //censor the remaining letter but not spaces
            if(full[full_pos] != ' ') 
                full[full_pos] = '_';
            continue;
        }
    
        if(full[full_pos] == abbreviated[abbreviated_pos])
        {
            //character in abbreviated utterance has been matched
            ++abbreviated_pos;
        }
        else
        {
            if(full[full_pos] != ' ') 
                full[full_pos] = '_';
        }
    }
}

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);
    
    string line;
    
    while (getline(file,line))
    {
        //split
        pair<string,string> strings = split(line, ';');
        //the sample input doesn't show extra space in the desired utterance
        //but it's vaguely worded as if it may be possible
        string original = remove_extra_space(strings.first);
        string desired = remove_extra_space(strings.second);
        
        //read in string one char at a time, edit out multiple spaces
        
        //loop through modified input string and find all positions in the 
        //string where the abbreviated utterance could start.
        //quadratic time worst-case.

        //before actually modifying the original string, check to see if the utterance
        //can be formed starting at a given position

        
        bool can_modify = false;
        
        for(int start_pos = 0; start_pos+desired.length()<original.length(); ++start_pos)
        {
            if(canForm(original,desired))
            {
                //modify string
                censor_utterance(original,desired);
                //print it
                cout << original << endl;
                can_modify = true;
                break;
            }
        }
        
        if(!can_modify)
        {
            cout << "I cannot fix history" << endl;
        } 
        
        
    }
}
