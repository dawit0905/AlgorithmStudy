d, h, w = map(int, input().split())

r = d/((h**2+w**2)**0.5)

print(int(r * h), int(r * w))