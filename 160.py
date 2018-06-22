import sys, math

#rounds down to the nearest second
def angle_to_ms(angle):
    degree = math.floor(angle)
    minutes = math.floor((angle - degree) * 60)
    seconds = math.floor((angle - degree - minutes/60)*3600)

    return (degree,minutes,seconds)
#end

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    
    for line in fin:
        decimal_angle = float(line)
        print '%d.%02d\'%02d"' % angle_to_ms(decimal_angle)
    #end
#end
