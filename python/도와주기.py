from itertools import product

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 7
num_selected = 5

# 중복을 허용하여 5개의 숫자를 선택한 순열 생성
permutations = list(product(arr, repeat = num_selected))

# 선택한 숫자들의 합이 6인 경우를 필터링
valid_permutations = [perm for perm in permutations if sum(perm) == target_sum]

print(f'합이 {target_sum}이 되는 5개의 숫자 순열의 경우의 수: {len(valid_permutations)}')
print('해당 순열:')
for permutation in valid_permutations:
    print(permutation)
