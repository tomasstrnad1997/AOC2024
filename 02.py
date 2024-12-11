import sys


def main():
    # print(A())
    print(B())


def is_safeB(line):
    return is_safe(line) or any(is_safe(line[:i] + line[i+1:]) for i in range(len(line)))


def is_safe(line):
    diff = line[0] - line[1]
    for x, y in zip(line, line[1:]):
        current_diff = x - y
        if current_diff * diff <= 0 or not (1 <= abs(current_diff) <= 3):
            return False
    return True


def A():
    return sum(is_safe(list(map(int, line.split()))) for line in sys.stdin)


def B():
    return sum(is_safeB(list(map(int, line.split()))) for line in sys.stdin)


if __name__ == "__main__":
    main()
