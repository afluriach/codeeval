import sys

test_cases = open(sys.argv[1], 'r')

#simpler if we map to the string representation of the digit
num_map = {'zero' : '0',
           'one' : '1',
           'two' : '2',
           'three' : '3',
           'four' : '4',
           'five' : '5',
           'six' : '6', 
           'seven' : '7',
           'eight' : '8',
           'nine' : '9'}

for line in test_cases:
    #slice newline character and split
    words = line[0:-1].split(';')
    output = ''
    
    for word in words:
        output += num_map[word]
    print(output)
test_cases.close()

