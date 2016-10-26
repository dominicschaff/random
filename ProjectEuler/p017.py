import inflect,re, string
p = inflect.engine()
pattern = re.compile('[\W_]+')
print sum([len(pattern.sub('', p.number_to_words(i))) for i in xrange(1, 1001)])
