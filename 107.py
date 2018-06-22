import sys, string

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        sequence = line[0:-1]
        
        if len(sequence) == 0:
            print(0)
            continue
        #end
        
        for p in xrange(1,len(sequence)+1):
            #in order for p to be the period of the sequence
            #it has to be a divisor for the length of the sequence
            if len(sequence) % p != 0:
                continue
            #end
            
            period = sequence[0:p]
            
            if string.count(sequence, period) == len(sequence)/p:
                #period has matched N/p non-overlapping times, meaing it has
                #covered the whole sequence
                print(p)
                break
            #end
        #end
    #end
#end
