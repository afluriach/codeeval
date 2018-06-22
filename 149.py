import sys

if __name__ == '__main__':

    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        tokens = line[0:-1].split(' ')
        bit_list = []
        
        for flag_pos in range(0,len(tokens), 2):
            flag, sequence = tokens[flag_pos], tokens[flag_pos+1]
            
            bit = 1 if flag == '00' else 0
            
            bit_list.extend([bit]*len(sequence)) 
        #end
        
        #parse bits. reverse list so we start with most significant bit
        bit_list.reverse()
        num = 0
        
        while bit_list:
            num *= 2
            num += bit_list.pop()
        #end
        
        print(num)
    #end

#end
