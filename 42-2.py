import sys

#a number can be represented as its mod with regard to each prime in consideration
primes = []

for pp in xrange(2,10):
	prime = True
	
	for div in primes:
		if pp%div == 0:
			prime = False
			break
		#end		
	#end
	
	if prime:
		primes.append(pp)
	#end

#end

print primes

#build tuple without using a list, generate tuple from generator

def mod_gen(n):
    for i in xrange(len(primes)):
        yield(n%primes[i])
    #end
#end

def prime_mod(n):
    return tuple(mod_gen(n))
    #return (n%2, n%3,n%5,n%7)
#end

def add_gen(m1,m2):
	assert len(m1) == len(primes)
	assert len(m2) == len(primes)
	
	for i in xrange(len(primes)):
		yield (m1[i] + m2[i]) % primes[i]
	#end
#end

def sub_gen(m1,m2):
	assert len(m1) == len(primes)
	assert len(m2) == len(primes)
	
	for i in xrange(len(primes)):
		yield (m1[i] - m2[i]) % primes[i]
	#end
#end

def sub_mod(m1,m2):
	assert len(m1) == len(primes)
	assert len(m2) == len(primes)
	
	for i in xrange(len(primes)):
		yield (m1[i] - m2[i]) % primes[i]
	#end
#end

def add_mod(m1,m2):
    return tuple(add_gen(m1,m2))
    #return((m1[0]+m2[0])%2,(m1[1]+m2[1])%3,(m1[2]+m2[2])%5, (m1[3]+m2[3])%7)
#end

def sub_mod(m1,m2):
    return tuple(sub_gen(m1,m2))
    #return((m1[0]-m2[0])%2,(m1[1]-m2[1])%3,(m1[2]-m2[2])%5, (m1[3]-m2[3])%7)
#end

#a mod set represents a set of numbers (described by mod tuple) and how many
#times they appear. or more concretely, how many ways it is possible to generate
#each possible mod value with a givne expression
def add_mod_sets(s1,s2):
    result = {}
    
    for a,countA in s1.iteritems():
        for b,countB in s2.iteritems():
            #if there are m ways to make a and n ways to make b,
            #then there are m*n ways to make add_mod(a,b)
            add = add_mod(a,b)
            if not add in result:
                result[add] = 0
            #end
            result[add] += countA*countB
        #end
    #end
    
    return result
#end

def sub_mod_sets(s1,s2):
    result = {}
    
    for a,countA in s1.iteritems():
        for b,countB in s2.iteritems():
            sub = sub_mod(a,b)
            if not sub in result:
                result[sub] = 0
            #end
            result[sub] += countA*countB
        #end
    #end
    return result
#end

#add the contents of the second set to the first
def add_set(target, addend):
    for num,count in addend.iteritems():
        if not num in target:
            target[num] = 0
        #end
        target[num] += count
    #end
#end

def is_ugly(t):
    for i in xrange(len(t)):
        if t[i] == 0:
            return True
        #end
    #end
    return False
#end

#a number is ugly if any of its prime mods are 0
def count_ugly(mod_set):
    total = 0
    
    for p,count in mod_set.iteritems():
        if is_ugly(p):
            total += count
        #end
    #end
    
    return total
#end

#all the expressions that can be formed.
#at each level of recursion, return a map representing how many of each
#number can be calculated, keyed by prime tuple, so the map will have a maximum
#size of 210
def iter_expr(number_mods, start, expr_len):
    #expr_len is ones based
    if expr_len == 1:
        #the only number that can be formed is that single digit number
        return {number_mods[0][start] : 1}
    #end
    
    #an expression of N digits can either be that n digit number
    #or any of the 1 _ e(N-1) to (N-1) _ 1 expressions that can be formed
    #to avoid double counting, the left side will only be considered as a number
    #and the expressions will be expanded on the right side
    count = {}
    
    #count the N digit number
    count[number_mods[expr_len-1][start]] = 1
        
    for left_expr_len in xrange(1,expr_len):
        #left = iter_expr(number_mods, start, left_expr_len)
        left = {number_mods[left_expr_len-1][start]: 1}
        right = iter_expr(number_mods, start+left_expr_len, expr_len-left_expr_len)
        
        sum_set = add_mod_sets(left,right)
        diff_set = sub_mod_sets(left,right)
                
        add_set(count,sum_set)
        add_set(count,diff_set)
    #end
    return count
#end

if __name__ == '__main__':
    
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        digits = line[0:-1]
        
        #a 2D list of all prime tuples representing all the numbers
        #that can be generated from the given numbers
        #the first row will be the prime tuple representing the single digit number at each position
        #the next row the prime tuple representing the two digit numbers starting at each position
        #(n-1 length) and so on
        number_mods = []
        
        for num_len in xrange(len(digits)):
            #zero-based length
            number_mods.append([])
            
            for start in xrange(len(digits)-num_len):
                #splice substring and parse to int, explicitly specify base 10 otherwise
                #a leading zero would cause it to parse as octal
                number_mods[num_len].append(prime_mod(int(digits[start:start+num_len+1],10)))
            #end
        #end
        count = iter_expr(number_mods, 0, len(digits))
        print(count_ugly(count))
    #end
#end
