import sys, string

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        n_locks, n_cycles = [int(x) for x in line[0:-1].split(' ') if x]
        
        #is locked
        locks = [False]*n_locks
        
        for count in xrange(n_cycles):
            #lock every other door
            for d in xrange(0,n_locks,2):
                locks[d] = True
            #switch lock state of every 3rd door            
            for d in xrange(0,n_locks,3):
                locks[d] = not locks[d]
            #end                                
            
            if count == n_cycles -1:
                locks[n_locks-1] = not locks[n_locks-1]
            #end
        #end
        #unlocked_count = len([x for x in locks if not x])
        unlocked_count = locks.count(False)
        print unlocked_count       
    #end
#end
