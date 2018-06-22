import sys, re

nodes = {}

class Node(object):
    def __init__(self, item):
        self.left = self.right = None
        self.item = item
        nodes[item] = self
        self.ancestor = None
    #end
    
    def add(self, side, item):
        setattr(self, side, Node(item))
        #self[side] = node
        setattr(getattr(self,side), 'ancestor', self)
    #end
#end

root = Node(30)
root.add('right', 52)
root.add('left',8)
root.left.add('left', 3)
root.left.add('right', 20)
root.left.right.add('left', 10)
root.left.right.add('right', 29)

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        id_str = line[0:-1].split(' ')
        a,b = int(id_str[0]),int(id_str[1])
        
        #generate lineage for node A
        lineage = []
        node = nodes[a]
        
        while node:
            lineage.append(node.item)
            node = node.ancestor
        #end
        
        #iterate through lineage of node B and find the first
        #match
        
        node = nodes[b]
        
        while node:
            if node.item in lineage:
                print(node.item)
                break
            #end
            node = node.ancestor
        #end
    #end
#end
