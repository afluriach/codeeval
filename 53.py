import sys

def all_space(s):
    for ch in s:
        if ch != ' ':
            return False
        #end
    #end
    return True
#end

if __name__ == '__main__':
    
    fin = open(sys.argv[1], 'r')
        
    for line in fin:
        seen = {}    
        longest_repeat = ''
    
        for start in xrange(len(line)-1):
            for end in xrange(start+1, len(line)-1):
                substr = line[start:end]
                
                if all_space(substr):
                    continue
                #end
                
                if not substr in seen:
                    #the first time a string is seen, store its position
                    #substrings are explored earliest first
                    # the first repeat of this string that does not overlap will be considered
                    seen[substr] = start
                elif len(substr) > len(longest_repeat) and start >= seen[substr]+len(substr):
                    longest_repeat = substr
                #end
            #end
        #end
    
        print(longest_repeat if longest_repeat else 'NONE')
    
    #end
    
#end
