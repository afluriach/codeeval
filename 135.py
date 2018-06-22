import sys

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
        
    for line in fin:
        words = line[0:-1].split(',')
        
        pairs = [(w[0],w[-1]) for w in words]
        
        #build set of possible word strings iteratively
        #try to add word to front or back of existing chains and add then with len+1
        #then add the word itself to the set as a chain of len 1
        
        chain_set = []
        
        for word_pair in pairs:
            word_start,word_end = word_pair
            new_chains = []
                        
            for chain in chain_set:
                chain_start, chain_end, chain_length = chain
                
                if chain_end == word_start:
                    #append word to end 
                    new_chains.append((chain_start, word_end, chain_length+1))
                #end
                if chain_start == word_end:
                    #append word to front
                    new_chains.append((word_start, chain_end, chain_length+1))
                #end
            #end
        
            new_chains.append((word_start, word_end, 1))
            
            chain_set.extend(new_chains)
        #end
        
        print chain_set
        
    #end
#end
