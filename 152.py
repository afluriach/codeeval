import sys

age_categories =[
(0,2, 'Still in Mama\'s arms'),
(3,4,'Preschool Maniac'), 
(5,11,'Elementary school'),
(12,14,'Middle school'),
(15,18,'High school'),
(19,22,'College'),
(23,65,'Working for the man'), 
(66,100,'The Golden Years')
]


if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        age = int(line)
        
        if age < 0 or age > 100:
            print "This program is for humans"
            continue
        #end
        
        for category in age_categories:
            if age >= category[0] and age <= category[1]:
                print category[2]
                break
            #end
        #end 
    #end
#end
