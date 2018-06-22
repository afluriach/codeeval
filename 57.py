import sys, string

#defined upper-left and bottom-right corner of the spiral to print
#move recursion to the beginning to print inside-out
def spiral(matrix, tl_x, tl_y, br_x, br_y):
    spiral_seq = []
    
    #if the width or height of the spiral section
    #is one, just print that row or column
    
    if tl_x == br_x:
        #there is only one column
        for y in xrange(tl_y, br_y+1):
            spiral_seq.append(matrix[y][tl_x])
        #end
        return spiral_seq
    #end 
    
    if tl_y == br_y:
        #there is only one row, use splice on row
        return matrix[tl_y][tl_x:br_x+1]
    #end
    
    #top row
    for x in xrange(tl_x, br_x+1):
        spiral_seq.append(matrix[tl_y][x])
    #end
    
    #right edge, excluding top and bottom row
    for y in xrange(tl_y+1, br_y):
        spiral_seq.append(matrix[y][br_x])
    #end
    
    #bottom row
    for x in xrange(br_x, tl_x-1, -1):
        spiral_seq.append(matrix[br_y][x])
    #end
    
    #left edge, excluding top and bottom row
    for y in xrange(br_y-1, tl_y, -1):
        spiral_seq.append(matrix[y][tl_x])
    #end
    
    #if the width and height of this spiral section is greater thanor equal to two, 
    #meaning at least 3 rows and columns wide, recurse
    if br_y - tl_y >= 2 and br_x - tl_x >= 2:
        spiral_seq.extend(spiral(matrix, tl_x+1, tl_y+1, br_x-1, br_y-1))
    #end  
    
    return spiral_seq    
#end

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    matrix = []
    
    for line in fin:
        row_str, col_str, seq_str = line[0:-1].split(';')
        rows,cols = int(row_str), int(col_str)
        seq = seq_str.split(' ')
        
        matrix = []
        
        for r in xrange(rows):
            matrix.append([])
            for c in xrange(cols):
                matrix[r].append(seq[r*cols+c])
            #end
        #end
        
        print string.join(spiral(matrix, 0, 0, cols-1, rows-1), ' ')
    #end
#end
