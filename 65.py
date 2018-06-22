import sys

board = [
'ABCE',
'SFCS',
'ADEE'
]

adjs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#add two 2-tuples together
def add(a,b):
    return (a[0]+b[0],a[1]+b[1])
#end

#track which positions have been visited
#the given position has been visited
def match_letters(word, visited, pos):
    if not word:
        return True
    #end
    
    #depth-first search, foreach adjacent unvisited position:    
    for adj_pos in [add(adj,pos) for adj in adjs if not add(adj,pos) in visited]:
        r,c = adj_pos
        
        #bounds check
        if r < 0 or r >= len(board):
            continue
        #end
        if c < 0 or c >= len(board[0]):
            continue
        #end
        
        visited[adj_pos] = True
        
        #check if adjacent position matches the next character
        #return match if any of the recursive calls matches
        if board[r][c] == word[0]:
            if match_letters(word[1:], visited, adj_pos):
                del visited[adj_pos]
                return True
            #end
        #end
        
        del visited[adj_pos]
    #end
    
    return False
#end

def contains(word):
    #consider each potential start position
    for row in xrange(len(board)):
        for col in xrange(len(board[0])):
            if board[row][col] == word[0]:
                #start letter match here
                if match_letters(word[1:], {(row,col) : True}, (row,col)):
                    return True
                #end
            #end
        #end
    #end
    return False
#end

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        word = line[0:-1]
        print contains(word)
    #end
#end
