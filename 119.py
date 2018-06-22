import sys

def seen_all_pairs(pairs, seen):
    for k in pairs:
        if not k in seen:
            return False
        #end
    #end
    return True
#end

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
        
    for line in fin:
        entry_strings = line[0:-1].split(';')
        entry_pairs = [tuple(s.split('-')) for s in entry_strings]
        
        pairs = {}
        for b,e in entry_pairs:
            pairs[b] = e
        #end
        
        seen = {}
        
        crnt = "BEGIN"
        
        while True:
            if crnt in seen:
                #loop detected
                print 'BAD'
                break
            elif crnt == 'END':
                #we reached END, it is good if we visited every entry
                print 'GOOD' if seen_all_pairs(pairs, seen) else 'BAD'
                break
            else:
                seen[crnt] = True
                crnt = pairs[crnt]                    
            #end
        #end
    #end
#end
