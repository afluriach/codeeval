import sys,math

#if there is 2*min_dist space available (space/min_dist)-1 can be added
#must be min_dist from bat on either side
def positions_available_between(min_dist, extra_space):
    if extra_space >= 2*min_dist:
        return int(math.floor(extra_space/min_dist))-1
    else:
        return 0
    #end
#end

#if there is min_dist space available (space/min_dist) can be added
#must be min_dist away from bat on both sides
def positions_available_from_edge(min_dist, extra_space):
    if extra_space >= min_dist:
        return int(math.floor(extra_space/min_dist))
    else:
        return 0
    #end
#end

#if there are no adjacent bats
def positions_available_total(min_dist, extra_space):
    return int(math.floor(extra_space/min_dist))+1
#end

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        nums = [int(x) for x in line.split(' ') if x]
        wire_len,min_dist,n = nums[0:3]
        positions = nums[3:]
        positions.sort()
        
        extra = 0
        
        if n > 0:
        
            left_dist_available = positions[0] - 6
            right_dist_available = wire_len - 6 - positions[-1]
            
            extra += positions_available_from_edge(min_dist, left_dist_available)
            extra += positions_available_from_edge(min_dist, right_dist_available)
            #check extra distance available between existing bats
            
            for bat in xrange(n-1):
                extra += positions_available_between(min_dist, positions[bat+1] - positions[bat])
            #end 
        else:
            dist_available = wire_len - 12
            extra += positions_available_total(min_dist, dist_available)
        #end
           
        print extra 
    #end
#end
