import sys, string

#translation = {}
#for input_char,output_char in zip(in_str,out_str):
#    translation[input_char] = output_char

translation = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'f': 'c', 'i': 'd', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 't': 'w'}

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        out = [translation[ch] for ch in line[0:-1]]
        
        print string.join(out, '')
    #end
#end
