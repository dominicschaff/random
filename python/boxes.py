from textwrap import wrap

def box(s, width=25):
    a = wrap(s, width)
    return ['+' + '-'*(width+2) + '+'] + \
        ['| ' + l.ljust(width) + ' |' for l in a] + \
        ['+' + '-'*(width+2) + '+']

def fillBoxes(boxes, maxWidth):
    s = ['']
    start = 0
    for b in boxes:
        # locate start line
        for x in range(start, len(s)):
            if len(s[start]) + len(b[0]) < maxWidth:
                break
            start += 1

        print 'Adding',len(s),start,len(b)
        if len(b) > len(s)-start:
            s += ['' for i in range(len(b))]

        p = len(s[start])
        for l in range(len(b)):
            if len(s[start+l]) < p:
                s[start+l] += ' '*p
            s[start+l] += b[l]

    return '\n'.join(s).strip()


b2 = box('1this is a very long string that needs to be wrapped into shorted lines', 45)
b1 = box('2this is a very long string that needs to be wrapped into shorted lines')
b3 = box('3this is a very long string that needs to be wrapped into shorted lines', 45)
b4 = box('4this is a very long string that needs to be wrapped into shorted lines')
b5 = box('5this is a very long string that needs to be wrapped into shorted lines')

b6 = box(' '.join([str(i).zfill(2) for i in range(100)]), 29)
print fillBoxes([b1,b2,b3,b4,b5,b6], 150)
