import sys

if __name__ == '__main__':

    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        #remove trailing newline, split by semicolon, remove empty
        #strings caused by multiple spaces
        cities = [x for x in line[0:-1].split(';') if x]
        
        #split name,dist pair by comma and convert distance to integer
        distances = [int(x.split(',')[1]) for x in cities]
        
        distances.sort()
        
        prev = 0
        first = True
        
        for pos in distances:
            if not first:
                sys.stdout.write(',')
            #end
            first = False
            sys.stdout.write(str(pos-prev))
            prev = pos
        #end
        print('')    
    #end

#end
