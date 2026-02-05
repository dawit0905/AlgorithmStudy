import sys


vowels = set("aeiou")

while True:
    word = sys.stdin.readline().strip()
    if word == 'end':
        break

    if not any(ch in vowels for ch in word):
        print(f"<{word}> is not acceptable.")
        continue


    invalid = False
    # 모음/자음 3연속 검사
    for i in range(len(word) - 2):
        if (word[i] in vowels) == (word[i+1] in vowels) == (word[i+2] in vowels):
            invalid = True
            break

        # 같은 글자 연속 검사 (ee, oo만 허용)
    if not invalid:
        for i in range(len(word) - 1):
            if word[i] == word[i+1] and word[i] not in ("e", "o"):
                invalid = True
                break

    if invalid:
        print(f"<{word}> is not acceptable.")
    else:
        print(f"<{word}> is acceptable.")