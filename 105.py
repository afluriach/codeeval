import sys

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    matrix = []
    
    for line in fin:
        nums = [int(x) for x in line[0:-1].split(' ') if x]
        matrix.append(nums)
    #end
    
    print matrix
    
    #compute value of every n by m sub-array
    
    subarray_sums = []
    
    #this will n^2 * m^2
    #1x1 is just each cell value
    #then compute each N by 1 matrix by 
    
    for sub_height in xrange(len(matrix)):
        for sub_width in xrange(len(matrix[0])):
        
            pass
        
        #end
    #end
#end
