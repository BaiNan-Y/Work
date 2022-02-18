import os


def test(path_):
    last = 0
    for root, dir, file in os.walk(path_):
        for name in file:
            last += os.path.getsize(os.path.join(root, name))
    return last


print(test('./test') * 1024)


