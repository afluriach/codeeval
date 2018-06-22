import sys

if __name__ == '__main__':

    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        
        num_lists = line[0:-1].split('|')
        
        #tokenize by space, remove empty strings and parse to ints
        
        factors1 = [int(x) for x in num_lists[0].split(' ') if x]
        factors2 = [int(x) for x in num_lists[1].split(' ') if x]
        
        products = [a*b for a,b in zip(factors1,factors2)] 
        
        for p in products:
            sys.stdout.write(str(p) +  ' ')
        #end
        
        sys.stdout.write('\n')
        
    #end

#end
