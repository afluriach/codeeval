import sys

if __name__ == '__main__':

    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        #remove trailing newline, split by space, remove empty
        #strings caused by multiple spaces, and parse to integers
        picks = [int(x) for x in line[0:-1].split(' ') if x]
        
        seen = {}
        #the first player to play a given pick: pick -> player_id
        #only matters if the pick is unique, so no concern for overwriting
        unique_pick = {}
        
        for player_id in range(len(picks)):
            pick = picks[player_id]

            if not pick in seen:
                seen[pick] = 1
                unique_pick[pick] = player_id
            else:
                seen[pick] += 1
            #end
        #end
                
        found = False
        
        #find the lowest key that is unique
        for pick,count in seen.iteritems():
            if count == 1:
                #print one-based player ID
                print(unique_pick[pick]+1)
                found = True
                break
            #end
        #end
        
        if not found:
            print(0)
        #end
    #end

#end
