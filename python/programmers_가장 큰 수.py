import functools

def comparator(a, b):
    t1 = a + b
    t2 = b + a

    return (int(t1) > int(t2)) - (int(t1) < int(t2))

def solution(numbers):
    arr = list(map(str, numbers))
    arr.sort(key=functools.cmp_to_key(comparator), reverse=True)

    answer = str(int(''.join(arr)))
    # answer = ''.join(arr)


    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
