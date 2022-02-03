n, k = map(int, input().split())
index_k = k - 1

q = [i for i in range(1, n + 1)]
array = []
num = 0
for i in range(n):
    num = (num + (k-1)) % len(q)
    popElement = q.pop(num)
    array.append(str(popElement))

print(f"<{', '.join(array)}>")
