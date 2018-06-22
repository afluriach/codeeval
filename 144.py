import sys, string, math

def digit_cycle(base):
    cycle = []
    cycle.append(base)
    
    n = (base*base)%10
    
    while n != base:
        cycle.append(n)
        n *= base
        n %= 10
    #end
    return cycle
#end

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        base,max_power = [int(x) for x in line[0:-1].split(' ') if x]
        digits = {}
        for i in xrange(10):
            digits[i] = 0
        #end
        
        #closed form solution. each sequence has a cycle for its last digit
        cycle = digit_cycle(base)
        
        #the number of complete cycles that will appear
        cycle_count = math.floor(max_power / len(cycle))
        #the remainder, the first n of the cycle that will appear once at the end
        partial_count = int(max_power - cycle_count*len(cycle))

        for digit in cycle:
            digits[digit] += cycle_count
        #end
        
        for i in xrange(partial_count):
            digits[cycle[i]] += 1
        #end
        
        print string.join(['%d: %d' % (digit,count) for digit,count in digits.iteritems()], ', ')
    #end
#end
