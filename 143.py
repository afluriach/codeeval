import sys

#return substitute string if possible, otherwise empty string
def sub_word(orig, target):
    
    #print('sub %s to %s' % (orig,target))
    
    #the modified string as a list, each character in order from the target sequence or an underscore
    sub_list = []
    
    #convert to list and reverse so we can efficiently pop from the end
    target_list = list(target)
    target_list.reverse()
    
    for orig_letter in orig:
        if not target_list:
            #every character has been matched
            #output underscore foreach remaining character in
            #the original word
            sub_list.append('_')
            continue
        #end
    
        target_letter = target_list[-1]
        
        if orig_letter == target_letter:
            #pop letter from target_list only if it matches
            target_list.pop()
            sub_list.append(target_letter)
        else:
            sub_list.append('_')
        #end
    #end

    #if empty, every letter for the substitute string has been 
    #matched in order
    if not target_list:
        return ''.join(sub_list)
    else:
        return ""
    #end
#end

#return an empty list if not possible, or the list of modified original words
def sub_phrase(orig, sub):
    
    modified = []
    
    #reverse sub so it can efficiently used as a stack
    sub.reverse()
    for word in orig:
        if not sub:
            #every word has been matched
            #each remaining word will be blanked
            modified.append("_"*len(word))
            continue
        #end
    
        sub_result = sub_word(word, sub[-1])
        if sub_result:
            sub.pop()
            modified.append(sub_result)
        else:
            #no match, entire word will be blanked. push string with as many underscores
            #to represent this
            modified.append("_"*len(word))
        #end
    #end
    
    if not sub:
        return modified
    else:
        return None
    #end
#end

if __name__ == "__main__":
    fin = open(sys.argv[1], 'r')

    for line in fin:
        oldspeak,newspeak = line[0:-1].split(';')
        oldspeak_wordlist = oldspeak.split(' ')
        newspeak_wordlist = newspeak.split(' ')
        
        #split will create empty strings for multiple spaces
        #filter these out
        oldspeak_wordlist = [word for word in oldspeak_wordlist if word]
        newspeak_wordlist = [word for word in newspeak_wordlist if word]
        
        #print(oldspeak_wordlist)
        #print(newspeak_wordlist)
        
        sub = sub_phrase(oldspeak_wordlist, newspeak_wordlist)
        
        if sub:
            for word in sub:
                sys.stdout.write(word)
                sys.stdout.write(" ")
            sys.stdout.write('\n')
        else:
            print("I cannot fix history")
        #end
    #end
#end
