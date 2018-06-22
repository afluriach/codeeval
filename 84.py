import sys

def can_concat(valid_expressions, start, subexpr_len):
    for left_len in xrange(1,subexpr_len):
        right_len = subexpr_len-left_len
        if valid_expressions[left_len-1][start] and valid_expressions[right_len-1][start+left_len]:
            return True
        #end
    #end
    return False
#end

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        expression = line[0:-1]
        
        if len(expression) == 0:
            print "YES"
            continue
        elif len(expression) == 1:
           print "YES" if expression[0] != '(' and expression[0] != ')' else "NO"
           continue
       #end
        
        valid_exprs = []
        
        valid_exprs.append([])
        valid_exprs.append([])
        
        #any single character expression is valid if it is not a parenthesis        
        for ch in expression:
            valid_exprs[0].append(True if ch != '(' and ch != ')' else False)
        #end
        
        #any two character expression is valid if it is two non-parentheses,
        #an emoticon, or ()
        for start_pos in xrange(len(expression)-1):
            subexpr = expression[start_pos:start_pos+2]
            
            if subexpr == '()' or subexpr == ':)' or subexpr == ':(':
                valid_exprs[1].append(True)
            elif subexpr.find('(') != -1 or subexpr.find(')') != -1:
                valid_exprs[1].append(False)
            else:
                valid_exprs[1].append(True)
            #end            
        #end
        
        for sub_expr_len in xrange(3,len(expression)+1):
            #an n-length expression is valid if it starts with a ( followed by a valid
            #n-2 length subexpression followed by )
            #or if it is starts with a valid k-length subexpression followed by a valid
            #n-k length expression
            valid_exprs.append([])
            
            for start_pos in xrange(len(expression)-sub_expr_len+1):
                #print expression[start_pos:start_pos+sub_expr_len+1]
                end_pos = start_pos + sub_expr_len - 1
                
                if expression[start_pos] == '(' and expression[end_pos] == ')':
                    #parens match, but do they enclose a valid subexression?
                    valid_exprs[sub_expr_len-1].append(valid_exprs[sub_expr_len-3][start_pos+1])
                else:
                    #try to concatenate two subexpressions
                    valid_exprs[sub_expr_len-1].append(can_concat(valid_exprs,start_pos, sub_expr_len))
                #end
            #end
        #end
                
        #is the whole expression valid?
        print "YES" if valid_exprs[len(expression)-1][0] else "NO"
    #end
#end
