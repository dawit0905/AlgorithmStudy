array = [0] * 100

def fibo(n):
    if n == 1 or n == 2 :
        return 1
    if array[n] != 0 :
        return array[n]

    array[n] = fibo(n-1) + fibo(n-2)
    return array[n]

print(fibo(99))