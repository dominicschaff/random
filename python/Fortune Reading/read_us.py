# -*- coding: utf-8 -*-
def _read_fortunes(fortune_file):
    """ Yield fortunes as lists of lines """
    result = []
    start = None
    pos = 0
    for line in fortune_file:
        if line == "%\n":
            if pos == 0: # "%" at top of file. Skip it.
                continue
            yield (start, pos - start, result)
            result = []
            start = None
        else:
            if start == None:
                start = pos
            result.append(line)
        pos += len(line)

    if result:
        yield (start, pos - start, result)

f = open("fortunes")
for fortune in _read_fortunes(f):
    if fortune[2][-1:][0].strip().startswith('― ') or fortune[2][-1:][0].strip().startswith('— '):
        text = fortune[2][:-1]
        author = fortune[2][-1:]
        author[0] = author[0].lstrip('― ').lstrip('— ')
    else:
        text = fortune[2]
        author = ['Unknown']
    text = "\n+".join(['"' + a.replace("\"", "\\\"").strip() + ' "' for a in text])
    author = "\n+".join(['"' + a.replace("\"", "\\\"").strip().lstrip('― ').lstrip('— ') + '"' for a in author])
    print "            new Quote(\n                  %s,\n                  %s\n            ),"%(text, author)