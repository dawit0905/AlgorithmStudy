import sys
from typing import Union, List


def bracket_value(s: str) -> int:
    stack: List[Union[int, str]] = []

    for c in s:
        if c in '([':
            stack.append(c)

        elif c in ')]':
            if not stack:
                return 0

            # 스택 맨 위가 숫자(이미 계산된 값)면 모두 합산
            if isinstance(stack[-1], int):
                total = 0
                while stack and isinstance(stack[-1], int):
                    total += stack.pop()
                if not stack:
                    return 0
                open_br = stack.pop()
                # 올바른 짝인지 확인
                if open_br == '(' and c == ')':
                    multiplier = 2
                elif open_br == '[' and c == ']':
                    multiplier = 3
                else:
                    return 0
                stack.append(total * multiplier)

            # 바로 앞이 여는 괄호인 경우
            else:
                open_br = stack.pop()
                if open_br == '(' and c == ')':
                    stack.append(2)
                elif open_br == '[' and c == ']':
                    stack.append(3)
                else:
                    return 0

        else:
            # 허용되지 않은 문자 발견 시
            return 0

    # 남은 값이 전부 정수여야 하고, 합산하여 반환
    result = 0
    for item in stack:
        if not isinstance(item, int):
            return 0
        result += item

    return result


def main():
    s = sys.stdin.readline().rstrip()
    print(bracket_value(s))


if __name__ == '__main__':
    main()
