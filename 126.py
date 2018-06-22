import sys, string


if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        line_splice = [x for x in line[0:-1].split(' ') if x]
        
        target, input_string = line_splice[0], line_splice[2]
        max_mismatch = int(line_splice[1])
        
        #first index is length of substring, second is start position of that
        #subtring. value stored is how many characters match
        substr_matches = []
        
        #calculate all perfect substring matches that are possible
        #substr_len is zero-based
        for substr_len in xrange(,len(target)):
            substr_matches.append([])
            
            for substr_pos in xrange():
                
            #end
            
        #end
        
    #end
#end
