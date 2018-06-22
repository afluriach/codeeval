import sys, math

#start by populating the set of palindromes within the given range

#DP to determine how many palindromes there are in a particular range

#starting the ranges of length 0 (just that single number)
#then for length 1. 

def is_palindrome(n):
    if n==0:
        return True
    #end
    
    digits = []
    
    while n != 0:
        digits.append(n%10)
        n /= 10
    #end

    #minus index is ones-based, starts at -1 for the last element    
    for i in xrange(len(digits)/2):
        if digits[i] != digits[-(i+1)]:
            return False
        #end
    #end
    
    return True
#end

def build_palindrome_set(start,end):
    p = {}
    for i in xrange(start,end+1):
        if is_palindrome(i):
            p[i] = True
        #end
    #end
    
    return p
#end

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        l,r = [int(x) for x in line.split(' ')]
        p_set = build_palindrome_set(l,r)
        
        #DP to determine how many palindromes there are in a particular range
        #range is defined by its starting element and how long it is (end-start)
        ranges = []
        ranges.append([])
        
        #single element range has a palindrome count of one if its starting element is a 
        #palindrome, otherwise zero
        
        for i in xrange(l,r+1):
            ranges[0].append(1 if i in p_set else 0)
        #end
        
        #an N length range has the palindrome count of the N-1 element range starting at the 
        #same element, plus the palindrome count of the single element range that follows
        for range_length in xrange(1,r-l+1):
            ranges.append([])
            
            for range_start in xrange(0,r-l+1-range_length):
                ranges[range_length].append(ranges[range_length-1][range_start]+ranges[0][range_start+range_length])
            #end
        #end
        
        #for every subrange represented in ranges, count the number that are
        #interesting by having an even count of palindromes
        interesting_count = 0
        
        for range_length_list in ranges:
            for range_count in range_length_list:
                if range_count % 2 == 0:
                    interesting_count += 1
                #end
            #end
        #end
        
        print interesting_count
    #end
#end
