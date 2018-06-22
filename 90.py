import sys, string, math

def iter_binary_list(l):
    if l==1:
        return [[0],[1]]

    r = iter_binary_list(l-1)
    
    a = [[0] + x for x in r]
    b = [[1] + x for x in r]
    
    return a + b
#end

def binary_tuples(l):
    return [tuple(x) for x in iter_binary_list(l)]
#end

def sub_set_pairs(n):
    #each binary tuple represents a mask of which of the first n/2 elements
    #will be selected
    #for n = 10, that gives 32 possible subset partitions
    bit_masks = binary_tuples(n/2)
    partition = n/2
    
    for mask in bit_masks:
        s1 = [i if mask[i] else partition+i for i in xrange(partition)]
        s2 = [partition+i if mask[i] else i for i in xrange(partition)]
        print mask
        print s1
        print s2
        print ""
    #end
    
#end



if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    coords = []
    paths = []
    
    for line in fin:
        coord_str = line[0:-1].split('(')[1][0:-1]
        
        coord = [float(x) for x in coord_str.split(',') if x]
        coords.append(coord)        
    #end
    
    #start by finding distance between any two coords
    pair_dists = {}
    
    for i in xrange(len(coords)-1):
        for j in xrange(i+1,len(coords)):
            dx = coords[j][0] - coords[i][0]
            dy = coords[j][1] - coords[i][1]
            dist = math.sqrt(dx*dx+dy*dy)
            pair_dists[(i,j)] = pair_dists[(j,i)] = dist
        #end
    #end
    
    #first node is fixed
    
    #print binary_tuples(5)
    sub_set_pairs(10)
#end
