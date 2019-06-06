'''for p in combinations_with_replacement('BR', 3):
    print("".join(p))
n = []
for item in combinations_with_replacement('RB', 3):
    n.append(''.join(item))
n1 = []
for item in combinations_with_replacement(reversed('RB'), 3):
    n1.append(''.join(item))
print(set(n1).union(set(n)))

'''


# fetch two-word permutations, joined into a string
'''
for word in [''.join(s) for s in combinations_with_replacement(words,3)]:
    print (word)'''
'''
w = product('RB', repeat = 3)
for i in w:
    print("".join(i))
args = 'RB'
pools = [tuple(pool) for pool in args] * repeat
result = [[]]
for pool in pools:
    result = [x+[y] for x in result for y in pool]
v= []
for prod in result:
    v.append(tuple(prod))
print(v)