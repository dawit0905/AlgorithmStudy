
mod = 1000000
p = mod//10*15
fibo = [0,1,1] + [0] * (1500000-2)

n = int(input())
for i in range(2,p):
    fibo[i] = fibo[i-1] + fibo[i-2]
    fibo[i] %= mod

print(fibo[n%p])