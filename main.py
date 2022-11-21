A = ['12345', 'hello', 'hi', '_+()&12', 'World', '1']
B = []
for i in A:
  if len(i) <= 3:
    B.append(i)
print(B)
