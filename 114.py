import sys, math

def n_dec(n):
    dec = 0
    while math.floor(n) != n:
        dec += 1
        n *= 10
    #end
    return dec
#end

if __name__ == "__main__":
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        weight_str,items_str = line[0:-1].split(':')
        target_weight = int(weight_str)
        items = [x for x in items_str.split(' ') if x]
        item_tuples = []
        #convert to the integer weights knapsack problem by finding the
        #maximum number of decimal digits
        max_decimal = 0
        
        for item in items:
            #(1,10.00,$40)
            substr = item.split(',')
            #remove leading parens and parse to int
            index = int(substr[0][1:])
            weight = float(substr[1])
            #remove leading dollar sign and trailing parens
            cost = float(substr[2][1:-1])
            
            item_tuples.append((index,weight,cost))
            
            max_decimal = max(max_decimal, n_dec(weight))
        #end
        
        print target_weight
        print item_tuples
        
        weight_increment = 10**-max_decimal
        weight_factor = 10**max_decimal
        
        #max_package_value[i][j] represents the maximum package value that can be obtained 
        #given the first i items and a weight limit of j
        #these are ones-based indexes, which uses some extra memory but makes the program more elegant
        #the first row will be all zeroes because no value can be created with zero items
        #the first column will also be all zeroes as no item can be added with a weight limit of zero
        max_package_value = []        
        
        #similarly, we we will also need to track which elements comprise the package
        max_package_contents = []
        
        #initialize first row: 0 value is possible given 0 items
        max_package_value.append([])
        for w in xrange(0, target_weight+1, weight_increment):
            max_package_value[0].append(0)
        #end
                
        for set_size in xrange(1, len(item_tuples)+1):
            #set_size: the number of items we are considering with each iteration
            max_package_value.append([])
            
            #only one item is considered for each set_size iteration, the newly added item
            #convert to zero-based index
            crnt_item = items[set_size-1]
            scaled_weight = crnt_item[1]*weight_factor
            
            for weight_limit in xrange(target_weight*weight_factor+1):
                #convert weight_limit to its actual, floating point value
                if weight_limit < scaled_weight:
                    #item cannot be added with this weight limit
                    #the best solution is that of the same weight from the previous row
                    max_package_value[set_size].append(max_package_value[set_size-1][weight_limit])
                else:
                    #adding this item might be an improvement. compare maximum value for this weight
                    #from the previous row, or weight_limit - item_weight from previous row plus
                    #item's value
                    max_val = max(max_package_value[set_size-1][weight_limit], max_package_value[set_size-1][weight_limit-scaled_weight]+crnt_item[2])
                    max_package_value[set_size].append()
                #end
            #end
            
        #end
        
    #end
#end
