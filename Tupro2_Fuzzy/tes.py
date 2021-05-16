from operator import itemgetter
data = []

c = [1, 18, 17, 9, 21]
d = ['a', 'b', 'r', 'e', 'z']
f = ['rudi', 'carry', 'val', 'ambient', 'oya']

# data.append(c)
# data.append(d)
# data.append(f)

cek = list(zip(c, d, f))
print(cek)
res = sorted(cek, key=itemgetter(0))
print(res)

# for x in range(5):

# for x in range(5):

# for x in range(5):
