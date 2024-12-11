import sys


def main():
    # print(A())
    print(B())


def B():
    xs, ys = [], {}
    for line in sys.stdin:
        x, y = map(int, line.split())
        if y not in ys:
            ys[y] = 0
        xs.append(x)
        ys[y] += 1
    return sum(k*ys.get(k, 0) for k in xs)


def A():
    x_list, y_list = [], []
    for line in sys.stdin:
        x, y = map(int, line.split())
        x_list.append(x)
        y_list.append(y)
    x_list.sort()
    y_list.sort()
    return sum(abs(x-y)for x, y in zip(x_list, y_list))


if __name__ == "__main__":
    main()
