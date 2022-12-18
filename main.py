# https://www.youtube.com/watch?v=UAYeh7pSqXw


s = lambda a, b: a + b
y = [4, 5, lambda: print('lambda'), 7, 8]


def get_filter(a, filter=None):
    if filter is None:
        return a

    res = []
    for x in a:
        if filter(x):
            res.append(x)

    return res


if __name__ == '__main__':
    x = s(1, 2)
    print(x)

    # print(y)
    print(y[2]())

    lst = [5, 3, 0, -6, 8, 10, 1]
    r = get_filter(lst)

    z = get_filter(lst, lambda x: x % 2 == 0)
    h = get_filter(lst, lambda x: x > 0)

    print(r)
    print(z)
    print(h)
