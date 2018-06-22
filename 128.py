import sys

if __name__ == '__main__':
    
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        sequence = [int(x) for x in line.split(' ') if x]
        
        if sequence:
            #read first item
            value = sequence[0]
            count = 1
            compressed = []
            
            for i in xrange(1,len(sequence)):
                v = sequence[i]
                
                if v == value:
                    count+=1;
                else:
                    compressed.append((count,value))
                    value = v
                    count = 1
                #end
            #end
            
            compressed.append((count,value))
            
            for count,value in compressed:
                sys.stdout.write(str(count) + ' ' + str(value) + ' ')            #end
            
        #end
        
        sys.stdout.write('\n')
    #end
    
#end
