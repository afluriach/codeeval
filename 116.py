import sys, string

codes = {
    '.-' : 'a',
    '-...' : 'b',
    '-.-.' : 'c',
    '-..' : 'd',
    '.' : 'e',
    '..-.' : 'f',
    '--.' : 'g',
    '....' : 'h',
    '..' : 'i',
    '.---' : 'j',
    '-.-' : 'k',
    '.-..' : 'l',
    '--' : 'm',
    '-.' : 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.' : 'r',
    '...' : 's',
    '-' : 't',
    '..-': 'u',
    '...-' : 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
    
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',   
}

if __name__ == '__main__':

    fin = open(sys.argv[1], 'r')
    
    for line in fin:
    
        #remove trailing newline, split words by double-spaces
        #words are in turn a list of letter strings separated by single spaces
        morse_words = [x.split(' ') for x in line[0:-1].split('  ')]
        
        words = [[codes[letter] for letter in word] for word in morse_words]
    
        #join each word (list) to make a string, and then join list of words with a space
        text = string.joinfields([''.join(word) for word in words], ' ')
        
        print(text.upper())
    #end

#end
