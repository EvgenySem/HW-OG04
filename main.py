def greeting(name):
    print(f'Hello, {name}!')

greeting('Jack')


def countdown(n):
    for i in reversed(range(n+1)):
        print(i)


countdown(8)
