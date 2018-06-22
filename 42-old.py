import sys

ugly_primes = [2,3,5,7]

def is_ugly(n):
    for prime in ugly_primes:
        if n % prime == 0:
            return True
        #end
    #end
    return False
#end

def tokenize_expr(digits,ops):
    #separate into numbers and operators
    crnt_num = ord(digits[0]) - ord('0')
    tokens = []

    #for each digit pos, ops[pos-1] represents the op to its left
    #if not '', push the crnt num and set the next, as well as the separating operator
    #else, crnt_num *= 10 and add next digit
    for digit_pos in xrange(1,len(digits)):
        op = ops[digit_pos-1]
        digit = ord(digits[digit_pos]) - ord('0')
        
        if op:
            tokens.append(crnt_num)
            tokens.append(op)
            crnt_num = digit
        else:
            crnt_num *= 10
            crnt_num += digit
        #end
    #end
    
    #the last token will be a number
    tokens.append(crnt_num)
    
    return tokens
    #return eval(expr_str(digits,ops))
#end

def compute_expr(tokens):
    crnt_val = tokens[0]
    
    #apply each operation left to right with the adjacent operand
    for op_pos in range(1,len(tokens)-1,2):
        op,next_val = tokens[op_pos], tokens[op_pos+1]
        if op == '+':
            crnt_val += next_val
        elif op == '-':
            crnt_val -= next_val
        else:
            print('unknown operator %s to the left of %d' % (op,next_val))
        #end
    #end
    return crnt_val
#end

def evaluate_expr(digits,ops):
    tokens = tokenize_expr(digits,ops)
    return compute_expr(tokens)
#end

def expr_str(digits,ops):
    assert len(digits) == len(ops) + 1
    li = []
    
    for i in xrange(len(ops)):
        li.append(digits[i])
        
        if ops[i]:
            li.append(ops[i])
        #end
    #end
    
    li.append(digits[-1])
    return ''.join(li)
#end

op_symbols = ['', '+', '-']
#ops represents the symbols placed between
#the digits, either '+', '-', or '' for no op
def iter_expr(digits,ops):
    if len(ops) == len(digits) - 1:
        n = evaluate_expr(digits,ops)
        return 1 if is_ugly(n) else 0
    else:
        ugly_count = 0
        for op_symbol in op_symbols:
            ops.append(op_symbol)
            ugly_count += iter_expr(digits,ops)
            ops.pop()
        #end
        return ugly_count
    #end
#end

if __name__ == '__main__':
    
    fin = open(sys.argv[1], 'r')
    
    for line in fin:       
        digits = list(line[0:-1])
        
        count = iter_expr(digits, [])
        print(count)
    #end
    
#end
