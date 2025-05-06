a = [1,2,3]
b = ['a', 'b', 'c']

c = zip(a, b)


d = dict(c)
d = sorted(d.items(), key=lambda x: x[0], reverse=True)
print(d)

for key, value in c:
    print(key, value)